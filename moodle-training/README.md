# Capacitação Moodle

![](mapa-training.png)

Utilizamos a plataforma **Moodle** para formular a capacitação das voluntárias, dividindo por módulos.

Utilizamos o **Boost** como Plugin tema das nossas páginas e o arquivo de configuração mapa-default.css está dentro da pasta moodle-training desse repositório.

As configurações de estilização são feitas conforme descritas na documentação abaixo:

## Adicionar fonte do google fonts

1.1) Administração do site → Aparência → Código HTML adicional → **Dentro da tag HEAD** → adicionar link do google fonts. Exemplo:

![](mapa-1.png)

1.2) Administração do site → Aparência → Temas → Boost (ou outro que estiver aplicado) → Configurações gerais → Arquivos de predefinição adicionais → adicionar o arquivo acrescentando as configurações desejadas. Exemplo de mudança do nome de fonte da navegação:

![](mapa-2.png)

## Publicação  Moodle

Escolhemos publicar o moddle no Docker usando a [bitnami/moodle](https://hub.docker.com/r/bitnami/moodle) que possui todas as configurações e ferramentas necessárias para a instalação do moodle. Inclusive recursos para criar o banco de dados que será utilizado. Para isso, usamos escolhemos o postgres e fizemos uma publicação inicial setando as seguintes configurações para o banco de dados:


Create a database for Moodle using postgresql-client:

    POSTGRESQL_CLIENT_DATABASE_HOST: Hostname for the PostgreSQL server. Default: postgresql
    POSTGRESQL_CLIENT_DATABASE_PORT_NUMBER: Port used by the PostgreSQL server. Default: 5432
    POSTGRESQL_CLIENT_POSTGRES_USER: Database admin user. Default: root
    POSTGRESQL_CLIENT_POSTGRES_PASSWORD: Database password for the database admin user. No defaults.
    POSTGRESQL_CLIENT_CREATE_DATABASE_NAMES: List of new databases to be created by the postgresql-client module. No defaults.
    POSTGRESQL_CLIENT_CREATE_DATABASE_USER: New database user to be created by the postgresql-client module. No defaults.
    POSTGRESQL_CLIENT_CREATE_DATABASE_PASSWORD: Database password for the POSTGRESQL_CLIENT_CREATE_DATABASE_USER user. No defaults.
    ALLOW_EMPTY_PASSWORD: It can be used to allow blank passwords. Default: no

Uma vez criado montamos o docker-compose conforme o arquivo na pasta deploy.
