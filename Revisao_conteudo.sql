CREATE DATABASE IF NOT EXISTS videolocadora;

USE videolocadora;

CREATE TABLE filmes (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    titulo VARCHAR(50) NOT NULL,
    diretor VARCHAR(40) NOT NULL,
    ano INT NOT NULL,
    genero VARCHAR(200) NOT NULL
);

INSERT INTO filmes (titulo, diretor, ano, genero) VALUES ("Impacto profundo", "Arnol shalneger", 1990, "Comedia" );
INSERT INTO filmes (titulo, diretor, ano, genero) VALUES ("Matrix", "Neo", 1999, "Ação" );

SELECT titulo FROM filmes;

UPDATE filmes SET titulo = "A procura de um milagre" WHERE titulo = "Impacto profundo";

DELETE FROM filmes WHERE titulo = "Matrix";