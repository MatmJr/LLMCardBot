### Chatbot SQL com LangChain e Streamlit

Este projeto implementa um chatbot baseado em **LangChain** e **Streamlit**, projetado para responder a perguntas relacionadas a um banco de dados SQL utilizando o modelo GPT-4o-mini para geração de texto. O chatbot utiliza a técnica de **Text-to-SQL** para interpretar perguntas em linguagem natural, traduzindo-as para consultas SQL que são executadas no banco de dados.

---

### **Descrição**

O chatbot permite que usuários façam perguntas em linguagem natural sobre um banco de dados contendo informações sobre inadimplência, dados demográficos e outras características relacionadas. O modelo GPT-4 é usado para interpretar as perguntas e gerar respostas estruturadas, que incluem:

1. A **consulta SQL gerada**.
2. O **resultado da consulta**.
3. Uma interpretação amigável do resultado (opcional).

---

### **Configuração do Banco de Dados**

O banco de dados utilizado é uma base SQLite contendo os seguintes atributos:

| Atributo      | Descrição                                                                 |
|---------------|---------------------------------------------------------------------------|
| `REF_DATE`    | Data de referência do registro                                           |
| `TARGET`      | Alvo binário de inadimplência (1: Mau Pagador, atraso > 60 dias em 2 meses) |
| `VAR2`        | Sexo do indivíduo                                                        |
| `IDADE`       | Idade do indivíduo                                                       |
| `VAR4`        | Flag de óbito (indica se o indivíduo faleceu)                            |
| `VAR5`        | Unidade Federativa (UF) brasileira                                       |
| `VAR8`        | Classe social estimada                                                   |

---

### **Requisitos**

Basta abrir o terminal e seguir as instruções abaixo para configurar o ambiente virtual e instalar as dependências necessárias:

#### **Windows**
```bash
python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt
```

#### **Linux/Mac**
```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

Depois disso, você estará pronto para executar o projeto.

---

### **Como Executar**

1. Clone este repositório e entre no diretório do projeto.
2. Execute o arquivo que está no diretório etl e certifique-se de que o banco de dados está localizado em `datasets/Data.db`. Ajuste o caminho no código, se necessário.
3. Execute o aplicativo Streamlit com o comando:

   ```bash
   streamlit run app.py
   ```

4. Acesse a interface do chatbot no seu navegador.

---

### **Funcionalidades**

1. **Text-to-SQL:**
   - O chatbot converte perguntas em linguagem natural para consultas SQL, utilizando o modelo GPT-4o-mini.
   - Exemplo de pergunta: *"Qual a média da idade dos indivíduos?"*
     - SQL gerado: `SELECT AVG("IDADE") AS "media_idade" FROM ccdataset;`
     - Resultado: `41.87`.

2. **Exibição Estruturada:**
   - Para cada pergunta, o chatbot exibe:
     - A consulta SQL gerada.
     - O resultado da consulta.
     - (Opcional) Uma interpretação amigável da resposta.

3. **Manutenção de Contexto:**
   - O histórico de conversas é preservado, permitindo revisitar interações anteriores.

---

### **Exemplo de Uso**

**Entrada:**
Usuário pergunta: *"Quantos registros indicam inadimplência?"*

**Saída:**
```markdown
**SQL Query:**  
```sql
SELECT COUNT(*) AS "inadimplencia" FROM ccdataset WHERE TARGET = 1;
```

**Resultado:**  
[(1500,)]

**Interpretação:**  
Há 1.500 registros no banco de dados que indicam inadimplência.
