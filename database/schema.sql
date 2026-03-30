-- PLAYMC.PL - Database Schema v3.1
-- Created for High Performance Minecraft Shop System

CREATE DATABASE IF NOT EXISTS playmc_shop;
USE playmc_shop;

-- Tabela przechowująca wszystkie zakupy
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_nick VARCHAR(16) NOT NULL,
    rank_name VARCHAR(32) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'PLN',
    payment_method ENUM('PayPal', 'PSC', 'SMS', 'Transfer') DEFAULT 'PayPal',
    transaction_id VARCHAR(100) UNIQUE,
    status ENUM('PENDING', 'COMPLETED', 'FAILED') DEFAULT 'PENDING',
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela do logów bezpieczeństwa
CREATE TABLE IF NOT EXISTS security_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(45),
    action VARCHAR(255),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Przykładowe zapytanie do sprawdzania ile zarobił serwer:
-- SELECT SUM(price) FROM orders WHERE status = 'COMPLETED';