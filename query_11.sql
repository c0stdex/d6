SELECT
    t.first_name AS teacher_first_name,
    t.last_name AS teacher_last_name,
    s.first_name AS student_first_name,
    s.last_name AS student_last_name,
    AVG(g.grade) AS average_grade
FROM
    teachers t
JOIN
    subjects sub ON t.id = sub.teacher_id
JOIN
    grades g ON sub.id = g.subject_id
JOIN
    students s ON g.student_id = s.id
WHERE
    t.first_name = 'John'
    AND s.first_name = 'Alice'
GROUP BY
    t.id, s.id;
