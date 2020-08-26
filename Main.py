import os
import time
import random
import threading

def timer_function(): #thread that decreases time
    global timer
    while True:
        time.sleep(1)
        timer -= 1

#configure some variables
timer_max_time = 60
timer = timer_max_time
words_typed_correctly = 0
words_typed_incorrectly = 0

#greet the users
print("Welcome to speed typer!")
print(f"You have {timer_max_time} seconds to type words that are picked from 3000 words.\nGood luck!\n")

#import the words
File = open("word_list.txt", "r")
random_word_list = File.read().split("\n")
File.close()

#start timer thread
timer_thread = threading.Thread(target=timer_function)
timer_thread.start()

#main game
while True: #main loop for the game
    input("Press ENTER to start! ")
    os.system("cls")
    current_game_running = True
    timer = timer_max_time

    while True: #one round
        five_random_words = []
        for i in range(5): #generate random word list of 5 words
            five_random_words += [random.choice(random_word_list)]

        five_random_words_string = ""
        for item in five_random_words:
            five_random_words_string += item + " "

        print("\n" + five_random_words_string)
        user_input = input("Type: ")
        user_input_list = user_input.split(" ")
        
        for i in range(len(user_input_list)):
            if user_input_list[i].lower() == five_random_words[i].lower():
                words_typed_correctly += 1
            else:
                words_typed_incorrectly += 1

        os.system("cls")

        if timer < 1:
            break #exit round when timer is below 1 after a word

    os.system("cls")
    print(f"\nGame over!\nResults:\n\n - Words typed correctly: {words_typed_correctly}\n - Words typed incorrectly: {words_typed_incorrectly}\n - Words/minute: {words_typed_correctly / timer_max_time * 60}\n")