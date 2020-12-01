import random

from Python.Models.Card import Card
from Python.Models.Map import Map
from Python.Models.Player import Player


class Game():


    def __init__(self):
        self.map=Map()
        self.map.generate_tiles()
        self.map.generate_points()
        self.players=[]#player types
        self.resource_cards, self.action_cards=self.__generate_cards()
        self.map.append_points_to_tiles()


    def __generate_cards(self) -> [Card]:
        resource_cards = {"sheep":19,"iron":19,"wood":19,"clay":19,"hay":19}
        action_cards={"knight":8,"monopoly":3,"2_roades":3,"win_point":5,"2_resources":5}
        resource_stack={}
        action_stack=[]

        for key in resource_cards.keys():
            resource_stack[key]=[]
            for i in range(resource_cards[key]):
                resource_stack[key].append((Card(True,key)))


        for key in action_cards.keys():
            action_stack.append(Card(False,key))
            action_cards[key]-=1
            if action_cards[key]==0:
                del action_cards[key]

        random.shuffle(action_stack)
        return (resource_stack,action_stack)


    def add_player(self,player:Player)->None:
        self.players.append(player)

    def pull_single_card(self,type, resource=None):
        if type=="resource":
            if len(self.resource_cards[resource])>0:
                return (True, self.resource_cards[resource].pop())
            else:
                return (False, f"No {resource} cards left!")
        else:
            if len(self.action_cards)>0:
                return (True, self.action_cards.pop())
            else:
                return (False, "No action cards left!")

    #might be obsolete
    def add_cards_to_player(self,player:Player,amount,type:str,resource=None):
        for i in range(amount):
            pulled = self.pull_single_card(type,resource)
            if pulled[0]:
                if type=="resource":
                    player.resource_cards.append(pulled[1])
                else:
                    player.action_cards.append(pulled[1])
            else:
                print(f"No card pulled! {pulled[1]}")


    def roll_dices(self,player:Player):
        dice_value = random.randrange(2,12)
        print(f"Dices rolled... {dice_value}")
        if dice_value == 7:
            pass #THIEF!!!!
        else:
            print("No thief here")
            #passing resources to players
            matching_points = sum([x.points for x in self.map.tiles if x.number==dice_value and x.enabled],[])
            matching_buildings=[x for x in self.map.buildings if x.position in [y.position for y in matching_points] ]
            print(f"Matching buildings: {matching_buildings}")
            #todo pin

