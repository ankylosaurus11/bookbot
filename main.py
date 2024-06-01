def word_counter(text):
    text_list = text.split()
    return len(text_list)

def character_counter(words):
    letter_dictionary = {}
    for i in words:
        if i in letter_dictionary.keys():
            letter_dictionary[i] += 1
        else:
            letter_dictionary[i] = 1
    return letter_dictionary


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = word_counter(file_contents)
    individual_characters = character_counter(list(file_contents.lower()))
    print(individual_characters)
    print(word_count)

if __name__ == "__main__":
    main()