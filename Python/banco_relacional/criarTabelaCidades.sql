create table if not exists cidades ( --criando tabela com FK
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    estado_id INT UNSIGNED NOT NULL,
    area DECIMAL(10,2),
    PRIMARY KEY(id),
    FOREIGN KEY(estado_id) REFERENCES estados(id)

)

create table teste (
    id int unsigned not null auto_increment primary key
)

drop table if exists teste -- excluindo tabela