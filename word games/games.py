import random
from the_words import select_items


class WordJumble:
    NO_OF_WORDS = 10
    words = []
    jumble_ones = []

    def __init__(self) -> None:
        self.generate()
        self.jumble_words()

    def generate(self):
        self.words = select_items(self.NO_OF_WORDS)

    def jumble_words(self):
        for word in self.words:
            jumbled_word = "".join(random.sample(word, len(word)))
            self.jumble_ones.append(jumbled_word)

    def generate_en(self):
        chosen_word = random.choice(self.jumble_ones)
        # sln_word = self.jumble_ones[self.words.index(chosen_word)]
        return chosen_word

    # def generate_sw(self):
    #     chosen_word = random.choice(self.sw_words)
    #     # sln_word = self.jumble_sln_sw[self.sw_words.index(chosen_word)]
    #     return chosen_word

    def check_answer(self, quest, answer):
        if answer.lower() == self.words[self.jumble_ones.index(quest)].lower():
            return {"message": "Correct", "answer": self.words[self.jumble_ones.index(quest)].lower()}
        else:
            return {"message": "Wrong", "answer": self.words[self.jumble_ones.index(quest)].lower()}


class LetterCompletion:
    letters = [
        "Random",
        "Fish",
        "Planet",
        "Telecom",
        "Voucher",
        "Yellow",
        "Queen",
        "Hand"
    ]

    def randomize_word(self):
        chosen_word = random.choice(self.letters)
        # Choose the number of letters to replace
        num_replace = random.randint(1, len(chosen_word) - 1)

        # Choose which letters to replace
        replace_indices = random.sample(range(len(chosen_word)), num_replace)

        # Replace the letters with underscores
        new_word = ""
        for i in range(len(chosen_word)):
            if i in replace_indices:
                new_word += "_"
            else:
                new_word += chosen_word[i]

        return {
            "un_word": new_word,
            "answer": chosen_word
        }

    def check_answer(self, response, answer):
        if answer.lower() == response["answer"].lower():
            return "Correct"
        else:
            return "wrong"


game1 = WordJumble()
game2 = LetterCompletion()

attempts = 5
# Game 1
while attempts > 0:
    theWord = game1.generate_en()
    theAnswer = input(f"Answer this: {theWord} \n")
    print(game1.check_answer(theWord, theAnswer))
    attempts -= 1

# Game 2
# while attempts > 0:
#     theWord = game2.randomize_word()
#     theAnswer = input(f"Answer this: {theWord['un_word']} \n")
#     print(game2.check_answer(theWord, theAnswer))
#     attempts -= 1
