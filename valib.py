"""

Verbal Arithmetic Solver v1.1

Author: Halil Utku Unlu
Date: Fall 2016 - 9 Nov 2016

This program contains functions needed to solve the verbal arithmetic problems, which are puzzles given in the form:

    SEND
  + MORE
  ------
   MONEY 

The aim is to find correct substitutions for letters to satisfy the given equation.

v1.1:
    -   Improvements to reject function to enhance speed
    -   Some changes to variable names

"""

def create(eq_file):
    equation = open(eq_file)
    eq = []
    for line in equation:
        eq.append(line.strip())
    equation.close()
    return eq
    

def display(equation):
    """
    Given a list of strings, converts them into a visual sum. If there are no viable options (i.e. when an empty list is passed), the function prints "No solutions"
    """
    
    if not equation: 
        print("No solution")
        return
    
    max_len = 0
    list_len = len(equation)
    
    # Selecting the longest element in order to determine the placement of words
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
    """
    Given a list of strings, returns a list of integers, which are not present in any string in the initial list. Using this, a number to be replaced by replace function can be determined
    """

    available = list(range(0, 10))
    number = []
    all_items = ""
    for item in equation:
        all_items += item
    
    noLetter = True
    
    for char in all_items:
        if char.isdigit():  #The character is a number
            if int(char) in available: #The number has not already been removed
                available.remove(int(char))
        else:
            noLetter = False #There is still a character
    
    # If the list contains only numbers, no guesses are possible
    if noLetter:
        return []
    
    else:
        return available

def replace(equation, number):
    """
    Given a list of strings and an integer, replaces all instances of a letter by that integer as a string. Priority is given to the leftmost letter
    """
    eq = equation.copy()
    
    letter = []
    rank = []
    
    i = 0
    j = 1
    while i < len(eq):
        while j <= len(eq[i]):
            if not eq[i][-j].isalpha(): # Alternatively if xxx.isdigit(), but the focus is on the alpha, not on digit
                j += 1
            else:
                letter.append(eq[i][-j])
                rank.append(j)
                break
        i += 1
        j = 1
    
    # The lowest rank indicates the leftmost character
    replace_char = letter[rank.index(min(rank))]
    
    i = 0
    while i < len(eq):
        new = eq[i].replace(replace_char, str(number))
        eq[i] = new
        i += 1
        
    return eq

def accept(equation):
    """
    Given a list of strings, checks the equation to determine whether the given equation satisfies 3 rules: 
        1-) All characters are numbers
        2-) No number starts with 0
        3-) Out of n elements, the sum of first n-1 elements gives nth element
    
    If these conditions are met, the function returns True. Otherwise, the equation is not correct, and is not accepted
    """
    
    full = ""
    
    # Checking first digits (Rule 2)
    for item in equation:
        if item[0] == "0":
            return False
        full += item
    
    # Checking if all are numbers (Rule 3)
    for char in full:
        if char.isalpha():
            return False
            
    # At this point, all characters are legitimate numbers. Proceeding to check Rule 3    
    sum_list = []
    i = 0
    while i < len(equation) - 1:
        sum_list.append(int(equation[i]))
        i += 1
    
    # Solution is correct
    if sum(sum_list) == int(equation[-1]):
        return True
    else:
        return False

def reject(equation):    
    """
    Given a list of strings, checks if the completed digits satisfy the sum. If the progression is not viable, the solution is rejected and a different solution is tested 
    """
    
    #First letter position check
    letter_pos = []
    
    for word in equation:
        for char_pos in range(1, len(word)+1):
            if word[-char_pos].isalpha():
                letter_pos.append(char_pos-1)
                break
    
    if not letter_pos: # The equation is complete, so let accept check it
        return False
    
    level = min(letter_pos)
    
    if not level: # There are no digits which are complete
        return False
    
    until_level = []
    
    for word in equation:
        until_level.append(int(word[-level:]))
    
    # Equation legitimacy check
    if sum(until_level[:-1])%(10**level) != until_level[-1]:
        return True
    else:
        return False

def solve(equation):
    """
    Given an equation in the form of a list of strings, solves the equation recursively, using other functions defined in the program's scope.
    """
    # Base cases    
    if reject(equation):
        return []

    elif accept(equation):
        return equation
    
    elif not guess(equation):
        return []
    
    # Recursive step
    else:
        for num in guess(equation):
            temp = solve(replace(equation, num))
            if temp: # The solution found is correct if temp is assigned a non-empty list
                return temp
                
