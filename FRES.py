TEXT1 = ["The politician who holds the authority of all EU countries has just completely condemned a chunk of the British cabinet wondering aloud",
"What that special place in hell looks like for those who promoted Brexit without even a sketch of a plan how to carry it out safely",
"Sure for a long time the EU has been frustrated with how the UK has approached all of this",
"And sure plenty of voters in the UK are annoyed too at how politicians have been handling these negotiations",
"But it is quite something for Donald Tusk to have gone in like this studs up even though he sometimes reminisces about his time as a football hooligan in his youth"]

TEXT2 = ["An outbreak of the flu in Alabama has closed an elementary and middle school with school officials struggling to find enough healthy teachers to teach",
"The schools will be closed for the rest of the week because of the number of cases of flu among students and employees",
"Lawrence County Schools Superintendent Jon Bret Smith told news outlets that Moulton Elementary School and Moulton Middle School are closed Wednesday through Friday"]

 
def getFRES(sentenceCount,wordCount,syllableCount):
    # the given formula for "fres"
    fres = 206.835 - (1.015 * (wordCount / sentenceCount)) - (84.6 * (syllableCount / wordCount))
    return fres

def getTextData(text):
    vowels = "AEIOUaeiou"

    # using list comprehension for simplicity
    # not much different than a for loop, but more readable for this purpose

    # generate a list of words by splitting on whitespace in each sentence
    wordArr = [word
                for sentence in text
                for word in sentence.split()]
    
    #generate a list of letters ( vowels )
    vowelArr = [letter
                for sentence in text
                for letter in sentence
                if letter in vowels]
                
    #count the number of instances for each list
    sentenceCount = len(text)
    wordCount = len(wordArr)
    vowelCount = len(vowelArr)
    
    # return only what we actually need ( the numbers )
    return sentenceCount,wordCount,vowelCount



tex1 = getTextData(TEXT1) #tex1  contains all three of the parameters for Fres, in the same order ( for simplicity )
tex2 = getTextData(TEXT2)

#vowelCount as an estimate, substitutes for the actual syllable count 'getTextData()[2]'

fres1 = getFRES(*tex1) #pass the unpacked text1 data as params for the fres method
fres2 = getFRES(*tex2)

print(f"""
        _______________________________________________
        |  TEXT1:
        |
        |  number of sentences = {tex1[0]}
        |  number of words = {tex1[1]}
        |  number of vowels = {tex1[2]}
        |
        |  FRES score = {fres1}
        _______________________________________________
        |  TEXT2:
        |
        |  number of sentences = {tex2[0]}
        |  number of words = {tex2[1]}
        |  number of vowels = {tex2[2]}
        |
        |  FRES score = {fres2}
        _______________________________________________

""")