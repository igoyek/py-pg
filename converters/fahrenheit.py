temperatureF = float(input("Enter temperature in fahrenheit scale: "))

temperatureC = (temperatureF - 32) * 5 / 9

print("Temperature in Celsius scale is: ",
      format(temperatureC, ".2f"))

temperatureK = temperatureC + 273.15
print("Temperature in Kelwin scale is: ",
      format(temperatureK, ".2f"))