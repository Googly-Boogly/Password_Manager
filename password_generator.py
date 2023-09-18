import random

# Needs to add cryptography

def Generate_complex(pw_length):
    accepted_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']
    a2 = ['y', 'z', '!', '@', '{', '[', '}', ']',     '%', '^', '>', '<', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    final_inputs = accepted_inputs + a2
    length = len(final_inputs)
    password = ''
    for x in range(int(pw_length)):
        temp = final_inputs[(random.sample(range(0, length - 1),1))[0]]
        if str.isalpha(temp):
            if random.sample(range(0, 2),1)[0] == 0:
                temp = temp.upper()
        password = password + temp
    return password




def Generate_simple(pw_length):
    accepted_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    length = len(accepted_inputs)
    password = ''
    for x in range(int(pw_length)):
        temp = accepted_inputs[(random.sample(range(0, length - 1),1))[0]]
        if str.isalpha(temp):
            if random.sample(range(0, 2),1)[0] == 0:
                temp = temp.upper()
        password = password + temp
    return password

def Generate_medium(pw_length):
    accepted_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '%', '^', '&', '*', '?']
    length = len(accepted_inputs)
    password = ''
    for x in range(int(pw_length)):
        temp = accepted_inputs[(random.sample(range(0, length - 1),1))[0]]
        if str.isalpha(temp):
            if random.sample(range(0, 2),1)[0] == 0:
                temp = temp.upper()
        password = password + temp
    return password



# print(Generate_medium(15))