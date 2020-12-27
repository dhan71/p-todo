-- todo structure

CREATE TABLE IF NOT EXISTS todo
(
  id          integer  primary key autoincrement
, priority    integer
, begin_date  datetime
, end_date    datetime
, group_id    text
, title       text
, contents    text
);
