from Python.Models.Map import Map
from Python.Models.Player import Player
from Python.Models.Point import Point

if __name__ == "__main__":
    map = Map()
    map.generate_tiles()
    map.ugly_visualise_map()

    maciek = Player("Maciek")
    map.place_building(maciek,Point(0,(3,3)))
    map.place_building(maciek,Point(0,(3,4)))
    map.buildings[-1].upgrade()

    map.visualize_buildings()