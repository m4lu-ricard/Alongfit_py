-- ==========================================
-- USUARIOS
-- ==========================================
SET SQL_SAFE_UPDATES = 0;
INSERT INTO Usuario (Nome, email, senha, dataNasc) VALUES
('Maria Silva', 'maria@email.com', '123456', '2005-01-10'),
('Joao Pedro', 'joao@email.com', '123456', '2004-02-11'),
('Ana Clara', 'ana@email.com', '123456', '2003-03-12'),
('Carlos Henrique', 'carlos@email.com', '123456', '2002-04-13'),
('Julia Souza', 'julia@email.com', '123456', '2001-05-14'),
('Pedro Lucas', 'pedro@email.com', '123456', '2000-06-15'),
('Fernanda Lima', 'fernanda@email.com', '123456', '1999-07-16'),
('Lucas Mendes', 'lucas@email.com', '123456', '1998-08-17'),
('Amanda Costa', 'amanda@email.com', '123456', '1997-09-18'),
('Bruno Alves', 'bruno@email.com', '123456', '1996-10-19'),
('Camila Rocha', 'camila@email.com', '123456', '1995-11-20'),
('Rafael Gomes', 'rafael@email.com', '123456', '1994-12-21'),
('Larissa Martins', 'larissa@email.com', '123456', '1993-01-22'),
('Thiago Ribeiro', 'thiago@email.com', '123456', '1992-02-23'),
('Beatriz Oliveira', 'beatriz@email.com', '123456', '1991-03-24');

-- ==========================================
-- TIPOS DE DOR
-- ==========================================

INSERT INTO TipoDor (Nome, descricao, regiao_corpo) VALUES
('Dor Lombar', 'Dor causada por postura inadequada', 'Coluna'),
('Dor Cervical', 'Dor no pescoco', 'Pescoco'),
('Dor no Ombro', 'Tensao muscular', 'Ombro'),
('Dor no Punho', 'Movimentos repetitivos', 'Punho'),
('Dor no Joelho', 'Desgaste articular', 'Joelho'),
('Dor na Perna', 'Cansaco muscular', 'Perna'),
('Dor nos Pes', 'Sobrecarga muscular', 'Pes'),
('Dor no Braco', 'Esforco repetitivo', 'Braco'),
('Dor nas Costas', 'Postura inadequada', 'Costas'),
('Dor de Cabeca', 'Tensao muscular', 'Cabeca'),
('Dor no Quadril', 'Movimentos incorretos', 'Quadril'),
('Dor na Mao', 'Uso excessivo', 'Mao'),
('Dor no Tornozelo', 'Impacto repetitivo', 'Tornozelo'),
('Dor Muscular', 'Exercicio intenso', 'Corpo'),
('Dor Articular', 'Inflamacao articular', 'Articulacoes');

-- ==========================================
-- ALONGAMENTOS
-- ==========================================

INSERT INTO Alongamento (nome, descricao, duracao) VALUES
('Alongamento Lombar', 'Incline o tronco lentamente por 10 segundos', 10),
('Rotacao de Pescoco', 'Gire o pescoco lentamente por 10 segundos', 10),
('Alongamento Ombro', 'Movimente os ombros lentamente', 8),
('Alongamento Punho', 'Rotacione os punhos suavemente', 5),
('Alongamento Joelho', 'Flexione os joelhos lentamente', 7),
('Alongamento Perna', 'Toque os pes sem dobrar os joelhos', 12),
('Alongamento Pes', 'Gire os pes em circulos lentos', 6),
('Alongamento Bracos', 'Estique os bracos acima da cabeca', 9),
('Alongamento Costas', 'Alongue as costas sentado', 10),
('Relaxamento Facial', 'Respire profundamente e relaxe o rosto', 3),
('Alongamento Quadril', 'Movimente o quadril lentamente', 11),
('Alongamento Maos', 'Abra e feche as maos lentamente', 4),
('Alongamento Tornozelo', 'Gire os tornozelos devagar', 6),
('Alongamento Corpo Inteiro', 'Estique o corpo completamente', 15),
('Alongamento Articular', 'Movimente as articulacoes suavemente', 13);

-- ==========================================
-- USER DOR
-- ==========================================

INSERT INTO UserDor (TipoDor_idTipoDor, Usuario_idUsuario) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10),
(11,11),
(12,12),
(13,13),
(14,14),
(15,15);

-- ==========================================
-- RECOMENDACAO ALONG
-- ==========================================

INSERT INTO recomendacao_along (TipoDor_idTipoDor, Alongamento_idAI) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8),
(9,9),
(10,10),
(11,11),
(12,12),
(13,13),
(14,14),
(15,15);

-- ==========================================
-- HISTORICO ALONGAMENTO
-- PRIMEIRO INSERT
-- ==========================================

INSERT INTO HistoricoAlon
(Alongamento_idAI, Usuario_idUsuario, Inicio)
VALUES
(1,1,NOW()),
(2,2,NOW()),
(3,3,NOW()),
(4,4,NOW()),
(5,5,NOW()),
(6,6,NOW()),
(7,7,NOW()),
(8,8,NOW()),
(9,9,NOW()),
(10,10,NOW()),
(11,11,NOW()),
(12,12,NOW()),
(13,13,NOW()),
(14,14,NOW()),
(15,15,NOW());

-- ==========================================
-- UPDATE PARA ATIVAR A TRIGGER
-- ==========================================

UPDATE HistoricoAlon
SET dataFim = DATE_ADD(Inicio, INTERVAL 10 MINUTE);

-- ==========================================
-- JORNADA DE TRABALHO
-- ==========================================

INSERT INTO JornadaTrabalho
(inicioJornd, tempoLembrete, fimJornd, Usuario_idUsuario)
VALUES
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),1),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),2),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),3),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),4),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),5),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),6),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),7),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),8),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),9),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),10),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),11),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),12),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),13),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),14),
(NOW(),30,DATE_ADD(NOW(), INTERVAL 8 HOUR),15);

-- ==========================================
-- PAUSAS
-- ==========================================

INSERT INTO Pausas
(inicio, fim, concluida, Usuario_idUsuario)
VALUES
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',1),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',2),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',3),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',4),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',5),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',6),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',7),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',8),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',9),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',10),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',11),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',12),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',13),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',14),
(NOW(), DATE_ADD(NOW(), INTERVAL 15 MINUTE), 'SIM',15);