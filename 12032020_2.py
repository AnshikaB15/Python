"""
    Class to hold functionality related to students in a college.
        Every student should be able to -
            1. Register to college, by providing ID, First Name, Last Name, Country, Course
                Ex: ram = Student(100, "Ram", "X", "USA", "B.Tech")
                    The registration should fail in below cases -
                        (a) If Country is not USA (because we are accepting students from USA only)
                        (b) If Course is anything other than "B.Tech", "B.Law", "B.Arts" (because we are running only these 3 courses)
                        (c) If First Name is made up of anything other than Alphabets
                        (d) If Last Name is made up of anything other than Alphabets
                        
            2. Student should be able to upload marks from latest exams
                Ex: ram.marks_science(100)
                    ram.marks_math(90)
                    ram.marks_arts(50)

                    This should fail if the marks are not between 0 and 100.

            3. Student should be able to see the total, average marks.
"""
