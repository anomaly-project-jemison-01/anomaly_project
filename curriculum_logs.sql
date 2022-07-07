-- Stephen fitzsimon
-- anomaly project sql query

use curriculum_logs;

-- This is the right sql query
SELECT l.*, c.*, (CASE 
		WHEN c.program_id = 1 THEN "full_stack_php"
		WHEN c.program_id = 2 THEN "full_stack_java"
		WHEN c.program_id = 3 THEN "data_science"
		WHEN c.program_id = 4 THEN "front_end"
		ELSE "unknown_program"
		END) AS program_name
	FROM logs AS l
	LEFT JOIN cohorts AS c ON c.id = l.cohort_id;

SELECT * FROM logs
	WHERE cohort_id IS NULL;
    
SELECT * FROM cohorts;