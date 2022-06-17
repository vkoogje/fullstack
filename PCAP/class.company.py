from random import randint as rand
from time import perf_counter as pcount


def get_rand_id(blocks=5,block_len=4):
    id = str()
    # loop for the amount of blocks
    for x in range(blocks):
        # loop for the length of a block
        for y in range(block_len):
            rand_int = rand(0,16)
            rand_int_to_hex = "{0:X}".format(rand_int)
            # if a hex number comes up with len<2 (eg: len(a) = 1, len(9) but len(10) = 2) 
            # then add a 0 in front            
            if len(rand_int_to_hex) < 2:
                rand_int_to_hex = '{}{}'.format("0", rand_int_to_hex)
            id = '{}{}'.format(id, rand_int_to_hex)

        # if we're not at the last block (x=blocks-1), then add a seperator at the end
        if x != blocks-1:
            id = '{}{}'.format(id,"-")
    return id

class Company:
    def __init__(self,name_short,name_long,name_abbrevation,hq):
        self.name_short = name_short
        self.name_long = name_long
        self.name_abbrevation = name_abbrevation
        self.hq = hq
        self.id = get_rand_id()
    
    def get_name(self, type=1):
        if type == 1:
            return self.name_abbrevation
        elif type == 2:
            return self.name_long
        else:
            return self.name_short
    
    def get_hq(self):
        return self.hq

    def set_name(self, type, new_value):
        if type == 1:
            self.name_abbrevation = new_value
        elif type == 2:
            self.name_long = new_value
        else:
            self.name_short = new_value

    def get_id(self):
        return self.id

asml = Company("ASML Holding N.V.", "Advanced Semiconductor Materials Lithography Holding N.V.", "ASML", "Amsterdam")
print(asml.get_name())
print(asml.get_hq())
print(asml.get_id())