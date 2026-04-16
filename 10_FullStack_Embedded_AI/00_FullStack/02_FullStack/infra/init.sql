-- Create user if not exists
DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'ferganey') THEN
      CREATE USER ferganey WITH PASSWORD 'postgres';
   END IF;
END
$$;

-- Create database if not exists and set owner to 'ferganey'
DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'myapp_db') THEN
      CREATE DATABASE myapp_db OWNER ferganey;
   END IF;
END
$$;

-- Connect to the new database
\connect myapp_db;

-- Ensure schema exists
CREATE SCHEMA IF NOT EXISTS public AUTHORIZATION ferganey;

-- Grant privileges to app user
GRANT CONNECT ON DATABASE myapp_db TO ferganey;
GRANT ALL PRIVILEGES ON DATABASE myapp_db TO ferganey;
GRANT USAGE ON SCHEMA public TO ferganey;

-- Create tables

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS stores (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city_id INTEGER NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    owner_id INTEGER NOT NULL REFERENCES users(id) ON DELETE SET NULL
);

-- Many-to-many relation: store can have many customers (users)
CREATE TABLE IF NOT EXISTS store_customers (
    store_id INTEGER NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (store_id, user_id)
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    store_id INTEGER NOT NULL REFERENCES stores(id) ON DELETE CASCADE,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE
);

-- Change ownership of all tables to ferganey
ALTER TABLE users OWNER TO ferganey;
ALTER TABLE countries OWNER TO ferganey;
ALTER TABLE cities OWNER TO ferganey;
ALTER TABLE categories OWNER TO ferganey;
ALTER TABLE stores OWNER TO ferganey;
ALTER TABLE store_customers OWNER TO ferganey;
ALTER TABLE products OWNER TO ferganey;

-- Future permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ferganey;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ferganey;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ferganey;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ferganey;

