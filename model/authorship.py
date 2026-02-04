from dataclasses import dataclass

@dataclass
class Authorship:
    object_id:str
    role:str
    artist_id:str

    def __str__(self):
        return f"{self.object_id}  {self.role}  {self.artist_id})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.artist_id)