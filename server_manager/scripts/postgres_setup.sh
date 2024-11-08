# postgres_setup.sh
psql -U postgres -c "CREATE DATABASE mydb;"
psql -U postgres -c "CREATE USER myuser WITH PASSWORD 'password';"
psql -U postgres -d mydb -f /path/to/seed.sql
