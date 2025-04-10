def num_words(text):

    return len(text.split())

def letter_count(text):
    text = text.lower()
    letter_amount = {}
    for letter in text:
        if letter in letter_amount:
            letter_amount[letter] += 1
        else:
            letter_amount[letter] = 1
    return letter_amount

def sort_letters(letter_amount):
    letlist = []

    for char, count in letter_amount.items():
        letlist.append({"char": char, "count": count})

    def sorter(dict_items):
        return dict_items["count"]

    letlist.sort(reverse=True, key=sorter)
    return letlist
    