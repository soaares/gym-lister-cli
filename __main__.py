"""Main module."""
import sys
from dependency_injector.wiring import inject, Provide
from .containers import Container
from .listers import ClientLister

@inject
def main(lister: ClientLister = Provide[Container.lister]) -> None:
    """Main function."""

    name = input("Please, insert the client's name: ")
    print("Name:")
    for client in lister.clients_by_name(name.lower()):
        print("\t-", client)

    plan = int(input("Please, insert the plan number: "))
    print(f"Plan {plan} Clients:")
    for client in lister.clients_by_plan(plan):
        print("\t-", client)

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    main()
