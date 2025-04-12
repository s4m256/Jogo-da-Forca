import os
import random

class Game:
    def __init__(self, word, discovered, guessed, correct, attempts, left):
        self.word = word
        self.discovered = discovered
        self.guessed = guessed
        self.correct = correct
        self.attempts = attempts
        self.left = left
    
    def update(self, guess):
        correct = guess in self.word
        new_discovered = [self.discovered[i] | (self.word[i]==guess) for i in range(len(self.word))]
        new_attempts = self.attempts + [guess]
        if correct:
            new_left = self.left
        else:
            new_left = self.left - 1
        return Game(self.word, new_discovered, guess, correct, new_attempts, new_left)
    
    def win(self):
        return all(self.discovered)
    
    def loose(self):
        return self.left == 0
    
    def __str__(self):
        os.system('cls')
        output = "\n\n"

        if self.correct == True:
            output += f"Boa! A letra '{self.guessed}' está na palavra\n\n"
        elif self.correct == False:
            output += f"A letra '{self.guessed}' não está na palavra\n\n"
        else:
            output += f"Bem-vindo ao jogo da Forca!\n\n"

        output += "Palavra: "
        hidden_word = "".join([self.word[i] if self.discovered[i] else "_" for i in range(len(self.word))])

        output += f"{hidden_word}\n\n"

        output += f"Tentativas restantes: {self.left}\n\n"
        
        output += "Letras tentadas:"

        attempted_letters = ", ".join(self.attempts)
        output += f"{attempted_letters}\n\n"

        output += "Digite uma letra: "

        return output
    



words = []

with open("C:/Users/User/Desktop/words.txt") as file:
    for word in file:
        words.append(word[:-1])

word = random.choice(words).upper()
discovered = [False] * len(word)
guessed = None

correct = None
attempts = []
left = 6

game = Game(word, discovered, guessed, correct, attempts, left)

while(True):
    print(game)
    guess = input()
    while len(guess) != 1 or not guess.isalpha():
        print("Entrada inválida, tente novamente.")
        guess = input()
    guess = guess.upper()
    game = game.update(guess)
    if game.loose() or game.win():
        os.system("cls")
        break

if game.win():
    print(f"Parabéns! Você acertou a palavra: {word}")
elif game.loose():
    print(f"Fim de jogo! A palavra era: {word}")