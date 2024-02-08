import xml.etree.ElementTree as ET


Alphabets = []
States = []
Transition = []
transit = []
final = []
initial = []


def parser():
    global Alphabets, States, Transition, transit, final, initial
    tree = ET.parse('pattern.xml')
    root = tree.getroot()
    

    if root[0].tag == "Alphabets":
        for i in range(int(root[0].get("numberOfAlphabets"))):
            Alphabets.append(root[0][i].get('letter'))
    elif root[0].tag == "States":
        for i in range(int(root[0].get("numberOfStates"))):
            States.append(root[0][i].get('name'))
        num1 = num = int(root[0].get("numberOfStates"))
        initial.append(root[0][int(root[0].get("numberOfStates"))].get('name'))
        if root[0][int(root[0].get("numberOfStates"))+1].get('numberOfFinalStates'):
            for i in range(int(root[0][num+1].get('numberOfFinalStates'))):
                final.append(root[0][num+1][i].get('name'))           
    else :
        for i in range(0,2):
            transit.append(root[0][i].get('source'))
            transit.append(root[0][i].get('destination'))
            transit.append(root[0][i].get('label'))
            Transition.append(transit)
            transit = []
                
        
    if root[1].tag == "Alphabets":
        for i in range(int(root[1].get("numberOfAlphabets"))):
            States.append(root[1][i].get('letter'))
    elif root[1].tag == "States":
        for i in range(int(root[1].get("numberOfStates"))):
            States.append(root[1][i].get('name'))
        num1 = num = int(root[1].get("numberOfStates"))
        initial.append(root[1][int(root[1].get("numberOfStates"))].get('name'))
        if root[1][int(root[1].get("numberOfStates"))+1].get('numberOfFinalStates'):
            for i in range(int(root[1][num+1].get('numberOfFinalStates'))):
                final.append(root[1][num+1][i].get('name'))
    else :
        for i in range(0,2):
            transit.append(root[1][i].get('source'))
            transit.append(root[1][i].get('destination'))
            transit.append(root[1][i].get('label'))
            Transition.append(transit)
            transit = []
    if root[2].tag == "Alphabets":
        for i in range(int(root[2].get("numberOfAlphabets"))):
            States.append(root[2][i].get('letter'))
    elif root[2].tag == "States":
        for i in range(int(root[2].get("numberOfStates"))):
            States.append(root[2][i].get('name'))
        num1 = num = int(root[2].get("numberOfStates"))
        initial.append(root[2][int(root[2].get("numberOfStates"))].get('name'))
        if root[1][int(root[2].get("numberOfStates"))+1].get('numberOfFinalStates'):
            for i in range(int(root[2][num+1].get('numberOfFinalStates'))):
                final.append(root[2][num+1][i].get('name'))      
    else :
        for i in range(int(root[2].get("numberOfTrans"))):
            transit.append(root[2][i].get('source'))
            transit.append(root[2][i].get('destination'))
            transit.append(root[2][i].get('label'))
            Transition.append(transit)
            transit = []  
             
  
def Analysis(text):
    init = ''
    arr = []
    Arrtext = []
    
    for i in range(len(text)):
        Arrtext.append(text[i])
        
    for i in range(len(initial)):
        init = initial[i]
    arr.append(init)
    arr.append("")
    arr.append(Arrtext[0])
    Arrcount = 1
    for j in range(1,len(Arrtext)+1):
        for i in range(len(Transition)):
            if (arr[0] != Transition[i][0] or arr[2] != Transition[i][2]) and i == len(Transition)-1:
                print("unaccepted") 
                exit()
            if arr[0] == Transition[i][0] and arr[2] == Transition[i][2] or j > len(Arrtext):
                arr[0] = Transition[i][1]
                try:
                    arr[2] = Arrtext[j]
                except IndexError:
                    print("accepted")
                    exit()
                i=0
                break
            

        
parser()   
print(f"alph: {Alphabets}")
print(f"init: {initial}") 
print(f"state: {States}")
print(f"tran: {Transition}")
print(f"final: {final}")
Analysis('ababa')
 


