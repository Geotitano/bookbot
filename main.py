
def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()



def main():
    
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    # print(text)

    num_words = len(text.split())
    print(f"{num_words} words found in the document")


main()