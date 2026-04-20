# ==========================================
# calculos.py
# Integrante 1 - Arquiteto de Dados e Lógica
# ==========================================

# ========== ESTRUTURAS DE DADOS ==========

talhao = {
    "id": 1,
    "nome": "Talhão A",
    "area_hectares": 50.0,
    "producao_estimada_ton": 400.0
}

maquinas = [
    {"nome": "Colhedora Manual", "indice_perda": 0.05},
    {"nome": "Colhedora Mecânica A", "indice_perda": 0.08},
    {"nome": "Colhedora Mecânica B", "indice_perda": 0.15},
]

# ========== FUNÇÕES DE CÁLCULO ==========

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

# ========== VALIDAÇÃO DE ENTRADAS ==========

def ler_numero(mensagem, minimo=0.0):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < minimo:
                print(f"Valor inválido! Digite um número maior ou igual a {minimo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números, como 120 ou 3.5.")
