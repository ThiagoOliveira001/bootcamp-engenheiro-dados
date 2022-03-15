select avg(nu_nota_mt) as media, no_municipio_esc
from enem_glue
group by no_municipio_esc
order by media desc
limit 1;