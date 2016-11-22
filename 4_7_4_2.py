def parrot(voltage, state="a stiff", action="Voom"):
    print("-- This parrt wouldn't ", action, end="")
    print("if you put", voltage, "volts through it", end=" ")
    print("E's ", state, "!")


d = {"voltage": "four million", "state": "bleedin ' demised", "action": "Voom"}
parrot(**d)
