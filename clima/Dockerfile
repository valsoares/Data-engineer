FROM apache/airflow:2.9.2-python3.9

# Limpa o cache do apt-get e atualiza como root
USER root
RUN rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get update

# Instalação de ferramentas básicas e python3-dev
RUN apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Volta ao usuário padrão do Airflow
USER airflow

# Atualiza pip
RUN pip install --upgrade pip


# Copia o arquivo requirements.txt e instala dependências adicionais se necessário
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
