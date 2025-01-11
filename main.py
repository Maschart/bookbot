def main():
    book_path = "/home/martin/workspace/github.com/Maschart/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list= chars_dict_to_sorted_list(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character was found {item["num"]} times")

    print("------End report------")


def get_num_words(text):
    word = text.split()
    return len(word)



def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(chars):
    sort_lst = []
    for ch in chars:
        sort_lst.append({"char": ch, "num": chars[ch]})
    sort_lst.sort(reverse=True, key=sort_on)
    return sort_lst


#wird in ein dictonary einsortiert und gezählt
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def get_book_text(path):
    with open(path) as f:
        return  f.read()


main()