
INSERT OR IGNORE INTO Usuario (idUsuario, Nome, email, senha, dataNasc) VALUES
(1, 'Ana Souza',     'ana.souza@email.com',     'ana123',     '1990-03-15'),
(2, 'Carlos Lima',   'carlos.lima@email.com',   'carlos123',  '1985-07-22'),
(3, 'Mariana Costa', 'mariana.costa@email.com', 'mari123',    '1995-11-08'),
(4, 'Pedro Alves',   'pedro.alves@email.com',   'pedro123',   '1988-01-30');

INSERT OR IGNORE INTO TipoDor (idTipoDor, Nome, descricao, regiao_corpo) VALUES
(1, 'Cervicalgia',              'Dor na região do pescoço',              'Pescoço'),
(2, 'Lombalgia',                'Dor na região lombar da coluna',         'Lombar'),
(3, 'Tendinite',                'Inflamação nos tendões do punho/ombro',  'Punho'),
(4, 'Síndrome Túnel do Carpo',  'Compressão do nervo mediano',           'Mão'),
(5, 'Dorsalgia',                'Dor na região dorsal da coluna',         'Costas');

INSERT OR IGNORE INTO recomendacao_along (TipoDor_idTipoDor, Alongamento_idAl) VALUES
(1, 1), (1, 2), (1, 7), (1, 9), 
(2, 3), (2, 4), (2, 10),
(3, 5), (3, 6), (3, 11), 
(4, 5), (4, 12), 
(5, 8), (5, 4), (5, 13), (5, 14);

INSERT OR IGNORE INTO Alongamento (id, nome, descricao, duracao) VALUES
(1, 'Rotação Cervical',        'Rotacione a cabeça para cada lado',        30),
(2, 'Extensão de Pescoço',     'Incline a cabeça para trás suavemente',    20),
(3, 'Alongamento Lombar',      'Abrace os joelhos contra o peito',         40),
(4, 'Inclinação Lateral',      'Incline o tronco com braço estendido',     30),
(5, 'Extensão de Punho',       'Estenda o braço e puxe os dedos para trás', 20),
(6, 'Flexão de Punho',         'Dobre o punho para baixo com outra mão',   20),
(7, 'Alongamento do Trapézio', 'Incline a cabeça lateralmente',            30),
(8, 'Abertura de Peito',       'Entrelace mãos atrás e abra o peito',      25),
(9, 'Elevação de Ombros',      'Eleve os ombros até as orelhas e relaxe',  20),
(10, 'Torção de Tronco',       'Gire o tronco segurando na cadeira',       30),
(11, 'Rotação de Punhos',      'Gire os punhos suavemente em círculos',    20),
(12, 'Estiramento de Dedos',   'Abra as mãos e afaste bem os dedos',       15),
(13, 'Abraço de Urso',         'Abrace a si mesmo curvando as costas',     25),
(14, 'Flexão à Frente',        'Deixe o corpo cair sobre as pernas',       40);

INSERT OR IGNORE INTO JornadaTrabalho (nome, inicioJornd, tempoLembrete, Usuario_idUsuario, fimJornd) VALUES
('Foco Matinal', '2025-05-27 08:00:00', 60, 1, '2025-05-27 17:00:00'),
('Projeto AlongFit', '2025-05-27 09:00:00', 45, 2, '2025-05-27 18:00:00'),
('Estudos', '2025-05-27 07:30:00', 90, 3, '2025-05-27 16:30:00'),
('Trabalho Geral', '2025-05-27 08:00:00', 30, 4, NULL);

INSERT OR IGNORE INTO Pausas (inicio, fim, concluida, Usuario_idUsuario) VALUES
('2025-05-27 09:00:00', '2025-05-27 09:01:00', 'concluida', 1),
('2025-05-27 10:00:00', '2025-05-27 10:01:00', 'concluida', 1),
('2025-05-27 10:30:00', '2025-05-27 10:31:00', 'concluida', 2),
('2025-05-27 11:00:00', NULL,                  'ignorada',  3),
('2025-05-27 09:30:00', '2025-05-27 09:30:25', 'concluida', 4),
('2025-05-27 10:00:00', NULL,                  'pendente',  4);

INSERT OR IGNORE INTO HistoricoAlon (Alongamento_idAl, Usuario_idUsuario, tipoDor_idTipoDor, Inicio, tempoTotal, dataFim) VALUES
(1, 1, 1, '2026-05-25 09:00:00', 30, '2026-05-25 09:00:30'), 
(2, 1, 1, '2026-05-26 10:00:00', 20, '2026-05-26 10:00:20'),
(3, 1, 1, '2026-05-27 14:00:00', 45, '2026-05-27 14:00:45'), 
(4, 1, 2, '2026-05-28 16:30:00', 30, '2026-05-28 16:30:30'), 
(5, 1, 3, '2026-05-29 11:00:00', 20, '2026-05-29 11:00:20'),
(6, 1, 1, '2026-05-30 09:15:00', 30, '2026-05-30 09:15:30'), 
(1, 1, 4, '2026-05-31 18:00:00', 60, '2026-05-31 18:01:00');