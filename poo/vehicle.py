class Vehicle:
    def __init__(self, color, mark) -> None:
        self.color = color
        self.mark = mark
    def ligar(self):
        self.on = True
        return self.on