from .database import get_connection

# =============================
# CRUD — Banco de Dados
# =============================

def criar_sensor(tipo, local):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO sensores (tipo, local) VALUES (?, ?)", (tipo, local))
    conn.commit()

    sensor_id = cursor.lastrowid
    conn.close()
    return sensor_id


def buscar_sensor(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT tipo, local FROM sensores WHERE id = ?", (id,))
    row = cursor.fetchone()

    conn.close()
    return row


def registrar_leitura(sensor_id, valor):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO leituras (sensor_id, valor) VALUES (?, ?)", (sensor_id, valor))
    conn.commit()
    conn.close()


def listar_sensores():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sensores")
    sensores = cursor.fetchall()
    conn.close()
    return sensores


def listar_leituras(sensor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT valor FROM leituras WHERE sensor_id = ?", (sensor_id,))
    dados = cursor.fetchall()

    conn.close()
    return [d[0] for d in dados]


def gerar_relatorio():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT local, tipo, COUNT(*), AVG(valor)
        FROM sensores 
        JOIN leituras ON sensores.id = leituras.sensor_id 
        GROUP BY sensores.id
    """)

    dados = cursor.fetchall()
    conn.close()
    return dados
