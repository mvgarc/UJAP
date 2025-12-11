import matplotlib.pyplot as plt
import datetime as dt

# -----------------------------
# FECHAS DEL PROYECTO
# -----------------------------
# Periodos indicados:
# Octubre 2025 - Enero 2026
# Febrero 2026 - Mayo 2026

# Para el Gantt usaremos fechas específicas por actividad.
# Puedes adaptar las fechas si tu cronograma real cambia.

tasks = [
    # ---------------- FASE I: Diagnóstico ----------------
    ("Revisión documental y bibliográfica", "2025-10-01", "2025-11-15"),
    ("Aplicación de instrumentos a PyMEs", "2025-11-16", "2025-12-20"),
    ("Análisis de procesos de conciliación", "2026-01-05", "2026-01-31"),

    # ---------------- FASE II: Diseño ----------------
    ("Definición de requerimientos (OCR y Dashboard)", "2026-02-01", "2026-02-20"),
    ("Diseño de arquitectura y Base de Datos", "2026-02-21", "2026-03-15"),
    ("Prototipado de interfaces (UI/UX)", "2026-03-16", "2026-04-05"),

    # ---------------- FASE III: Desarrollo ----------------
    ("Configuración del entorno y Base de Datos", "2026-04-06", "2026-04-20"),
    ("Desarrollo módulo OCR", "2026-04-21", "2026-05-05"),
    ("Desarrollo Dashboard y reportes", "2026-05-06", "2026-05-20"),

    # ---------------- FASE IV: Validación ----------------
    ("Pruebas unitarias e integración", "2026-05-21", "2026-06-05"),
    ("Pruebas piloto con PyMEs", "2026-06-06", "2026-06-20"),
    ("Ajustes finales y redacción del tomo", "2026-06-21", "2026-07-05"),
]

# -----------------------------
# GENERACIÓN DEL GANTT
# -----------------------------
# Convertimos fechas y creamos posiciones
task_names = [t[0] for t in tasks]
start_dates = [dt.datetime.strptime(t[1], "%Y-%m-%d") for t in tasks]
end_dates = [dt.datetime.strptime(t[2], "%Y-%m-%d") for t in tasks]
durations = [(end_dates[i] - start_dates[i]).days for i in range(len(tasks))]

fig, ax = plt.subplots(figsize=(12, 8))

# Dibujar barras
for i, task in enumerate(tasks):
    ax.barh(i, durations[i], left=start_dates[i], height=0.5)

# Etiquetas
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(task_names, fontsize=9)
ax.invert_yaxis()

ax.set_xlabel("Fecha")
ax.set_title("Diagrama de Gantt – Desarrollo de la Tesis")

# Formateo de fechas
fig.autofmt_xdate()

# -----------------------------
# GUARDAR IMAGEN
# -----------------------------
plt.tight_layout()
plt.savefig("gantt_tesis.png", dpi=300)
plt.show()

print("Imagen guardada como 'gantt_tesis.png'")
