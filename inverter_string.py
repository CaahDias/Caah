# Defina a string a ser invertida
string = "exemplo"

# Crie uma variável para armazenar a string invertida
string_invertida = ""

# Itere sobre cada caractere da string original em ordem inversa
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exiba a string invertida
print("String original:", string)
print("String invertida:", string_invertida)

