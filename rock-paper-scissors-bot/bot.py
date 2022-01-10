from warnings import simplefilter
import discord, credentials, random

client = discord.Client()

# Called when this successfully connects to Discord.
@client.event
async def on_ready():
	print(f"Debug: {client.user} is ready.")

@client.event
async def on_message(message):
	print("Debug: Received message.")

	# Avoiding the bot responding to itself.
	if message.author == client.user:
		return

	message_command = message.content.split(" ")[0]
	message_choice = message.content.split(" ")[1]

	
	if message_command == "!play":

		print("Debug: Starting game.")

		options = ["ROCK", "PAPER", "SCISSORS"]
	
		if message_choice.upper() in options:
			bot_choice_index = random.randint(0,len(options) - 1)
			user_choice_index = options.index(message_choice.upper())

			result = ""

			# The next index beats the current index. Paper beats rock (1 beats 0), etc.
			if bot_choice_index - user_choice_index == 1 or bot_choice_index - user_choice_index == -2: # -2 for rocks vs scissors.
				result = "win"
			elif bot_choice_index - user_choice_index == -1 or bot_choice_index - user_choice_index == 2: # The reverse for when player wins.
				result = "lose"
			elif bot_choice_index == user_choice_index:
				result = "tie"

			# Handling resulting messages.
			if result == "win":
				await message.channel.send(f"{options[bot_choice_index].capitalize()} beats {options[user_choice_index].lower()}. I win!")
			elif result == "lose":
				await message.channel.send(f"{options[user_choice_index].capitalize()} beats {options[bot_choice_index].lower()}. I lose!")
			elif result == "tie":
				await message.channel.send(f"We both picked {options[user_choice_index].lower()}, so it's a tie! Want to try again?")

			print("Debug: Finishing game.")

		else:
			await message.channel.send("Sorry, you have to format the message as `!play rock/paper/scissors`")
			print("Debug: Sending error message.")



# Runs the client.
client.run(credentials.TOKEN())

