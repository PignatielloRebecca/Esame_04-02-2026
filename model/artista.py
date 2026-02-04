from dataclasses import dataclass

@dataclass
class Artista:

    artist_id:int
    name:str
    peso:int

    def __str__(self):
        return f"{self.artist_id}  {self.name }  {self.peso})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.artist_id)