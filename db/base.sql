create table mc_store (
	mc_id int primary key auto_increment,
	mc_name varchar(1000),
	mc_address varchar(2000),
	mc_address_line varchar(1000),
	mc_state varchar(256),
	mc_city varchar(512),
	mc_postcode varchar(8),
	mc_email varchar(512),
	mc_latitude double,
	mc_longtitude double,
	mc_telephone numeric
);

create table mc_store_fac (
	mcf_id int primary key auto_increment ,
	mcf_cat_id int ,
	mcf_cat_name varchar(1000),
	mcf_store_id int,
	foreign key (mcf_store_id) references mc_store(mc_id) on delete cascade
)