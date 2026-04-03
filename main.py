import os
from datetime import datetime
from categoria import Categoria
from controle_finaceiro import ControleFinanceiro

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "="*30)
    print("  CONTROLE FINANCEIRO RESIDENCIAL")
    print("="*30)
    print("1. Cadastrar Nova Despesa")
    print("2. Definir Limite de Categoria")
    print("3. Visualizar Resumo (Terminal)")
    print("4. Exportar Relatório PDF")
    print("5. Sair")
    print("-" * 30)

def main():
    # Inicializa o controlador (que carrega o JSON automaticamente)
    sistema = ControleFinanceiro()
    
    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Valor: R$ "))
                cat = input("Categoria: ").strip().capitalize()
                data = input("Data (DD/MM/AAAA) [Vazio para hoje]: ").strip()
                if not data:
                    data = datetime.now().strftime("%d/%m/%Y")
                desc = input("Descrição: ")
                
                sistema.registrar_despesa(valor, cat, data, desc)
                input("\n✅ Despesa salva! Pressione Enter...")
            except ValueError:
                input("\n❌ Erro: Digite um valor numérico válido. [Enter]")

        elif opcao == "2":
            cat = input("Categoria para definir limite: ").strip().capitalize()
            try:
                limite = float(input(f"Qual o limite mensal para {cat}? R$ "))
                # Se a categoria não existir, o sistema cria no dicionário
                if cat not in sistema.categorias:
                    sistema.categorias[cat] = Categoria(cat, limite)
                else:
                    sistema.categorias[cat].limite = limite
                
                sistema.salvar_dados()
                input(f"\n✅ Limite de {cat} atualizado! [Enter]")
            except ValueError:
                input("\n❌ Erro: Valor inválido. [Enter]")

        elif opcao == "3":
            print(f"\n{'CATEGORIA':<15} | {'GASTO':<10} | {'LIMITE':<10} | STATUS")
            print("-" * 55)
            for nome, obj_cat in sistema.categorias.items():
                gasto = obj_cat.total_gasto()
                limite = obj_cat.limite
                status = "🔴 EXCEDIDO" if limite > 0 and gasto > limite else "🟢 OK"
                print(f"{nome:<15} | R${gasto:>8.2f} | R${limite:>8.2f} | {status}")
            input("\nFim do resumo. Pressione Enter...")

        elif opcao == "4":
            print("\nGerando PDF...")
            nome_arquivo = sistema.gerar_pdf()
            input(f"✅ Arquivo '{nome_arquivo}' criado! [Enter]")

        elif opcao == "5":
            print("\nEncerrando sistema... Até logo!")
            break
        
        else:
            input("\n⚠️ Opção inválida! Tente novamente. [Enter]")

if __name__ == "__main__":
    main()