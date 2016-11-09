def create(eq_file):
    equation = open(eq_file)
    eq = []
    for line in equation:
        eq.append(line.strip())
    equation.close()
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
    
    eq = equation.copy()
    
    letter = []
    rank = []
    
    i = 0
    j = 1
    while i < len(eq):
        while j <= len(eq[i]):
            if not eq[i][-j].isalpha():
                j += 1
            else:
                letter.append(eq[i][-j])
                rank.append(j)
                break
        i += 1
        j = 1
    
    replace_char = letter[rank.index(min(rank))]
    
    i = 0
    while i < len(eq):
        new = eq[i].replace(replace_char, str(number))
        eq[i] = new
        i += 1
        
    return eq

def accept(equation):

    #print(equation)
    full = ""
    for item in equation:
        if item[0] == "0":
            return False
        full += item
    
    for char in full:
        if char.isalpha():
            return False
            
    # At this point, all characters are legitimate numbers. So they can be converted        
    sum_list = []
    i = 0
    while i < len(equation) - 1:
        sum_list.append(int(equation[i]))
        i += 1
    
    if sum(sum_list) == int(equation[-1]):
        #print("Found a solution")
        return True
    else:
        return False

def reject(equation):    
    
    #First digit check
    
    check_str = ""
    for item in equation:
        check_str += item[-1]
    for char in check_str:
        if char.isalpha(): # There are still digits to be changed
            return False # Therefore, the procedure must continue
    
    # All first items are digits
    first_digit = []
    for char in check_str:
        first_digit.append(int(char))
    
    if sum(first_digit[:-1])%10 != first_digit[-1]:
        return True
    else:
        return False

def solve(equation):
    
    if accept(equation):
        return equation
    
    elif not guess(equation):
        return []
    
    elif reject(equation):
        return []
                
    else:
        for num in guess(equation):
            temp = solve(replace(equation, num))
            
            if temp:
                return temp
            
eq = ["AB", "CB", "DBB"]#create("equations/00.txt")
    
for i in range(19):
    
    if len(str(i)) == 1:
        i = "0"+str(i)
    else:
        i = str(i)
            
    eq = create("equations/"+i+".txt")
    
    display(eq)
    print()
    display(solve(eq))
    print()

