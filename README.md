Financeiro Residencial em Python
Este é um projeto prático de controle de gastos domésticos focado em Programação Orientada a Objetos. O objetivo principal foi criar uma ferramenta funcional que utilize persistência de dados local (JSON) e gere relatórios profissionais em PDF.

🛠 O que o sistema faz
Organização por classes: Separação lógica entre Categoria, Despesa e Controle.

Persistência Local: Salva tudo em arquivos .json, então seus dados não somem ao fechar o terminal.

Alertas de Teto: O sistema avisa no terminal se você ultrapassar o limite definido para uma categoria.

Exportação: Gera um PDF formatado com o resumo dos gastos mensais.

📁 Estrutura de Arquivos
A modularização foi feita para facilitar a manutenção:

main.py: Interface de terminal e loop do programa.

controle_finaceiro.py: Gerenciamento da lógica, leitura e escrita de dados.

categoria.py e despesa.py: Definição dos objetos do sistema.

🚀 Como rodar
Instale a biblioteca necessária:

pip install fpdf

Execute o script principal:

python main.py

📑 Exemplo de Uso
Ao cadastrar uma despesa, o sistema valida os limites e salva automaticamente. O arquivo JSON é gerado na primeira execução, permitindo que você acompanhe seu histórico financeiro de forma offline.