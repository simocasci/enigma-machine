from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector


class Enigma:
    def __init__(self, rotors=3, plugboard_connections=10):
        assert(rotors >= 2)
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.rotors = [Rotor() for _ in range(rotors)]
        self.rotors_starting_config = [r.connections for r in self.rotors]
        self.plugboard = Plugboard(plugboard_connections)
        self.reflector = Reflector()

    def get_starting_config(self):
        return self.rotors_starting_config, self.plugboard, self.reflector

    def set_rotors_config(self, config):
        assert(len(self.rotors) == len(config))
        for i in range(len(self.rotors)):
            self.rotors[i].connections = config[i]
            self.rotors_starting_config[i] = config[i]

    def set_plugboard_config(self, config):
        self.plugboard.connections = config

    def set_reflector_config(self, config):
        self.reflector.connections = config

    def preprocess_message(self, message):
        message = message.strip().lower().replace(' ', '')
        message = ''.join(
            list(filter(lambda symbol: symbol in self.alphabet, message)))
        return message

    def read_file(self, file):
        elements = []
        with open(file, 'r') as f:
            for elem in f:
                elements.append(elem)
        elements = ''.join(elements)
        return elements

    def rotors_rotation(self):
        self.rotors[0].rotate()
        for i in range(1, len(self.rotors)):
            if self.rotors[i-1].connections == self.rotors_starting_config[i-1]:
                self.rotors[i].rotate()

    def enigma_pass(self, message):
        new_message = ''
        for letter in message:
            # first plugboard pass
            if letter in self.plugboard.connections:
                plugboard_letter = self.plugboard.connections[letter]
            else:
                plugboard_letter = letter

            # first rotors pass
            rotors_letter = plugboard_letter
            for i in range(len(self.rotors)):
                rotors_letter = self.rotors[i].connections[rotors_letter]

            # reflector pass
            reflector_letter = self.reflector.connections[rotors_letter]

            # second rotors pass
            opposite_rotors = []
            for i in range(len(self.rotors)):
                keys = list(self.rotors[i].connections.keys())
                values = list(self.rotors[i].connections.values())
                opposite_rotors.append(dict(zip(values, keys)))
            rotors_letter = reflector_letter
            for i in range(len(self.rotors)-1, -1, -1):
                rotors_letter = opposite_rotors[i][rotors_letter]

            # second plugboard pass
            if rotors_letter in self.plugboard.connections:
                final_plugboard_letter = self.plugboard.connections[rotors_letter]
            else:
                final_plugboard_letter = rotors_letter

            new_message += final_plugboard_letter
            self.rotors_rotation()
        return new_message

    def cypher(self):
        user_input = input('Insert a message: ')
        message = self.preprocess_message(user_input)
        cyphered_message = self.enigma_pass(message)
        print('Enigma encryption:', cyphered_message)

    def decypher(self, cyphered_message):
        for i in range(len(self.rotors)):
            self.rotors[i].connections = self.rotors_starting_config[i]
        decyphered_message = self.enigma_pass(cyphered_message)
        print(decyphered_message)
