"""Listers module."""
import abc
from typing import List
from .finders import FinderInterface

class InterfaceLister(abc.ABC):
    """Lister's Interface Class."""

    @abc.abstractmethod
    def clients_by_name(self, name: str) -> List:
        """Lister's Interface Method."""

    @abc.abstractmethod
    def clients_by_plan(self, plan: int) -> List:
        """Lister's Interface Method."""

class ClientLister(InterfaceLister):
    """Lister's Client Class."""

    def __init__(self, client_finder: FinderInterface) -> None:
        self._client_finder = client_finder

    def clients_by_name(self, name: str) -> List:
        return [client for client in self._client_finder.find_all() if client.name.lower() == name]

    def clients_by_plan(self, plan: int) -> List:
        return [client for client in self._client_finder.find_all() if client.plan == plan]
