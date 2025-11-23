# How to install PostgreSql on Manjaro or any other CLI based Operating system

## End

## Installation

    Steps to install and run PostgreSql are as follows:
    1.  sudo pacman -S postgresql postgis
    2.  Switch to the postgres user account and initialize the database cluster with this command:
        1.  sudo su postgres -l # or sudo -u postgres -i
        2.  initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data/'
        3.  exit
    3. Options for initdb are as follows:
       1. --locale is the one defined in /etc/locale.conf.
       2. -E is the default encoding for new databases.
       3. -D is the default location for storing the database cluster.
    4. Now, start and enable the postgresql.service:
       1. sudo systemctl enable --now postgresql.service
    5. You can check PostgreSQL’s version with:
       1. psql --version

## DB Creation Example

Create a DB user for local development or deployment
    1.  sudo su postgres -c psql
    2.  CREATE USER deployer WITH PASSWORD 'eldeployerloco';
    3.  ALTER ROLE deployer WITH CREATEDB;
    4.  \q

### Configure your database with Phoenix

if you're using Phoenix package manager you’d use this in config/dev.exs like this:
    1.  config :my_app, MyApp.Repo,
    2.  username: "deployer",
    3.  password: "eldeployerloco",
    4.  database: "my_app_dev",
    5.  hostname: "localhost",
    6.  show_sensitive_data_on_connection_error: true,
    7.  pool_size: 10

## Start
