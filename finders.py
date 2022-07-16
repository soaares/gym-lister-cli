"""Finders module."""
import abc
from typing import Callable, List
from gym.entities import Client
from gym.contexts import DatabaseInterface

class FinderInterface(abc.ABC):
    """Finder Interface Class."""

    @abc.abstractmethod
    def find_all(self) -> List[Client]:
        """Finder Interface method."""

class MySqlFinder():
    """MySQL Finder Class."""

    def __init__(
        self,
        client_factory: Callable[...,Client],
        database: DatabaseInterface,
        credentials: dict
        ) -> None:
        self._client_factory = client_factory
        self._database = database
        self.credentials = credentials

    def find_all(self) -> List[Client]:
        """Find all rows from clients' table."""

        with self._database(self.credentials) as db_cursor:
            rows = db_cursor.execute("SELECT * FROM clients")
            return [self._client_factory(*row) for row in rows]
