-- =========================
-- INSERTs
-- =========================

-- Usuários
INSERT INTO Usuario (Nome, email, senha, dataNasc) VALUES
('Ana Souza',     'ana.souza@email.com',     'ana123',     '1990-03-15'),
('Carlos Lima',   'carlos.lima@email.com',   'carlos123',  '1985-07-22'),
('Mariana Costa', 'mariana.costa@email.com', 'mari123',    '1995-11-08'),
('Pedro Alves',   'pedro.alves@email.com',   'pedro123',   '1988-01-30');

-- Tipos de Dor
INSERT INTO TipoDor (Nome, descricao, regiao_corpo) VALUES
('Cervicalgia',              'Dor na região do pescoço',              'Pescoço'),
('Lombalgia',                'Dor na região lombar da coluna',         'Lombar'),
('Tendinite',                'Inflamação nos tendões do punho/ombro',  'Punho'),
('Síndrome Túnel do Carpo',  'Compressão do nervo mediano',           'Mão'),
('Dorsalgia',                'Dor na região dorsal da coluna',         'Costas');

-- Alongamentos
INSERT INTO Alongamento (nome, descricao, duracao) VALUES
('Rotação Cervical',        'Rotacione a cabeça para cada lado',         30),
('Extensão de Pescoço',     'Incline a cabeça para trás suavemente',     20),
('Alongamento Lombar',      'Abrace os joelhos contra o peito',          40),
('Inclinação Lateral',      'Incline o tronco com braço estendido',      30),
('Extensão de Punho',       'Estenda o braço e puxe os dedos para trás', 20),
('Flexão de Punho',         'Dobre o punho para baixo com outra mão',    20),
('Alongamento do Trapézio', 'Incline a cabeça lateralmente',             30),
('Abertura de Peito',       'Entrelace mãos atrás e abra o peito',       25);

-- Recomendações de Alongamento (TipoDor + Alongamento + Usuário)
INSERT INTO recomendacao_along (TipoDor_idTipoDor, Alongamento_idAl, Usuario_idUsuario) VALUES
(1, 1, 1),  
(1, 2, 1), 
(1, 7, 1), 
(2, 3, 2), 
(2, 4, 2),
(3, 5, 3), 
(3, 6, 3), 
(4, 5, 3), 
(5, 8, 4), 
(5, 4, 4); 

-- Histórico de Alongamentos
INSERT INTO HistoricoAlon (Alongamento_idAl, Usuario_idUsuario, Inicio, tempoTotal, dataFim) VALUES
(1, 1, '2025-05-27 09:00:00', 30, '2025-05-27 09:00:30'),
(7, 1, '2025-05-27 10:00:00', 30, '2025-05-27 10:00:30'),
(3, 2, '2025-05-27 10:30:00', 40, '2025-05-27 10:31:10'),
(5, 3, '2025-05-27 11:00:00', NULL, NULL),
(8, 4, '2025-05-27 09:30:00', 25, '2025-05-27 09:30:25'),
(4, 4, '2025-05-27 10:00:00', 30, '2025-05-27 10:00:30');

-- Jornadas de Trabalho
INSERT INTO JornadaTrabalho (inicioJornd, tempoLembrete, Usuario_idUsuario, fimJornd) VALUES
('2025-05-27 08:00:00', 60, 1, '2025-05-27 17:00:00'),
('2025-05-27 09:00:00', 45, 2, '2025-05-27 18:00:00'),
('2025-05-27 07:30:00', 90, 3, '2025-05-27 16:30:00'),
('2025-05-27 08:00:00', 30, 4, NULL);

-- Pausas
INSERT INTO Pausas (inicio, fim, concluida, Usuario_idUsuario) VALUES
('2025-05-27 09:00:00', '2025-05-27 09:01:00', 'concluida', 1),
('2025-05-27 10:00:00', '2025-05-27 10:01:00', 'concluida', 1),
('2025-05-27 10:30:00', '2025-05-27 10:31:00', 'concluida', 2),
('2025-05-27 11:00:00', NULL,                  'ignorada',  3),
('2025-05-27 09:30:00', '2025-05-27 09:30:25', 'concluida', 4),
('2025-05-27 10:00:00', NULL,                  'pendente',  4);
