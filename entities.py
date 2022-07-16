"""Entities module."""
import dataclasses

@dataclasses.dataclass
class Client:
    """Client entity Class."""

    cliente_id: str
    name: str
    last_name: str
    address: str
    country_code: str
    phone_number: int
    plan: int

    def __repr__(self) -> str:
        return f"""Id: {self.cliente_id},
        Name: {self.name},
        Last_Name: {self.last_name},
        Address: {self.address},
        Coutry Code: {self.country_code},
        Phone Number: {self.phone_number},
        Plan: {self.plan}"""
