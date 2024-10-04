class ErrorNotacionPolaca(Exception):
    pass


class ErrorEnPila(Exception):
    pass


class ErrorTransaccion(Exception):
    pass


class NotacionPolacaInversa:

    def __init__(self, expresion):
        # [INICIO]: Implemente el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        self.expresion = expresion.split() #Para separar los tokens
        
        # [FIN]

    def evaluar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        pila = PilaCapacidadFija(capacidad = 100, sobrescribir = False)
        
        for token in self.expresion:
            if token.isdigit():
                pila.apilar(int(token))
                
            else:
                b = pila.desapilar()
                a = pila.desapilar()
                
                if token == '+':
                    resultado = a + b
                
                elif token == '-':
                    resultado = a - b
                
                elif token == '*':
                    resultado = a * b
                
                elif token == '/':
                    resultado = a / b
                    
                else:
                    raise ErrorNotacionPolaca("Operador no válido.")

                pila.apilar(resultado)
        
        return pila.desapilar()
    
        # [FIN]


class PilaCapacidadFija:

    def __init__(self, capacidad, sobrescribir):
        self.elementos = [None for _ in range(capacidad)]
        self.sobrescribir = sobrescribir
        self.capacidad = capacidad
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        self.elementos = [None]  * capacidad
        self.tamanio_actual = 0 # Utilizado para llevar la cuenta del tamaño actual de la pila
        
        # [FIN]

    def tamanio(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        return self.tamanio_actual
    
        # [FIN]

    def apilar(self, elemento):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        if self.tamanio_actual < self.capacidad:
            self.elementos[self.tamanio_actual] = elemento  # Para colocar el elemento en la posicion actual
            self.tamanio_actual = self.tamanio_actual + 1 # Para aumentar el tamaño actual
        
        else:
            if self.sobrescribir:
                self.elementos = self.elementos[1:] + [elemento] # Para desplazar y agregar el nuevo elemento
            
            else:
                raise ErrorEnPila("La pila se encuentra llena.")
        
        # [FIN]

    def esta_vacia(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        return self.tamanio_actual == 0
    
        # [FIN]

    def cima(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        if self.esta_vacia():
            raise ErrorEnPila("La pila se encuentra vacia.")
        
        return self.elementos[self.tamanio_actual - 1]
    
        # [FIN]

    def desapilar(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        if self.esta_vacia():
            raise ErrorEnPila("La pila se encuentra vacia.")
        
        self.tamanio_actual = self.tamanio_actual - 1
        return self.elementos[self.tamanio_actual]
    
        # [FIN]


class CalculadoraGanancias:

    def __init__(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        self.compras = []
        
        # [FIN]

    def registrar_compra(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        
        partes = descripcion_transaccion.strip().split() # Utilizado para limpiar la entrada y dividirla en partes
        
        print("Partes de la transaccion:", partes)
        
        # Validacion del formato
        if len(partes) != 9 or partes[1] != "accion(es)" or partes[2] != "al" or partes[3] != "precio" or \
            partes[4] != "de" or partes[6] != "PEN" or partes[7] != "cada" or partes[8] != "una.":
                raise ErrorTransaccion("El formato de transaccion es invalido. Debe ser: '<NUMERO-ACCIONES' accion(es) al precio de <PRECIO-ACCIONES> PEN cada una.")        
        
        try:
            # Extraer el precio y el numero de acciones
            numero_acciones = int(partes[0])   # Priemro
            precio_acciones = int(partes[5])    # Sexto elemento, que es el precio
            
            if numero_acciones < 0 or precio_acciones < 0:
                raise ErrorTransaccion("Los valores de acciones y precios deben ser enteros mayores a cero.")
            
            self.compras.append({'unidades': numero_acciones, 'precio': precio_acciones})
            print("La compra fue registrada correctamente:", self.compras[-1])   # Para comprobar que la compra se registró con exito
            
        except ValueError:
            raise ErrorTransaccion("Formato de transaccion invalido. Debe ser: 'NUMERO-ACCIONES' accion(es) al precio de <PRECIO-ACCIONES> PEN cada una.")
        
        # [FIN]

    def registrar_venta(self, descripcion_transaccion):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.

        pass
        # [FIN]

    def catalogo_acciones(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def acciones_disponibles(self):
        # [INICIO]: Implemente este método entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

#         ****    E J E M P L O S          D E          U S O    ****

if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.

    # 1)
    # EJEMPLO 1 : 10 + 5 * 2 - 1 ......... Resultado Esperado : 19
    expresion_1 = "10 5 2 * + 1 -"
    calculadora_1 = NotacionPolacaInversa(expresion_1)
    resultado_1 = calculadora_1.evaluar()
    
    print("El resultado de la expresion '10 + 5 * 2 - 1' es:", resultado_1)

    # EJEMPLO 2 : 6 / 2 + 8 * 3 .......... Resultado Esperado : 27
    expresion_2 = "6 2 / 8 3 * +"
    calculadora_2 = NotacionPolacaInversa(expresion_2)
    resultado_2 = calculadora_2.evaluar()
    print("El resultado de la expresion '6 / 2 + 8 * 3' es:", resultado_2)
    
    calculadora_ganancias = CalculadoraGanancias()
    
    
    print()
    print()
    
    
    # 2)
    print("Emjemplo. Pila con sobrescritura deshabilitada")
    try:
        pila1 = PilaCapacidadFija(capacidad=3, sobrescribir=False)
        print("¿Pila Vacia?", pila1.esta_vacia())  # True
        pila1.apilar(1)
        pila1.apilar(2)
        pila1.apilar(3)
        print("Elementos dentro de la pila:", pila1.elementos)  # [1, 2, 3]
        print("Cima de pila:", pila1.cima())  # 3
        print("Tamaño de pila:", pila1.tamanio())  # 3

        # Intentamos con otro elemento, esperamos ErrorEnPila)
        pila1.apilar(4)  # ErrorEnPila: la pila se encuentra llena
    except ErrorEnPila as e:
        print("Excepción lanzada:", e)


    print()
    print()
    
    
    # 3)
    try:
        # Ejemplo para una entrada valida
        calculadora_ganancias.registrar_compra("100 accion(es) al precio de 20 PEN cada una.")
        print("La compra se registro exitosamente.")
        
        # Ejemplo para una entrada no valida
        calculadora_ganancias.registrar_compra("100 accion(es) al precio de y20 PEN cada una.") # En teoria, deberia lanzar el error
    
    except ErrorTransaccion as e:
        print("Error", e)
    
    
    # [FIN]