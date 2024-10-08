
SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month, 
        t.country, 
        COUNT(*) as trans_count, 
        SUM(CASE WHEN t.state='approved' THEN 1 ELSE 0 END) AS approved_count, 
        SUM(amount) as trans_total_amount,
        SUM(CASE WHEN t.state='approved' THEN t.amount ELSE 0 END) AS approved_total_amount
FROM Transactions t
GROUP BY month, country