file = open("text.txt", "w")
file.write('kaaramba')
file.close()
file = open("text.txt", "r")
data = (file.readline())
how_much = data.count("a")

print("Ilosc liter : ", how_much)
