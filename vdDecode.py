import re

def replacer(phrase, index, char):
    result = phrase[:index] + char + phrase[index + 1:]
    return result

#print(replacer("hello", 1, "w"))

def xremover(phrase):
    lqueue = ""
    i=0
    removed = phrase.lower()
    for letter in removed:
        #print(lqueue)
        if letter in "aeiou":
            if len(lqueue) ==2:
                lqueue = lqueue[1:]
            lqueue += letter
        elif letter == "x":
            removed = replacer(removed, i, lqueue[0])
            lqueue = lqueue[::-1]
        i+=1
    return removed

# (Unused)
""" def scanner(phrase, index):
    cut = phrase[index+1:]
    
    for letter in cut:
        print(cut)
        if letter in "aeiou-+='/:":
            if letter in "aeiou":
                print(letter)
                return False
            else:
                return True
 """

def translate(phrase):
    lowered = phrase.lower()
    translation = ""
    symbols = "-+='/:"
    vowel = None
    space = ""
    lastThingIsLetter = False   
    i=0
    skip = False
    backSlashed = False
    for letter in lowered:
        
        if letter in "aeiou":
            if lastThingIsLetter:
                translation += vowel
            translation += space
            space = ""
            lastThingIsLetter = True
            vowel = letter
            backSlashed = False
            
        elif letter == "\\":
            if not backSlashed:  
                if lastThingIsLetter:
                    translation += vowel
                backSlashed = True
            skip = True
            
        elif letter in symbols:
            lastThingIsLetter = False
            i = symbols.find(letter)
            translation += space
            if skip == False:
                translation += chr(ord(vowel) + i)
            else:
                translation += letter
            skip = False   
            space = ""
            backSlashed = False
        else:
            space += letter
        
    if not backSlashed:        
        if lastThingIsLetter:
            translation += vowel
    if space != "":
        translation += space
    return translation        

def spacerem(phrase):
    nospace = ""
    for letter in phrase:
        if letter in "AEIOUaeiou-+='/:":
            nospace += letter

    return nospace

def lint(phrase):
    
    lsearch = re.search("[aeiou]-[aeiou]|[Aa][-\+'/:]*[Aa][-\+'/:]*|[Ee][-\+'/:]*[Ee][-\+'/:]*|[Ii][-\+'/:]*[Ii][-\+'/:]*|[Oo][-\+'/:]*[Oo][-\+'/:]*|[Uu][-\+'/:]*[Uu][-\+'/:]*", phrase)
    if lsearch != None:
        print("=== Imperfect phrase -->", lsearch)



print("Welcome to VowelDash Decoder! Enter a phrase to decode it into readable text.")
while True:

    n = input("VD>> ")
    lint(spacerem(n))
    t = translate(xremover(n))
    
    print(t)

#print(xremover("u+ox=ei'a'-o/e' io/ ai/xu:i-:e="))