# creating a yellow color for the text
YELLOW = '\033[93m'

# defining the function
def count_words(text):
    # creating an array of words from the text by splitting the text on spaces and storing it in the variable words
    words = text.split()
    # using len function to get the length of the array, which is the number of words
    num_words = len(words)
    # returning the number of words... so easy
    return num_words

# getting input from the user
text = input("\nEnter a sentence or paragraph: ")
# calling the function and storing the return value in the variable word_count
word_count = count_words(text)
# printing the number of words
print(f"\nNumber of words: {YELLOW}{word_count}")