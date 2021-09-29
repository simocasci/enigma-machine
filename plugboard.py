import random
import copy


class Plugboard:
    def __init__(self, connected_holes=10):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.connected_holes = connected_holes
        self.connections = self.generate_random_connections()

    def generate_random_connections(self):
        alphabet = copy.deepcopy(self.alphabet)
        connections = {}
        for _ in range(self.connected_holes):
            letter1 = random.choice(alphabet)
            alphabet.remove(letter1)
            letter2 = random.choice(alphabet)
            alphabet.remove(letter2)
            connections[letter1] = letter2
            connections[letter2] = letter1
        return connections
