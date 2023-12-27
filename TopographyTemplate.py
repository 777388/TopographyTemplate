import sys
class instantiate:
    instance = []
if (sys.argv[2] == "number"):
    for i in range(int(sys.argv[1])):
        instantiate.instance.append(i)
if (sys.argv[2] == "string"):
    for I in sys.argv[1]:
        instantiate.instance.append(I)
if (sys.argv[2] == "file"):
    with open(sys.argv[1], "r") as f:
        for line in f:
            for character in line:
                instantiate.instance.append(character)
topography = lambda node: print(node, end="")

(list(map(topography, instantiate.instance)))
