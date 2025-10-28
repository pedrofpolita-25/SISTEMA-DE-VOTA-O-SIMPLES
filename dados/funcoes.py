import csv
import os
from datetime import datetime

# --- CONFIGURAÇÕES ---
ARQUIVO_DADOS = 'dados/votos.csv'
ARQUIVO_LOG = 'dados/log.txt'
CAMPOS_DADOS = ['Candidato', 'Total_de_Votos']

# --- FUNÇÕES DE UTENSÍLIO ---

def registrar_log(acao):
    """Registra a ação do usuário, data e hora no arquivo de log."""
    # Requisito 11 e 12: Registrar logs
    try:
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        with open(ARQUIVO_LOG, 'a', encoding='utf-8') as f:
            f.write(f"[{agora}] - {acao}\n")
    except Exception as e:
        # Tratamento de erro ao escrever no arquivo
        print(f"🚨 ERRO ao registrar log: {e}")

def carregar_dados():
    """Lê os dados do arquivo CSV e retorna como uma lista de dicionários."""
    # Requisito 8: Carregar dados em memória ao iniciar
    dados = []
    # Requisito 14: Tratamento de erro para arquivo inexistente
    if not os.path.exists('dados'):
        os.makedirs('dados')
    
    try:
        with open(ARQUIVO_DADOS, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for linha in reader:
                # Converte o total de votos para inteiro
                linha['Total_de_Votos'] = int(linha['Total_de_Votos'])
                dados.append(linha)
    except FileNotFoundError:
        # Cria o arquivo e o cabeçalho se não existir
        salvar_dados([]) # Cria arquivo vazio
    except Exception as e:
        print(f"🚨 ERRO ao carregar dados do arquivo: {e}")
        registrar_log(f"ERRO ao carregar dados: {e}")
        
    return dados

def salvar_dados(dados):
    """Salva a lista de dicionários (dados) no arquivo CSV."""
    # Requisito 9: Atualizar o arquivo automaticamente
    try:
        # Cria a pasta 'dados' se não existir
        if not os.path.exists('dados'):
            os.makedirs('dados')
            
        with open(ARQUIVO_DADOS, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=CAMPOS_DADOS, delimiter=';')
            writer.writeheader()
            writer.writerows(dados)
    except Exception as e:
        print(f"🚨 ERRO ao salvar dados no arquivo: {e}")
        registrar_log(f"ERRO ao salvar dados: {e}")

# --- FUNÇÕES PRINCIPAIS (CRUD) ---

def cadastrar_candidato():
    """Função para cadastrar um novo candidato com 0 votos."""
    # Requisito 5: Uso de função para cadastrar
    print("\n--- NOVO CADASTRO ---")
    dados = carregar_dados()
    nome = input("Pedro henrique Malásia: ").strip()
    
    if any(d['Candidato'].lower() == nome.lower() for d in dados):
        print("❌ Candidato já cadastrado!")
        registrar_log(f"Tentativa de cadastro duplicado: {nome}")
        return
        
    if nome:
        novo_candidato = {'Candidato': nome, 'Total_de_Votos': 0}
        dados.append(novo_candidato)
        salvar_dados(dados)
        print(f"✅ Candidato '{nome}' cadastrado com sucesso!")
        registrar_log(f"Cadastro de novo candidato: {nome}")
    else:
        print("❌ O nome do candidato não pode ser vazio.")
        registrar_log("Tentativa de cadastro com nome vazio")

def listar_candidatos():
    """Função para listar todos os candidatos e seus votos, ordenados."""
    # Requisito 5: Uso de função para listar
    dados = carregar_dados()
    
    if not dados:
        print("\nℹ️ Nenhuma candidato cadastrado.")
        return

    # Ordena por Total_de_Votos (decrescente) e depois por Candidato (alfabética)
    dados_ordenados = sorted(dados, key=lambda x: (x['Total_de_Votos'], x['Candidato']), reverse=True)
    
    print("\n--- LISTA DE CANDIDATOS (Total: %d) ---" % len(dados_ordenados)) # Exemplo de personalização
    for i, candidato in enumerate(dados_ordenados, 1):
        print(f"{i}. {candidato['Candidato']} -> Votos: {candidato['Total_de_Votos']}")
    print("-" * 35)
    
    registrar_log("Listagem de candidatos")

def editar_candidato():
    """Permite alterar o nome de um candidato ou a contagem de votos."""
    # Requisito 5: Uso de função para editar
    listar_candidatos()
    dados = carregar_dados()
    
    if not dados:
        return
        
    try:
        # Requisito 14: Tratamento de entrada inválida (não numérica)
        indice_para_editar = int(input("\nDigite o NÚMERO do candidato para editar: ")) - 1
        
        if 0 <= indice_para_editar < len(dados):
            candidato = dados[indice_para_editar]
            print(f"\nCandidato selecionado: {candidato['Candidato']}")
            
            # Opção de Edição
            print("O que deseja editar?")
            print("1. Nome")
            print("2. Votos")
            escolha = input("Escolha uma opção (1 ou 2): ")
            
            if escolha == '1':
                novo_nome = input(f"Novo nome para '{candidato['Candidato']}': ").strip()
                if novo_nome:
                    log_msg = f"Nome do candidato '{candidato['Candidato']}' alterado para '{novo_nome}'"
                    dados[indice_para_editar]['Candidato'] = novo_nome
                    print(f"✅ Nome alterado com sucesso! {log_msg}")
                    registrar_log(log_msg)
                    salvar_dados(dados)
                else:
                    print("❌ Nome não pode ser vazio.")
            
            elif escolha == '2':
                # Requisito 14: Tratamento de entrada inválida (valor de voto)
                novos_votos = int(input(f"Nova contagem de votos para '{candidato['Candidato']}': "))
                if novos_votos >= 0:
                    log_msg = f"Votos de '{candidato['Candidato']}' alterados de {candidato['Total_de_Votos']} para {novos_votos}"
                    dados[indice_para_editar]['Total_de_Votos'] = novos_votos
                    print(f"✅ Votos atualizados com sucesso! {log_msg}")
                    registrar_log(log_msg)
                    salvar_dados(dados)
                else:
                    print("❌ O total de votos não pode ser negativo.")
            
            else:
                print("❌ Opção de edição inválida.")
        else:
            print("❌ Número de candidato inválido.")
            registrar_log("Tentativa de edição com índice inválido")
            
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")
        registrar_log("Erro de entrada de usuário em edição")
    except Exception as e:
        print(f"🚨 ERRO durante a edição: {e}")
        registrar_log(f"ERRO inesperado em edição: {e}")

def excluir_candidato():
    """Função para excluir um candidato do sistema."""
    # Requisito 5: Uso de função para excluir
    listar_candidatos()
    dados = carregar_dados()
    
    if not dados:                                      
        return
        
    try:
        # Requisito 14: Tratamento de entrada inválida
        indice_para_excluir = int(input("\nDigite o NÚMERO do candidato para EXCLUIR: ")) - 1
        
        if 0 <= indice_para_excluir < len(dados):
            candidato_excluido = dados.pop(indice_para_excluir)
            salvar_dados(dados)
            print(f"✅ Candidato '{candidato_excluido['Candidato']}' EXCLUÍDO com sucesso!")
            registrar_log(f"Exclusão do candidato: {candidato_excluido['Candidato']}")
        else:
            print("❌ Número de candidato inválido.")
            registrar_log("Tentativa de exclusão com índice inválido")
            
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")
        registrar_log("Erro de entrada de usuário em exclusão")
    except Exception as e:
        print(f"🚨 ERRO durante a exclusão: {e}")
        registrar_log(f"ERRO inesperado em exclusão: {e}")

def registrar_voto():
    """Função para adicionar um voto a um candidato existente."""
    # Esta é a principal funcionalidade do tema "Sistema de Votação Simples"
    listar_candidatos()
    dados = carregar_dados()
    
    if not dados:
        print("\n❌ Não há candidatos para votar.")
        return

    try:
        # Requisito 14: Tratamento de entrada inválida
        indice_para_votar = int(input("\nDigite o NÚMERO do candidato para VOTAR: ")) - 1
        
        if 0 <= indice_para_votar < len(dados):
            dados[indice_para_votar]['Total_de_Votos'] += 1
            candidato_votado = dados[indice_para_votar]['Candidato']
            salvar_dados(dados)
            print(f"✅ Voto registrado com sucesso para '{candidato_votado}'!")
            registrar_log(f"Voto registrado para: {candidato_votado}")
        else:
            print("❌ Número de candidato inválido.")
            registrar_log("Tentativa de voto em índice inválido")
            
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")
        registrar_log("Erro de entrada de usuário em registro de voto")
    except Exception as e:
        print(f"🚨 ERRO durante o registro de voto: {e}")
        registrar_log(f"ERRO inesperado em registro de voto: {e}")