# Student Class

## Attributes

- `name`: The first and last name of the student
- `student_id`: A unique identification number assigned to the student
- `courses`: A list or collection of courses the student is currently enrolled in
- `grades`: A record or dictionary mapping courses to the student's grades
- `email`: The student's contact email address

## Behaviour

- `register_course(course)`: Enrolls the student in a new course
- `add_grade(course, grade)`: Records a grade for a specified course
- `calculate_gpa()`: Computes and returns the overall average grade or GPA
- `update_email(new_email)`: Updates the student's contact email address
- `__str__()`: Returns a string representation of the student's details