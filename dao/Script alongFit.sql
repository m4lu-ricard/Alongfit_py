CREATE DATABASE AlongFit;
USE AlongFit;

-- =========================
-- TABELA USUARIO
-- =========================

CREATE TABLE Usuario (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    dataNasc DATE NOT NULL
);

-- =========================
-- TABELA TIPO DOR
-- =========================

CREATE TABLE TipoDor (
    idTipoDor INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    descricao VARCHAR(100),
    regiao_corpo VARCHAR(45)
);

-- =========================
-- TABELA ALONGAMENTO
-- =========================

CREATE TABLE Alongamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    descricao VARCHAR(250),
    duracao INT NOT NULL
);

-- =========================
-- TABELA USER DOR
-- =========================

CREATE TABLE UserDor (
    TipoDor_idTipoDor INT,
    Usuario_idUsuario INT,

    PRIMARY KEY (TipoDor_idTipoDor, Usuario_idUsuario),

    CONSTRAINT fk_userdor_tipodor
        FOREIGN KEY (TipoDor_idTipoDor)
        REFERENCES TipoDor(idTipoDor)
        ON DELETE CASCADE,

    CONSTRAINT fk_userdor_usuario
        FOREIGN KEY (Usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
);

-- =========================
-- TABELA RECOMENDACAO ALONG
-- =========================

CREATE TABLE recomendacao_along (
    TipoDor_idTipoDor INT,
    Alongamento_idAI INT,

    PRIMARY KEY (TipoDor_idTipoDor, Alongamento_idAI),

    CONSTRAINT fk_recomendacao_tipodor
        FOREIGN KEY (TipoDor_idTipoDor)
        REFERENCES TipoDor(idTipoDor)
        ON DELETE CASCADE,

    CONSTRAINT fk_recomendacao_alongamento
        FOREIGN KEY (Alongamento_idAI)
        REFERENCES Alongamento(id)
        ON DELETE CASCADE
);

-- =========================
-- TABELA HISTORICO
-- =========================

CREATE TABLE HistoricoAlon (
    idHisto INT AUTO_INCREMENT PRIMARY KEY,

    Alongamento_idAI INT NOT NULL,
    Usuario_idUsuario INT NOT NULL,

    Inicio DATETIME NOT NULL,
    tempoTotal INT,
    dataFim DATETIME,

    CONSTRAINT fk_hist_alongamento
        FOREIGN KEY (Alongamento_idAI)
        REFERENCES Alongamento(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_hist_usuario
        FOREIGN KEY (Usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
);

-- =========================
-- TABELA JORNADA TRABALHO
-- =========================

CREATE TABLE JornadaTrabalho (
    id INT AUTO_INCREMENT PRIMARY KEY,

    inicioJornd DATETIME NOT NULL,
    tempoLembrete INT,
    fimJornd DATETIME,

    Usuario_idUsuario INT NOT NULL,

    CONSTRAINT fk_jornada_usuario
        FOREIGN KEY (Usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
);

-- =========================
-- TABELA PAUSAS
-- =========================

CREATE TABLE Pausas (
    idPausas INT AUTO_INCREMENT PRIMARY KEY,

    inicio DATETIME NOT NULL,
    fim DATETIME,
    concluida ENUM('SIM','NAO') DEFAULT 'NAO',

    Usuario_idUsuario INT NOT NULL,

    CONSTRAINT fk_pausa_usuario
        FOREIGN KEY (Usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
);

-- =========================
-- INDEX
-- =========================

CREATE INDEX idx_usuarioDor_usuario
ON UserDor (Usuario_idUsuario);

CREATE INDEX idx_usuarioDor_tipoDor
ON UserDor (TipoDor_idTipoDor);

CREATE INDEX idx_hist_usuario
ON HistoricoAlon (Usuario_idUsuario);

CREATE INDEX idx_hist_alongamento
ON HistoricoAlon (Alongamento_idAI);

-- =========================
-- TRIGGER
-- =========================

DELIMITER $$

CREATE TRIGGER trg_calc_tempo
BEFORE UPDATE ON HistoricoAlon
FOR EACH ROW
BEGIN

    SET NEW.tempoTotal =
    TIMESTAMPDIFF(
        MINUTE,
        NEW.Inicio,
        NEW.dataFim
    );

END $$

DELIMITER ;