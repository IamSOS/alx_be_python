weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("It's sunny outside. Wear light clothes and sunglasses!")
elif weather == "rainy":
    print("It's rainy today. Don't forget your umbrella and wear waterproof shoes.")
elif weather == "cold":
    print("It's cold today. Wear a warm coat, scarf, and gloves.")
else:
    print("Sorry, I don't have advice for that kind of weather.")
