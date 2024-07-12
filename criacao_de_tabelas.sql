
-- Cria o banco de dados se ele não existir
CREATE DATABASE IF NOT EXISTS banco_de_dados_novas_tabelas;

-- Seleciona o banco de dados
USE banco_de_dados_novas_tabelas;

-- Cria a tabela `bancario`
CREATE TABLE IF NOT EXISTS bancario (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- ID único para cada usuário
    titular VARCHAR(100) NOT NULL,          -- Nome do usuário
    conta VARCHAR(100) NOT NULL UNIQUE,  -- Email do usuário, deve ser único
    senha VARCHAR(255) NOT NULL, -- Senha do usuário
    saldo DECIMAL(8, 2),
    data_nascimento DATE,                -- Data de nascimento do usuário
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data e hora de criação do registro
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Data e hora da última atualização do registro
);

-- Seleciona o banco de dados
USE banco_de_dados_novas_tabelas;

-- Exemplo de inserção de dados na tabela `bancario`
INSERT INTO bancario (titular, conta, senha, saldo, data_nascimento) VALUES
('John Doe', 1877629, 'senha_segura_123', 1000.00, '1999-01-01'),
('Jane Smith', 8761387, 'senha_segura_456', 2000.00, '1985-05-15');

-- Atualizar dados na tabela `bancario`
UPDATE bancario
SET 
    titular = 'João',        -- Novo valor para a coluna `titular`
    conta = 74879809 -- Novo valor para a coluna `conta`
WHERE 
    id = 1;                    -- Condição para encontrar o registro correto (por exemplo, id = 1)

-- Verificando se o update foi realizado com sucesso
SELECT * FROM bancario WHERE id = 1;

 

    