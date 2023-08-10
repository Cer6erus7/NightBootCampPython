# Problem 1

class Modellaptop:
    def __init__(self, model, cp, RAM, GPU, HDD, motherboard, resolution):
        self.model = model
        self.cp = cp
        self.RAM = RAM
        self.GPU = GPU
        self.HDD = HDD
        self.motherboard = motherboard
        self.resolution = resolution


    def slovarik(self):
        return {"model": self.model, "cp": self.cp, "RAM": self.RAM, "GPU": self.GPU, "HDD": self.HDD, "motherboard": self.motherboard, "resolution": self.resolution}



# Problem 2

class Newclassic:
    def __init__(self, dict:dict):
        self.dict = dict


    def get_tuplik_keys(self):
        return tuple(self.dict.keys())

    def get_tuplik_values(self):
        return tuple(self.dict.values())

    def get_listik_keys(self):
        return list(self.dict.keys())

    def get_listik_values(self):
        return list(self.dict.values())

    def get_setik_keys(self):
        return set(self.dict.keys())

    def get_setik_values(self):
        return set(self.dict.values())
