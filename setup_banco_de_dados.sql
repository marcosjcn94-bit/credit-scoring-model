CREATE TABLE clientes_credito (
    id_cliente SERIAL PRIMARY KEY,
    idade INTEGER,
    renda_mensal NUMERIC(10, 2),
    valor_emprestimo NUMERIC(10, 2),
    taxa_comprometimento NUMERIC(5, 2),
    historico_credito VARCHAR(50),
    inadimplente INTEGER
);