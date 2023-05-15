#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abiodun Obafemi
CPS 3320-01
Final Project
Language Learning App
"""
# Importing random module
import random

# Dictionary with greetings in a list of different languages
greetings = {
    "English": "Hello!",
    "Spanish": "¡Hola!",
    "Chinese": "Nǐ hǎo",
    "French": "Bonjour!",
    "German": "Guten Tag!",
    "Italian": "Ciao!",
    "Japanese": "こんにちは！",
    "Mandarin": "你好！",
    "Turkish": "Selam!",
    "Korean": "안녕하세요!",
    "Russian": "Здравствуйте!",
    "Arabic": "مرحبا!",
    "Portuguese": "Oi",
    "Hindi": "नमस्ते!",
    "Greek": "Yassou",
}

# Looping through the dictionary to print a list of language choices
print("\nWelcome to the Language Learning App!\n")
print("Here is a list of languages where you can learn how to greet someone:\n")
for i, language in enumerate(greetings, start=1):
    print(f"{i}. {language}")

# User input
pick = int(input("Choose a language by number: "))

# Creating list of languages
languages = list(greetings.keys())

# Checking if input is within the range of the list
if pick in range(1, len(languages) + 1):
    chosenLang = languages[pick - 1]
    greet = greetings[chosenLang]
    print(greet)

# Asks user if they want to practice
    practice = input("Would you like to practice this greeting? ('Y' for Yes / 'N' for No): ").lower()

# Asks user to translate the greeting if they choose yes to practice
    if practice == 'y':
        translate = input(f"Please translate the following '{greet}' into English: ")
        # Checking if input is correct
        if translate.lower() == 'hi' or translate.lower() == 'hello':
            print("That is correct!")
        else:
            print(f"This is incorrect. The correct translation is '{greetings['English']}'")
            
else:
    print("Invalid input. Please choose a language within the range of 1-13.")
