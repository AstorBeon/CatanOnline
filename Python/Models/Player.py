class Player():

    price_list={
        "village":["wood","clay","sheep","hay"],
        "city":["stone","stone","stone","hay","hay"],
        "road":["clay","wood"],
        "actioncard":["sheep","stone","hay"]
    }


    def __init__(self, name:str):
        self.name=name
        self.resource_cards=[]#card types
        self.action_cards=[]#card types
        self.points=0


    def show_cards(self):
        for card in self.resource_cards:
            print(card)
        for card in self.action_cards:
            print(card)


    def __str__(self):
        return f"Player {self.name}"

    def __repr__(self):
        return f"Player {self.name}"