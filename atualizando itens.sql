USE banco_de_dados_novas_tabelas;

UPDATE estoque
SET 
	em_estoque = 0
WHERE 
	nome = 'Caneta';