# pig latin

# if start with consanant, move the first letter to the end, and add i
# if start with vowel, move the first letter to the end, and add ah
# this is slightly diff from the rule in wikipedia, i purposely did it in reverse order

# input a text, split by space, and change the words, put the back


import sys


def changeText(str1):
    temp = str1[0]
    if type(temp) is str:
        if temp.lower() in ['a','e','i','o','u']:
            str2 = str1[1:] + temp + 'ah'
        else:
            str2 = str1[1:] + temp + 'i'
    else:
        str2 = str1
    return str2


text = sys.argv[1]
newWords = map(lambda x:changeText(x),text.split())
newParagraph = ''
for item in newWords:
    newParagraph = newParagraph+item+' '

print newParagraph
