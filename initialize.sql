--How to Run:
-----------

--Initialize with:  psql -U isdb -d postgres -f initialize.sql

--Run with:  python us01-find-bug-comments.py
--or        python us01-find-bug-comments-sql-fn.py

\c postgres

drop database if exists airbnb;
create database airbnb;
\c airbnb
\i create.sql 

\copy Users FROM 'Users.csv' csv header;
\copy Guests FROM 'Guests.csv' csv header;
\copy Hosts FROM 'Hosts.csv' csv header;
\copy Products FROM 'Products.csv' csv header;
\copy Properties FROM 'Properties.csv' csv header;
\copy Experiences FROM 'Experiences.csv' csv header;
\copy Bookings(check_in_date,check_out_date,price,booking_status,updated_date,guest_id,product_id) FROM 'Bookings.csv' csv header;
\copy Messages(message_content,date,time,guest_id,host_id) FROM 'Messages.csv' csv header;
\copy Reviews FROM 'Reviews.csv' csv header;
\copy Saves FROM 'Saves.csv' csv header;


