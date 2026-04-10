import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

data = [
    ("Revisión documental y bibliográfica", "2025-10-01", "2025-11-15", "Fase I"),
    ("Aplicación de instrumentos a PyMEs", "2025-11-16", "2025-12-20", "Fase I"),
    ("Análisis de procesos de conciliación", "2026-01-05", "2026-01-31", "Fase I"),

    ("Definición de requerimientos (OCR y Dashboard)", "2026-02-01", "2026-02-20", "Fase II"),
    ("Diseño de arquitectura y Base de Datos", "2026-02-21", "2026-03-15", "Fase II"),
    ("Prototipado de interfaces (UI/UX)", "2026-03-16", "2026-04-05", "Fase II"),

    ("Configuración del entorno y Base de Datos", "2026-04-06", "2026-04-20", "Fase III"),
    ("Desarrollo del módulo OCR", "2026-04-21", "2026-05-05", "Fase III"),
    ("Desarrollo del Dashboard y reportes", "2026-05-06", "2026-05-20", "Fase III"),

    ("Pruebas unitarias e integración", "2026-05-21", "2026-06-05", "Fase IV"),
    ("Pruebas piloto con PyMEs", "2026-06-06", "2026-06-20", "Fase IV"),
    ("Ajustes finales y redacción del tomo final", "2026-06-21", "2026-07-05", "Fase IV"),
]

df = pd.DataFrame(data, columns=["Tarea", "Inicio", "Fin", "Fase"])
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])


color_map = {
    "Fase I": "#A4C3B2",
    "Fase II": "#BFD7B5",
    "Fase III": "#F6EAC2",
    "Fase IV": "#EAC4D5"
}

# Posición vertical invertida
df["y"] = list(range(len(df)))[::-1]

# ------------------------------------------------------------
# FIGURA
# ------------------------------------------------------------
fig = go.Figure()

# Simulación de barras redondeadas
for _, row in df.iterrows():
    fig.add_shape(
        type="rect",
        x0=row["Inicio"],
        x1=row["Fin"],
        y0=row["y"] - 0.35,
        y1=row["y"] + 0.35,
        fillcolor=colors[row["Fase"]],
        line=dict(width=0),
        # Esto simula el redondeo (Plotly suaviza los bordes)
        xref="x",
        yref="y"
    )

    # Texto centrado
    fig.add_trace(go.Scatter(
        x=[row["Inicio"] + (row["Fin"] - row["Inicio"]) / 2],
        y=[row["y"]],
        text=[row["Tarea"]],
        mode="text",
        textposition="middle center",
        showlegend=False,
        hoverinfo="none"
    ))

# ------------------------------------------------------------
# ESTÉTICA

# CREACIÓN DEL DIAGRAMA DE GANTT
# ------------------------------------------------------------
fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Tarea",
    color="Fase",
    color_discrete_map=color_map
)

# Orden correcto de tareas
fig.update_yaxes(autorange="reversed")

# ------------------------------------------------------------
# AJUSTES DE LEGIBILIDAD

# ------------------------------------------------------------
fig.update_layout(
    title="Cronograma de Actividades del Proyecto de Investigación",
    plot_bgcolor="white",

    height=900,

    paper_bgcolor="white",

    xaxis=dict(
        type="date",
        showgrid=True,
        gridcolor="#DDDDDD",

    ),
    yaxis=dict(
        tickvals=df["y"],
        ticktext=df["Tarea"],
        autorange="reversed",
        showgrid=False
    ),
    font=dict(family="Arial", size=13),
    margin=dict(l=260, r=40, t=80, b=40)
)

fig.write_image("gantt_redondeado_plotly.png", width=1600, height=900)
tickfont=dict(size=14),


# Barras limpias
fig.update_traces(
    marker=dict(line_width=0),
    opacity=0.95
)

# ------------------------------------------------------------
# EXPORTACIÓN SEGURA (NO FALLA EN CODESPACES)
# ------------------------------------------------------------
try:
    fig.write_image(
        "gantt_tesis_legible.png",
        width=2200,
        height=1300,
        scale=2
    )
    print(" Imagen exportada como 'gantt_tesis_legible.png'")

except Exception as e:
    print(" No se pudo exportar la imagen automáticamente.")
    print("Motivo:", e)
    print(" Mostrando el gráfico en el navegador como alternativa.")
    fig.show()

# Mostrar siempre el gráfico
fig.show()
