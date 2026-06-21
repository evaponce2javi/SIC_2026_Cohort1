import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Dashboard EME",
    page_icon="📊",
    layout="wide"
)

# Paleta de colores principal para los gráficos
PALETA_DASHBOARD = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728"]

# 2. CARGA DEL DATASET CON RUTA RELATIVA DINÁMICA (SOLUCIÓN AL ERROR DE RUTA)
BASE_DIR = Path(__file__).resolve().parent

# El código intenta buscar el archivo de manera inteligente en las ubicaciones posibles
RUTA_DATASET = BASE_DIR / "data" / "dataset_limpio.csv"

if not RUTA_DATASET.exists():
    RUTA_DATASET = BASE_DIR / "los-santos-en-la-corte" / "data" / "dataset_limpio.csv"

@st.cache_data
def cargar_datos():
    return pd.read_csv(RUTA_DATASET)

try:
    df = cargar_datos()
except FileNotFoundError:
    st.error(f"❌ No se encontró el archivo 'dataset_limpio.csv'. Por favor, asegúrate de guardarlo dentro de la carpeta 'data' de tu proyecto.")
    st.info(f"Ruta donde el sistema lo está buscando actualmente:\n{RUTA_DATASET}")
    st.stop()

# 3. FILTROS LATERALES INTERACTIVOS (Sidebar Estilizada)
st.sidebar.markdown("<h2 style='color: #1f77b4; font-weight: bold;'>⚙️ Panel de Filtros</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

regiones_disponibles = sorted(df['region'].dropna().unique())
region_seleccionada = st.sidebar.multiselect(
    "Selecciona las Regiones a analizar:",
    options=regiones_disponibles,
    default=regiones_disponibles
)

# Filtrar datos de forma dinámica
df_filtrado = df[df['region'].isin(region_seleccionada)]

# =========================================================
# ENCABEZADO PRINCIPAL Y TITULAR (EL RECUADRO OSCURO ELEGANTE)
# =========================================================
st.markdown("""
<div style="background-color: #0e1117; padding: 25px; border-radius: 10px; margin-bottom: 25px; border-left: 8px solid #1f77b4;">
    <h1 style="color: #ffffff; margin-bottom: 5px; font-weight: bold;">📊 Panel de Análisis Estratégico</h1>
    <p style="color: #aec7e8; font-size: 16px; margin: 0;">Encuesta de Microemprendimiento (EME) — Diagnóstico de Informalidad y Entorno Productivo</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 4. TARJETAS DE INDICADORES CLAVE (KPIs Estilizados)
# =========================================================
total_emprendedores = len(df_filtrado)
porcentaje_informal = (df_filtrado['informalidad'] == 'Informal').mean() * 100 if total_emprendedores > 0 else 0

kpi1, kpi2 = st.columns(2)

with kpi1:
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #e9ecef; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
        <p style="color: #6c757d; font-size: 14px; text-transform: uppercase; margin-bottom: 5px; font-weight: bold;">Muestra Analizada</p>
        <h2 style="color: #1f77b4; margin: 0; font-size: 36px; font-weight: bold;">{total_emprendedores:,}</h2>
        <p style="color: #212529; font-size: 13px; margin-top: 5px;">Microemprendedores filtrados</p>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; text-align: center; border: 1px solid #e9ecef; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
        <p style="color: #6c757d; font-size: 14px; text-transform: uppercase; margin-bottom: 5px; font-weight: bold;">Brecha de Formalización</p>
        <h2 style="color: #e74c3c; margin: 0; font-size: 36px; font-weight: bold;">{porcentaje_informal:.1f}%</h2>
        <p style="color: #212529; font-size: 13px; margin-top: 5px;">Tasa de informalidad laboral real</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# ORGANIZACIÓN POR PESTAÑAS (TABS)
# =========================================================
tab1, tab2, tab3 = st.tabs([
    "📈 1. Enfoque de Género", 
    "🎯 2. Motivaciones del Negocio", 
    "🏭 3. Sectores Económicos"
])

# ---------------------------------------------------------
# PESTAÑA 1: GÉNERO E INFORMALIDAD
# ---------------------------------------------------------
with tab1:
    st.markdown("<h3 style='color: #1f77b4; font-weight: bold; margin-top: 10px;'>Situación de Informalidad según Sexo</h3>", unsafe_allow_html=True)
    
    df_sexo_inf = df_filtrado.groupby(['sexo', 'informalidad']).size().reset_index(name='Cantidad')
    
    fig_sexo = px.bar(
        df_sexo_inf,
        x="sexo",
        y="Cantidad",
        color="informalidad",
        barmode="group",
        labels={"sexo": "Género", "Cantidad": "Cantidad de Emprendimientos", "informalidad": "Situación Laboral"},
        color_discrete_map={"Formal": "#2ecc71", "Informal": "#e74c3c"},
        text_auto=True
    )
    fig_sexo.update_layout(
        xaxis_title="Sexo del Emprendedor", 
        yaxis_title="Número de Casos",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=20, b=20, l=20, r=20)
    )
    fig_sexo.update_traces(textposition='outside')
    st.plotly_chart(fig_sexo, use_container_width=True)
    
    # Recuadro explicativo en color negro nítido para que sea ultra legible
    st.markdown("""
    <div style="color: #000000; background-color: #ffffff; padding: 25px; border-radius: 8px; border: 1px solid #e9ecef; border-left: 5px solid #2ecc71; box-shadow: 2px 2px 5px rgba(0,0,0,0.02); margin-top: 15px;">
        <h4 style="color: #000000; margin-top: 0; font-weight: bold; font-size: 18px;">🔍 Diagnóstico Crítico: Género e Informalidad</h4>
        <p style="color: #212529; font-size: 15px; line-height: 1.6;">Al corregir el gráfico a barras agrupadas, el impacto visual es directo: la proporción interna de <strong>mujeres en situación de informalidad es alarmantemente superior</strong> en comparación con la distribución de los hombres.</p>
        <p style="color: #212529; font-size: 15px; font-weight: bold; margin-top: 15px; margin-bottom: 8px;">Implicancias estructurales de la problemática:</p>
        <ul style="color: #212529; font-size: 14px; line-height: 1.6; padding-left: 20px;">
            <li style="margin-bottom: 8px;"><strong>Precarización y Vejez Vulnerable:</strong> Al operar al margen de la formalidad, estas microemprendedoras carecen de cotizaciones de salud y no acumulan fondos previsionales, garantizando una vejez en situación de desprotección económica.</li>
            <li style="margin-bottom: 8px;"><strong>El Atrapamiento de la Subsistencia:</strong> Un negocio informal no emite boletas ni facturas, quedando fuera del sistema de financiamiento bancario comercial y de los fondos de fomento estatal (Sercotec/Corfo), impidiendo su escalabilidad.</li>
            <li style="margin-bottom: 8px;"><strong>La Brecha de los Cuidados:</strong> Los datos reflejan que la informalidad femenina suele ser el único mecanismo de flexibilidad que encuentran las mujeres para compatibilizar la generación de ingresos autónomos con los roles de cuidado no remunerado en el hogar.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PESTAÑA 2: MOTIVACIONES (SOLUCIONADO EL ERROR DE LEYENDA)
# ---------------------------------------------------------
with tab2:
    st.markdown("<h3 style='color: #1f77b4; font-weight: bold; margin-top: 10px;'>Principales Motivaciones para Iniciar el Emprendimiento</h3>", unsafe_allow_html=True)
    
    df_mot = df_filtrado['motivacion'].value_counts().reset_index()
    df_mot.columns = ['Motivación', 'Cantidad']
    
    fig_mot = px.bar(
        df_mot.head(10),
        y='Motivación',
        x='Cantidad',
        orientation='h',
        color='Motivación',
        color_discrete_sequence=PALETA_DASHBOARD,
        text_auto=True
    )
    
    # SOLUCIÓN TÉCNICA: El 'showlegend' se declara correctamente dentro de update_layout
    fig_mot.update_layout(
        yaxis={'categoryorder':'total ascending', 'title': ''}, 
        xaxis_title="Número de Respuestas",
        showlegend=False, 
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    # UBICACIÓN DIRECTA: Obliga al número exacto a posicionarse al final exterior de cada barra
    fig_mot.update_traces(textposition='outside') 
    st.plotly_chart(fig_mot, use_container_width=True)
    
    st.markdown("""
    <div style="color: #000000; background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e9ecef; border-left: 5px solid #ff7f0e; margin-top: 15px;">
        <p style="color: #212529; font-size: 15px; margin: 0; line-height: 1.6;">
        <strong>Análisis de Motivaciones:</strong> Este gráfico permite ponderar si el ecosistema microemprendedor de la muestra se dinamiza por <strong>Oportunidad</strong> (visión de negocio, independencia) o por <strong>Necesidad</strong> (falta de empleo asalariado, complemento de ingresos). Los emprendimientos que nacen por necesidad suelen correlacionarse de manera directa con las altas tasas de informalidad antes expuestas.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PESTAÑA 3: SECTORES ECONÓMICOS
# ---------------------------------------------------------
with tab3:
    st.markdown("<h3 style='color: #1f77b4; font-weight: bold; margin-top: 10px;'>Distribución por Rama Económica de la Actividad</h3>", unsafe_allow_html=True)
    
    df_rama = df_filtrado['rama_economica'].value_counts().reset_index()
    df_rama.columns = ['Sector', 'Cantidad']
    
    fig_rama = px.pie(
        df_rama.head(7),
        values='Cantidad',
        names='Sector',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_rama.update_traces(
        textposition='inside', 
        textinfo='percent+label',
        hole=0.3
    )
    fig_rama.update_layout(
        margin=dict(t=30, b=30, l=20, r=20)
    )
    st.plotly_chart(fig_rama, use_container_width=True)
    
    st.markdown("""
    <div style="color: #000000; background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e9ecef; border-left: 5px solid #2ca02c; margin-top: 15px;">
        <p style="color: #212529; font-size: 15px; margin: 0; line-height: 1.6;">
        <strong>Análisis de Sectores:</strong> La alta concentración en áreas específicas como el <em>Comercio minorista</em> o <em>Servicios de alimentación</em> evidencia barreras de entrada bajas. Estos sectores, aunque absorben una gran cantidad de mano de obra independiente, son históricamente los más propensos a la informalidad económica debido a su baja complejidad operativa inicial.
        </p>
    </div>
    """, unsafe_allow_html=True)