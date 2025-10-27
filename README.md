# 🛍️ Fashion Retail Inventory Dashboard (BigQuery × Streamlit)

A clean and reproducible data app demonstrating:

- **BigQuery View** creation for inventory analysis  
- **Streamlit** dashboard connected securely to BigQuery  
- **Real-time visualization** of current inventory levels  

🎯 **Goal:** Showcase data engineering + visualization workflow

---

## 🧭 Project Overview

**Problem:** Retail teams need real-time visibility into inventory to avoid stock-outs.  
**Solution:** A BigQuery view aggregates product-level stock and orders, and a Streamlit dashboard displays live metrics and visualizations.  
**Dataset:** [`bigquery-public-data.thelook_ecommerce`](https://console.cloud.google.com/marketplace/product/bigquery-public-data/thelook-ecommerce)

**Key Features:**
- 🔹 Real-time inventory status from BigQuery  
- 🔹 Low-stock product flagging  
- 🔹 Interactive charts & downloadable CSV  
- 🔹 Deployed with Streamlit Cloud  

---

## 📁 Repository Structure

```
    fashion-inventory-dashboard/
    ├─ README.md
    ├─ sql/
    │ └─ create_view_current_inventory.sql
    ├─ app/
    │ ├─ app.py
    │ └─ requirements.txt
    ├─ .streamlit/
    │ └─ secrets.toml.example
    ├─ tests/
    │ └─ test_bigquery_connection.py
    ├─ .github/
    │ └─ workflows/
    │ └─ ci.yml
    ├─ docs/
    │ ├─ architecture.png # optional
    │ └─ demo.gif # optional
    ├─ .gitignore
    └─ LICENSE
```

---

## 🚀 How to Run Locally

### 1️⃣ Create and Activate Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2️⃣ Install Requirements

```
pip install -r app/requirements.txt
```


### 3️⃣ Add BigQuery Credentials

```
[gcp_service_account]
project_id = "YOUR_PROJECT_ID"
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
client_email = "svc-bq@YOUR_PROJECT_ID.iam.gserviceaccount.com"
token_uri = "https://oauth2.googleapis.com/token"
```

---

## 🧾 Tech Stack

- Python 3.11
- BigQuery (SQL)
- Streamlit 1.x
- Google Cloud Authentication
- Matplotlib / Pandas

## Final Dashboard link

- https://fashion-inventory-dashboard-jsgamzpdzfb4odumiwv6gl.streamlit.app/
  <img width="723" height="602" alt="Image" src="https://github.com/user-attachments/assets/9f638efa-fb2d-4d3a-9e88-4296a674ccb0" />

---

## 📜 License
MIT License
