CREATE DATABASE IF NOT EXISTS tarefas_db;


USE tarefas_db;

-- Criação da tebla tarefas --
CREATE TABLE IF NOT EXISTS tarefas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    concluida BOOLEAN
);

-- Inserção de dados ma tabela tarefas --
INSERT INTO tarefas (descricao, concluida) VALUES ('Estudar SQL', FALSE);
INSERT INTO tarefas (descricao, concluida) VALUES ('Faxer exercicios de SQL', FALSE);
INSERT INTO tarefas (descricao, concluida) VALUES ('Revisar Python', FALSE);

-- Seleção de dados para visualizar -- 
SELECT * FROM tarefas;

-- Atualização de dados sa minha tabela --
UPDATE tarefas SET concluida = TRUE WHERE id = 1;
