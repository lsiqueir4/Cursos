SELECT e.nome, c.nome FROM empresas e, empresas_unidades eu, cidades c
WHERE e.id = eu.empresa_id AND c.id = eu.cidade_id AND SEDE = 1; 

Bradesco	Niterói
Vale	    Caruaru

--Executar pelo Workbench