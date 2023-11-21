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


CREATE TABLE Student_takingcourses (
    student_id varchar(10) NOT NULL,
    course_id varchar(1024) NOT NULL
);

/* student information in who's taking which courses */
INSERT INTO Student_takingcourses VALUES
    ('3035678110', '{COMP3278 ELEC3143 MECH2407 ELEC2243 BSTC2022}'),
    ('3035678111', '{COMP3278 GEOG1021 MECH4412 IMSE4175}'),
    ('3035661360', '{COMP3278 ELEC3143 MECH2407 ELEC2243 BSTC2022}');

CREATE TABLE Course (
    course_id varchar(8) NOT NULL,
    course_name varchar(80) NOT NULL,
    teacher_message text NOT NULL,
    tutorial_notes text NOT NULL,
    course_website_link varchar(120) NOT NULL,
    checked BOOLEAN,
    course_start_time time NOT NULL,
    course_end_time time NOT NULL,
    class_day varchar(10)
    class_location varchar(10)
);

INSERT INTO Course VALUES
    ("COMP3278", "Introduction to database management systems", "Welcome to the course COMP3278", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1060", null, "14:30:00", "15:20:00", "Monday", "MWT1"),
    ("COMP3278", "Introduction to database management systems", "Welcome to the course COMP3278", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1060", null, "13:30:00", "15:20:00", "Thursday", "MWT1"),
    ("ELEC3143", "Power Electronics", "Welcome to the course ELEC3143", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1059", null, "09:30:00", "10:20:00", "Tuesday", "CBC"),
    ("ELEC3143", "Power Electronics", "Welcome to the course ELEC3143", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1059", null, "09:30:00", "11:20:00", "Friday", "CBC"),
    ("MECH2407", "Multivariable calculus and partial differential equations", "Welcome to the course MECH2407", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1060", null, "10:30:00", "11:20:00", "Tuesday", "TT404"),
    ("MECH2407", "Multivariable calculus and partial differential equations ", "Welcome to the course MECH2407", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1060", null, "10:30:00", "11:20:00", "Thursday", "TT404"),
    ("BSTC2022", "Evolution of Buddhist meditation", "Welcome to the course BSTC2022", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "16:30:00", "18:20:00", "Thursday", "CPD 2.16"),
    ("CHIN9511", "Cantonese as a foreign language I", "Welcome to the course CHIN9511", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "12:30:00", "14:20:00", "Monday", "CPD LG.37"),
    ("CHIN9511", "Cantonese as a foreign language I", "Welcome to the course CHIN9511", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "12:30:00", "14:20:00", "Friday", "CPD G.03"),
    ("ACCT4104", "Advanced financial accounting", "Welcome to the course ACCT4104", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "14:30:00", "17:20:00", "Monday", "LE2"),
    ("ACCT3106", "Management control", "Welcome to the course ACCT3106", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "11:30:00", "12:20:00", "Monday", "CYPP2"),
    ("ACCT3106", "Management control", "Welcome to the course ACCT3106", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "10:30:00", "12:20:00", "Thursday", "CYPP2"),
    ("BIOL4411", "Plant and food biotechnology", "Welcome to the course BIOL4411", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "09:30:00", "11:20:00", "Monday", "MB141"),
    ("COMP3271", "Computer graphics", "Welcome to the course COMP3271", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "12:30:00", "14:20:00", "Monday", "CBA"),
    ("COMP3271", "Computer graphics", "Welcome to the course COMP3271", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "12:30:00", "13:20:00", "Thursday", "CBA"),
    ("COMP3230", "Principles of operating systems", "Welcome to the course COMP3230", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "10:30:00", "12:20:00", "Tuesday", "LE4"),
    ("COMP3230", "Principles of operating systems", "Welcome to the course COMP3230", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "10:30:00", "12:20:00", "Thursday", "LE4"),
    ("CCGL9042", "The evolution of civilization", "Welcome to the course CCGL9042", "Check the website", 
    "https://moodle.hku.hk/course/index.php?categoryid=1037", null, "16:30:00", "18:20:00", "Wednesday", "MB226");

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

/* CREATE TABLE Record (
    currtime timestamp NOT NULL,
    login_duration time NOT NULL,
    student_id int NOT NULL
); */

CREATE TABLE TimeTable (
    table_id int NOT NULL,
    student_id VARCHAR(10) NOT NULL,
    time_table_image LONGBLOB
);

/* student timetable information inserting in with images */

INSERT INTO TimeTable VALUES 
    (1, "3035678110", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_1.png')),
    (2, "3035678111", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_2.png')),
    (3, "3035678112", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_3.png')),
    (4, "3035678113", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_4.png')),
    (5, "3035678114", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_5.png')),
    (6, "3035678115", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_6.png')),
    (7, "3035678116", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_7.png')),
    (8, "3035661360", LOAD_FILE('/home/joe/HKU/dbms_pro/assets/images/timetable_8.png'));
