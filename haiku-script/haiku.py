import requests, json, random

def CreateLine(wordOptions, desiredSyllables):

	optionLength = len(wordOptions)

	currentSyllables = 0
	choices = []

	# Selecting a random word.
	while (currentSyllables != desiredSyllables):

		word = wordOptions[random.randint(0, optionLength - 1)]

		while word["numSyllables"] + currentSyllables > desiredSyllables:
			word = wordOptions[random.randint(0, optionLength - 1)]
		
		currentSyllables += word["numSyllables"]
		choices.append(word)

	words = []

	# Converting to string.
	for choice in choices:
		words.append(choice["word"])

	return " ".join(words)

def main():

	# Getting topic.
	topic = input("Please enter a topic for the haiku: ")

	# Retrieving from API.
	url = "http://api.datamuse.com/words?rel_trg=" + topic.replace(" ", "+") + "&md=s"
	wordOptions = requests.get(url).json()
	
	# Getting lines.
	line1 = CreateLine(wordOptions, 5)
	line2 = CreateLine(wordOptions, 7)
	line3 = CreateLine(wordOptions, 5)

	# Printing output.
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(line1)
	print(line2)
	print(line3)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if __name__ == "__main__":
	main()