import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = {}

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result[value[0]] = value[1]

    def execute(self, data, mapper, reducer):
        
        for line in data:
            mapper(line)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        with open('data/index.json', 'w') as f:
            json.dump(self.result, f)
