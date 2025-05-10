shellcodeString = input("Paste shellcode >>> ")

splitted = shellcodeString.split("\\")

for i in range(len(splitted)):
    print("0" + splitted[i] + ", ", end="")
