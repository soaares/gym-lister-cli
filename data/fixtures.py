"""Fixtures module."""
import os
import faker
import dotenv
import sqlalchemy

dotenv.load_dotenv()

fake = faker.Faker()

CREDENTIALS = dict(
        SERVER = os.environ.get('SERVER'),
        DATABASE = os.environ.get('DATABASE'),
        UID = os.environ.get('UID'),
        PASSWORD = os.environ.get('PASSWORD')
    )

class DatabaseContext:
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

def create_database():
    """Create database structure."""

    with DatabaseContext(CREDENTIALS) as db_cursor:
        try:
            db_cursor.execute("DROP TABLE IF EXISTS clients")
            db_cursor.execute("DROP TABLE IF EXISTS plans")
            db_cursor.execute("""
                CREATE TABLE plans (
                id INT PRIMARY KEY AUTO_INCREMENT,
                activity VARCHAR(20),
                princing VARCHAR(10),
                week_frequency INT
                )""")

            db_cursor.execute("""
                CREATE TABLE clients (
                    id VARCHAR(36) PRIMARY KEY,
                    name VARCHAR(20),
                    last_name VARCHAR(20),
                    address VARCHAR(50),
                    country_code VARCHAR(5),
                    phone_number BIGINT,
                    plan INT,
                    FOREIGN KEY (plan) REFERENCES plans(id)
                )
            """)
        except TypeError as error:
            print(f'TypeError: Database insert error - {error}')

def create_plans():
    """Insert fake plans into plans' table."""

    plans = [(
        fake.word(ext_word_list=['aerobic', 'dancing', 'crossfit']),
        fake.pricetag(),
        fake.random_int(min=1, max=7)
    ) for _ in range(6)]

    with DatabaseContext(CREDENTIALS) as db_cursor:
        try:
            for plan in plans:
                query = """INSERT INTO plans (activity, princing, week_frequency) VALUES (%s,%s,%s)"""
                db_cursor.execute(query, plan)
        except TypeError as error:
            print(f'TypeError: Database insert error - {error}')

def create_clients():
    """Insert fake clients into clients' table."""

    clients = [(
        fake.uuid4(),
        fake.first_name(),
        fake.last_name(),
        fake.address().replace("\n", ''),
        fake.country_calling_code().replace(' ', ''),
        fake.msisdn(),
        fake.random_int(min=1, max=6)
        ) for _ in range(30)
        ]

    with DatabaseContext(CREDENTIALS) as db_cursor:
        try:
            for client in clients:
                query = """INSERT INTO clients (id, name, last_name, address, country_code, phone_number, plan) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                db_cursor.execute(query, client)
        except TypeError as error:
            print(f'TypeError: Database insert error - {error}')

if __name__ == "__main__":
    create_database()
    create_plans()
    create_clients()
