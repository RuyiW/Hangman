import art
import words_list
import random

end_of_game = False
live = 6

random_word = random.choice(words_list.word_list)
word_len = len(random_word)
display = ["_"] * word_len

print(art.logo)
while not end_of_game:
    guess = input(f"Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed '{guess}'")
    else:
        if guess in random_word:
            for i in range(0, word_len):
                if guess == random_word[i]:
                    display[i] = guess
            if "_" not in display:
                end_of_game = True
        else:
            print(f"You guessed {guess}, that is not in the word. You lose a live.")
            live -= 1
            if live == 0:
                end_of_game = True
        print(' '.join(display))
        print(art.stages[live])

if live == 0:
    print("Game Over!")
else:
    print("You win!")