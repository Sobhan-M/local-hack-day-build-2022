# Description
This script uses the [OpenWeatherMap](https://openweathermap.org/) API. The purpose is simply to retrieve the current weather temperature and description. It is only used in the console.

# How To Run
First create a file called `credentials.py` and create the following method with your API key:
```
def GetWeatherAPIKey():
	return [API key]
```

Then run:

```
python3 weather.py
```