import turtle as t
import string
import random

def draw_square(color, letter):
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()
    t.pu()
    t.fd(50)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.color('white')
    t.write(letter.upper(),
            font=("Arial",
                  50, "bold"),
            align='center')
    t.color('black')
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.bk(50)
    

def draw_empty_square():
    t.pd()
    t.fillcolor('#646464')
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.lt(90)
    t.end_fill()
    t.pu()

def draw_empty_row():
    t.setheading(0)
    for i in range(4):
        draw_empty_square()
        t.fd(150)
    draw_empty_square()
    t.bk(600)

def draw_board():
    global word
    global guesses
    global game_over
    if game_over:
        return
    t.goto(-350, 375)
    for i in range(len(guesses)):
        draw_guess_results(word, guesses[i])
        t.rt(90)
        t.fd(150)
        t.lt(90)
    for i in range(len(guesses),6):
        draw_empty_row()
        t.rt(90)
        t.fd(150)
        t.lt(90)

def draw_guess_results(word, guess):
    for i in range(len(word)):
        if guess[i] == word[i]:
            draw_square("green", guess[i])
        elif guess[i] in word:
            draw_square("#DDCD29", guess[i])
        else:
            draw_square('#646464', guess[i])
        t.fd(150)
    t.bk(150 * len(word))

def backspace():
    global index
    global guesses
    global cur_guess
    global game_over
    if game_over:
        return
    if index > 0:
        t.goto(-350, 375)
        t.rt(90)
        for i in range(len(guesses)):
            t.fd(150)
        t.lt(90)
        for i in range(index-1):
            t.fd(150)
        t.pu()
        draw_empty_square()
        cur_guess = cur_guess[:-1]
        index -= 1

def write(letter):
    global index
    global guesses
    global cur_guess
    global game_over
    if game_over:
        return
    if index < 5:
        t.goto(-350, 375)
        t.rt(90)
        for i in range(len(guesses)):
            t.fd(150)
        t.lt(90)
        for i in range(index):
            t.fd(150)
        t.pu()
        t.fd(50)
        t.lt(90)
        t.fd(10)
        t.rt(90)
        t.color('white')
        t.write(letter.upper(),
                font=("Arial",
                      50, "bold"),
                align='center')
        t.color('black')
        t.lt(90)
        t.bk(10)
        t.rt(90)
        t.bk(50)
        cur_guess += letter
        index += 1

def enter_word():
    global index
    global guesses
    global cur_guess
    global word
    global game_over
    global word_set
    if game_over:
        return
    if index == 5 and len(cur_guess) == 5 and cur_guess in word_set:
        guesses += [cur_guess]
        t.clear()
        index = 0
        draw_board()
        if cur_guess == word:
            game_over = True
        cur_guess = ""
    if len(guesses) >= 6:
        t.goto(0, -470)
        t.color('white')
        t.write("The word was " + word,
                font=("Arial", 25, "normal"),
                align='center')

global word
words = []
global word_set
word_set = set()
with open('wordle_word_list.txt', 'r') as file:
    for line in file:
        words.append(line.strip())
        word_set.add(line.strip())
word = random.choice(words)
t.bgcolor('black')
#print(word[0])
guesses_made = 0
screen = t.Screen()
#6 rows, 100x100, gap of 50, 75 on top and bottom
#600 + 250 + 150 = 1000
#5 cols, 100x100, gap of 50, 150 on top and bottom
#500 + 200 + 300
screen.setup(1000, 1000)
t.pu()
t.speed(0)
#t.hideturtle()
t.tracer(0)
t.goto(-350, 375)
global index
index = 0
global guesses
guesses = []
global cur_guess
cur_guess = ""
global game_over
game_over = False
draw_board()
t.color('white')
all_characters = string.ascii_letters
for key in all_characters:
    screen.onkeypress(lambda key=key: write(key), key)
screen.onkeypress(backspace, "BackSpace")
screen.onkeypress(enter_word, "Return")
screen.listen()
screen.mainloop()
