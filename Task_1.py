import random

# Predefined list of words
word_list = ["apple", "grape", "mango", "peach", "melon"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game variables
guessed_word = ["_"] * word_length
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("Guess the word: ", " ".join(guessed_word))

# Game loop
while tries > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabetical letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
        for i in range(word_length):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
    else:
        tries -= 1
        print("❌ Wrong guess! Tries left:", tries)

    print("Current word: ", " ".join(guessed_word))

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
