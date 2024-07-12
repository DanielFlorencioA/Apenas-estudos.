CREATE DATABASE IF NOT EXISTS Disco_Vinil;

USE Disco_Vinil;

CREATE TABLE IF NOT EXISTS Vinil (
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    artista VARCHAR(50),
    ano INT,
    genero VARCHAR(50),
    alugado BOOLEAN,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE Disco_Vinil;

INSERT INTO Vinil (titulo, artista, ano, genero, alugado) VALUES ("Construção", "Chico Buarque", 1968, "MPB", FALSE);
INSERT INTO Vinil (titulo, artista, ano, genero, alugado) VALUES ("Sem Crise", "Gabriel Pensador", 1990, "RAP", FALSE);
INSERT INTO Vinil (titulo, artista, ano, genero, alugado) VALUES ("Alvorada", "Cartola", 1950, "Sampa", FALSE);

SELECT * FROM Vinil;

UPDATE Vinil SET alugado = TRUE WHERE id = 1;

DELETE FROM Vinil WHERE titulo = "Sem Crise";