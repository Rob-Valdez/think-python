#!python3 C:\Users\kruser\PycharmProjects\think-python

def spell_down(word):
    for i in range(len(word)):
        print(word[i])

spell_down("turtle")

def count_up():
    index = 0
    fruit = "banana"
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index += 1

count_up()

def duck_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O':
            print(letter + 'u' + suffix)
        elif letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)

duck_names()