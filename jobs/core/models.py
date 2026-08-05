from dataclasses import dataclass

@dataclass
class Job:
    id: int
    title: str
    company: str
    city: str
    state: str
    published_at: str
    url: str