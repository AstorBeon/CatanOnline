from random import shuffle,choice

from Python.Models.Building import Building
from Python.Models.Player import Player
from Python.Models.Point import Point
from Python.Models.Tile import Tile


class Map():


    def __init__(self):
        self.tiles =[]
        self.points=[]
        self.buildings=[]
        self.rows=[]


    def generate_tiles(self):
        standard_tiles={"sheep":4,"iron":3,"wood":4,"clay":3,"hay":4}
        row_sizes=[3,4,5,4,3]
        numbers=[2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        shuffle(numbers)

        for row in row_sizes:
            for i in range(row):


                if row==5 and i ==2:
                    #so it's desert
                    temp_type="desert"
                else:
                    temp_type = choice(list(standard_tiles.keys()))
                    standard_tiles[temp_type]-=1
                    if standard_tiles[temp_type]==0:
                        del standard_tiles[temp_type]

                self.tiles.append(Tile(len(self.tiles),-1,temp_type,(i,row_sizes.index(row))))


    def generate_points(self):
        row_sizes = [3,4,4,5,5,6,6,5,5,4,4,3]
        for row in range(len(row_sizes)):
            for i in range(row):
                self.points.append(Point(len(self.points),(row,i)))


    def visualize_map(self):
        totalprint = ""
        row_sizes = [3, 4, 5, 4, 3]

        for tile in self.tiles:

            if tile.position[0] == 0:
                totalprint += "\n" + (5 - row_sizes[tile.position[1]]) * " "
            totalprint += "  " + tile.type[0]

        print(totalprint)


    def ugly_visualise_map(self):
        totalprint = ""
        row_sizes = [3, 4, 5, 4, 3]

        for tile in self.tiles:

            if tile.position[0] == 0:
                totalprint += "\n"
            totalprint += "  " + tile.type[0]

        print(totalprint)

    def place_building(self,player:Player,point:Point) -> bool:
        #check if can be placed
        for place in point.generate_neighbour_locations():
            if place in [x.position for x in self.buildings]:
                print("ERROR, placing building is not allowed here due to not enough distance from other buildings.")
                return False

        print("Building placed!")
        self.buildings.append(Building(player,point))

        return True

    def visualize_buildings(self):
        totalprint = ""
        row_sizes = [3,4,4,5,5,6,6,5,5,4,4,3]
        building_positions = [x.position for x in self.buildings]
        print(f"Building:{self.buildings[0].position}")

        for row in range(len(row_sizes)):
            for i in range(row_sizes[row]):
                if i == 0:
                    totalprint += "\n" + (6 - row_sizes[row]) * "  "
                print(f"({row},{i})")
                if (row,i) in building_positions:
                    building = self.buildings[building_positions.index((row, i))]
                    if building.type=="village":
                        totalprint+= "   " + building.player.name[0].lower()
                    else:
                        totalprint += "   " + building.player.name[0].capitalize()

                else:
                    totalprint+= "   -"





        print(totalprint)