import streamlit as st
from rag_with_rbac import get_response

st.set_page_config(page_title="RAG with RBAC", page_icon="💬")

st.title("RAG with RBAC")

# Role toggle button
role = st.radio("Select your role:", ["hr", "finance"], key="role_toggle")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat input (Streamlit's original chat component pattern)
user_input = st.chat_input("Ask a question...")

if user_input:
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": user_input})
    # Placeholder for get_response function with role parameter
    response = get_response(user_input, role)
    st.session_state["messages"].append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 