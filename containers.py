"""Containers module."""
import os
from dotenv import load_dotenv
from dependency_injector import containers, providers
from . import contexts, listers, entities, finders

load_dotenv()

class Container(containers.DeclarativeContainer):
    """Classes and configuration needed by the project are here."""

    config = providers.Configuration(yaml_files=['config.yml'])

    credentials = {
        "SERVER": os.environ.get('SERVER'),
        "DATABASE": os.environ.get('DATABASE'),
        "UID": os.environ.get('UID'),
        "PASSWORD": os.environ.get('PASSWORD')
    }

    client = providers.Factory(entities.Client)

    database = providers.Factory(contexts.DatabaseContext)

    mysql_finder = providers.Factory(
        finders.MySqlFinder,
        client_factory = client.provider,
        database = database.provider,
        credentials = credentials
    )

    lister = providers.Factory(
        listers.ClientLister,
        client_finder = mysql_finder
    )
