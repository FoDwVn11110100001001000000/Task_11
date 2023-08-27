
SELECT subjects.subj
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 26
