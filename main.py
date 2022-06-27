import os

folder = input("Podaj folder, w którym sa obliczenia częstości.\n")
for i in os.listdir(folder):
    if ".out" in i:
        file = os.path.join(folder, i)
r = open(file,"r")
text = r.readlines()
