def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def number_words(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def sorted_list(chars):
    list = []
    for c in chars:
        list.append({"char": c, "num": chars[c]})
    list.sort(reverse=True, key=sort_on)
    return list