import uuid
import dataclasses


@dataclasses.dataclass
class User:
    id: uuid.UUID
    name: str
    birth_place: str
