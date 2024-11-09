# db_setup.py

import os
from subprocess import call

DB_ENGINE = os.getenv('DB_ENGINE', 'postgresql')
DB_NAME = os.getenv('DB_NAME', 'flux_db')

def setup_database():
    if DB_ENGINE == 'postgresql':
        call(["createdb", DB_NAME])
    elif DB_ENGINE == 'mysql':
        call(["mysqladmin", "create", DB_NAME])
    # Add any other database setups here as needed

def backup_database():
    if DB_ENGINE == 'postgresql':
        call(["pg_dump", DB_NAME, "-f", f"{DB_NAME}_backup.sql"])
    elif DB_ENGINE == 'mysql':
        call(["mysqldump", DB_NAME, "-r", f"{DB_NAME}_backup.sql"])

setup_database()
