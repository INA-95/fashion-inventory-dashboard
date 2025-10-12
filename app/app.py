import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import numpy as np
from datetime import datetime

#st.set_page_config(page_title="BigQuery 연결 테스트", layout="wide")
#st.title("📦 BigQuery 뷰 연결 테스트")

# 1) BigQuery 클라이언트 만들기 (secrets의 서비스계정 우선)
def get_bq_client():
    if "gcp_service_account" in st.secrets:
        creds = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"]
        )
        project_id = st.secrets["gcp_service_account"].get("project_id")
        return bigquery.Client(project=project_id, credentials=creds)
    # (백업) ADC 사용 시
    return bigquery.Client()

# 2) 조회할 뷰(FQN)
VIEW_FQN = st.secrets["view_fqn"]

# 3) 쿼리 실행
client = get_bq_client()
query = f"""
SELECT *
FROM `{VIEW_FQN}`
ORDER BY 1
LIMIT 10
"""
try:
    df = client.query(query).result().to_dataframe(create_bqstorage_client=True)
    st.title("Inventory Status")

    df_clean = df.copy()
    df_clean["current_inventory"] = (
        df_clean["current_inventory"]
        .fillna(0)
        .astype(int)
    )
    df_clean = df_clean.rename(columns={
        "product_id": "Product ID",
        "current_inventory": "Current Inventory"
    })

    total_sku = df_clean["Product ID"].nunique()
    sold_out = int((df_clean["Current Inventory"] == 0).sum())
    low_stock = int((df_clean["Current Inventory"] <= 5).sum())  # 임계치 5개(포트폴리오용)

    col1, col2, col3 = st.columns(3)
    col1.metric("TOTAL SKU", f"{total_sku:,}")
    col2.metric("SOLD OUT SKU", sold_out)
    col3.metric("LOW STOCK(≤5)", low_stock)

    # 3) 상태 라벨(간단 규칙)
    df_clean["Status"] = np.select(
        condlist=[
            df_clean["Current Inventory"] == 0,
            df_clean["Current Inventory"] <= 5,
            df_clean["Current Inventory"] >= df_clean["Current Inventory"].quantile(0.9),
        ],
        choicelist=["Sold Out", "Low", "High"],
        default="OK"
    )

    # 4) 표: 10행만, 보기 좋게 정렬/색상 강조
    sample = (
        df_clean
        .sort_values(["Status", "Current Inventory"], ascending=[True, True])
        .head(10)
        .reset_index(drop=True)
    )

    st.caption(f"BigQuery Connection Result • {datetime.now().strftime('%Y-%m-%d %H:%M')} ")
    st.dataframe(
        sample.style
        .background_gradient(subset=["Current Inventory"], cmap="RdYlGn_r")
        .apply(lambda s: ["font-weight:700" if v in ["Sold Out","Low"] else "" for v in s] 
                if s.name=="Status" else [""]*len(s), axis=0),
        use_container_width=True,
        hide_index=True
    )

    # 5) 포트폴리오용 푸터(선택)
    st.markdown(
        """
        <div style="font-size:0.9rem; color:#777;">
        
        
        </div>
        """, unsafe_allow_html=True
    )
except Exception as e:
    st.error("❌ BigQuery 연결 실패. 메시지를 확인하세요:")
    st.exception(e)
