CREATE TABLE Student (
    student_id varchar(10) NOT NULL,
    email varchar(60) NOT NULL,
    pwd varchar(80) NOT NULL,
    username varchar(80) NOT NULL
);

/* student information inserting into student values */
INSERT INTO Student VALUES 
    ('3035678110', "kyoungmin2@connect.hku.hk", "qkrrudals123!@", "Jamie"),
    ('3035678111', "dayekim1@connect.hku.hk", "rlaekdP12!@", "Diana"),
    ('3035678112', "seunghoon2@connect.hku.hk", "dltmdgns123!@", "Kevin"),
    ('3035678113', "hosungkang3@connect.hku.hk", "rkdghtjd12!@", "Harvey"),
    ('3035678114', "dongjunyeom1@connect.hku.hk", "duaehdwns123!@","Andy"),
    ('3035678115', "jihoo2@connect.hku.hk", "rlaekdP12!@", "Jim"),
    ('3035678116', "soheehee@connect.hku.hk", "dlathgml12!@","Helena"),
    ('3035678117', "yuhyun2@connect.hku.hk", "dldbgus123!@", "Mindy"),
    ('3035661360', "wngks873@connect.hku.hk", "1q2w3e4r!!", "joe");

CREATE TABLE Course (
    course_id int NOT NULL,
    course_name varchar(80) NOT NULL,
    teacher_message text NOT NULL,
    tutorial_notes text NOT NULL,
    course_website_link varchar(120) NOT NULL,
    checked BOOLEAN,
    course_start_time time NOT NULL,
    course_end_time time NOT NULL /* added course start and end time here, deleted from the 'LogIn_Time' table below */
);

CREATE TABLE LogIn_Time (
    student_id varchar(10) NOT NULL,
    login_date date NOT NULL,
    login_time time NOT NULL,
    logout_date date NOT NULL,
    logout_time time NOT NULL
);

INSERT INTO LogIn_Time VALUES
    ('3035678110', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678111', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678112', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678113', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678114', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678115', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678116', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035678117', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00"),
    ('3035661360', '2023-11-20', "12:00:00", '2023-11-20', "12:00:00");

CREATE TABLE Record (
    currtime timestamp NOT NULL,
    login_duration time NOT NULL,
    student_id int NOT NULL
);

CREATE TABLE TimeTable (
    table_id int NOT NULL,
    student_id int NOT NULL,
    time_table_image LONGBLOB NOT NULL
);

/* student timetable information inserting in with images */

INSERT INTO TimeTable VALUES 
    (1, 3035678110, LOAD_FILE('/project_DB/timetable_1.png')),
    (2, 3035678111, LOAD_FILE('/project_DB/timetable_2.png')),
    (3, 3035678112, LOAD_FILE('/project_DB/timetable_3.png')),
    (4, 3035678113, LOAD_FILE('/project_DB/timetable_4.png')),
    (5, 3035678114, LOAD_FILE('/project_DB/timetable_5.png')),
    (6, 3035678115, LOAD_FILE('/project_DB/timetable_6.png')),
    (7, 3035678116, LOAD_FILE('/project_DB/timetable_7.png')),
    (8, 3035678117, LOAD_FILE('/project_DB/timetable_8.png'));