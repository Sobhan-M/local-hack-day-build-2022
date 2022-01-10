# Description
This is a Discord Bot that will play rock, papers, scissors with the users of the server.

# How To Run
First install the Discord API for Python:

```
pip install -U discord.py
```
Next create a file called `credentials.py` with the following function:
```
def TOKEN():
	return [your-bot-token-as-a-string]
```
Finally run the script:
```
python3 bot.py
```

# Bot Interaction
To use the bot after adding it to the server and running the script, simply type `!play [rock/paper/scissors]` in a server channel. Do not include the square brackets, and only pick one option.
