# Dicionário de Dados  
## Dataset — Customer Marketing & Campaign Analytics

### Descrição Geral

Este dataset contém informações demográficas, comportamentais e históricas de campanhas de marketing de clientes, sendo adequado para análises de **CRM Analytics**, **segmentação**, **propensão à resposta**, **avaliação de campanhas** e **modelagem preditiva**.

Os dados foram originalmente derivados de um **case técnico de CRM Analytics**, amplamente utilizado em estudos acadêmicos e práticos há alguns anos, com circulação em repositórios públicos de código.  
Nesta POC, o dataset é utilizado exclusivamente para fins **educacionais, analíticos e demonstrativos**, sem qualquer vínculo comercial ativo.

---

## Identificação do Cliente

| Coluna | Tipo | Descrição |
|------|------|----------|
| `ID` | int | Identificador único do cliente |

---

## Perfil Demográfico

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Year_Birth` | int | Ano de nascimento do cliente |
| `Education` | string | Nível educacional do cliente |
| `Marital_Status` | string | Estado civil |
| `Income` | float | Renda anual estimada |

---

## Composição Familiar

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Kidhome` | int | Número de crianças no domicílio |
| `Teenhome` | int | Número de adolescentes no domicílio |

---

## Relacionamento com a Plataforma

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Dt_Customer` | date | Data de cadastro do cliente |
| `Recency` | int | Dias desde a última compra |

---

## Gastos por Categoria de Produto  
*(valores monetários acumulados)*

| Coluna | Tipo | Descrição |
|------|------|----------|
| `MntWines` | int | Gastos com vinhos |
| `MntFruits` | int | Gastos com frutas |
| `MntMeatProducts` | int | Gastos com produtos de carne |
| `MntFishProducts` | int | Gastos com peixes |
| `MntSweetProducts` | int | Gastos com doces |
| `MntGoldProds` | int | Gastos com produtos premium |

---

## Comportamento de Compra

| Coluna | Tipo | Descrição |
|------|------|----------|
| `NumDealsPurchases` | int | Compras realizadas com desconto |
| `NumWebPurchases` | int | Compras via canal web |
| `NumCatalogPurchases` | int | Compras via catálogo |
| `NumStorePurchases` | int | Compras em loja física |
| `NumWebVisitsMonth` | int | Visitas mensais ao site |

---

## Histórico de Campanhas de Marketing

| Coluna | Tipo | Descrição |
|------|------|----------|
| `AcceptedCmp1` | int (0/1) | Aceite da campanha 1 |
| `AcceptedCmp2` | int (0/1) | Aceite da campanha 2 |
| `AcceptedCmp3` | int (0/1) | Aceite da campanha 3 |
| `AcceptedCmp4` | int (0/1) | Aceite da campanha 4 |
| `AcceptedCmp5` | int (0/1) | Aceite da campanha 5 |

---

## Satisfação e Reclamações

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Complain` | int (0/1) | Indica se houve reclamação registrada |

---

## Variáveis Técnicas (Constantes)

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Z_CostContact` | int | Custo fixo de contato (constante) |
| `Z_Revenue` | int | Receita fixa associada (constante) |

> Observação: essas variáveis normalmente **não agregam poder analítico** e podem ser removidas em etapas de modelagem.

---

## Variável Alvo (Target)

| Coluna | Tipo | Descrição |
|------|------|----------|
| `Response` | int (0/1) | Indica se o cliente respondeu à última campanha |

---

## Observações Técnicas

- Dataset adequado para:
  - Segmentação de clientes
  - Modelagem de propensão à resposta
  - Análises de comportamento e valor
  - Estudos de performance de campanhas
- Estrutura clara entre:
  - Perfil
  - Comportamento
  - Histórico de marketing
- Amplamente utilizado como benchmark em estudos de CRM Analytics

---

## Procedência dos Dados

Dataset derivado de um **case técnico de CRM Analytics**, utilizado historicamente em estudos acadêmicos e demonstrações práticas, originalmente distribuído em repositórios públicos de código.
