import random
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


        for row in row_sizes:
            for i in range(row):


                if row==5 and i ==2:
                    #so it's desert
                    temp_type="desert"
                    self.tiles.append(Tile(-1, len(self.tiles), temp_type, (i, row_sizes.index(row))))
                else:
                    temp_type = choice(list(standard_tiles.keys()))
                    standard_tiles[temp_type]-=1
                    if standard_tiles[temp_type]==0:
                        del standard_tiles[temp_type]
                    chosen_number = random.choice(numbers)
                    numbers.remove(chosen_number)
                    self.tiles.append(Tile(chosen_number, len(self.tiles), temp_type, (i, row_sizes.index(row))))




    def generate_points(self):
        row_sizes = [3,4,4,5,5,6,6,5,5,4,4,3]
        for row in range(len(row_sizes)):

            for i in range(row_sizes[row]):

                self.points.append(Point(len(self.points),(row,i)))





    def append_points_to_tiles(self):
        # kind of hardcoded :/
        point_tile_scheme=[
            [1,4,5,8,9,13],
            [2,5,6,9,10,14],
            [3,6,7,10,11,15],

            [8,12,13,17,18,23],
            [9,13,14,18,19,24],
            [10,14,15,19,20,25],
            [11,15,16,20,21,26],

            [17,22,23,28,29,34],
            [18,23,24,29,30,35],
            [19,24,25,30,31,36],
            [20,25,26,31,32,37],
            [21,26,27,32,33,38],

            [29,34,35,39,40,44],
            [29,35,36,40,41,45],
            [30,36,37,41,42,46],
            [31,37,38,42,43,47],

            [40,44,45,48,49,52],
            [41,45,46,49,50,53],
            [42,46,47,50,51,54],
            ]


        for tile,points in zip(self.tiles,point_tile_scheme):
            for i in points:

                tile.points.append(self.points[i-1])


    def visualize_map(self,show_number=False):
        totalprint = ""
        row_sizes = [3, 4, 5, 4, 3]

        for tile in self.tiles:

            if tile.position[0] == 0:
                totalprint += "\n" + (5 - row_sizes[tile.position[1]]) * "  "
            totalprint += "  " if not show_number else "   "
            totalprint += str(tile.number) if show_number else ""
            totalprint+= tile.type[0]

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


        for row in range(len(row_sizes)):
            for i in range(row_sizes[row]):
                if i == 0:
                    totalprint += "\n" + (6 - row_sizes[row]) * "  "

                if (row,i) in building_positions:
                    building = self.buildings[building_positions.index((row, i))]
                    if building.type=="village":
                        totalprint+= "    " + building.player.name[0].lower()
                    else:
                        totalprint += "    " + building.player.name[0].capitalize()

                else:
                    totalprint+= "    -"
        print(totalprint)



    def show_points(self):
        scheme = [3,4,5,4,3]
        counter=0
        for i in scheme:
            line=""
            for j in range(i):
                line += str(self.points[counter].position)
                line += " "
                counter+=1
            print(line)