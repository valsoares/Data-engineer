# ETL de Dados Climáticos

### :page_facing_up: Descrição do Projeto

Este projeto utiliza o Apache Airflow para criar um pipeline de ETL que coleta dados climáticos da API OpenWeather, transforma os dados e os carrega em um banco de dados PostgreSQL.

### :books: Etapas 
#### Extração de Dados
`Dados climáticos`: coletados diretamente da API OpenWeather, fornecendo informações detalhadas sobre as condições climáticas de Brasília.

#### Limpeza de Dados
`Tratamento de Colunas Irrelevantes`: Filtragem e exclusão de colunas desnecessárias, assegurando que apenas as informações relevantes sejam mantidas. 

#### Transformação de Dados
`Conversão de Tipos de Dados`: Normalização dos tipos de dados, incluindo a conversão de timestamps para formatos de data e hora, ajustando para o fuso horário local. \
`Armazenamento Temporário`: Salvamento dos dados transformados em um arquivo CSV temporário para facilitar o carregamento posterior.

#### Carregamento de Dados
`Inserção no Banco de Dados`: Leitura do arquivo CSV temporário e inserção dos dados no banco de dados PostgreSQL, garantindo que todas as informações meteorológicas estejam disponíveis para consultas futuras.

### :wrench: Ferramentas e Técnicas Utilizadas

- `Apache Airflow` para orquestração dos dados.
- `Docker` para containerização.
- `Python` e Pandas para operações de limpeza e persistência.
- `Pandas` para leitura e manipulação de arquivos `CSV` e `DataFrames`.
- Banco de dados`PostgreSQL` para manipulação avançada de strings.
- Versionamento de Arquivos usando `Git` para controle de versões e histórico de alterações.

### :camera_flash: Imagens do Projeto
#### Container Docker para o Airflow
<img src="https://github.com/valsoares/Data-engineer/blob/main/clima/images/4.png" alt="docker" width="700">

#### DAG Configurado no Airflow
<img src="https://github.com/valsoares/Data-engineer/blob/main/clima/images/1.png" alt="airflow" width="700">

#### Execução do DAG Agendado no Airflow
<img src="https://github.com/valsoares/Data-engineer/blob/main/clima/images/3.png" alt="airflow" width="700">
<img src="https://github.com/valsoares/Data-engineer/blob/main/clima/images/5.png" alt="airflow" width="700">

#### Dados Salvos no Banco de Dados
<img src="https://github.com/valsoares/Data-engineer/blob/main/clima/images/2.png" alt="bd" width="700">
