"""SQLite context managers used by the day 4 examples."""

from __future__ import annotations

import sqlite3
import logging
from contextlib import contextmanager
from pathlib import Path
from sqlite3 import Connection, Cursor

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


class DBConnection:
    """Open a connection for a with-block and handle its transaction."""

    def __init__(self, db_path: str | Path):
        self.db_path = db_path
        self.connection: Connection | None = None

    def __enter__(self) -> Cursor:
        logger.info("Opening connection to %s", self.db_path)
        self.connection = sqlite3.connect(self.db_path)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.connection is not None:
            if exc_type is None:
                self.connection.commit()
                logger.info("Committed changes and closing connection.")
            else:
                self.connection.rollback()
                logger.error("Error occurred (%s) — rolled back changes.", exc_value)
            self.connection.close()

        return False


@contextmanager
def db_connection_cm(db_path: str | Path):
    """The function-based version of DBConnection."""
    logger.info("Opening connection to %s (function-based)", db_path)
    connection = sqlite3.connect(db_path)
    try:
        yield connection.cursor()
        connection.commit()
        logger.info("Committed changes and closing connection.")
    except Exception as e:
        connection.rollback()
        logger.error("Error occurred (%s) — rolled back changes.", e)
        raise
    finally:
        connection.close()


def initialize_sample_table(db_path: str | Path) -> None:
    """Create the users table if it is not already there."""
    with DBConnection(db_path) as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
