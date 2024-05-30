def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_counter(file_contents)

def word_counter(text):
    text_list = text.split()
    total_count = len(text_list)
    print(total_count)


main()