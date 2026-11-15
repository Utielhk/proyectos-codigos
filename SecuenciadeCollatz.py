def encontrar_cadena_mas_larga(limite):
    memoria = {1: 1}
    
    mejor_numero = 1
    max_longitud = 1

    for inicio in range(2, limite):
        actual = inicio
        pasos = 0

        while actual not in memoria:
            if actual % 2 == 0:
                actual //= 2
            else:
                actual = 3 * actual + 1
            pasos += 1

        longitud_total = pasos + memoria[actual]
        memoria[inicio] = longitud_total

        if longitud_total > max_longitud:
            max_longitud = longitud_total
            mejor_numero = inicio

    return mejor_numero, max_longitud


LIMITE = 1_000_000
numero, terminos = encontrar_cadena_mas_larga(LIMITE)

print(f"Número inicial con la cadena más larga: {numero}")
print(f"Cantidad de términos en la cadena: {terminos}")