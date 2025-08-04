from dataclasses import dataclass

@dataclass
class PostDTO:
    title: str
    body: str
    userId: int
    id: int