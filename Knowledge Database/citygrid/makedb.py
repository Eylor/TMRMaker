import sqlite3
conn = sqlite3.connect('LEIA.db')
c = conn.cursor()
c.execute('''CREATE TABLE location (loc_id integer primary key asc, city text default "", postal_code text default "", state text default "", street text default "", latitude real default 0.0, longitude real default 0.0)''')
c.execute('''create table restaurant (rest_id integer primary key asc, rest_name text not null, rating real default 5.0, rest_location int not null, phone text, open int default 0, foreign key (rest_location) references location(loc_id))''')
c.execute('''create table categories (cat_id integer primary key asc, cat_name text not null, parent_id integer, parent_name text)''')
c.execute('''create table cat_matching (match_id integer primary key asc, rest_id integer, cat_id integer, foreign key (rest_id) references restaurant(rest_id), foreign key (cat_id) references categories(cat_id))''')
c.execute('''create table social_circle (circle_id integer primary key asc, human_id integer, friend_id integer)''')
c.execute('''create table pref_cuisine(taste_id integer primary key asc, human_id integer, cat_id integer)''')
c.execute('''create table kin(kin_id integer primary key asc, human_id integer, relative_id integer, kin_relation text)''')
c.execute('''create table possessions(possession_id integer primary key asc, human_id integer, possession_name text)''')
c.execute('''create table rest_history(history_id integer primary key asc, human_id integer, rest_id integer, rating real)''')
c.execute('''create table schedule(schedule_id integer primary key asc, is_human integer default 0, rest_id integer, human_id integer, dow integer, start_time real, end_time real)''')
c.execute('''create table human(human_id integer primary key asc, name text, gender text, age integer, mood text, kindness real, home_addr integer, work_addr integer)''')
conn.commit()
conn.close()
