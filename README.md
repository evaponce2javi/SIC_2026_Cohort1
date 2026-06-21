venv\Scripts\activate# SIC_2026_Cohort1
# Caracterización del Microemprendimiento en Chile (VIII EME 2025)

## Integrantes (Cohorte 1)
* **Fernanda Daza** (GitHub: [@fernand.css]) 
* **Nickolle Silva** (GitHub: [@nickollesilva]) 
* **Cristóbal Vergara** (GitHub: [@crisalvav]) 
* **Eva Ponce** (GitHub: [@evaponce2javi]) 
* **Francisca Reyes** (GitHub: [@franto5]) 
* **Amaro Jofré** (GitHub: [@amarojofre])
---
## Enlace al Dashboard Interactivo
🚀 **https://sic2026cohort1.streamlit.app/**

---
## Descripción del Proyecto
Este proyecto final para el curso de *Código y Programación del Samsung Innovation Campus Chile 2026* presenta un análisis interactivo y accesible del ecosistema microemprendedor en el país. 

El objetivo principal es traducir datos masivos de interés nacional en herramientas de visualización dinámicas, permitiendo a audiencias no técnicas comprender los desafíos estructurales que enfrentan los trabajadores independientes.

## Conjunto de Datos (Dataset)
* **Fuente Oficial:** Instituto Nacional de Estadísticas (INE) - VIII Encuesta de Microemprendimiento (EME 2025).
* **Licencia:** Pública / Verificable (INE Chile).
* **Volumen del dataset original:** ~8,000 registros (encuestas individuales).
* **Optimización aplicada:** Se realizó un proceso de limpieza en Python para mapear códigos numéricos del INE a variables de lenguaje natural en español (como Región, Sexo y Rama Económica), reduciendo el peso de la base de datos para asegurar un rendimiento óptimo en la nube.
---
## Pregunta de Análisis
> *¿Cómo influyen el sexo, la región geográfica y la rama económica de los microemprendedores en su nivel de informalidad, la brecha de sus ganancias mensuales y el acceso a financiamiento público en Chile?*

### Público Beneficiario
* **Organismos Públicos (Sercotec, Fosis, Ministerio de la Mujer):** Para optimizar y ajustar las bases de postulación de fondos públicos hacia sectores informales vulnerables.
* **Gremios y Municipalidades:** Para visibilizar con datos reales la situación socioeconómica de sus comunidades locales.
---
## Hallazgo Principal 
Al interactuar con el ecosistema de datos, se evidencia que **la precariedad del microemprendimiento en Chile está cruzada por el género y la motivación de origen**. 
Las mujeres que se ven empujadas a emprender por *necesidad económica* (cesantía o urgencia familiar) se concentran mayoritariamente en el sector servicios y en la informalidad laboral, percibiendo los ingresos más bajos. El análisis revela una asimetría en la focalización del Estado: los *subsidios públicos* tienden a concentrarse en emprendimientos estructurados por *oportunidad*, dejando un vacío financiero crítico para los segmentos que iniciaron por subsistencia inmediata.

---
## Requisitos e Instalación

**1. Abre la carpeta del proyecto en VS Code** y abre terminal con `` Ctrl+` ``.

**2. Confirma que estás en la carpeta correcta** (la que tiene `app.py`):
```bash
ls
```
Si no ves `app.py`, navega hasta ella con `cd SIC_2026_Cohort1-main`.

**3. Crea y activa un entorno virtual:**
```bash
python -m venv venv
venv\Scripts\activate
```
(En Mac/Linux sería `source venv/bin/activate`)

**4. Instala las librerías que el proyecto realmente usa:**
```bash
pip install streamlit pandas numpy plotly
```

**5. Ejecuta el dashboard:**
```bash
streamlit run app.py
```

Se abrirá solo en el navegador (`http://localhost:8501`). Para detenerlo, `Ctrl+C` en la terminal.

Notas:
- Tienes que ejecutarlo **desde la raíz del proyecto**, porque el CSV se carga con ruta relativa (`los-santos-en-la-corte/data/dataset_limpio.csv`).
