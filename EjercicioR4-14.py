# Leer las ventas de los tres departamentos
ventas_depto1 = float(input("Ventas del departamento 1: "))
ventas_depto2 = float(input("Ventas del departamento 2: "))
ventas_depto3 = float(input("Ventas del departamento 3: "))

# Leer el salario mensual de los vendedores
salario_vendedores = float(input("Salario mensual de los vendedores: ")) # todos cobran el mismo sueldo


# Calcular las ventas totales entre los tres departamentos
ventas_totales = ventas_depto1 + ventas_depto2 + ventas_depto3

# Calcular el umbral para la bonificación en base a el 33% de las ventas totales
umbral_bonificacion = 0.33 * ventas_totales

# Calcular el salario final de los vendedores en cada departamento
salario_final_vendedor1 = salario_vendedores
salario_final_vendedor2 = salario_vendedores
salario_final_vendedor3 = salario_vendedores

if ventas_depto1 > umbral_bonificacion:
    salario_final_vendedor1 += 0.20 * salario_vendedores

if ventas_depto2 > umbral_bonificacion:
    salario_final_vendedor2 += 0.20 * salario_vendedores

if ventas_depto3 > umbral_bonificacion:
    salario_final_vendedor3 += 0.20 * salario_vendedores

# Mostrar los salarios finales de los vendedores de cada departamento y los datos con los que se consiguió dicha información
print("valor total de las ventas:", ventas_totales)
print("el valor correspondiente al 33% de las ventas totales es:", umbral_bonificacion)
print("Salario final del departamento 1:", salario_final_vendedor1)
print("Salario final del departamento 2:", salario_final_vendedor2)
print("Salario final del departamento 3:", salario_final_vendedor3)
