class flashcard:
    def __init__(self, word,meaning ):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+ "( " + self.meaning + " )"
flashcards = []
print("Welcome to Flashcards!")
while True:
 word = input("Enter a word to add to the flashcards: ")
 meaning = input("Enter the meaning of the word: ")
 flashcards.append(flashcard(word, meaning))
 option = int(input("Do you want to add another flashcard? (1 for yes, 0 for no): "))
 if (option == 0):
    break
print("\nHere are your flashcards:")
for i in flashcards:
    print(i)