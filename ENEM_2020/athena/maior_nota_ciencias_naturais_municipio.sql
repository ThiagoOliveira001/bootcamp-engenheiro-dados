select nu_nota_cn, no_municipio_prova from enem_glue 
where no_municipio_prova in ('Governador Valadares', 'Ipatinga', 'Ouro Preto', 'Montes Claros')
order by nu_nota_cn desc
limit 5;