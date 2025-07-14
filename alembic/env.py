import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Proje yolunu tanıt (app klasörünü bulmak için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Modelleri ve metadata'yı import et
from app.models import Movie
from app.database import Base

# Alembic Config
config = context.config

# Logging ayarları
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# SQLAlchemy metadata (autogenerate burayı takip eder)
target_metadata = Base.metadata

# Migration offline modu
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# Migration online modu
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

# Hangi modda çalıştığını kontrol et
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
