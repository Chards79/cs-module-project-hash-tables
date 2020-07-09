def word_count(s):
    # Your code here
    word_num = {}

    tr = str.maketrans('', '', '":, .- += /\| []{}()*^ &')
    s = s.translate(tr).lower()

    words = s.split()

    for word in words:
        if word not in word_num:
            word_num[word] = 1
        else:
            word_num[word] =


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
