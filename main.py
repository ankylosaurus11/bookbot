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

def aggregate_data(data):
    new_data = {}
    for i in data:
        if i.isalpha():
            new_data[i] = data[i]
    return new_data

def sort_dic(aggregation):
    full_data = []
    for key, value in aggregation.items():
        full_data.append({"letter": key, "count": value})
    return full_data

def sorting(sort):
    return sort["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = word_counter(file_contents)
    individual_characters = character_counter(list(file_contents.lower()))
    aggregation = aggregate_data(individual_characters)
    sorted_out = sort_dic(aggregation)
    sorted_out.sort(reverse=True, key=sorting)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document" 
    "\n")
    for i in sorted_out:
        print(f"The {i["letter"]} character was found {i["count"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()