class ArabicEnglishDict:
	'''
	def __init__(self, dict):
		self.dict = dict
	'''

	#Reverse dictionary from english_to_arabic and arabic_to_english
	def reverse_dict(self, dictionary):
	
		#Initalize empty dictionary
		new_dict = {}

		for key, value in dictionary.items():
			new_dict[value] = key

		return new_dict

	#Function takes a dictionary containing english words and their
	#corresponding arabic words and outputing them in alphabetical order
	#The letters iterable object are the letters in the alphabet that 
	#are being outputed to study
	def ordered_dict(self, dictionary, *letters):

		#Initalize ordered dictionary
		linear_dict = {}

		#Initalize letters list
		letters_list = []

		#Unpack the letters argument
		#It's a iterable (dict, tuple, etc) inside a tuple
		for iterable in letters:
			for letter in iterable:
				letters_list.append(letter)

		#Sort letters iterable in alphabetical order
		letters = sort(letters_list)

		#Go through dict and output the words where the english word
		#starts with each letter in the letters list
		for letter in letters:
			#For each set of words in dictionary
			for english_word, arabic_word in dictionary.items():
				#If the first letter is equal to the desired letters
				#add it to ordered dictionary to study
				if english_word[0] == letter[0]:
					linear_dict[english_word] = arabic_word

		return linear_dict

	#Shuffle dictionary and output it
	#If specific letters are desired - will output shuffled dict of those letters 
	def shuffled_dict(self, dictionary, *letters):
		import random

		#Initalize shuffled dict 
		nonlinear_dict = {}

		#Dict shuffled with letters included
		nonlinear_letter_dict = {}

		#Initalize letters list
		letters_list = []

		for iterable in letters:
			for letter in iterable:
				letters_list.append(letter)

		#Create a list containing dict keys
		keys = list(dictionary.keys())
		#Shuffle them to create a newly ordered dict
		random.shuffle(keys)

		for key in keys:
			nonlinear_dict[key] = dictionary[key]

		#If letters list is not empty, then output only the words with
		#that start with the letters in the list
		if letters_list is not None:
			for letter in letters_list:
				for key, value in nonlinear_dict.items():
					if key[0] == letter:
						nonlinear_letter_dict[key] = value

			return nonlinear_letter_dict

		return nonlinear_dict


	def one_at_a_time(self, dictionary):

		for key, values in dictionary.items():
			print(key)
			input("Press Enter to get the definition")
			print(values)
			quit = input("\nPress Enter for the next word or q to quit\n")

			#press q to exit
			if quit == 'q':
				break

		return None