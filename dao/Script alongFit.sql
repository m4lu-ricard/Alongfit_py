PRAGMA foreign_keys = ON;

-- TABELA Usuario
-- =========================

CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,

    nome VARCHAR(45) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    data_nasc DATE NOT NULL
);

-- TABELA Tipo_dor
-- =========================

CREATE TABLE Tipo_dor (
    id_tipo_dor INTEGER PRIMARY KEY AUTOINCREMENT,

    nome VARCHAR(45) NOT NULL,
    descricao VARCHAR(100),
    regiao_corpo VARCHAR(45)
);

-- TABELA Usuario_dor
-- =========================

CREATE TABLE Usuario_dor (
    id_usuario_dor INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario_id INTEGER NOT NULL,
    tipo_dor_id INTEGER NOT NULL,

    intensidade INTEGER,
    frequencia VARCHAR(20),
    observacao VARCHAR(255),

    FOREIGN KEY (usuario_id)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (tipo_dor_id)
        REFERENCES Tipo_dor(id_tipo_dor)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- TABELA Alongamento
-- =========================

CREATE TABLE Alongamento (
    id_alongamento INTEGER PRIMARY KEY AUTOINCREMENT,

    nome VARCHAR(45) NOT NULL,
    descricao VARCHAR(100),
    duracao INTEGER
);


-- TABELA Alongamento_tipo_dor
-- =========================

CREATE TABLE Alongamento_tipo_dor (
    alongamento_id INTEGER NOT NULL,
    tipo_dor_id INTEGER NOT NULL,

    PRIMARY KEY (alongamento_id, tipo_dor_id),

    FOREIGN KEY (alongamento_id)
        REFERENCES Alongamento(id_alongamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (tipo_dor_id)
        REFERENCES Tipo_dor(id_tipo_dor)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


-- TABELA Jornada_trabalho
-- =========================

CREATE TABLE Jornada_trabalho (
    id_jornada INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario_id INTEGER NOT NULL,

    inicio_jornada DATETIME NOT NULL,
    fim_jornada DATETIME,

    intervalo_lembrete_min INTEGER NOT NULL,

    FOREIGN KEY (usuario_id)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

 TABELA Pausas
-- =========================

CREATE TABLE Pausas (
    id_pausa INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario_id INTEGER NOT NULL,
    alongamento_id INTEGER NOT NULL,

    inicio DATETIME,
    fim DATETIME,

    status VARCHAR(20),

    FOREIGN KEY (usuario_id)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (alongamento_id)
        REFERENCES Alongamento(id_alongamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


 TABELA Historico_alongamento
-- =========================

CREATE TABLE Historico_alongamento (
    id_historico INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario_id INTEGER NOT NULL,
    alongamento_id INTEGER NOT NULL,

    inicio DATETIME NOT NULL,
    data_fim DATETIME,

    tempo_total INTEGER,

    FOREIGN KEY (usuario_id)
        REFERENCES Usuario(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (alongamento_id)
        REFERENCES Alongamento(id_alongamento)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
