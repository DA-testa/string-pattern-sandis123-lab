# python3

def read_input():
    data = input()
    if data[0]=="I":
        pattern=input()
        text = inpit()
     elif data[0]=="F":
        inputf = '06'
        inputf = "tests/" + inputf
       
        with open(inputf, 'r') as file:
                pattern, text = file.read().splitlines()
    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
            
        
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
     print(' '.join(map(str, output)))
def get_occurrences(pattern, text):
    lP = len(pattern)
    lT = len(text)
    hP = hash(pattern)
    hT = hash(text[:lP])
    output = []
    for i in range(lT-lP+1):
        if hP == hT:
            if pattern == text[i:i+lP]:
                output.append(i)
            else:
                for j in range(lP):
                    if text[i+j] != pattern[j]:
                        break
                else:
                    output.append(i)
        if i < lT-lP:
            hT = hash(text[i+1:i+lP+1])
    return output
    
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
