import sys, os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# 1) point to your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2) load your Settings (and override sqlalchemy.url)
from app.core.config import settings
config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# 3) set up logging
fileConfig(config.config_file_name)

# 4) import your metadata
from app.db.base import Base  
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as conn:
        context.configure(connection=conn, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
