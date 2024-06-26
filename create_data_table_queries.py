
create_teacher_table = """
CREATE TABLE teacher(
teacher_id INT PRIMARY KEY,
first_name VARCHAR(100) NOT NULL,
last_name VARCHAR(100) NOT NULL,
language_1 VARCHAR(3) NOT NULL,
dob DATE,
tax_id int UNIQUE,
phone_number VARCHAR(20)
);
"""

create_client_table = """
CREATE TABLE client(
client_id INT PRIMARY KEY,
client_name VARCHAR(50) NOT NULL,
address VARCHAR(100) NOT NULL,
industry VARCHAR(30) NOT NULL
);
"""


create_participant_table = """
CREATE TABLE participant(
participant_id INT PRIMARY KEY,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
phone_no VARCHAR(20),
client INT
);
"""


create_course_table = """
CREATE TABLE course(
course_id INT PRIMARY KEY,
course_name VARCHAR(40) NOT NULL,
language VARCHAR(3) NOT NULL,
level VARCHAR(2),
course_length_weeks INT,
start_date DATE,
in_school BOOLEAN,
teacher INT,
client INT
);
"""