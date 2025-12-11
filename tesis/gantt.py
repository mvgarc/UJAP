import plotly.express as px
import pandas as pd

# ------------------------------------------------------------
# DATOS DEL PROYECTO
# ------------------------------------------------------------

data = [
    # Fase I: Diagnóstico
    ("Revisión documental y bibliográfica", "2025-10-01", "2025-11-15", "Fase I"),
    ("Aplicación de instrumentos a PyMEs", "2025-11-16", "2025-12-20", "Fase I"),
    ("Análisis de procesos de conciliación", "2026-01-05", "2026-01-31", "Fase I"),

    # Fase II: Diseño
    ("Definición de requerimientos (OCR y Dashboard)", "2026-02-01", "2026-02-20", "Fase II"),
    ("Diseño de arquitectura y Base de Datos", "2026-02-21", "2026-03-15", "Fase II"),
    ("Prototipado de interfaces (UI/UX)", "2026-03-16", "2026-04-05", "Fase II"),

    # Fase III: Desarrollo
    ("Configuración del entorno y Base de Datos", "2026-04-06", "2026-04-20", "Fase III"),
    ("Desarrollo módulo OCR", "2026-04-21", "2026-05-05", "Fase III"),
    ("Desarrollo Dashboard y reportes", "2026-05-06", "2026-05-20", "Fase III"),

    # Fase IV: Validación
    ("Pruebas unitarias e integración", "2026-05-21", "2026-06-05", "Fase IV"),
    ("Pruebas piloto con PyMEs", "2026-06-06", "2026-06-20", "Fase IV"),
    ("Ajustes finales y redacción del tomo final", "2026-06-21", "2026-07-05", "Fase IV"),
]

# Crear DataFrame
df = pd.DataFrame(data, columns=["Tarea", "Inicio", "Fin", "Fase"])
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# ------------------------------------------------------------
# CREAR DIAGRAMA DE GANTT
# ------------------------------------------------------------

fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Tarea",
    color="Fase",
    title="Cronograma de la Tesis (Gantt Estilo Profesional)",
    color_discrete_map={
        "Fase I": "#6A8EAE",
        "Fase II": "#9BBF8B",
        "Fase III": "#EFCB68",
        "Fase IV": "#E5989B"
    }
)

# Orden vertical de tareas invertido
fig.update_yaxes(autorange="reversed")

# Diseño visual más limpio
fig.update_layout(
    plot_bgcolor="white",
    xaxis=dict(
        showgrid=True,
        gridcolor="lightgray",
        tickformat="%b %Y"
    ),
    title_font_size=20,
    legend_title_text="Fases",
    margin=dict(l=120, r=50, t=80, b=50)
)

# Opciones de texto
fig.update_traces(
    marker=dict(line_color="black", line_width=0.5),
    hovertemplate="<b>%{y}</b><br>Inicio: %{base|%Y-%m-%d}<br>Fin: %{x|%Y-%m-%d}"
)

# ------------------------------------------------------------
# GUARDAR IMAGEN (PNG)
# ------------------------------------------------------------

fig.write_image("gantt_tesis_estetico_plotly.png", width=1400, height=800)
fig.show()

print("Imagen guardada como 'gantt_tesis_estetico_plotly.png'")
