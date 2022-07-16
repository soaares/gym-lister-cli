# Gym Lister CLI Project

## About

Gym Lister it's a module who fetch data and print it out on the terminal.
In this project, it's possible to find clients by the name and by the client's plan.
On the terminal by typing a name, the lister search for a matching client's name.

Gym Lister was mainly created to practice some principles like:

- Dependency Injection with dependency_injector library;
- Dependency Inversion with abc library;

I practiced too:

- Type hints (It's not so much usual in python, but I love it);
- Custom Context Manager;
- Dataclasses with dataclasses library;
- Magic Methods;
- YAML files for store configurations;
- Formatting files with Pylint;
- Getting informations from .env files with python-dotenv libraries;


## Libraries

All the needed libraries to run this project it's stored in requirements.txt file.

### Enviroment

To run this project, you only will need a instance of MySQL database.

You can download Xampp project here:

- Windows x64 Bit: https://downloadsapachefriends.global.ssl.fastly.net/7.4.29/xampp-windows-x64-7.4.29-1-VC15-installer.exe?from_af=true
- Linux x64 Bit: https://downloadsapachefriends.global.ssl.fastly.net/7.4.29/xampp-linux-x64-7.4.29-1-installer.run?from_af=true

After install it, you can click on Start button on the MySql row and connect into the database with Beekeeper program or similar.

## Running the project

1. Clone the repository
2. Run the command in the terminal: pip install -r requirements.txt
3. Rename .env_example to .env and put database information into the file.
3. Run: python data/fixtures.py
4. Run: cd .. && python -m gym