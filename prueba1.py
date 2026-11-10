limite = 2000000
es_primo = [True] * (limite + 1)
es_primo[0] = False
es_primo[1] = False

p = 2
while p * p <= limite:
  if es_primo[p]:
    for i in range(p * p, limite + 1, p):
      es_primo[i] = False
  p += 1

suma_primos = 0
for numero in range(2, limite + 1):
  if es_primo[numero]:
    suma_primos += numero

print("La suma de todos los números primos hasta 2,000,000 es:")
print(suma_primos)