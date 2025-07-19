# 📦 nfe-monitor-focus

Monitoramento de NF-e recebidas via API da [Focus NFe](https://focusnfe.com.br)

## ✅ O que este projeto faz

- Consulta NF-e emitidas contra seu CNPJ usando API da Focus NFe
- Agenda consulta automática a cada 15 minutos
- Exibe status via API FastAPI
- Pronto para expansão com armazenamento e rastreamento de transportadora

## 🚀 Como usar

1. Clone o projeto:

```bash
git clone https://github.com/Lumieregyn/nfe-monitor-focus.git
cd nfe-monitor-focus
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Copie o `.env`:

```bash
cp .env.example .env
```

4. Configure seu token e CNPJ no `.env`

5. Execute:

```bash
uvicorn app.main:app --reload
```

## ⏱️ Consulta automática

A cada 15 minutos o sistema consulta as NF-e emitidas contra o CNPJ informado.

## 🛠️ Em breve

- Armazenamento em banco de dados
- Integração com APIs de transportadoras
