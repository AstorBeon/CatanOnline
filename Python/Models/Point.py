class Point():
    def __init__(self,id:int,position:tuple,perk=None):
        self.perk=perk
        self.position=position #(row,index)
        self.id=id

    def generate_neighbour_locations(self):
        return [self.position,
                (self.position[0],self.position[1]-1),
                (self.position[0],self.position[1]+1),
                (self.position[0]-1, self.position[1] - 1),
                (self.position[0]-1, self.position[1] + 1),
                (self.position[0]+1, self.position[1] - 1),
                (self.position[0]+1, self.position[1] + 1),
                ]