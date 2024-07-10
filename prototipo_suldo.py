
import csv
import random
import math

ruta = 'reporte_sueldos.csv'
trabajadores =  [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]

sueldo = []

# generar un sueldo aleatorio por cada trabajador 
def sueldo_aleatorio():
    global sueldo
    sueldo = [random.randint(300000,2500000) for _ in trabajadores  ]
    print('sueldos asignados de forma aleatoria.')


def clasificar_sueldos():
    print(f'sueldos menores a 800.000 TOTAL:',len([e for e in sueldo if e < 800000]))
    for empleado, sueldos in zip(trabajadores, sueldo):
        if sueldos < 800000:
            print(f'Nombre empleado : {empleado["nombre"]}, Cargo: {empleado["cargo"]}, sueldo: ${sueldo}')
   
    print('sueldos entre 800.000 y 2.000.000 Total :',len([e for e in sueldo if 800000 <= e <= 2000000 ]))
    for empleado, sueldos in zip(trabajadores, sueldo):
        if 800000 <= sueldos <= 2000000:
            print(f'Nombre empleado : {empleado["nombre"]}, Cargo: {empleado["cargo"]}, sueldo: ${sueldo}')

    print('sueldos mayores a 2.000.000 Total:',len([e for e in sueldo if e > 2000000]))
    for empleado, sueldos in zip(trabajadores, sueldo):
        if sueldos > 2000000:
            print(f'Nombre empleado : {empleado["nombre"]}, Cargo: {empleado["cargo"]}, sueldo: ${sueldo}')
            print('...')

    print('Total sueldos :', sum(sueldo))   

def ver_estadistica():
    sueldo_max = max(sueldo)
    sueldo_min = min(sueldo)       
    sueldo_promedio = sum(sueldo) / len(sueldo)
    
    print(f'sueldo mas alto : ${sueldo_max}')
    print(f'sueldo minimo: ${sueldo_min}')  
    print(f'sueldo promedio: ${sueldo_promedio:.2f}')
      

def reporte_de_sueldos():
    with open(ruta,'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre empleado', 'Cargo','Sueldo base', 'Descuento salud', 'Descuento AFP', 'sueldo Liquido'])
        for empleado, sueldos in zip(trabajadores, sueldo):
            descuento_salud = sueldo*0.7
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([empleado['nombre'], empleado['cargo'], sueldo,descuento_salud,descuento_afp,sueldo_liquido])

            print(f'Nombre empleado:{empleado["nombre"]}, Cargo:{empleado["cargo"]}, sueldo Base: {sueldo}, Descuento salud:{descuento_salud}, Descuento AFP:{descuento_afp}, sueldo liquido:{sueldo_liquido} ')


def cerrar_programa():
    print('saliendo del programa....') 
    print('Desarrollado por[Guerben]\n Rut[26.792.130-k]')           


def menu():
    while True:
        print('Menu')
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción: "))


        if opcion == 1:
            sueldo_aleatorio()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadistica()
        elif opcion == 4:
            reporte_de_sueldos()
        elif opcion == 5:
            cerrar_programa()
            break
        else:
            print('opcion no valida ') 

if __name__ == "__main__":
    menu()
