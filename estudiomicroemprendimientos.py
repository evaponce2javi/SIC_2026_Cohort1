import pandas as pd

# 1. RUTA DEL ARCHIVO (Cambia esto por tu ruta xd)
ruta_entrada = "ruta/a/tu/archivo.csv"
df = pd.read_csv('Base de Datos Full - VIII EME CSV.csv')

# 2. CENTRALIZACIÓN DE MAPEOS
mapeos = {
    "region": {
        1: "Tarapacá", 2: "Antofagasta", 3: "Atacama", 4: "Coquimbo",
        5: "Valparaíso", 6: "O'Higgins", 7: "Maule", 8: "Biobío",
        9: "La Araucanía", 10: "Los Lagos", 11: "Aysén", 12: "Magallanes",
        13: "Metropolitana", 14: "Los Ríos", 15: "Arica y Parinacota", 16: "Ñuble"
    },
    "sexo": {1: "Hombre", 2: "Mujer"},
    "tramo_etario": {
        1: "15 a 24 años", 2: "25 a 34 años", 3: "35 a 44 años",
        4: "45 a 54 años", 5: "55 a 64 años", 6: "65 años o más"
    },
    "informalidad": {1.0: "Informal", 0.0: "Formal"},
    "cine_eme_red": {
        1: "Sin instrucción / Básica incompleta", 2: "Básica completa / Media incompleta",
        3: "Media completa", 4: "Superior incompleta (IP/CFT/Univ)",
        5: "Superior completa (IP/CFT)", 6: "Superior completa (Universitaria o más)"
    },
    "lugar_trabajo": {
        1: "En su propio hogar", 2: "En el hogar del cliente", 3: "Local/Oficina/Taller establecido",
        4: "En la vía pública / Kiosco", 5: "Vehículo", 6: "No tiene un lugar fijo",
        7: "Predio agrícola", 8: "Obra en construcción", 9: "Otro lugar fijo fuera del hogar"
    },
    "financiamiento_inicial": {
        1: "Solo ahorros/recursos propios", 2: "Préstamos de familiares/amigos",
        3: "Financiamiento formal (Bancos/Instituciones)", 4: "Subsidios públicos / Fondos del Estado"
    },
    "motivacion": {
        1: "Tradición familiar", 2: "Oportunidad (Aumentar ingresos/Independencia)",
        3: "Necesidad (Desempleo/Falta de oportunidades)", 4: "Complementar ingresos", 77: "Otra razón"
    },
    "tramos_ganancias": {
        1: "Menos de $300.000", 2: "De $300.000 a $600.000", 3: "De $600.000 a $1.000.000",
        4: "De $1.000.000 a $1.500.000", 5: "De $1.500.000 a $2.500.000", 6: "Más de $2.500.000"
    },
    "c1_b": {
        1: "Agricultura, silvicultura y pesca", 2: "Explotación de minas", 3: "Industrias manufactureras", 
        4: "Suministro de electricidad y agua", 5: "Construcción", 6: "Comercio", 
        7: "Transporte y almacenamiento", 8: "Alojamiento y comidas", 9: "Información y comunicaciones", 
        10: "Actividades financieras", 11: "Actividades inmobiliarias", 12: "Actividades profesionales", 
        13: "Servicios administrativos", 14: "Enseñanza", 15: "Atención de la salud", 
        16: "Artes y recreación", 17: "Otras actividades", 18: "Hogares empleadores", 19: "Extraterritoriales"
    }
}

# 3. PREPARACIÓN DEL DATASET
col_ganancia = 'ganancia_final' if 'ganancia_final' in df.columns else ('ganancia_estimada' if 'ganancia_estimada' in df.columns else None)
columnas_claves = ['id'] + list(mapeos.keys()) + ([col_ganancia] if col_ganancia else [])

df_dashboard = df[[c for c in columnas_claves if c in df.columns]].copy()

if col_ganancia and col_ganancia != 'ganancia_final':
    df_dashboard.rename(columns={col_ganancia: 'ganancia_final'}, inplace=True)

# 4. APLICACIÓN DE MAPEOS Y LIMPIEZA
for columna, diccionario in mapeos.items():
    if columna in df_dashboard.columns:
        df_dashboard[columna] = df_dashboard[columna].map(diccionario)

cols_limpieza = [c for c in ['region', 'sexo', 'informalidad'] if c in df_dashboard.columns]
if cols_limpieza:
    df_dashboard.dropna(subset=cols_limpieza, inplace=True)

df_dashboard.rename(columns={'cine_eme_red': 'nivel_educativo', 'c1_b': 'rama_economica'}, inplace=True)

# 5. EXPORTAR
ruta_salida = "dataset_limpio.csv" # <-- Ruta de guardado
df_dashboard.to_csv(ruta_salida, index=False)
print(f"¡Listo! Archivo guardado en: {ruta_salida}")