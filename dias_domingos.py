import datetime

def contar_domingos():
    contador = 0
    
    for anio in range(1900, 2001):
        for mes in range(1, 13):
            fecha = datetime.date(anio, mes, 1)
            if fecha.weekday() == 6:
                contador += 1
                
    return contador
resultado = contar_domingos()
print(f"Total de domingos que cayeron en el primer día de mes: {resultado}")