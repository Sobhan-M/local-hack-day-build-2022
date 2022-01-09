import credentials, requests, json

def main():

	city = input("Enter the city name: ")
	url = "https://api.openweathermap.org/data/2.5/weather?q=" + city.replace(" ", "+") + "&appid=" + credentials.GetWeatherAPIKey()

	result = (requests.get(url)).json()

	if result["cod"] == 200:
		print("Successfully retrieved the information.")

		kelvin = result["main"]["temp"]
		celsius = int(kelvin - 273.15)
		
		weather = result["weather"][0]["main"]

		print("The temperature in ", city," is ", celsius, " C.")
		print("The weather in ", city, " is ", weather)

	else:
		print("Error ", result["cod"], ": Could not receive the information.")

if __name__ == "__main__":
    main()