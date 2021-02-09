class Box:
    def __init__(self):
        self._contents = []

    def __contains__(self,valeur):
        return valeur in self._contents

    def add(self, truc):
        self._contents.append(truc)
    
    def remove(self,truc):
        self._contents.remove(truc)