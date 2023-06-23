import matplotlib.pyplot as plt

def calcular_velocidad_promedio(velocidad_inicial, distancia, tiempo):
    velocidad_final = (2 * distancia / tiempo) - velocidad_inicial
    velocidad_promedio = (velocidad_inicial + velocidad_final) / 2
    return velocidad_promedio

def calcular_aceleracion(velocidad_inicial, distancia, tiempo):
    aceleracion = 2 * (distancia - (velocidad_inicial * tiempo)) / (tiempo ** 2)
    return aceleracion

def graficar_resultados(distancia, tiempo):
    plt.plot(tiempo, distancia)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia (m)')
    plt.title('MRUA')
    plt.show()

def main():
    velocidad_inicial = float(input('Ingresa la velocidad inicial (en m/s): '))
    distancia = float(input('Ingresa la distancia (en metros): '))
    tiempo = float(input('Ingresa el tiempo (en segundos): '))

    velocidad_promedio = calcular_velocidad_promedio(velocidad_inicial, distancia, tiempo)
    aceleracion = calcular_aceleracion(velocidad_inicial, distancia, tiempo)
    
    print('Velocidad promedio:', velocidad_promedio, 'm/s')
    print('Aceleración:', aceleracion, 'm/s^2')

    # Crear una lista de tiempo desde 0 hasta el tiempo ingresado con incrementos de 0.1 segundos
    tiempo_grafica = [t/10 for t in range(int(tiempo*10)+1)]

    # Calcular la distancia en cada punto de tiempo
    distancia_grafica = [velocidad_inicial*t + 0.5*aceleracion*t**2 for t in tiempo_grafica]

    graficar_resultados(distancia_grafica, tiempo_grafica)

if __name__ == '__main__':
    main()