#created by ehsan alami


address = "grammer.txt"

def build_structure(address):
    with open(address, "r") as file:
        lines = file.readlines()
        
    strucure = {
        "Variables": [], "Terminals": [],"Start_Var": "", "Rules": {}
    }

    for line in lines:
        
        if line.startswith("V"):
            line = line.replace("Variables: ", "")
            variables = line.split(",")
            for v in variables:
                strucure["Variables"].append(v.strip())
            
        elif line.startswith("T"):
            line = line.replace("Terminals: ", "")
            terminals = line.split(",")
            for t in terminals:
                strucure["Terminals"].append(t.strip())
        
        elif line.startswith("Start"):
            line = line.replace("Start_Var: ", "")
            start = line.split(",")
            for s in start:
                strucure["Start_Var"] = [s.strip()]
            
            
            
        elif line.startswith("Rules"):
            pass
        
        else:
            rule = line.split(",")
            if not strucure["Rules"].get(rule[0], []):
                strucure["Rules"][rule[0]] = [rule[1].strip()]
            
            else:
                strucure["Rules"][rule[0]].append(rule[1].strip())
    return strucure                
                
def checktext(text, structure):

    lookahead = 0    
    rules = structure["Rules"]
    stack = structure["Start_Var"]    
           
    for i in text:
        if i not in structure["Terminals"]:
            return False
    
        
    while lookahead < len(text) and len(stack) > 0:
        top = stack.pop()
        if top in structure["Variables"]:
            for rule in rules[top]:
                    if rule[0] == text[lookahead]:
                        stack.extend(reversed(rule))
        elif top == text[lookahead]:
            lookahead += 1
        else:
            return False
        
    status = lookahead == len(text) and len(stack) == 0      
    return status


status = True

grammer = build_structure(address)


string = input()


if checktext(string, grammer):
    print("The input string is accepted.")
else:
    print("The input string is not accepted.")
        
    
            
    
    
    
    
    
        