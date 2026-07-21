from dataclasses import dataclass

@dataclass
class Job:

    id: int
    title: str
    company: str
    city: str
    state: str
    url: str