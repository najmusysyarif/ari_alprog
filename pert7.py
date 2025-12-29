# operasi logika atau bolean
# not, or, and, xor

print("========== not ==========")
a = True
b = not a
print("nilai dari b = ", b)


print("========== or (atau) ==========")
print("hasil akan True, selama ada satu saja true")
a = False
b = False
hasil = a or b
print(a, "or", b, "=", hasil)
a = False
b = True
hasil = a or b
print(a, "or", b, "=", hasil)
a = True
b = False
hasil = a or b
print(a, "or", b, "=", hasil)
a = True
b = True
hasil = a or b
print(a, "or", b, "=", hasil)