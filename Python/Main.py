from Python.Models.Game import Game
from Python.Models.Map import Map
from Python.Models.Player import Player
from Python.Models.Point import Point

if __name__ == "__main__":
    # map = Map()
    # map.generate_tiles()
    # map.ugly_visualise_map()

    maciek = Player("Maciek")

    # map.place_building(maciek,Point(0,(3,4)))
    # map.buildings[-1].upgrade()
    #
    # map.visualize_buildings()

    game = Game()
    game.add_player(maciek)
    game.add_cards_to_player(maciek,4,"resource","wood")
    game.add_cards_to_player(maciek,4,"action")
    maciek.show_cards()

    game.map.place_building(maciek,Point(0,(3,3)))

    game.map.visualize_map(True)
    game.map.visualize_buildings()


    game.roll_dices(maciek)


#    print("POINTS")
    # for i in game.map.points:
    #     print(i.position
    #           )