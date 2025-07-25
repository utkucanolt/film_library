import os
import sys
from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context

# ————— proje kökünü ekle —————
# env.py alembic/ klasöründe, bir üst dizin projenin root’u:
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# alembic.ini’yi yükle
config = context.config

# ENV’den DATABASE_URL al (fallback de belirtebilirsiniz)
db_url = os.getenv("DATABASE_URL", "sqlite:///./movies.db")
config.set_main_option("sqlalchemy.url", db_url)

# logging
fileConfig(config.config_file_name)

# **Burayı güncelledik**: app/database.py içindeki Base ve engine
from app.database import Base, engine
target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
