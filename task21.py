str1 = input('Type (enter) string:\n')
str1 = str1.split()
start = 0

def max_word (str1):
    global start
    for i in str1:
        if len(i) > start:
            start = len(i)
            x = i    
    print('The longest word is: ' + str(x))
max_word (str1)
