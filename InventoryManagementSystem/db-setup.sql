-- Create Database
CREATE DATABASE IF NOT EXISTS inventory_management;

-- Use the Database
USE inventory_management;

-- Create Table
CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    serial_number VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL
);

