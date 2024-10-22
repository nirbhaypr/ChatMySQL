from langchain_code import get_few_shots_chain
import streamlit as st
from langchain.schema import AIMessage, HumanMessage

st.set_page_config(page_title="Chat with MySQL", page_icon=":speech_balloon:")

st.title("classicmodel Database Chatbot")
st.markdown("[Know more about the Database.](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
    ]

# Display chat history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        st.markdown(f"**AI:** {message.content}")
    elif isinstance(message, HumanMessage):
        st.markdown(f"**You:** {message.content}")

# Initialize the question if not already set in session state
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# Input box for user questions
question = st.text_input("Ask anything related to the dataset: ", value=st.session_state.input_text, key="input_box")

if st.session_state.input_text and question != "":
    # Append the user's question to chat history
    st.session_state.chat_history.append(HumanMessage(content=question))
    
    # Get the answer from Langchain
    chain = get_few_shots_chain()
    answer = chain.invoke(question)
    
    # Append the AI's answer to chat history
    st.session_state.chat_history.append(AIMessage(content=answer['result']))
    
    # Clear the input box
    st.session_state.input_text = ""

    # Refresh to display the updated chat history
    st.rerun()

st.session_state.input_text = question