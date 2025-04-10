
def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()



def main():
    
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    # print(text)


    from stats import num_words
    from stats import letter_count
    from stats import sort_letters

    letter_counts = letter_count(text)

    sorted_letters = sort_letters(letter_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")
    print("--------- Character Count -------")


    for item in sorted_letters:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")


    print("============= END ===============")

main()