class Persona:

    def __init__(self, name, craft) -> None:
        self.name = name
        self.craft = craft

    def __str__(self) -> str:
        return f'Nombre: {self.name}, Tripulación: {self.craft}'

class RespuestaSatelite:
    def __init__(self, message, people, number) -> None:
        self.people = people
        self.number = number
        self.message = message