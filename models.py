from dataclasses import dataclass

@dataclass
class Player:
    name: str
    position: str
    phone: str
    goals: int = 0 
    tallies: int = 0
    id: int = None 

    def __str__(self):
        return f'{self.name}, {self.position}, {self.phone}, {self.goals}, {self.tallies}, {self.id}'
    
    def is_flagged(self) -> bool:
        return self.tallies >= 3

        