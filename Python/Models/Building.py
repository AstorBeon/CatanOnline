from Python.Models.Player import Player
from Python.Models.Point import Point


class Building():

    def __init__(self,player:Player,point:Point):
        self.player=player
        self.type="village"
        self.position = point.position

    def upgrade(self):
        self.type="city"