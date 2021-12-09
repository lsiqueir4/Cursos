select c.nome as Cidade, e.nome as Estados from estados e, cidades c
where e.id = c.estado_id;

select c.nome as Cidade, e.nome as Estados from estados e  --mesmo SELECT com inner join
inner join cidades c on e.id = c.estado_id;