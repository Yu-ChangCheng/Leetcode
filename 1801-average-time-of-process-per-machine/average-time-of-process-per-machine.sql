WITH table1 AS (
  SELECT 
    s.machine_id, 
    s.process_id, 
    (e.timestamp - s.timestamp) AS processing_time
  FROM 
    (SELECT machine_id, process_id, timestamp 
     FROM Activity 
     WHERE activity_type = 'start') s
  JOIN 
    (SELECT machine_id, process_id, timestamp 
     FROM Activity 
     WHERE activity_type = 'end') e
  ON 
    s.machine_id = e.machine_id 
    AND s.process_id = e.process_id
)

SELECT 
  machine_id, 
  ROUND(AVG(processing_time), 3) AS processing_time
FROM 
  table1
GROUP BY 
  machine_id;