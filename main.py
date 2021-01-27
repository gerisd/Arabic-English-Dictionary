from ArabicEnglishDict import ArabicEnglishDict
import Vocab
import argparse

#Initalize Classes 
dictionary = ArabicEnglishDict()

#Initalize the dict that holds all the words being outputed
word_holder = {}

#Construct argparse, parse arguments for what letters I want to study
ap = argparse.ArgumentParser()
ap.add_argument("-fl", "--firstletter", required=True, help="First letter for vocab")
ap.add_argument("-sl", "--secondletter", help="Second letter for vocab")

args = vars(ap.parse_args())

#Get Vocab
dict_a = Vocab.a_dict()
dict_b = Vocab.b_dict()
dict_c = Vocab.c_dict()
dict_d = Vocab.d_dict()

#Merge dictionaries
word_holder = {**dict_a, **dict_b, **dict_c, **dict_d}

first_letter = str(args["firstletter"])

if args["secondletter"] != None:
	second_letter = str(args["secondletter"])
	letters = [first_letter, second_letter]
else:
	letters = first_letter

#Preprocess the Vocab
letter_a = dictionary.shuffled_dict(word_holder, letters)

#Run Vocab - Execute one at a time
dictionary.one_at_a_time(letter_a)


