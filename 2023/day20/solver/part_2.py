from solver import utils
from collections import defaultdict
import time, math, itertools

class Module():
    name = ""
    dests = []
    module_type = ""
    def __init__(self, name, dests):
        self.name = name
        self.dests = dests
    
    def input(self, pulse, source):
        output = []
        for dest in self.dests:
            output.append((self.name, dest, pulse))
        return output

    def __repr__(self):
        return f"{self.name}->(Type={self.module_type} Dests={self.dests})"
    def __str__(self):
        return f"{self.name}->(Type={self.module_type} Dests={self.dests})"

class Flipflop(Module):
    state = False
    module_type = "flipflop"
    
    def input(self, pulse, source):
        output = []
        if pulse == "low":
            if self.state:
                output = super().input("low", source)
            else:
                output = super().input("high", source)
            self.state =  not self.state
        return output

class Conjuction(Module):
    module_type = "conjuction"
    memory = None

    def __init__(self, name, dests):
        self.memory = {}
        super().__init__(name, dests)
    
    def init_memory(self, dests):
        for dest in dests:
            self.memory[dest] = "low"
        print(self.memory)

    def input(self, pulse, source):
        self.memory[source] = pulse
        output = super().input("high", source)

        if all([x == "high" for x in self.memory.values()]):
            output = super().input("low", source)

        return output

class Broadcast(Module):
    module_type = "broadcaster"

class Output(Module):
    module_type = "output"

    def __init__(self, name="rx", dests=[]):
        super().__init__(name, dests)

class Button(Module):
    module_type = "button"

def solve(input_file: str):
    lines = [x.replace(" ", "").split("->") for x in utils.read_lines(input_file)]
    print()

    modules = defaultdict(Output)
    conjuction_dests = defaultdict(list)
    for line in lines:
        mod_type = line[0][0]
        mod_name = line[0][1:]
        mod_dests = line[1].split(",")  

        module = None
        match mod_type:
            case "%":
                module = Flipflop(mod_name, mod_dests)
            case "&":
                module = Conjuction(mod_name, mod_dests)
            case "b":
                mod_name = "b" + mod_name
                module = Broadcast(mod_name, mod_dests)
        
        modules[mod_name] = module
        for dest in mod_dests:
            conjuction_dests[dest].append(mod_name)

    for module in modules.values():
        # print(module)
        if module.module_type == "conjuction":
            modules[module.name].init_memory(conjuction_dests[module.name])
    
    print() 

    counts = {"high": 0, "low":0}
    nlines = len(modules)
    print(f"\033[{nlines}S", end="")

    # move cursor back up
    print(f"\033[{nlines}A", end="")

    print("\nStarting Loop")
    # save current cursor position
    print("\033[s", end="")

    counter = 0
    per_key_state = defaultdict(lambda: defaultdict(int))

    for button_press in range(40000):
        counter +=1
        print("\033[u", end="")
        print(f"{button_press=}, {modules['jz'].memory}")

        queue = [[("button", "broadcaster", "low")]]
        per_button_count = 0
        for i, signal in enumerate(queue):
            for output in signal:
                source, dest, pulse = tuple(output)
                module = modules[dest]

                mod_key = None
                if module.module_type == "conjuction":
                    mod_key = str(module.memory)
                    
                if module.name == "rx":
                    mod_key = "on"

                if mod_key:
                    state = per_key_state[module.name][mod_key]
                    count = 0
                    occurances = [counter]
                    if type(state) == tuple:
                        count = state[1] + 1
                        if count < 10:
                            occurances = state[0] + occurances
                        else:
                            occurances = state[0]
                    per_key_state[module.name][mod_key] = (occurances, count)

                new_signals = module.input(pulse, source)

                queue.append(new_signals)
                counts[pulse] += 1

    print()
    cycles = []

    for state in per_key_state["jz"].items():
        # print(state)
        if "high" in state[0]:
            print(state)
            cycles.append(state[1][0])
    
    possible_combinations = list(itertools.product(*cycles))
    print("A posisble combination:", possible_combinations[0])
    possible_lcm = []
    for possible in possible_combinations:
        possible_lcm.append(math.lcm(*possible))

    print(min(possible_lcm))