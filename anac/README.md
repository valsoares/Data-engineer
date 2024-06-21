# ETL dos Dados de Tarifas Domésticas Aéreas da ANAC
### :page_facing_up: Descrição do Projeto
Este projeto visa realizar um pipeline de engenharia de dados completo, desde a coleta até a persistência de dados de tarifas domésticas aéreas 
fornecidas pela ANAC (Agência Nacional de Aviação Civil). O período de análise abrange de janeiro de 2023 a março de 2024. 
As etapas do projeto incluem extração, transformação e carga (ETL), com foco em práticas de engenharia de dados para garantir a qualidade e a usabilidade dos dados para futuras análises.

### :books: Etapas 
#### Extração de Dados

`Dados de tarifas aéreas`: coletados diretamente do site da ANAC em formato CSV. \
`Dados complementares de aeródromos`: contendo informações como nome, cidade e UF também coletados do site da ANAC.
   
#### Limpeza de Dados

`Carregamento de Dados`: Utilização de Pandas para leitura dos arquivos CSV, com tratamento de possíveis valores ausentes na leitura inicial. \
`Tratamento de Colunas Irrelevantes`: Filtragem e exclusão de colunas desnecessárias, assegurando que apenas as informações relevantes sejam mantidas. \
`Tratamento de Dados Faltantes`: Identificação e remoção de linhas com valores ausentes críticos (ex: códigos OACI), usando técnicas de imputação de dados quando aplicável. \
`Conversão de Tipos de Dados`: Normalização de tipos de dados, incluindo a conversão de valores monetários para tipos numéricos e tratamento de formatações regionais, como substituição de vírgulas por pontos decimais.

#### Transformação de Dados

`Mapeamento de Códigos OACI`: Utilização de arquivos auxiliares para mapear códigos OACI para nomes de aeródromos, cidades e UFs, garantindo enriquecimento de dados por meio de joins e merges. \
`Normalização e Padronização`: Padronização dos nomes de colunas entre diferentes fontes de dados para facilitar operações de merge e concatenação.
  
#### Persistência de Dados

`Remoção de Duplicatas`: Identificação e remoção de registros duplicados para assegurar a integridade dos dados. \
`Persistência em CSV`: Exportação do DataFrame final para um arquivo CSV, aplicando práticas de versionamento e backup para garantir a segurança dos dados.
  
#### Análise de Dados (Próximos Passos)
Com os dados devidamente processados e persistidos, as próximas etapas incluem análises exploratórias e avançadas, tais como:

`Análise Temporal`: Investigação das tendências de variação das tarifas ao longo do período de estudo. \
`Análise de Distribuição Geográfica`: Avaliação das tarifas por localização, analisando cidades e UFs. \
`Análise de Diferentes Empresas`: Avaliação das tarifas por diferentes empresas para as mesmas localizações.

### :wrench: Ferramentas e Técnicas Utilizadas

- `Python` e Pandas para operações de limpeza e persistência.
- `Pandas` para leitura e manipulação de arquivos `CSV` e `DataFrames`.
- `Regex` para manipulação avançada de strings.
- `SQL-like` operations dentro do Pandas para joins e merges eficientes.
- Versionamento de Arquivos usando `Git` para controle de versões e histórico de alterações.

### :trophy: Conclusão
Este projeto exemplifica um ciclo completo de engenharia de dados, desde a extração de dados brutos até a transformação e persistência de um dataset limpo e
enriquecido, pronto para análises. As técnicas aplicadas são fundamentais para garantir a qualidade dos dados, facilitando insights precisos e 
acionáveis. Este pipeline pode ser adaptado e expandido para diversos outros contextos.
