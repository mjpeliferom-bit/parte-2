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
    if producao == 0:
        return 0
    return round((perda / producao) * 100, 2)

# ========== VALIDAÇÃO DE ENTRADAS ========

def ler_numero(mensagem, minimo=0.0):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo:
                print(f"Valor inválido! Digite um número maior ou igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números (ex: 120 ou 3.5).")

# ========== PROGRAMA PRINCIPAL ===========

print("=" * 48)
print("   SISTEMA DE PERDAS NA COLHEITA DE CANA")
print("=" * 48)
print(f"Talhão : {talhao['nome']}")
print(f"Área   : {talhao['area_hectares']} hectares")
print("=" * 48)

producao = ler_numero("\nProdução estimada (toneladas): ", minimo=1.0)
preco    = ler_numero("Preço por tonelada (R$): ", minimo=1.0)

print()
print("-" * 48)
print(f"{'Máquina':<22} {'Perda(ton)':>10} {'Prejuízo R$':>15}")
print("-" * 48)

for maq in maquinas:
    perda    = calcular_perda_toneladas(producao, maq["indice_perda"])
    prejuizo = calcular_prejuizo_reais(perda, preco)
    pct      = calcular_percentual(perda, producao)

    print(f"{maq['nome']:<22} {perda:>10.2f} {prejuizo:>15.2f} ({pct}%)")

print("-" * 48)
print("\nFonte: índices baseados nos dados da SOCICANA")
print("=" * 48)