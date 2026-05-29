PRAGMA foreign_keys = ON;

-- =========================
-- TABELA Usuario
-- =========================
CREATE TABLE Usuario (
    idUsuario   INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        VARCHAR(45)  NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    senha       VARCHAR(255) NOT NULL,
    dataNasc    DATE         NOT NULL
);

-- =========================
-- TABELA TipoDor
-- =========================
CREATE TABLE TipoDor (
    idTipoDor     INTEGER PRIMARY KEY AUTOINCREMENT,
    nome          VARCHAR(45)  NOT NULL,
    descricao     VARCHAR(100),
    regiao_corpo  VARCHAR(45)
);

-- =========================
-- TABELA Alongamento
-- =========================
CREATE TABLE Alongamento (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            VARCHAR(45) NOT NULL,
    descricao       VARCHAR(100),
    duracao         INTEGER
);

-- =========================
-- TABELA recomendacao_along
-- Associativa entre Alongamento e TipoDor
-- =========================
CREATE TABLE recomendacao_along (
    tipoDor_idTipoDor   INTEGER NOT NULL,
    alongamento_idAl    INTEGER NOT NULL,

    PRIMARY KEY (
        tipoDor_idTipoDor,
        alongamento_idAl
    ),

    FOREIGN KEY (tipoDor_idTipoDor)
        REFERENCES TipoDor(idTipoDor)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (alongamento_idAl)
        REFERENCES Alongamento(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================
-- TABELA JornadaTrabalho
-- =========================
CREATE TABLE JornadaTrabalho (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,

    inicioJornd           DATETIME NOT NULL,
    fimJornd              DATETIME,
    
     tempo                 INTEGER,
    tempoLembrete         INTEGER NOT NULL,

    usuario_idUsuario     INTEGER NOT NULL,
    tipoDor_idTipoDor     INTEGER NOT NULL,

    FOREIGN KEY (usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (tipoDor_idTipoDor)
        REFERENCES TipoDor(idTipoDor)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================
-- TABELA HistoricoAlon
-- =========================
CREATE TABLE HistoricoAlon (
    idHisto               INTEGER PRIMARY KEY AUTOINCREMENT,

    alongamento_idAl      INTEGER NOT NULL,
    usuario_idUsuario     INTEGER NOT NULL,

    inicio                DATETIME NOT NULL,
    dataFim               DATETIME,

    tempoTotal            INTEGER,

    FOREIGN KEY (alongamento_idAl)
        REFERENCES Alongamento(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (usuario_idUsuario)
        REFERENCES Usuario(idUsuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
