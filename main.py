def word_counter(text):
    text_list = text.split()
    return len(text_list)

def character_counter(words):
    character_count = {}


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = word_counter(file_contents)
    print(word_count)

if __name__ == "__main__":
    main()