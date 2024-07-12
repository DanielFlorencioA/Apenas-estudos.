CREATE DATABASE IF NOT EXISTS meu_estoque;

-- Seleciona o banco de dados --
USE meu_estoque;

-- Cria a tabela estoque --
CREATE TABLE IF NOT EXISTS estoque (

	id INT AUTO_INCREMENT PRIMARY KEY,  -- ID único para cada usuário
    nome VARCHAR(100) NOT NULL,          -- Nome do usuário
	marca VARCHAR(20) NOT NULL UNIQUE,   -- NOT NULL obrigado que o usuario especifique oque como será preenchido --
    modelo TEXT,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL,
    em_estoque TINYINT(1),
    imagem BLOB,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data e hora de criação do registro
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Data e hora da última atualização do registro
    
);

-- Seleciona o banco de dados
USE meu_estoque;

-- Exemplo de inserção de dados na tabela `estoque`
INSERT INTO estoque (nome, marca, modelo, preco, quantidade) VALUES
('John Doe', 'Nike', 'verde',1.0000, 30),
('Jane Smith', 'Adidas', 'azul', 500.00, 50);

-- Atualizar dados na tabela `estoque`
UPDATE estoque
SET 
    nome = 'João',        -- Novo valor para a coluna `nome`
    marca = 'Puma' -- Novo valor para a coluna `marca`
WHERE 
    id = 1;                    -- Condição para encontrar o registro correto (por exemplo, id = 1)

-- Verificando se o update foi realizado com sucesso
SELECT * FROM estoque WHERE id = 1;





