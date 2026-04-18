import json

# 1. Função para carregar os dados salvos pelo Persistência.py
def carregar_dados_do_disco(nome_arquivo="dados_agro.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("⚠️ Erro: O arquivo 'dados_agro.json' não foi encontrado!")
        print("Execute o arquivo 'Persistência.py' primeiro para gerar os dados.")
        return []

# 2. Sua função de Saída Formatada
def gerar_relatorio_txt(lista_colheitas, nome_relatorio="relatorio_perdas.txt"):
    try:
        with open(nome_relatorio, "w", encoding="utf-8") as f:
            f.write("="*40 + "\n")
            f.write("  RELATÓRIO DE PERDAS NA COLHEITA\n")
            f.write("="*40 + "\n\n")
            
            if not lista_colheitas:
                f.write("Nenhum dado encontrado no banco de dados.\n")
            else:
                for i, item in enumerate(lista_colheitas, 1):
                    f.write(f"Registro #{i}\n")
                    f.write(f"Talhão: {item['talhao']}\n")
                    f.write(f"Máquina: {item['maquina']}\n")
                    f.write(f"Perda Estimada: {item['perda_p']}%\n")
                    f.write("-" * 20 + "\n")
            
            f.write("\nFim do Relatório.\n")
        print(f"✅ Sucesso! O relatório '{nome_relatorio}' foi atualizado com os dados do JSON.")
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {e}")

# --- EXECUÇÃO ---

# Passo A: Busca os dados que o Persistência.py salvou
dados_veneros_do_json = carregar_dados_do_disco()

# Passo B: Se houver dados, gera o TXT
if dados_veneros_do_json:
    gerar_relatorio_txt(dados_veneros_do_json)