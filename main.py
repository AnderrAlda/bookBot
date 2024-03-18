def main():
    path = "books/frankenstein.txt"
    book = readText(path)
    number = countWords(book)
    chars_dict = get_chars_dict(book)
    print(chars_dict)


 
def get_chars_dict(book):
    res = { }
    for c in book:
        lower = c.lower()
        if lower in res:
            res[lower] += 1
        else:
            res[lower] = 1
    return res



def countWords(text):
    words = text.split()
    return len(words)

def readText(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


main()