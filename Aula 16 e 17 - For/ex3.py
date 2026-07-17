n1 = int(input("\nTabuada de que número? "))
tabuada = 1

print("\nADIÇÃO")
for i in range(0, 10 + 1):

    
    print(f"{n1} + {i} = ", n1 + i)

print("\nSUBTRAÇÃO")
for i in range(0, 10 + 1):
    
    print(f"{n1} - {i} = ", n1 - i)

print("\nMULTIPLICAÇÃO")
for i in range(0, 10 + 1):
    
    print(f"{n1} * {i} = ", n1 * i)

print("\nDIVISÃO")
for i in range(1, 10 + 1):
    
    print(f"{n1} / {i} = ", n1 / i)