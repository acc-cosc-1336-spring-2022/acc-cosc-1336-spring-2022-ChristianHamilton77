#main program

import strings
#strings.hello_world()

#strings.loop_str("hello")

#strings.loop_str_while("Hello")

#print(strings.concat_strings("Hello ","World"))

#print(strings.str_sub_str("seven","four scores in seven years ago"))

str = "Four score and Seven Years ago."
wordList = str.split()
print(wordList)
for word in wordList:
    print(word)