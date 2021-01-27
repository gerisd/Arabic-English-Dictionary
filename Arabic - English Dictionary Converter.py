import PyPDF2
import re

#file = r"C:\Users\andre\Desktop\Textbooks\Books/ArabicEgyptianDictionary.pdf"
file = r'ArabicEgyptianDictionary.pdf'

pdfFileObj = open(file, 'rb')

#pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#number of pages in pdf
#print(pdfReader.numPages)

#List to hold all the english words found
eng_list = []

#List to hold all the arabic words found
arab_list = []

for i in range(300, 302):
    #A page object that extracts a page text
    pageObj = pdfReader.getPage(i)

    #Gets the words on the page
    page_words = pageObj.extractText()

    english_words = re.compile(r'EN\s(n|v|vi)(\s)?(coll|inf|s)?:(\s)*(\w)+')
    eng_matches = english_words.finditer(page_words)

    arabic_words = re.compile(r'(MS|EG)\s(n|v|vi)\s(m|f|p):(\s)*\'?(\w)+(\')?(\w)?(\s)?(?!pl\b)(?!imp\b)(\w)*')
    arab_matches = arabic_words.finditer(page_words)

    print("\nEnglish words\n")
    for eng_match in eng_matches:
        
        #Got last section of the regular expression matches
        word = eng_match.group(0)
        
        #split the match to get only the english words
        eng_word = word.split(":")[1]
        
        #remove spaces before and after word
        eng_word = eng_word.strip()


        #if the last 2 letters are pl or last letter is p, we need to remove it
        #it is not part of the word
        if eng_word[-2:] == "pl":
            eng_word = eng_word[:-2]
            
        if eng_word[-1] == "p":
            eng_word = eng_word[:-1]

        #Add the english word to the english list
        eng_list.append(eng_word)
        
        print(eng_word)


    print("\nArabic words\n")
    for arab_match in arab_matches:
        
        #Got last section of the regular expression matches
        word = arab_match.group(0)
        
        #split the match to get only the english words
        arab_word = word.split(":")[1]
        
        #remove spaces before and after word
        arab_word = arab_word.strip()

        #Add arabic word to the arabic list
        arab_list.append(arab_word)

        print(arab_word)

print('\n')
for word in eng_list:
    print("english word : ",word)

print('\n')
for word in arab_list:
    print("arabic word :" , word)

print(f"length of eng list: {len(eng_list)}, and arabic list: {len(arab_list)}")
#Close pdf
pdfFileObj.close()
