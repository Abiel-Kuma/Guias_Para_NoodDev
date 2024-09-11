#desafios N1
for i in range(1, 101):
    #fizz
    if (i%3) == 0:
        print("Fizz")
        
    #Buzz
    elif (i%5) == 0:
        print("Buzz")
    
    else :print(i)



# desafio N2
def palin(word):
    wordPali = word[::-1]
    if word == wordPali:
        print(f"{word} es una palabra palíndroma")
    else: print(f"{word} no es una palabra palíndroma")

word = input("Introduce una palabra políndroma: ")
palin(word)

# desafio N3
word = "bienvenidos a la fabrica de unicornios"
contador = 0
for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador += 1

print(f"total de vocales: {contador}")