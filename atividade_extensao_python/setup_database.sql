-- Criar o banco de dados 
CREATE DATABASE IF NOT EXISTS banco_de_dados;

-- Usar o banco de dados criado
USE banco_de_dados;

-- Criar a tabela 'relatorio'
CREATE TABLE IF NOT EXISTS relatorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    equipamento VARCHAR(255) NOT NULL,
    bmp VARCHAR(255) NOT NULL,
    problema TEXT NOT NULL
);


