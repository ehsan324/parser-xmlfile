def read_grammar(address: str):
    with open(address, "r") as file:
        lines = file.readlines()

    lines = [l.strip() for l in lines]

    grammar = {
        "Variables": [],
        "Terminals": [],
        "Start_Var": "",
        "Rules": {}
    }

    for line in lines:
        if line.startswith("Variables"):
            variables = line.replace("Variables: ", "").split(",")
            grammar["Variables"] = [v.strip() for v in variables]

        elif line.startswith("Terminals"):
            terminals = line.replace("Terminals: ", "").split(",")
            grammar["Terminals"] = [t.strip() for t in terminals]

        elif line.startswith("Start_Var"):
            grammar["Start_Var"] = line.replace("Start_Var: ", "").strip()
        elif line.startswith("Rules"):
            pass
        else:
            rule = line.split(",")
            if not grammar["Rules"].get(rule[0], []):
                grammar["Rules"][rule[0]] = [rule[1].strip()]
            else:
                grammar["Rules"][rule[0]].append(rule[1].strip())

    return grammar


def accept_string(string, grammar):
    # check characters in string
    for char in string:
        if char not in grammar["Terminals"]:
            return False

    rules = grammar["Rules"]
    stack = [grammar["Start_Var"]]
    index = 0

    while len(stack) > 0 and index < len(string):
        top = stack.pop()
        if top in grammar["Variables"]:
            if string[index] in grammar["Terminals"]:
                for rule in rules[top]:
                    if rule[0] == string[index]:
                        stack.extend(reversed(rule))
            else:
                return False
        elif top == string[index]:
            index += 1
        else:
            return False

    return index == len(string) and len(stack) == 0


if __name__ == "__main__":
    grammar = read_grammar("grammer.txt")

    while True:
        string = input()

        if string == "end":
            break

        if accept_string(string, grammar):
            print("The input string is accepted.")
        else:
            print("The input string is not accepted.")
