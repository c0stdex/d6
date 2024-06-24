SELECT
    s.first_name,
    s.last_name
FROM
    students s
JOIN
    groups grp ON s.group_id = grp.id
WHERE
    grp.name = 'Group 1';
