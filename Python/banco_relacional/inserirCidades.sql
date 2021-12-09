INSERT INTO cidades (nome, area, estado_id)
VALUES ('Niterói', 795, 19)

select nome, id from estados

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Caruaru', 920.6, (SELECT id from estados where sigla = 'PE')) --procurando o ID com um SELECT dentro do INSERT