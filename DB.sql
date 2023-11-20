CREATE TABLE Student (
    student_id int NOT NULL,
    email varchar(60) NOT NULL,
    password varchar(80) NOT NULL,
    name varchar(80) NOT NULL,
    login_time time NOT NULL,
    login_date date NOT NULL
);

CREATE TABLE Course (
    course_id int NOT NULL,
    course_name varchar(80) NOT NULL,
    teacher_message text NOT NULL,
    lecture_notes text NOT NULL,
    course_website_link varchar(120) NOT NULL,
    checked BOOLEAN.
    lecture_time time NOT NULL,
    which_day int NOT NULL
);

CREATE TABLE LogIn_Time (
    login_date date NOT NULL,
    start_time time NOT NULL,
    end_time time NOT NULL,
    current_day varchar(20) NOT NULL,
    course_id int NOT NULL
);

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

INSERT INTO Student VALUES (
    1,
    "wngks873@connect.hku.hk",
    "1q2w3e4r!!",
    "joe",
    "00:00:00",
    "2023-11-14"
);

INSERT INTO Course VALUES (
    "COMP3278",
    "INTRO To DBMS",
    "this is a test announcement",
    "https://moodle.hku.hk/mod/resource/view.php?id=3081895",
    "https://moodle.hku.hk/course/view.php?id=106523",
    1,
    "14:30:00,15:30:00",
    12
);