
CREATE DATABASE IF NOT EXISTS ATIC;


USE ATIC;


CREATE TABLE IF NOT EXISTS relatorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    equipamento VARCHAR(255) NOT NULL,
    bmp VARCHAR(255) NOT NULL,
    problema TEXT NOT NULL
);


