def es_primo(n):
  if n < 2:
    return False
  if n % 2 == 0:
    return n == 2
  i = 3
  while i * i <= n:
    if n % i == 0:
      return False
    i += 2
  return True

def lista_primos(a, b):
  primos = []
  for n in range(a, b + 1):
    if es_primo(n):
      primos.append(n)
  return primos

entrada = input("Ingrese el límite inferior y el límite superior separados por un guion: ")
a, b = map(int, entrada.split("-"))
primos = lista_primos(a, b)
print(f"Los números primos en el rango {a}-{b} son: {primos}")