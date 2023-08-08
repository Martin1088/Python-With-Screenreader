create table users(
    id integer primary key autoincrement,
    name text not null,
    password text not null,
    expert boolean not null default 0,
    admin boolean not null default 0
);
create  table questions (
    
    id integer primary key autoincrement,
    question_text text not null,
    answer_text text,
    asked_by_id integer not null,
    expert_id integer not null

)
