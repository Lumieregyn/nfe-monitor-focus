import sqlite3

def init_db():
    conn = sqlite3.connect("nfes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nfes (
            chave TEXT PRIMARY KEY,
            emitente TEXT,
            valor REAL,
            data_emissao TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_nfe(chave, emitente, valor, data_emissao):
    conn = sqlite3.connect("nfes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO nfes VALUES (?, ?, ?, ?)",
                   (chave, emitente, valor, data_emissao))
    conn.commit()
    conn.close()
