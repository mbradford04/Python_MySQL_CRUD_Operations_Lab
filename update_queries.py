# create a query to update the last name of Stefanie from teacher table to have
# have a last name of green

update_teacher_table = """
UPDATE teacher
SET last_name = "Greene"
WHERE first_name = "Stefanie";
"""