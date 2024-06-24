SELECT
    s.first_name,
    s.last_name,
    g.grade,
    g.date
FROM
    students s
JOIN
    grades g ON s.id = g.student_id
JOIN
    subjects sub ON g.subject_id = sub.id
JOIN
    groups grp ON s.group_id = grp.id
WHERE
    grp.name = 'Group 2'
    AND sub.name = 'Chemistry';
