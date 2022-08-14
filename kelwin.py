temperatureK = float(input("Enter the temperature in Kelwin scale: "))

temperatureC = temperatureK - 273.15
print("Temperature in Celsius scale is: ",
      format(temperatureC, ".2f"))

temperatureF = 32 + 9*temperatureC/5
print("Temperature in Fahrenheit scale is: ",
      format(temperatureF, ".2f"))