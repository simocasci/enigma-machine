import random
import copy


class Rotor:
    def __init__(self):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.connections = self.generate_random_connections()

    def generate_random_connections(self):
        alphabet_from = copy.deepcopy(self.alphabet)
        alphabet_to = copy.deepcopy(self.alphabet)
        connections = {}
        while len(alphabet_from) > 0:
            letter1 = random.choice(alphabet_from)
            alphabet_from.remove(letter1)
            letter2 = letter1
            while True:
                letter2 = random.choice(alphabet_to)
                if letter2 != letter1:
                    break
            alphabet_to.remove(letter2)
            connections[letter1] = letter2
        return connections

    def rotate(self):
        values = list(self.connections.values())
        values = [values[-1]] + values[:-1]
        self.connections = dict(zip(self.connections.keys(), values))
