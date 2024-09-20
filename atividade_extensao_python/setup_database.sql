-- Criar o banco de dados 
CREATE DATABASE IF NOT EXISTS ATIC;

-- Usar o banco de dados criado
USE ATIC;

-- Criar a tabela 'relatorio'
CREATE TABLE IF NOT EXISTS relatorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    equipamento VARCHAR(255) NOT NULL,
    bmp VARCHAR(255) NOT NULL,
    problema TEXT NOT NULL
);


