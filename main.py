temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
if(unit == "F" or unit == "f"):
  print(f"{temp}° in Fahrenheit is equivalent to {(float(temp)-32)*(5/9)}° Celsius.")
elif(unit == "C" or unit =="c"):
  print(f"{temp}° in Celsius is equivalent to {(float(temp)*1.8)+(32)}° Fahrenheit.")
else:
  print(f"Invalid unit({unit}).")
