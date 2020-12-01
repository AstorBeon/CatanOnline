class Tile():
    avaliable_types=["sheep","stone","wood","clay","hay",'desert']
    present_types ={"sheep":0,"stone":0,"wood":0,"clay":0,"hay":0,"desert":0}



    def __init__(self,number:int, id:int,type,position:tuple):
        self.number=number
        self.id=id
        self.type=type
        self.position=position #(row,index)
        self.points=[]
        self.enabled=True




