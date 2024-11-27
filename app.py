import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain


_ = load_dotenv()


db = SQLDatabase.from_uri(
    "sqlite:///datasets/Data.db"
)  
llm = ChatOpenAI(model="gpt-4o-mini")  


chain = create_sql_query_chain(llm, db)


def chatbot_page():
    st.title("Chatbot com LangChain e Banco de Dados SQL")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    messages = st.session_state["messages"]

    st.header("Bem-vindo(a) ao Chatbot SQL!")
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Digite sua pergunta:")

    if user_input:

        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            try:

                response = chain.invoke({"question": user_input})

                sql_query = response.split("SQLQuery:")[1].strip()

                db_result = db.run(sql_query)

                resposta_formatada = f"""
                **SQL Query:**  
                ```sql
                {sql_query}
                ```

                **Resultado:**  
                {db_result}

                """

                placeholder.markdown(resposta_formatada)
            except Exception as e:
                error_message = f"Erro ao processar sua pergunta: {e}"
                placeholder.markdown(error_message)
                response = error_message

            messages.append({"role": "assistant", "content": resposta_formatada})
        st.session_state["messages"] = messages


if __name__ == "__main__":
    chatbot_page()
