# ==========================================
# arquivos.py
# Integrante 2 - Manipulação de Arquivos
# ==========================================

import json

# ========== PERSISTÊNCIA (JSON) ==========

def salvar_dados_json(lista_colheitas, nome_arquivo="dados_agro.json"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista_colheitas, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")

def carregar_dados_json(nome_arquivo="dados_agro.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("⚠️ Arquivo 'dados_agro.json' não encontrado!")
        print("Execute salvar_dados_json() primeiro para gerar os dados.")
        return []
    except Exception as e:
        print(f"❌ Erro ao carregar: {e}")
        return []

# ========== SAÍDA FORMATADA (TXT) ==========

def gerar_relatorio_txt(lista_colheitas, nome_relatorio="relatorio_perdas.txt"):
    try:
        with open(nome_relatorio, "w", encoding="utf-8") as f:
            f.write("=" * 40 + "\n")
            f.write("  RELATÓRIO DE PERDAS NA COLHEITA\n")
            f.write("=" * 40 + "\n\n")

            if not lista_colheitas:
                f.write("Nenhum dado encontrado.\n")
            else:
                for i, item in enumerate(lista_colheitas, 1):
                    f.write(f"Registro #{i}\n")
                    f.write(f"Talhão   : {item['talhao']}\n")
                    f.write(f"Máquina  : {item['maquina']}\n")
                    f.write(f"Perda    : {item['perda_p']}%\n")
                    f.write("-" * 20 + "\n")

            f.write("\nFim do Relatório.\n")
        print(f"✅ Relatório '{nome_relatorio}' gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {e}")
