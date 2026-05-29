-- =========================
-- INSERTs
-- =========================

-- Usuários
INSERT INTO Usuario (nome, email, senha, dataNasc) VALUES
('Ana Souza',     'ana.souza@email.com',     'ana123',     '1990-03-15'),
('Carlos Lima',   'carlos.lima@email.com',   'carlos123',  '1985-07-22'),
('Mariana Costa', 'mariana.costa@email.com', 'mari123',    '1995-11-08'),
('Pedro Alves',   'pedro.alves@email.com',   'pedro123',   '1988-01-30');

-- Tipos de Dor
INSERT INTO TipoDor (nome, descricao, regiao_corpo) VALUES
('Cervicalgia',             'Dor na região do pescoço',             'Pescoço'),
('Lombalgia',               'Dor na região lombar da coluna',       'Lombar'),
('Tendinite',               'Inflamação nos tendões',               'Punho'),
('Síndrome Túnel do Carpo', 'Compressão do nervo mediano',          'Mão'),
('Dorsalgia',               'Dor na região dorsal da coluna',       'Costas');

-- Alongamentos
INSERT INTO Alongamento (nome, descricao, duracao) VALUES
('Rotação Cervical',        'Rotacione a cabeça para cada lado',         30),
('Extensão de Pescoço',     'Incline a cabeça para trás suavemente',     20),
('Alongamento Lombar',      'Abrace os joelhos contra o peito',          40),
('Inclinação Lateral',      'Incline o tronco com braço estendido',      30),
('Extensão de Punho',       'Estenda o braço e puxe os dedos',           20),
('Flexão de Punho',         'Dobre o punho para baixo',                  20),
('Alongamento do Trapézio', 'Incline a cabeça lateralmente',             30),
('Abertura de Peito',       'Entrelace mãos atrás e abra o peito',       25);

-- Recomendações de Alongamento
INSERT INTO recomendacao_along (tipoDor_idTipoDor, alongamento_idAl) VALUES
(1, 1),
(1, 2),
(1, 7),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 5),
(5, 8),
(5, 4);

-- Histórico de Alongamentos
INSERT INTO HistoricoAlon (
    alongamento_idAl,
    usuario_idUsuario,
    tipoDor_idTipoDor,
    inicio,
    tempoTotal,
    dataFim
) VALUES
(1, 1, 1, '2025-05-27 09:00:00', 30, '2025-05-27 09:00:30'),
(7, 1, 1, '2025-05-27 10:00:00', 30, '2025-05-27 10:00:30'),
(3, 2, 2, '2025-05-27 10:30:00', 40, '2025-05-27 10:31:10'),
(5, 3, 3, '2025-05-27 11:00:00', NULL, NULL),
(8, 4, 5, '2025-05-27 09:30:00', 25, '2025-05-27 09:30:25'),
(4, 4, 5, '2025-05-27 10:00:00', 30, '2025-05-27 10:00:30');

-- Jornadas de Trabalho
INSERT INTO JornadaTrabalho (
    inicioJornd,
    fimJornd,
    tempo,
    tempoLembrete,
    usuario_idUsuario,
    tipoDor_idTipoDor
) VALUES
('2025-05-27 08:00:00', '2025-05-27 17:00:00', 540, 60, 1, 1),
('2025-05-27 09:00:00', '2025-05-27 18:00:00', 540, 45, 2, 2),
('2025-05-27 07:30:00', '2025-05-27 16:30:00', 540, 90, 3, 3),
('2025-05-27 08:00:00', NULL,                  NULL, 30, 4, 5);
