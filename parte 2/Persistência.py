import json

# 1. FUNÇÃO (A lógica de salvar)
def salvar_dados_json(lista_colheitas, nome_arquivo="dados_agro.json"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista_colheitas, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Arquivo '{nome_arquivo}' gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

# 2. DADOS DE TESTE (Simulando o que o Integrante 1 enviaria)
dados_veneros = [
    {"talhao": "Norte-01", "maquina": "Colhedora A", "perda_p": 12.5},
    {"talhao": "Sul-04", "maquina": "Colhedora B", "perda_p": 8.0}
]

# 3. CHAMADA DA FUNÇÃO (O comando que faz acontecer)
salvar_dados_json(dados_veneros)