from solver import utils
from collections import defaultdict

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

    def __init__(self, name="output", dests=[]):
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
    for button_press in range(1000):
        # print()
        # for mods in [modules["con"], modules["inv"]]:
        #     print("\t",mods, mods.memory)
        # for mods in [modules["a"], modules["b"] ]:
        #     print("\t",mods, mods.state)

        queue = [[("button", "broadcaster", "low")]]
        for signal in queue:
            for output in signal:

                source, dest, pulse = tuple(output)
                # print(f"{source} -{pulse}-> {dest}")
                queue.append(modules[dest].input(pulse, source))
                counts[pulse] += 1
        # print(f"\t{counts=}")
        # for mods in [modules["con"], modules["inv"]]:
        #     print("\t",mods, mods.memory)
        # for mods in [modules["a"], modules["b"] ]:
        #     print("\t",mods, mods.state)

    
    total_pulses = (counts["high"]) * (counts["low"])
    print(f"\n{total_pulses=}\n\t{counts=}")
    return total_pulses