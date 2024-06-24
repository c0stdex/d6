WITH last_dates AS (
    SELECT
        g.student_id,
        MAX(g.date) AS last_date
    FROM
        grades g
    JOIN
        students s ON g.student_id = s.id
    JOIN
        groups grp ON s.group_id = grp.id
    JOIN
        subjects sub ON g.subject_id = sub.id
    WHERE
        grp.name = 'Group 3'
        AND sub.name = 'Biology'
    GROUP BY
        g.student_id
)
SELECT
    s.first_name,
    s.last_name,
    g.grade,
    g.date
FROM
    grades g
JOIN
    last_dates ld ON g.student_id = ld.student_id AND g.date = ld.last_date
JOIN
    students s ON g.student_id = s.id
JOIN
    subjects sub ON g.subject_id = sub.id
WHERE
    sub.name = 'Biology';
