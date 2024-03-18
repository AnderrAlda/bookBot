def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number = text_character_number(text)
    counts = count_each_letter(text)
    sorted_counts = counts_to_sorted(counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number} words found in the document")

    for i in sorted_counts:
        if not i["char"].isalpha():
            continue
        print(f"The item {i['char']} character was found {i['num']} times")
    
    print("--- End report ---")

def counts_to_sorted(counts):
    res = []
    for o in counts:
        res.append({"char":o,"num":counts[o]})
    res.sort(reverse=True, key=lambda x: x["num"])
    return res

def count_each_letter(text):
    res = {}
    for c in text:
        c_lowered= c.lower()
        if c_lowered in res:
            res[c_lowered] += 1
        else:
            res[c_lowered] = 1
    return res

def text_character_number(text):
    splited = text.split()
    return len(splited)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()