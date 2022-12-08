string = input("x: ")

string = string.replace(" ","")

string2 = string[::-1]

print(f"string: {string2}")

if string == string2:
    print("...")
else:
    print(".....")