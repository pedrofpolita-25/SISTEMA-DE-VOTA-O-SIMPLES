# SISTEMA-DE-VOTAÇÃO-SIMPLES

**Integrantes**
- [Pedro Henrique Fernandes Polita] — RA:1138911
- [Guilherme Vieira Marques] — RA:1138951

**Tema: Sistema de Votação Simples**
Este projeto é um sistema de votação desenvolvido em **Python**, executado diretamente pelo terminal.  
Ele permite **cadastrar candidatos, listar, editar, excluir e registrar votos**, armazenando tudo em arquivos para manter as informações mesmo após fechar o programa.

**Descrição do Sistema**
O sistema apresenta um menu interativo no terminal, onde o usuário escolhe a ação desejada.  
Os dados são armazenados no arquivo `dados/votos.json` para que permaneçam salvos entre as execuções do programa.  
Além disso, todas as ações realizadas são registradas no arquivo `dados/log.txt`, com data e hora, para manter um **histórico de auditoria** do sistema.

**Sistema de Votação Simples**
O usuário pode:
- Cadastrar candidatos
- Listar candidatos existentes
- Registrar votos
- Editar informações
- Excluir um candidato
- Visualizar resultados

**Descrição:** Programa em Python que permite cadastrar candidatos, listar, votar, editar e excluir. Os dados ficam em dados/votos.json e logs em dados/log.txt.

**Tecnologias:** Python, manipulação de arquivos (.json), modularização (main.py, funcoes.py), tratamento de exceções.

**Como executar:**
1. python main.py
2. Dados salvos em dados/votos.json e logs em dados/log.txt.

**Observações:**
-Todo o projeto realizado acima foi feito em linguagem Python, usando o VS CODE; 
-O site está rodando e contabilizando todas as votações.
