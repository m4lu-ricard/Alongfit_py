-- =========================================
-- INSERTs SEGUROS (Usa OR IGNORE para não dar erro)
-- =========================================

-- Usuários
INSERT OR IGNORE INTO Usuario (idUsuario, Nome, email, senha, dataNasc) VALUES
(1, 'Ana Souza',     'ana.souza@email.com',     'ana123',     '1990-03-15'),
(2, 'Carlos Lima',   'carlos.lima@email.com',   'carlos123',  '1985-07-22'),
(3, 'Mariana Costa', 'mariana.costa@email.com', 'mari123',    '1995-11-08'),
(4, 'Pedro Alves',   'pedro.alves@email.com',   'pedro123',   '1988-01-30');

-- Tipos de Dor
INSERT OR IGNORE INTO TipoDor (idTipoDor, Nome, descricao, regiao_corpo) VALUES
(1, 'Cervicalgia',              'Dor na região do pescoço',              'Pescoço'),
(2, 'Lombalgia',                'Dor na região lombar da coluna',         'Lombar'),
(3, 'Tendinite',                'Inflamação nos tendões do punho/ombro',  'Punho'),
(4, 'Síndrome Túnel do Carpo',  'Compressão do nervo mediano',           'Mão'),
(5, 'Dorsalgia',                'Dor na região dorsal da coluna',         'Costas');

-- Alongamentos
INSERT OR IGNORE INTO Alongamento (id, nome, descricao, duracao) VALUES
(1, 'Rotação Cervical',        'Rotacione a cabeça para cada lado',         30),
(2, 'Extensão de Pescoço',     'Incline a cabeça para trás suavemente',     20),
(3, 'Alongamento Lombar',      'Abrace os joelhos contra o peito',          40),
(4, 'Inclinação Lateral',      'Incline o tronco com braço estendido',      30),
(5, 'Extensão de Punho',       'Estenda o braço e puxe os dedos para trás', 20),
(6, 'Flexão de Punho',         'Dobre o punho para baixo com outra mão',    20),
(7, 'Alongamento do Trapézio', 'Incline a cabeça lateralmente',             30),
(8, 'Abertura de Peito',       'Entrelace mãos atrás e abra o peito',       25);

-- Recomendações de Alongamento (TipoDor + Alongamento + Usuário)
INSERT OR IGNORE INTO recomendacao_along (TipoDor_idTipoDor, Alongamento_idAl, Usuario_idUsuario) VALUES
(1, 1, 1), (1, 2, 1), (1, 7, 1), 
(2, 3, 2), (2, 4, 2),
(3, 5, 3), (3, 6, 3), (4, 5, 3), 
(5, 8, 4), (5, 4, 4); 

-- Histórico de Alongamentos (Os testes do Progresso Semanal da Ana Souza!)
INSERT OR IGNORE INTO HistoricoAlon (Alongamento_idAl, Usuario_idUsuario, tipoDor_idTipoDor, Inicio, tempoTotal, dataFim) VALUES
(1, 1, 1, '2025-05-25 09:00:00', 30, '2025-05-25 09:00:30'), 
(2, 1, 1, '2025-05-26 10:00:00', NULL, NULL),                
(3, 1, 1, '2025-05-27 14:00:00', 45, '2025-05-27 14:00:45'), 
(4, 1, 2, '2025-05-28 16:30:00', 30, '2025-05-28 16:30:30'), 
(5, 1, 3, '2025-05-29 11:00:00', NULL, NULL),                
(6, 1, 1, '2025-05-30 09:15:00', 30, '2025-05-30 09:15:30'), 
(1, 1, 4, '2025-05-31 18:00:00', 60, '2025-05-31 18:01:00');

-- Jornadas de Trabalho
INSERT OR IGNORE INTO JornadaTrabalho (nome, inicioJornd, tempoLembrete, Usuario_idUsuario, fimJornd) VALUES
('Foco Matinal', '2025-05-27 08:00:00', 60, 1, '2025-05-27 17:00:00'),
('Projeto AlongFit', '2025-05-27 09:00:00', 45, 2, '2025-05-27 18:00:00'),
('Estudos', '2025-05-27 07:30:00', 90, 3, '2025-05-27 16:30:00'),
('Trabalho Geral', '2025-05-27 08:00:00', 30, 4, NULL);

-- Pausas
INSERT OR IGNORE INTO Pausas (inicio, fim, concluida, Usuario_idUsuario) VALUES
('2025-05-27 09:00:00', '2025-05-27 09:01:00', 'concluida', 1),
('2025-05-27 10:00:00', '2025-05-27 10:01:00', 'concluida', 1),
('2025-05-27 10:30:00', '2025-05-27 10:31:00', 'concluida', 2),
('2025-05-27 11:00:00', NULL,                  'ignorada',  3),
('2025-05-27 09:30:00', '2025-05-27 09:30:25', 'concluida', 4),
('2025-05-27 10:00:00', NULL,                  'pendente',  4);