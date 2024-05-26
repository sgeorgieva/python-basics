# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.

animal = str(input())

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")