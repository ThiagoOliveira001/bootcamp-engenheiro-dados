# Trabalho de análise dos microdados do enem 2020

1. Upload dos dados
2. Conversão em parquet
3. Disponibilização dos dados para consulta via AWS Athena

### Para realização deste trabalho foram seguidos os passos (foi usada base de 2020)

- Necessário base dos [microdados do enem](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados)
- Criação de bucket S3 na AWS
- Criação de Glue Spark Job para transformar em parquet
- Criação de um crawler no glue para disponibilizar os dados
- Consultas usando sql pelo athena para responder as questões propostas pelo professor
