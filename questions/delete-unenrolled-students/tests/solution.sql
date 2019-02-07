DELETE FROM Students WHERE NOT EXISTS (SELECT * FROM Enrollments WHERE NetId = Students.NetId);
