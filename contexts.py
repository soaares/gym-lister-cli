"""Contexts module."""
import abc
import sqlalchemy

class DatabaseInterface(abc.ABC):
    """Database Interface Class."""

    @abc.abstractmethod
    def __enter__(self) -> None:
        ...

    @abc.abstractmethod
    def __exit__(self, exc_log, exc_type, traceback) -> None:
        ...

class DatabaseContext(DatabaseInterface):
    """Database Context Class."""

    def __init__(self, credentials: dict):
        try:
            engine = sqlalchemy.create_engine(f"mysql://{credentials.get('UID')}:{credentials.get('PASSWORD')}@{credentials.get('SERVER')}:3306/{credentials.get('DATABASE')}?charset=utf8mb4")

            self.connection = engine.connect()
        except ValueError as error:
            print(f'Failed to connect on database: {error}')

    def __enter__(self):
        return self.connection

    def __exit__(self, exc_log, exc_type, traceback):
        self.connection.close()
