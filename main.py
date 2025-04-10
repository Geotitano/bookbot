import sys 


def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)


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

if __name__ == "__main__":
    main()