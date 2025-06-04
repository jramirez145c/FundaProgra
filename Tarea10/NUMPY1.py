import numpy as np

# Datos de consumo (ya definidos)
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# 1. Consumo del hogar 5 el viernes (día 5)
consumo_hogar5_viernes = consumo[4, 4]
print("1. Consumo del hogar 5 el viernes:", consumo_hogar5_viernes)

# 2. Consumo de los últimos 3 hogares el domingo (día 7)
consumo_domingo_ultimos3 = consumo[-3:, 6]
print("2. Consumo de los últimos 3 hogares el domingo:", consumo_domingo_ultimos3)

# 3. Promedio de consumo los fines de semana (sábado y domingo → columnas 5 y 6)
fines_semana = consumo[:, 5:7]  # columnas 5 y 6
promedio_finde = np.mean(fines_semana)
print("3. Promedio de consumo en fin de semana:", round(promedio_finde, 2))

# 4. Día con mayor desviación estándar entre hogares
desviaciones = np.std(consumo, axis=0)  # std por día
dia_mayor_std = np.argmax(desviaciones)
print("4. Día con mayor desviación estándar:", dia_mayor_std)  # 5 = sábado
print("   Desviación estándar:", desviaciones[dia_mayor_std])

# 5. Tres hogares con menor consumo total semanal
total_semanal = np.sum(consumo, axis=1)
indices_menores = np.argsort(total_semanal)[:3]
valores_menores = total_semanal[indices_menores]
print("5. Tres hogares con menor consumo total:")
print("   Índices:", indices_menores)
print("   Valores:", np.round(valores_menores, 1))

# 6. Nuevo consumo total del hogar 3 con 10% de aumento diario
hogar3 = consumo[2]
hogar3_aumentado = hogar3 * 1.10
nuevo_total_hogar3 = np.sum(hogar3_aumentado)
print("6. Nuevo consumo total del hogar 3 con +10% diario:", round(nuevo_total_hogar3,2))