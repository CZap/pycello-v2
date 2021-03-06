__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class Gate:

    def __init__(self):
        self.name = ""
        self.promoter = ""

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def promoter(self):
        return self.__promoter

    @promoter.setter
    def promoter(self, promoter):
        self.__promoter = promoter

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, parts):
        self.__parts = parts

    @property
    def equation(self):
        return self.__equation

    @equation.setter
    def equation(self, equation):
        self.__equation = equation

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters):
        self.__parameters = parameters

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, variables):
        self.__variables = variables

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Part:

    def __init__(self):
        self.name = ""
        self.type = ""
        self.sequence = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):
        self.__sequence = sequence


class InputSensor(Gate):

    @property
    def hi(self):
        return self.__hi

    @hi.setter
    def hi(self, hi):
        self.__hi = hi

    @property
    def lo(self):
        return self.__lo

    @lo.setter
    def lo(self, lo):
        self.__lo = lo


class OutputReporter(Gate):
    pass


class Terminator(Part):

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        self.__strength = strength


class Ribozyme(Part):

    @property
    def efficiency(self):
        return self.__efficiency

    @efficiency.setter
    def efficiency(self, efficiency):
        self.__efficiency = efficiency


class UCF:

    def __init__(self, ucf):
        self.parts = []
        self.gates = []
        for coll in ucf:
            if coll['collection'] == 'parts':
                if coll['type'] == 'terminator':
                    part = Terminator()
                elif coll['type'] == 'ribozyme':
                    part = Ribozyme()
                else:
                    part = Part()
                part.name = coll['name']
                part.type = coll['type']
                part.sequence = coll['dnasequence']
                self.parts.append(part)
        for coll in ucf:
            if coll['collection'] == 'terminators':
                terminator = self.part(coll['name'])
                if (terminator):
                    terminator.strength = coll['strength']
            if coll['collection'] == 'ribozymes':
                ribozyme = self.part(coll['name'])
                if (ribozyme):
                    ribozyme.efficiency = coll['efficiency']
            if coll['collection'] == 'gate_structure':
                gate = Gate()
                gate.name = coll['gate_name']
                gate.promoter = self.part(coll['output'])
                # parts = []
                # for part in coll['expression_cassettes'][0]['cassette_parts']:
                #     parts.append(self.part(part))
                # gate.parts = parts
                self.gates.append(gate)
            if coll['collection'] == 'input_sensors':
                sensor = InputSensor()
                sensor.name = coll['name']
                sensor.promoter = self.part(coll['promoter'])
                sensor.parameters = coll['parameters']
                self.gates.append(sensor)
            if coll['collection'] == 'output_reporters':
                reporter = OutputReporter()
                reporter.name = coll['name']
                parts = []
                for part in coll['parts']:
                    parts.append(self.part(part))
                reporter.parts = parts
                self.gates.append(reporter)
        for coll in ucf:
            if coll['collection'] == 'response_functions':
                gate = self.gate(coll['gate_name'])
                gate.equation = coll['equation']
                parameters = {}
                for param in coll['parameters']:
                    parameters[param['name']] = param['value']
                gate.parameters = parameters
                variables = []
                for var in coll['variables']:
                    variables.append(var['name'])
                gate.variables = variables
            if coll['collection'] == 'gates':
                gate = self.gate(coll['gate_name'])
                gate.group = coll['group_name']
                gate.color = coll['color_hexcode']

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, parts):
        self.__parts = parts

    def part(self, name):
        for part in self.parts:
            if part.name == name:
                return part

    @property
    def gates(self):
        return self.__gates

    @gates.setter
    def gates(self, gates):
        self.__gates = gates

    def gate(self, name):
        for gate in self.gates:
            if gate.name == name:
                return gate
