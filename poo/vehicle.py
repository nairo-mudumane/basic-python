class Vehicle:
    def __init__(self, color, mark) -> None:
        self.color = color
        self.mark = mark
    def ligar(self:bool):
        self.on = True
        return self.on