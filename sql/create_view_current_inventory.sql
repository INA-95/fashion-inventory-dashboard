CREATE OR REPLACE VIEW `YOUR_PROJECT.fashion_retail.current_inventory_status` AS
WITH sold AS (
  SELECT
    product_id,
    COUNTIF(status = 'Complete') AS sold_qty
  FROM `bigquery-public-data.thelook_ecommerce.order_items`
  GROUP BY product_id
),
stock AS (
  SELECT
    product_id,
    COUNT(*) AS total_stock
  FROM `bigquery-public-data.thelook_ecommerce.inventory_items`
  GROUP BY product_id
)
SELECT 
  stock.product_id,
  IFNULL(stock.total_stock, 0) - IFNULL(sold.sold_qty, 0) AS current_inventory
FROM stock
LEFT JOIN sold USING (product_id)
ORDER BY current_inventory DESC;
