SELECT
    grp.name AS group_name,
    AVG(g.grade) AS average_grade
FROM
    groups grp
JOIN
    students s ON grp.id = s.group_id
JOIN
    grades g ON s.id = g.student_id
JOIN
    subjects sub ON g.subject_id = sub.id
WHERE
    sub.name = 'Physics'
GROUP BY
    grp.id;
