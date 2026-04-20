# ==========================================
# SISTEMA DE PERDAS NA COLHEITA DE CANA
# FIAP - Gestão do Agronegócio em Python
# ==========================================

# ========== ESTRUTURAS DE DADOS ==========

talhao = {
    "id": 1,
    "nome": "Talhão A",
    "area_hectares": 50.0,
    "producao_estimada_ton": 400.0
}

maquinas = [
    {"nome": "Colhedora Manual",     "indice_perda": 0.05},
    {"nome": "Colhedora Mecânica A", "indice_perda": 0.08},
    {"nome": "Colhedora Mecânica B", "indice_perda": 0.15},
]

# ========== FUNÇÕES DE CÁLCULO ===========

def calcular_perda_toneladas(producao, indice_perda):
    perda = producao * indice_perda
    return round(perda, 2)

def calcular_prejuizo_reais(toneladas_perdidas, preco_por_tonelada):
    prejuizo = toneladas_perdidas * preco_por_tonelada
    return round(prejuizo, 2)

def calcular_percentual(perda, producao):
    return round((perda / producao) * 100, 2)

# ========== VALIDAÇÃO DE ENTRADAS ========

def ler_numero(mensagem, minimo=0.0):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo:
                print(f"  Valor inválido! Digite um número maior que {minimo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida! Digite apenas números (ex: 120 ou 3.5).")

# ========== PROGRAMA PRINCIPAL ===========

print("=" * 48)
print("   SISTEMA DE PERDAS NA COLHEITA DE CANA")
print("=" * 48)
print(f"  Talhão : {talhao['nome']}")
print(f"  Área   : {talhao['area_hectares']} hectares")
print("=" * 48)

producao = ler_numero("\nProdução estimada (toneladas): ", minimo=1.0)
preco    = ler_numero("Preço por tonelada (R$)      : ", minimo=1.0)

print()
print("-" * 48)
print(f"  {'Máquina':<22} {'Perda(ton)':>8} {'Prejuízo R$':>12}")
print("-" * 48)

for maq in maquinas:
    perda    = calcular_perda_toneladas(producao, maq["indice_perda"])
    prejuizo = calcular_prejuizo_reais(perda, preco)
    pct      = calcular_percentual(perda, producao)
    print(f"  {maq['nome']:<22} {perda:>8.2f} {prejuizo:>12.2f}  ({pct}%)")

print("-" * 48)
print("\n  Fonte: índices baseados nos dados da SOCICANA")
print("=" * 48)
# ========== MANIPULAÇÃO DE ARQUIVOS ==========
import json
import os
from datetime import datetime

def salvar_relatorio_txt(talhao, maquinas, producao, preco):
    """Salva o relatório em arquivo de texto."""
    nome_arquivo = "relatorio_cana.txt"
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 48 + "\n")
        arquivo.write(f"  DATA: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        arquivo.write(f"  Talhão : {talhao['nome']}\n")
        arquivo.write(f"  Área   : {talhao['area_hectares']} hectares\n")
        arquivo.write(f"  Produção: {producao} toneladas\n")
        arquivo.write(f"  Preço  : R$ {preco:.2f}/ton\n")
        arquivo.write("-" * 48 + "\n")
        arquivo.write(f"  {'Máquina':<22} {'Perda(ton)':>8} {'Prejuízo R$':>12}\n")
        arquivo.write("-" * 48 + "\n")
        for maq in maquinas:
            perda    = calcular_perda_toneladas(producao, maq["indice_perda"])
            prejuizo = calcular_prejuizo_reais(perda, preco)
            pct      = calcular_percentual(perda, producao)
            arquivo.write(f"  {maq['nome']:<22} {perda:>8.2f} {prejuizo:>12.2f}  ({pct}%)\n")
        arquivo.write("=" * 48 + "\n\n")
    print(f"\n  Relatório salvo em '{nome_arquivo}'!")


def salvar_json(talhao, maquinas, producao, preco):
    """Salva os dados e resultados em arquivo JSON."""
    nome_arquivo = "dados_cana.json"

    # Monta os resultados
    resultados = []
    for maq in maquinas:
        perda    = calcular_perda_toneladas(producao, maq["indice_perda"])
        prejuizo = calcular_prejuizo_reais(perda, preco)
        pct      = calcular_percentual(perda, producao)
        resultados.append({
            "maquina"         : maq["nome"],
            "indice_perda"    : maq["indice_perda"],
            "perda_toneladas" : perda,
            "prejuizo_reais"  : prejuizo,
            "percentual"      : pct
        })

    # Monta o registro completo
    registro = {
        "data"     : datetime.now().strftime("%d/%m/%Y %H:%M"),
        "talhao"   : talhao,
        "producao" : producao,
        "preco"    : preco,
        "resultados": resultados
    }

    # Carrega registros anteriores se o arquivo já existir
    historico = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)

    # Adiciona o novo registro e salva
    historico.append(registro)
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)

    print(f"  Dados salvos em '{nome_arquivo}'!")


def exibir_historico():
    """Lê e exibe todos os registros salvos no JSON."""
    nome_arquivo = "dados_cana.json"
    if not os.path.exists(nome_arquivo):
        print("\n  Nenhum histórico encontrado ainda.")
        return
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        historico = json.load(arquivo)
    print("\n" + "=" * 48)
    print("        HISTÓRICO DE REGISTROS")
    print("=" * 48)
    for i, reg in enumerate(historico, 1):
        print(f"\n  Registro {i} — {reg['data']}")
        print(f"  Talhão  : {reg['talhao']['nome']}")
        print(f"  Produção: {reg['producao']} ton  |  Preço: R$ {reg['preco']:.2f}")
        for r in reg["resultados"]:
            print(f"    {r['maquina']:<22} {r['perda_toneladas']:>6.2f} ton  R$ {r['prejuizo_reais']:>8.2f}  ({r['percentual']}%)")
    print("=" * 48)


# ========== CHAMA AS FUNÇÕES DE ARQUIVO ==========
salvar_relatorio_txt(talhao, maquinas, producao, preco)
salvar_json(talhao, maquinas, producao, preco)

# Pergunta se quer ver o histórico
ver = input("\nDeseja ver o histórico de registros? (s/n): ").strip().lower()
if ver == "s":
    exibir_historico()