# Modelagem Preditiva de Risco de Crédito (Credit Scoring) 🏦

## 📌 O Problema de Negócio
No mercado financeiro, a concessão de crédito exige um equilíbrio delicado: aprovar o máximo de clientes legítimos minimizando a exposição a calotes (inadimplência). O objetivo deste projeto é desenvolver um modelo preditivo capaz de separar proativamente os bons pagadores dos perfis de alto risco em uma carteira de cooperados, otimizando a tomada de decisão da equipe de risco.

## 💡 A Solução e Arquitetura
Construção de um pipeline de *Machine Learning End-to-End*, desde a extração segura dos dados até a avaliação de métricas de negócios em dados desbalanceados.
* Conexão segura ponta a ponta (SSL) com um banco de dados relacional hospedado na nuvem (Microsoft Azure).
* Análise Exploratória (EDA) e engenharia de *features* focada em variáveis financeiras críticas (como comprometimento de renda).
* Treinamento e otimização de um algoritmo de *Random Forest*.

## 📊 Resultados Alcançados (Impacto)
Em cenários de crédito, a acurácia global pode ser uma métrica ilusória devido ao desbalanceamento natural dos dados. Por isso, o modelo foi otimizado para maximizar a segurança operacional:
*   **Precisão (Bons Pagadores):** 86% de segurança ao aprovar crédito.
*   **Recall (Inadimplentes):** Capacidade de identificar e reter proativamente 49% dos prováveis calotes antes que ocorram.
*   **Acurácia Global:** 77%.

## 🛠️ Tecnologias Utilizadas
* Python, Pandas, Scikit-Learn
* Bancos de Dados Relacionais (SQL, PostgreSQL)
* Microsoft Azure (Cloud)

## ⚙️ Como executar este projeto
1. Clone o repositório: `git clone https://github.com/marcosjcn94-bit/credit-scoring-model.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o notebook principal ou script de modelagem.

## Licença

A [licença MIT](LICENSE) cobre exclusivamente o código-fonte e a documentação originais. Dados, imagens, PDFs, pesos de modelos e materiais de terceiros ficam fora desta licença e seguem os termos aplicáveis. A licença do notebook `analise_exploratoria.ipynb` cobre as células originais de código e texto. Os dados gerados e as saídas armazenadas ficam excluídos.
