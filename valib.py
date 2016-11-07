def create(eq_file):
    equation = open(eq_file)
    eq = []
    for line in equation:
        eq.append(line.strip())
    return eq

def display(equation):
    max_len = 0
    list_len = len(equation)
    
    for item in equation:
        if max_len < len(item):
            max_len = len(item)
    
    i = 0
    while i < (list_len - 2):
        string = " "*(max_len-len(equation[i]) + 2) + equation[i]
        print(string)
        i += 1
        
    print("+ " + " "*(max_len - len(equation[-2])) + equation[-2])
    print("-"*(max_len+2))
    print(" "*(max_len - len(equation[-1])+2) + equation[-1])
    
    return
    
def guess(equation):
    available = list(range(0, 10))
    number = []
    all_items = ""
    for item in equation:
        all_items += item
    
    noLetter = True
    
    for char in all_items:
        if char.isdigit(): #The character is a number
            if int(char) in available: #The number has not already been removed
                available.remove(int(char))
        else:
            noLetter = False #There is still a character
    
    if noLetter:
        return []
    
    else:
        return available

def replace(equation, number):
    
    letter = []
    rank = []
    
    i = 0
    j = 1
    while i < len(equation):
        while j <= len(equation[i]):
            if not equation[i][-j].isalpha():
                j += 1
            else:
                letter.append(equation[i][-j])
                rank.append(j)
                break
        i += 1
        j = 1
        
    replace_char = letter[rank.index(min(rank))]
    
    i = 0
    while i < len(equation):
        new = equation[i].replace(replace_char, str(number[0]))
        equation[i] = new
        i += 1
        
    return equation

def accept(equation):
    if reject(equation):
        return False
    else:  # At this point, all characters are legitimate numbers. So they can be converted        
        sum_list = []
        i = 0
        while i < len(equation) - 1:
            sum_list.append(int(equation[i]))
            i += 1
        
        if sum(sum_list) == int(equation[-1]):
            print("Found the solution")
            return True
        else:
            print("Numbers are not correct")
            return False

def reject(equation):
    full = ""
    for item in equation:
        if item[0] == "0":
            print("One item starts with 0")
            return True
        full += item
    for char in full:
        if char.isalpha():
            print("Not all are characters")
            return True
    return False

def solve(equation):
    if accept(equation):
        return equation
    elif guess(equation):
        print("Can try more:", guess(equation))
        equation2 = replace(equation, guess(equation))
        print(equation2)
        return solve(equation2)
    else:
        return []
    
eq = create("equations/00.txt")

print(solve(eq))
