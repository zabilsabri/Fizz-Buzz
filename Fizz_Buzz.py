angka = int(input("MASUKKAN ANGKA: "))

for x in range(1, angka + 1):
    if x % 3 == 0 and x % 5 == 0:
        x = ("Fizz Buzz")
    elif x % 3 == 0:
        x = ("fizz")
    elif x % 5 == 0:
        x = ("Buzz")
    print(x)