select regiao, sum(populacao) as Total from estados --soma da populacao divida em regioes em ordem decrescente
group by regiao
order by Total desc

select sum(populacao) as 'População Total' from estados --populacao total

select avg(populacao) as 'Media Total' from estados --media total