#set -e
#export PGPASSWORD=postgres;
#psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "demo_db" <<-EOSQL
#  CREATE USER postgres WITH PASSWORD 'postgres';
#  CREATE DATABASE demo_db;
#  GRANT ALL PRIVILEGES ON DATABASE demo_db TO postgres;
#  \connect demo_db postgres
#   COMMIT;
#EOSQL