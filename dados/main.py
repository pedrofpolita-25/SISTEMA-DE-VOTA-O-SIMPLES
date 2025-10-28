# Importa todas as funções do arquivo funcoes.py
from funcoes import (
    cadastrar_candidato, 
    listar_candidatos, 
    editar_candidato, 
    excluir_candidato,
    registrar_voto,
    registrar_log
)

def exibir_menu():
    """Exibe o menu principal do sistema de votação."""
    # Requisito 1: Menu principal (Pelo menos 4 opções)
    print("\n" + "=" * 40)
    print("🗳️ SISTEMA DE VOTAÇÃO SIMPLES - MENU") # Personalização
    print("=" * 40)
    print("1. Registrar Voto")
    print("2. Listar Candidatos (Ver Placar)")
    print("3. Gerenciar Candidatos (Cadastrar/Excluir/Editar)")
    print("4. Sair")
    print("-" * 40)
    
def gerenciar_candidatos():
    """Sub-menu para gerenciar as operações CRUD em candidatos."""
    while True:
        print("\n--- GERENCIAR CANDIDATOS ---")
        print("1. Cadastrar Novo Candidato")
        print("2. Editar Candidato/Votos")
        print("3. Excluir Candidato")
        print("4. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ").strip()
        
        # Requisito 3: Estrutura de condição
        if escolha == '1':
            cadastrar_candidato()
        elif escolha == '2':
            editar_candidato()
        elif escolha == '3':
            excluir_candidato()
        elif escolha == '4':
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

def main():
    """Função principal que executa o programa."""
    
    # Requisito 2 e 4: Programa em execução até Sair, usando laço de repetição
    while True:
        exibir_menu()
        
        try:
            escolha = input("Digite a opção desejada: ").strip()
            
            # Requisito 3: Estrutura de condição (if/elif/else)
            if escolha == '1':
                registrar_voto()
            elif escolha == '2':
                listar_candidatos()
            elif escolha == '3':
                gerenciar_candidatos()
            elif escolha == '4':
                print("👋 Sistema encerrado. Até mais!")
                registrar_log("Encerrando sistema")
                break # Encerra o laço 'while'
            else:
                print("❌ Opção inválida. Escolha uma das opções acima (1 a 4).")
                registrar_log(f"Tentativa de opção de menu inválida: {escolha}")
                
        # Requisito 14: Tratamento de erro geral para evitar 'quebras'
        except Exception as e:
            print(f"🚨 Ocorreu um erro inesperado: {e}")
            registrar_log(f"ERRO INESPERADO no menu principal: {e}")

# Execução do programa
if __name__ == '__main__':
    main()