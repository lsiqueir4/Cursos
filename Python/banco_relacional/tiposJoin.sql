select * from cidades c inner join prefeitos p on c.id = p.cidade_id;

select * from cidades c left join prefeitos p on c.id = p.cidade_id; -- comando buga no vscode, fazer no workbench
--o left join vai trazer tudo da tabela cidades, mesmo que não tenha prefeitos associados

resultado:

1	Niterói	19	795.00	1	Rodrigo Neves	1
2	Caruaru	17	920.60	2	Raquel Lyra	2


select * from cidades c right join prefeitos p on c.id = p.cidade_id;
-- o right join vai trazer tudo da tabela prefeitos, mesmo q nao tenha cidades associadas
1	Niterói	19	795.00	1	Rodrigo Neves	1
2	Caruaru	17	920.60	2	Raquel Lyra	2
				3	Zenaldo Coutinho	
				7	Rafael Greca	

select * from cidades c right join prefeitos p on c.id = p.cidade_id
union
select * from cidades c left join prefeitos p on c.id = p.cidade_id;
--mesma coisa q um full join(mysql nao suporte o comando full join)

1	Niterói	19	795.00	1	Rodrigo Neves	1
2	Caruaru	17	920.60	2	Raquel Lyra	2
				3	Zenaldo Coutinho	
				7	Rafael Greca	