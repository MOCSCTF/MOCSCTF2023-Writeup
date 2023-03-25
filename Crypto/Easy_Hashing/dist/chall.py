def babyhash(key: str) -> int:
    hash_value = 0
    prime = 31
    max_value = 5000000
    for i in range(len(key)):
        char = key[i]
        hash_value += (ord(char) - 96) * (prime ** i)
    return hash_value % max_value

password = open('password.txt', 'r').read().strip()
flag = open('flag.txt', 'r').read()

known_password = babyhash(password)
print(known_password)

while(1):
    print("----------------------")
    your_password = input("Type the correct password:\n>")
    hashed_password = babyhash(your_password)

    if your_password[0:7] == "MOCSCTF" and hashed_password == known_password:
        print("!!!Correct password!!!")
        print(flag)
        break
    else:
        print("Wrong password")

