PRAGMA foreign_keys = ON;

-- ==========================================
-- USUARIOS
-- ==========================================

INSERT INTO Usuario (nome, email, senha, data_nasc) VALUES
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

INSERT INTO Tipo_dor (nome, descricao, regiao_corpo) VALUES
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
-- ALONGAMENTO_TIPO_DOR
-- ==========================================

INSERT INTO Alongamento_tipo_dor (alongamento_id, tipo_dor_id) VALUES
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
-- ==========================================

INSERT INTO Historico_alongamento
(alongamento_id, usuario_id, inicio, data_fim, tempo_total)
VALUES
(1,1,datetime('now'),datetime('now','+10 minutes'),10),
(2,2,datetime('now'),datetime('now','+10 minutes'),10),
(3,3,datetime('now'),datetime('now','+10 minutes'),10),
(4,4,datetime('now'),datetime('now','+10 minutes'),10),
(5,5,datetime('now'),datetime('now','+10 minutes'),10),
(6,6,datetime('now'),datetime('now','+10 minutes'),10),
(7,7,datetime('now'),datetime('now','+10 minutes'),10),
(8,8,datetime('now'),datetime('now','+10 minutes'),10),
(9,9,datetime('now'),datetime('now','+10 minutes'),10),
(10,10,datetime('now'),datetime('now','+10 minutes'),10),
(11,11,datetime('now'),datetime('now','+10 minutes'),10),
(12,12,datetime('now'),datetime('now','+10 minutes'),10),
(13,13,datetime('now'),datetime('now','+10 minutes'),10),
(14,14,datetime('now'),datetime('now','+10 minutes'),10),
(15,15,datetime('now'),datetime('now','+10 minutes'),10);

-- ==========================================
-- JORNADA DE TRABALHO
-- ==========================================

INSERT INTO Jornada_trabalho
(usuario_id, inicio_jornada, fim_jornada, intervalo_lembrete_min)
VALUES
(1,datetime('now'),datetime('now','+8 hours'),30),
(2,datetime('now'),datetime('now','+8 hours'),30),
(3,datetime('now'),datetime('now','+8 hours'),30),
(4,datetime('now'),datetime('now','+8 hours'),30),
(5,datetime('now'),datetime('now','+8 hours'),30),
(6,datetime('now'),datetime('now','+8 hours'),30),
(7,datetime('now'),datetime('now','+8 hours'),30),
(8,datetime('now'),datetime('now','+8 hours'),30),
(9,datetime('now'),datetime('now','+8 hours'),30),
(10,datetime('now'),datetime('now','+8 hours'),30),
(11,datetime('now'),datetime('now','+8 hours'),30),
(12,datetime('now'),datetime('now','+8 hours'),30),
(13,datetime('now'),datetime('now','+8 hours'),30),
(14,datetime('now'),datetime('now','+8 hours'),30),
(15,datetime('now'),datetime('now','+8 hours'),30);

-- ==========================================
-- PAUSAS
-- ==========================================

INSERT INTO Pausas
(usuario_id, alongamento_id, inicio, fim, status)
VALUES
(1,1,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(2,2,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(3,3,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(4,4,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(5,5,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(6,6,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(7,7,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(8,8,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(9,9,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(10,10,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(11,11,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(12,12,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(13,13,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(14,14,datetime('now'),datetime('now','+15 minutes'),'realizada'),
(15,15,datetime('now'),datetime('now','+15 minutes'),'realizada');
