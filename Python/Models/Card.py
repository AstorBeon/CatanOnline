class Card():

    def __init__(self,is_resource:bool,value:str):
        self.is_resource = is_resource #resource or action
        self.value = value


    def __str__(self):
        return f"card type: {'resource' if self.is_resource else 'action'}, value: {self.value}"

