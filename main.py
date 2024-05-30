text = file_contents

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_counter(text):
    text_list = text.split()
    print(text_list)


main()