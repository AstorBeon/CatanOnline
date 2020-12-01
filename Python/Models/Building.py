from Python.Models.Player import Player
from Python.Models.Point import Point


class Building():

    def __init__(self,player:Player,point:Point):
        self.player=player
        self.type="village"
        self.position = point.position

    def upgrade(self):
        self.type="city"

    def __str__(self):
        return f"{self.type} of {self.player} on position {self.position}"

    def __repr__(self):
        return f"{self.type} of {self.player} on position {self.position}"