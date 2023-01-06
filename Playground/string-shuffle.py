import string_utils

txt = "türkçe"

x = string_utils.shuffle(txt)

print(x)
guess = input("Tahmin et: ")

if guess == txt:
    print("Doğru bildin!")
else:
    print("Yanlış tahmin ettin!")