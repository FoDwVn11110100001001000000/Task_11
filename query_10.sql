
SELECT subjects.subj
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE students.id = 19
AND subjects.id = 2
