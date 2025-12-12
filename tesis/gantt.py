import plotly.express as px
import pandas as pd

# ------------------------------------------------------------
# DATOS DEL PROYECTO
# ------------------------------------------------------------

data = [
    ("Revisión documental y bibliográfica", "2025-10-01", "2025-11-15", "Fase I"),
    ("Aplicación de instrumentos a PyMEs", "2025-11-16", "2025-12-20", "Fase I"),
    ("Análisis de procesos de conciliación", "2026-01-05", "2026-01-31", "Fase I"),

    ("Definición de requerimientos (OCR y Dashboard)", "2026-02-01", "2026-02-20", "Fase II"),
    ("Diseño de arquitectura y Base de Datos", "2026-02-21", "2026-03-15", "Fase II"),
    ("Prototipado de interfaces (UI/UX)", "2026-03-16", "2026-04-05", "Fase II"),

    ("Configuración del entorno y Base de Datos", "2026-04-06", "2026-04-20", "Fase III"),
    ("Desarrollo módulo OCR", "2026-04-21", "2026-05-05", "Fase III"),
    ("Desarrollo Dashboard y reportes", "2026-05-06", "2026-05-20", "Fase III"),

    ("Pruebas unitarias e integración", "2026-05-21", "2026-06-05", "Fase IV"),
    ("Pruebas piloto con PyMEs", "2026-06-06", "2026-06-20", "Fase IV"),
    ("Ajustes finales y redacción del tomo final", "2026-06-21", "2026-07-05", "Fase IV"),
]

df = pd.DataFrame(data, columns=["Tarea", "Inicio", "Fin", "Fase"])
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# Paleta pastel más editorial
color_map = {
    "Fase I": "#A4C3B2",
    "Fase II": "#BFD7B5",
    "Fase III": "#F6EAC2",
    "Fase IV": "#EAC4D5"
}

# ------------------------------------------------------------
# GANTT
# ------------------------------------------------------------

fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Tarea",
    color="Fase",
    color_discrete_map=color_map,
)

fig.update_yaxes(autorange="reversed")

# Estética más limpia
fig.update_layout(
    title="Cronograma de Actividades – Tesis",
    plot_bgcolor="white",
    paper_bgcolor="white",
    xaxis=dict(
        showgrid=True,
        gridcolor="#DDDDDD",
        tickformat="%b %Y",
        title=""
    ),
    yaxis=dict(title=""),
    font=dict(family="Arial", size=13),
    legend_title_text="",
    margin=dict(l=160, r=40, t=80, b=40),
)

# Barras sin borde (más estilo Canva)
fig.update_traces(
    marker=dict(line_width=0),
    opacity=0.95,
)

# Guardar imagen si Kaleido está instalado
fig.write_image("gantt_tesis_plotly_estetico.png", width=1600, height=900)
fig.show()

print("Imagen guardada como 'gantt_tesis_plotly_estetico.png'")
