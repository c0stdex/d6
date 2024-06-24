SELECT
    sub.name AS subject_name
FROM
    subjects sub
JOIN
    teachers t ON sub.teacher_id = t.id
WHERE
    t.first_name = 'John';
