import sqlite3

# Caminho do banco de dados SQLite
DB_PATH = "nfes.db"

# Criação da tabela ao iniciar a aplicação
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas_fiscais (
            chave TEXT PRIMARY KEY,
            emitente TEXT,
            documento_emitente TEXT,
            valor REAL,
            data_emissao TEXT,
            situacao TEXT,
            tipo_nfe TEXT,
            raw_payload TEXT
        )
    """)
    conn.commit()
    conn.close()

# Salva uma NF-e recebida pelo webhook
def salvar_nfe(data: dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO notas_fiscais (
            chave, emitente, documento_emitente, valor,
            data_emissao, situacao, tipo_nfe, raw_payload
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("chave_nfe"),
        data.get("nome_emitente"),
        data.get("documento_emitente"),
        float(data.get("valor_total", 0)),
        data.get("data_emissao"),
        data.get("situacao"),
        data.get("tipo_nfe"),
        str(data)
    ))
    conn.commit()
    conn.close()

# Lista todas as notas fiscais armazenadas
def listar_nfes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            chave, emitente, documento_emitente, valor,
            data_emissao, situacao, tipo_nfe
        FROM notas_fiscais
        ORDER BY data_emissao DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    nfes = []
    for row in rows:
        nfes.append({
            "chave": row[0],
            "emitente": row[1],
            "documento_emitente": row[2],
            "valor": row[3],
            "data_emissao": row[4],
            "situacao": row[5],
            "tipo_nfe": row[6],
        })
    return nfes
