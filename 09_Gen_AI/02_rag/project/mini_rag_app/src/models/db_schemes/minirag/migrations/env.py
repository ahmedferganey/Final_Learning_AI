import asyncio
import os
import sys
from pathlib import Path
from urllib.parse import quote_plus
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Ensure project modules are importable when alembic runs from this nested directory.
SRC_ROOT = Path(__file__).resolve().parents[4]
PROJECT_ROOT = Path(__file__).resolve().parents[5]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

# Load env values before constructing settings (src/.env is the main app env file).
load_dotenv(SRC_ROOT / ".env", override=False)
load_dotenv(PROJECT_ROOT / ".env", override=False)



#################################### MY LOGIC ####################################

from database.base import Base
# any schemas will try inherit Base, this will permit alembic to detect it 
from models.db_schemes.minirag.schemes import AssetORM, DataChunkORM, ProjectORM


def get_database_url() -> str:
    direct_url = os.getenv("DATABASE_URL", "").strip()
    if direct_url:
        return direct_url

    username = (os.getenv("POSTGRES_USERNAME") or os.getenv("POSTGRES_USER") or "").strip()
    password = os.getenv("POSTGRES_PASSWORD", "").strip()
    host = os.getenv("POSTGRES_HOST", "").strip()
    port = (os.getenv("POSTGRES_PORT") or "5432").strip()
    database = (os.getenv("POSTGRES_MAIN_DATABASE") or os.getenv("POSTGRES_DB") or "").strip()

    if username and password and host and database:
        encoded_user = quote_plus(username)
        encoded_pass = quote_plus(password)
        return f"postgresql+asyncpg://{encoded_user}:{encoded_pass}@{host}:{port}/{database}"

    raise RuntimeError(
        "Unable to resolve database URL for Alembic. Set DATABASE_URL or POSTGRES_* variables."
    )


config.set_main_option("sqlalchemy.url", get_database_url())

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
