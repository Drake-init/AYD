def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)
n = int(input("Ingrese un número: "))
f = factorial(n)
if n <= 1:
   return 1
else:
   return n * factorial(n - 1)
print(f"El factorial de {n} es {f}")