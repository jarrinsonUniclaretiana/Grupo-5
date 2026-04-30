# Jhon Alisson Hernandez Cordoba

def verificar_retiro(monto, saldo):
    return monto <= saldo and monto > 0

def procesar_retiros():
    saldo = 500000
    print(f"Saldo inicial: ${saldo:,}".replace(",", "."))
    
    while True:
       try:
           monto =float(input("Ingrese monto para retirar (0 para salir): $"))
           if monto == 0:
              break
           if verificar_retiro(monto, saldo):
              saldo = saldo - monto
              print(f"Retiro exitoso. Saldo actualizado: ${saldo:,}".replace(",", "."))

           else:
                print("Error: Monto invalido o fondos insuficientes.")
       except ValueError:
           print("Error: Ingrese un numero valido.")

    print("\nReporte de 5 intentos posibles:")
    for intento in range(1,6):
        monto_simulado = intento * 500000
        if verificar_retiro(monto_simulado, saldo):
           print(f"Intento {intento}: Puede retirar ${monto_simulado:,} (saldo valido)".replace(",", "."))
        else:
           print(f"Intento {intento}: No posible (${monto_simulado:,} > saldo)".replace(",", "."))

    print(f"Saldo final: ${saldo:,}".replace(",", "."))
 
if __name__ == "__main__":
    procesar_retiros()            
                