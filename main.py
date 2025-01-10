def main():
    book_path = "/home/martin/workspace/github.com/Maschart/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    word = text.split()
    return len(word)


def get_book_text(path):
    with open(path) as f:
        return  f.read()


main()