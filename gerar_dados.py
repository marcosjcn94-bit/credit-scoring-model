import pandas as pd
import numpy as np
from sqlalchemy import create_engine

print("Gerando dados de clientes...")

# 1. Configurando a semente para que os dados gerados sejam sempre os mesmos
np.random.seed(42)
n_clientes = 3000 # Criando o histórico de 3.000 clientes

# 2. Criando características aleatórias, mas realistas
idade = np.random.randint(18, 70, n_clientes)
renda_mensal = np.random.uniform(1500, 25000, n_clientes)
valor_emprestimo = np.random.uniform(2000, 100000, n_clientes)
taxa_comprometimento = np.random.uniform(0.05, 0.45, n_clientes) # De 5% a 45% da renda
historico = np.random.choice(['Bom', 'Regular', 'Ruim'], n_clientes, p=[0.5, 0.3, 0.2])

# 3. Lógica comportamental 
inadimplente = []
for i in range(n_clientes):
    chance_calote = 0.05 # Risco base
    
    # Adicionando "peso" às variáveis de risco
    if historico[i] == 'Ruim': chance_calote += 0.40
    if taxa_comprometimento[i] > 0.30: chance_calote += 0.25
    if renda_mensal[i] < 3000: chance_calote += 0.10
    
    # Sorteio com base na chance de calote do cliente específico
    inadimplente.append(1 if np.random.rand() < chance_calote else 0)

# 4. Agrupando tudo em uma tabela no Python (DataFrame)
df_clientes = pd.DataFrame({
    'idade': idade,
    'renda_mensal': np.round(renda_mensal, 2),
    'valor_emprestimo': np.round(valor_emprestimo, 2),
    'taxa_comprometimento': np.round(taxa_comprometimento, 2),
    'historico_credito': historico,
    'inadimplente': inadimplente
})

# 5. Conectando ao Banco de Dados PostgreSQL
conexao_azure = 'postgresql://admin_unicred:Mjcn997!@unicred-risco-db.postgres.database.azure.com:5432/postgres?sslmode=require'
engine = create_engine(conexao_azure)

print("Conectando ao PostgreSQL e enviando dados...")

# 6. Inserindo os dados na tabela
df_clientes.to_sql('clientes_credito', engine, if_exists='append', index=False)

print("SUCESSO! 3.000 registros inseridos no banco de dados.")