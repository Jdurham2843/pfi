#!/bin/bash

sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql-9.6

sudo -u postgres psql -c "CREATE USER john WITH PASSWORD 'john';"
sudo -u postgres psql -c "CREATE DATABASE pfi;"
sudo -u postgres psql -c "ALTER ROLE john SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE john SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE john SET timezone TO 'US/Central';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE pfi TO john;"
sudo -u postgres psql -c "ALTER USER john CREATEDB;"

sudo cp /vagrant/setupEnv/postgresql.conf /etc/postgresql/9.6/main/
sudo cp /vagrant/setupEnv/pg_hba.conf /etc/postgresql/9.6/main/

sudo iptables -A INPUT -p tcp --dport 5432 -j ACCEPT
sudo service postgresql restart
