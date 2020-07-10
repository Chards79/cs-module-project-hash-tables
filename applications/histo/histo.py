# Your code here

def count_words(file):
    ignored_chars = '\":;,.-+=/\|[]{}()*^&'

    word_map = {}

    with open(file) as f:
        words = f.read().lower()
        for char in ignored_chars:
            words = words.replace(char, "")
        words = words.split()

    for word in words:
        if word not in word_map:
            word_map[word] = 1
        else:
            word_map[word] += 1
    return word_map

def render_word_count(dic):
    counts = [(dic[word], word) for word in dic]
    counts.sort(key = lambda e: (-e[0], e[1]))

    max_length = 0
    for word in counts:
        if len(word[1]) > max_length:
            max_length = len(word[1])

    print(max_length)
    for word in counts:
        print(f'{word[1]}\t'.expandtabs(max_length + 2) + "#" * word[0])
    

render_word_count(count_words("robin.txt"))
