# ==========================================
# main.py
# Sistema de Perdas na Colheita de Cana
# FarmTech Solutions
# ==========================================

from calculos import (
    talhao, maquinas,
    calcular_perda_toneladas,
    calcular_prejuizo_reais,
    calcular_percentual,
    ler_numero
)

# ========== EXIBIÇÃO ==========

def exibir_cabecalho():
    print("=" * 50)
    print("   FARMTECH - SISTEMA DE PERDAS NA COLHEITA")
    print("=" * 50)

def exibir_talhao():
    print(f"\nTalhão   : {talhao['nome']}")
    print(f"Área     : {talhao['area_hectares']} hectares")
    print(f"Produção : {talhao['producao_estimada_ton']} toneladas estimadas")
    print("-" * 50)

def exibir_maquinas():
    print("\nMáquinas disponíveis:")
    for i, maq in enumerate(maquinas, 1):
        print(f"  {i}. {maq['nome']} (índice de perda: {int(maq['indice_perda'] * 100)}%)")

def escolher_maquina():
    exibir_maquinas()
    while True:
        try:
            opcao = int(input("\nEscolha o número da máquina: "))
            if 1 <= opcao <= len(maquinas):
                return maquinas[opcao - 1]
            else:
                print(f"Opção inválida! Digite um número entre 1 e {len(maquinas)}.")
        except ValueError:
            print("Entrada inválida! Digite apenas o número da opção.")

# ========== RELATÓRIO ==========

def exibir_relatorio(maquina, producao, preco):
    perda = calcular_perda_toneladas(producao, maquina["indice_perda"])
    prejuizo = calcular_prejuizo_reais(perda, preco)
    percentual = calcular_percentual(perda, producao)

    print("\n" + "=" * 50)
    print("              RELATÓRIO DE PERDAS")
    print("=" * 50)
    print(f"  Talhão          : {talhao['nome']}")
    print(f"  Máquina usada   : {maquina['nome']}")
    print(f"  Produção total  : {producao} toneladas")
    print(f"  Perda estimada  : {perda} toneladas ({percentual}%)")
    print(f"  Prejuízo        : R$ {prejuizo:,.2f}")
    print("=" * 50)

    # Avaliação da perda
    if percentual <= 5:
        print("  ✔ Perda dentro do aceitável. Boa colheita!")
    elif percentual <= 10:
        print("  ⚠ Atenção: perda moderada. Avalie a máquina.")
    else:
        print("  ✘ Perda alta! Considere trocar o método de colheita.")
    print("=" * 50)

# ========== MENU PRINCIPAL ==========

def menu():
    exibir_cabecalho()
    exibir_talhao()

    producao = ler_numero("\nProdução estimada (toneladas): ", minimo=1.0)
    preco = ler_numero("Preço por tonelada (R$): ", minimo=1.0)

    maquina = escolher_maquina()

    exibir_relatorio(maquina, producao, preco)

    print("\nDeseja fazer outra simulação?")
    resposta = input("Digite 'sim' para continuar ou qualquer tecla para sair: ").strip().lower()
    if resposta == "sim":
        print()
        menu()
    else:
        print("\nObrigado por usar o FarmTech! Até logo.")
        print("=" * 50)

# ========== INÍCIO ==========

if __name__ == "__main__":
    menu()
