import streamlit as st
import random
import datetime
from pathlib import Path
import base64
import time

# --- Configuración básica ---
st.set_page_config(page_title="Moomin y los Participios", page_icon="🌸", layout="centered")

# --- Directorios base ---
BASE_DIR = Path(__file__).parent
STATIC_PATH = BASE_DIR / "static"

# --- Función para convertir imágenes/GIFs a base64 ---
def get_base64(filepath: Path):
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Determinar color de fondo según la hora ---
hora_actual = datetime.datetime.now().hour
if hora_actual < 12:
    reloj_color = "#fff5cc"   # mañana
elif hora_actual < 19:
    reloj_color = "#e6ffe6"   # tarde
else:
    reloj_color = "#dbeafe"   # noche

# --- CSS del reloj ---
st.markdown(
    f"""
    <style>
        .clock-container {{
            position: fixed;
            bottom: 15px;
            left: 15px;
            background-color: rgba(0,0,0,0.65);
            color: white;
            border-radius: 12px;
            padding: 8px 14px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            font-size: 15px;
            z-index: 999;
            font-family: 'Segoe UI', sans-serif;
            border: 1px solid rgba(255,255,255,0.3);
        }}
        .clock-container img {{
            width: 30px;
            height: 30px;
            margin-right: 10px;
            border-radius: 50%;
            border: 1px solid white;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


# --- Crear contenedor de reloj ---
clock_placeholder = st.empty()

def mostrar_reloj():
    """Renderiza el reloj actualizado cada segundo."""
    mini_moomin_path = STATIC_PATH / "moomin_mini.png"
    if not mini_moomin_path.exists():
        return
    mini_moomin_b64 = get_base64(mini_moomin_path)
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    reloj_html = f"""
    <div class="clock-container">
        <img src="data:image/png;base64,{mini_moomin_b64}" alt="Moomin">
        <span><b>{hora_actual}</b></span>
    </div>
    """
    clock_placeholder.markdown(reloj_html, unsafe_allow_html=True)

# Actualiza la hora una vez (para Streamlit Cloud)
mostrar_reloj()

# --- Título principal ---
st.title("🌸 Moomin y los Participios")
st.markdown("Practica participios con un toque de calma y magia Moomin 💫")

# --- Saludo según hora ---
if hora_actual < 12:
    saludo = "☀️ ¡Buenos días!"
elif hora_actual < 19:
    saludo = "🌻 ¡Buenas tardes!"
else:
    saludo = "🌙 ¡Buenas noches!"
st.subheader(saludo)

# --- Diccionario de GIFs ---
gif_moods = {
    "default": [
        "moomin_wave.gif",
        "moomin_reading.gif",
        "moomin_thinking.gif",
        "moomin_walking.gif",
    ],
    "correcto": [
        "moomin_happy.gif",
        "moomin_clap.gif",
        "moomin_dance.gif",
    ],
    "incorrecto": [
        "moomin_confused.gif",
        "moomin_sad.gif",
        "moomin_ponder.gif",
    ],
}

# --- Función para mostrar GIF animado ---
def mostrar_gif(nombre_archivo: str, ancho: int = 250):
    ruta = STATIC_PATH / nombre_archivo
    if ruta.exists():
        gif_data = get_base64(ruta)
        gif_html = f'<img src="data:image/gif;base64,{gif_data}" width="{ancho}" style="display:block;margin:auto;">'
        st.markdown(gif_html, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ No se encontró {nombre_archivo}")

# Mostrar un GIF inicial (aleatorio)
mostrar_gif(random.choice(gif_moods["default"]))

# --- Lista de ejercicios ---
ejercicios = [
    # --- Nivel básico ---
    {"frase": "No he ___ que me llamaste anoche.", "opciones": ["oído", "oido", "escuchado"], "respuesta": "oído", "pista": "Participio de 'oír'."},
    {"frase": "Hemos ___ muchas veces sobre ese tema.", "opciones": ["discutido", "discudido", "discuto"], "respuesta": "discutido", "pista": "Verbo que empieza por 'discu-'."},
    {"frase": "¿Has ___ las llaves del coche?", "opciones": ["perdido", "perdidas", "perdio"], "respuesta": "perdido", "pista": "Participio regular terminado en -ido."},
    {"frase": "He ___ toda la serie de principio a fin.", "opciones": ["visto", "mirado", "viendo"], "respuesta": "visto", "pista": "Participio irregular de 'ver'."},
    {"frase": "¿Has ___ la carta que te envié?", "opciones": ["leído", "leido", "leyendo"], "respuesta": "leído", "pista": "Participio irregular de 'leer'."},
    {"frase": "Habíamos ___ la puerta antes de salir.", "opciones": ["cerrado", "cerrada", "cierra"], "respuesta": "cerrado", "pista": "Participio regular de 'cerrar'."},
    {"frase": "Nunca había ___ un espectáculo tan bonito.", "opciones": ["visto", "mirado", "observado"], "respuesta": "visto", "pista": "Irregular, no termina en -ado / -ido."},
    {"frase": "Hemos ___ todos los documentos del proyecto.", "opciones": ["revisado", "revisto", "revisando"], "respuesta": "revisado", "pista": "Verbo regular en -ar."},
    {"frase": "He ___ en enviar ese mensaje, pero al final lo hice.", "opciones": ["dudado", "dudando", "dudar"], "respuesta": "dudado", "pista": "Participio regular de un verbo que expresa inseguridad."},
    {"frase": "Ellos han ___ el informe correctamente.", "opciones": ["redactado", "redacto", "redactar"], "respuesta": "redactado", "pista": "Acción de escribir formalmente."},
    {"frase": "Has ___ los platos después de comer, ¿verdad?", "opciones": ["lavado", "lavar", "lavando"], "respuesta": "lavado", "pista": "Participio de verbo de acción cotidiana."},
    {"frase": "Habíamos ___ el viaje desde hacía meses.", "opciones": ["planeado", "planificado", "planea"], "respuesta": "planeado", "pista": "Regular, verbo terminado en -ar."},
    {"frase": "¿Habías ___ que hoy era festivo?", "opciones": ["olvidado", "olvido", "olvidar"], "respuesta": "olvidado", "pista": "De un verbo relacionado con la memoria."},
    {"frase": "Nunca he ___ tanto trabajo en un día.", "opciones": ["tenido", "tenio", "tener"], "respuesta": "tenido", "pista": "Participio de un verbo auxiliar común."},
    {"frase": "Hemos ___ la reunión por motivos técnicos.", "opciones": ["suspendido", "suspenso", "suspendir"], "respuesta": "suspendido", "pista": "Participio irregular de 'suspender'."},
    {"frase": "He ___ el documento tres veces antes de enviarlo.", "opciones": ["revisado", "revisto", "reviso"], "respuesta": "revisado", "pista": "Regular, termina en -ado."},
    {"frase": "No habíamos ___ de tus planes.", "opciones": ["sabido", "saber", "sabiendo"], "respuesta": "sabido", "pista": "Participio del verbo 'saber'."},
    {"frase": "Han ___ las flores en el jardín.", "opciones": ["plantado", "plantar", "plantando"], "respuesta": "plantado", "pista": "Acción que haces con tierra y semillas."},
    {"frase": "He ___ la puerta para que no entre el ruido.", "opciones": ["cerrado", "cerrando", "cerrar"], "respuesta": "cerrado", "pista": "Participio de 'cerrar'."},
    {"frase": "¿Habéis ___ alguna vez en un castillo?", "opciones": ["dormido", "dormir", "duermido"], "respuesta": "dormido", "pista": "Participio regular, termina en -ido."},

    # --- Nivel intermedio ---
    {"frase": "He ___ todos los correos antes de salir.", "opciones": ["leído", "leer", "leyendo"], "respuesta": "leído", "pista": "Participio irregular de 'leer'."},
    {"frase": "Hemos ___ los libros a la biblioteca.", "opciones": ["devuelto", "devuelto", "devolver"], "respuesta": "devuelto", "pista": "Participio irregular de 'devolver'."},
    {"frase": "Nunca había ___ una película tan conmovedora.", "opciones": ["visto", "mirado", "observado"], "respuesta": "visto", "pista": "Participio irregular de 'ver'."},
    {"frase": "He ___ la lección varias veces.", "opciones": ["aprendido", "aprendiendo", "aprender"], "respuesta": "aprendido", "pista": "Participio regular de 'aprender'."},
    {"frase": "Hemos ___ de la reunión a tiempo.", "opciones": ["llegado", "llegar", "llegando"], "respuesta": "llegado", "pista": "Participio regular de 'llegar'."},
    {"frase": "He ___ la respuesta correcta después de pensar.", "opciones": ["escogido", "escogiendo", "escoger"], "respuesta": "escogido", "pista": "Participio irregular de 'escoger'."},
    {"frase": "Nunca había ___ un proyecto tan ambicioso.", "opciones": ["emprendido", "emprendiendo", "emprender"], "respuesta": "emprendido", "pista": "Participio irregular de 'emprender'."},
    {"frase": "He ___ todas las ventanas antes de salir.", "opciones": ["cerrado", "cerrando", "cerrar"], "respuesta": "cerrado", "pista": "Participio regular de 'cerrar'."},
    {"frase": "Han ___ la noticia sin avisarnos.", "opciones": ["divulgado", "divulgar", "divulgando"], "respuesta": "divulgado", "pista": "Participio regular de 'divulgar'."},
    {"frase": "He ___ la invitación, pero no podré asistir.", "opciones": ["rechazado", "rechazando", "rechazar"], "respuesta": "rechazado", "pista": "Participio regular de 'rechazar'."},
    {"frase": "Nunca había ___ algo tan impresionante.", "opciones": ["contemplado", "contemplando", "contemplo"], "respuesta": "contemplado", "pista": "Participio regular de 'contemplar'."},
    {"frase": "He ___ las luces antes de dormir.", "opciones": ["apagado", "apagando", "apagar"], "respuesta": "apagado", "pista": "Participio regular de 'apagar'."},
    {"frase": "Hemos ___ los platos del almuerzo.", "opciones": ["lavado", "lavando", "lavar"], "respuesta": "lavado", "pista": "Participio regular de 'lavar'."},
    {"frase": "He ___ la tarea que me asignaron.", "opciones": ["realizado", "haciendo", "hacer"], "respuesta": "realizado", "pista": "Participio regular de 'realizar'."},
    {"frase": "Hemos ___ a todos los invitados.", "opciones": ["recibido", "recibiendo", "recibir"], "respuesta": "recibido", "pista": "Participio regular de 'recibir'."},
    {"frase": "Nunca había ___ tanto en tan poco tiempo.", "opciones": ["aprendido", "aprender", "aprendiendo"], "respuesta": "aprendido", "pista": "Participio regular de 'aprender'."},
    {"frase": "He ___ todo lo que necesitaba para el viaje.", "opciones": ["preparado", "preparando", "preparar"], "respuesta": "preparado", "pista": "Participio regular de 'preparar'."},
    {"frase": "Hemos ___ los documentos oficiales.", "opciones": ["firmado", "firmando", "firmar"], "respuesta": "firmado", "pista": "Participio regular de 'firmar'."},
    {"frase": "Nunca había ___ tan contento.", "opciones": ["estado", "estar", "estando"], "respuesta": "estado", "pista": "Participio irregular de 'estar'."},
    {"frase": "He ___ todo lo que me pediste.", "opciones": ["hecho", "hacido", "hacer"], "respuesta": "hecho", "pista": "Participio irregular de 'hacer'."},
    {"frase": "Hemos ___ todo lo planeado.", "opciones": ["cumplido", "cumpliendo", "cumplir"], "respuesta": "cumplido", "pista": "Participio regular de 'cumplir'."},

    # --- Nivel avanzado ---
    {"frase": "He ___ a todos los alumnos presentes.", "opciones": ["saludado", "saludando", "saludar"], "respuesta": "saludado", "pista": "Participio regular de 'saludar'."},
    {"frase": "Han ___ el problema sin ayuda.", "opciones": ["resuelto", "resolvido", "resolver"], "respuesta": "resuelto", "pista": "Participio irregular de 'resolver'."},
    {"frase": "He ___ las luces del escenario.", "opciones": ["encendido", "encendiendo", "encender"], "respuesta": "encendido", "pista": "Participio irregular de 'encender'."},
    {"frase": "Hemos ___ toda la documentación requerida.", "opciones": ["entregado", "entregando", "entregar"], "respuesta": "entregado", "pista": "Participio regular de 'entregar'."},
    {"frase": "Nunca había ___ un viaje tan largo.", "opciones": ["realizado", "realizando", "realizar"], "respuesta": "realizado", "pista": "Participio regular de 'realizar'."},
    {"frase": "He ___ que lo había olvidado.", "opciones": ["recordado", "recordando", "recordar"], "respuesta": "recordado", "pista": "Participio regular de 'recordar'."},
    {"frase": "Hemos ___ a tiempo todos los informes.", "opciones": ["entregado", "entregando", "entregar"], "respuesta": "entregado", "pista": "Participio regular de 'entregar'."},
    {"frase": "He ___ la respuesta a la pregunta difícil.", "opciones": ["conseguido", "consiguiendo", "conseguir"], "respuesta": "conseguido", "pista": "Participio irregular de 'conseguir'."},
    {"frase": "Nunca había ___ tan preparado para un examen.", "opciones": ["estado", "estar", "estando"], "respuesta": "estado", "pista": "Participio irregular de 'estar'."},
    {"frase": "He ___ que la reunión estaba cancelada.", "opciones": ["descubierto", "descubriando", "descubrir"], "respuesta": "descubierto", "pista": "Participio irregular de 'descubrir'."},
    {"frase": "Hemos ___ todos los mensajes importantes.", "opciones": ["leído", "leyendo", "leer"], "respuesta": "leído", "pista": "Participio irregular de 'leer'."},
    {"frase": "Nunca había ___ tan nervioso antes de un examen.", "opciones": ["estado", "estar", "estando"], "respuesta": "estado", "pista": "Participio irregular de 'estar'."},
    {"frase": "He ___ todos los errores del informe.", "opciones": ["corregido", "corrigiendo", "corregir"], "respuesta": "corregido", "pista": "Participio irregular de 'corregir'."},
    {"frase": "Hemos ___ la decisión correcta a tiempo.", "opciones": ["tomado", "tomando", "tomar"], "respuesta": "tomado", "pista": "Participio regular de 'tomar'."},
    {"frase": "He ___ todo lo que estaba pendiente.", "opciones": ["resuelto", "resolviendo", "resolver"], "respuesta": "resuelto", "pista": "Participio irregular de 'resolver'."},
    {"frase": "Nunca había ___ una decisión tan difícil.", "opciones": ["tomado", "tomando", "tomar"], "respuesta": "tomado", "pista": "Participio regular de 'tomar'."},
    {"frase": "He ___ todas las ventanas antes de salir.", "opciones": ["cerrado", "cerrando", "cerrar"], "respuesta": "cerrado", "pista": "Participio regular de 'cerrar'."},
    {"frase": "Hemos ___ todas las tareas correctamente.", "opciones": ["realizado", "realizando", "realizar"], "respuesta": "realizado", "pista": "Participio regular de 'realizar'."},
]


# --- Estado inicial ---
if "indice_actual" not in st.session_state:
    st.session_state.indice_actual = random.randint(0, len(ejercicios) - 1)
    st.session_state.resultado = None
    st.session_state.mostrar_pista = False

ejercicio = ejercicios[st.session_state.indice_actual]

st.write("### ✏️ Completa la frase:")
st.write(f"**{ejercicio['frase']}**")

# --- Mostrar opciones ---
for opcion in ejercicio["opciones"]:
    if st.button(opcion):
        if opcion == ejercicio["respuesta"]:
            st.session_state.resultado = ("✅ ¡Muy bien!", random.choice(gif_moods["correcto"]))
            st.session_state.mostrar_pista = False
        else:
            st.session_state.resultado = ("❌ Casi... inténtalo otra vez.", random.choice(gif_moods["incorrecto"]))
            st.session_state.mostrar_pista = True

# --- Mostrar resultado ---
if st.session_state.resultado:
    mensaje, gif_nombre = st.session_state.resultado
    mostrar_gif(gif_nombre)
    if "✅" in mensaje:
        st.success(mensaje)
    else:
        st.warning(mensaje)

# --- Pista opcional ---
if st.session_state.mostrar_pista:
    if st.button("💡 Ver pista"):
        st.info(ejercicio["pista"])

# --- Botón nueva frase ---
if st.button("🔁 Nueva frase"):
    st.session_state.indice_actual = random.randint(0, len(ejercicios) - 1)
    st.session_state.resultado = None
    st.session_state.mostrar_pista = False
    st.rerun()

# --- 🪶 Modo Repaso / Cuaderno ---
st.markdown("---")
if st.checkbox("🪶 Ver modo repaso (todas las frases)"):
    mostrar_gif("moomin_teacher.gif", ancho=180)
    st.write("### 📘 Cuaderno de Participios")

    filtro = st.text_input("🔍 Buscar palabra o verbo:")
    for e in ejercicios:
        if filtro.lower() in e["frase"].lower() or filtro.lower() in e["respuesta"].lower():
            st.markdown(f"**{e['frase']}** → ✅ **{e['respuesta']}**")
            st.caption(f"💡 *{e['pista']}*")
