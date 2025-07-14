dependencies 
requests-html
lxml-html-clean
mysql-connector-python
fastapi
uvicorn
python-dotenv

table 
create table mcdonaldsMalaysia (
	mc_id numeric primary key,
	mc_name varchar(1000),
	mc_address varchar(2000),
	mc_state varchar(256),
	mc_city varchar(512),
	mc_email varchar2(512),
	mc_latitude double,
	mc_longtitude double,
	mc_telephone numeric,
	mc_facility varchar(2000)
);
