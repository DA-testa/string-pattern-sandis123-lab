# python3
def read_input():
    choice = input()
    if "I" in choice[:1]:
        text = input().rstrip()
        pattern = input().rstrip()
    elif "F" in choice:
        with open("./tests/06", "r") as file:
            text = file.readline().rstrip()
            pattern = file.readline().rstrip()
    return (text, pattern)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    for i in range(text_len - pattern_len + 1):
        text1 = text[i:i + pattern_len]
        if hash(text1) == pattern_hash:
            if text1 == pattern:
                occurrences.append(i)
    return occurrences
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow 
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    # this function should control output, it doesn't need any return
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    # this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
