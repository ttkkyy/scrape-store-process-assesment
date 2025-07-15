CREATE TABLE IF NOT EXISTS mc_store (
    mc_id SERIAL PRIMARY KEY,
    mc_name VARCHAR(1000),
    mc_address VARCHAR(2000),
    mc_address_line VARCHAR(1000),
    mc_state VARCHAR(256),
    mc_city VARCHAR(512),
    mc_postcode VARCHAR(8),
    mc_email VARCHAR(512),
    mc_latitude DOUBLE PRECISION,
    mc_longitude DOUBLE PRECISION,
    mc_telephone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS mc_store_fac (
    mcf_id SERIAL PRIMARY KEY,
    mcf_cat_id INT,
    mcf_cat_name VARCHAR(1000),
    mcf_store_id INT,
    FOREIGN KEY (mcf_store_id) REFERENCES mc_store(mc_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_store_fac_store_id ON mc_store_fac(mcf_store_id);