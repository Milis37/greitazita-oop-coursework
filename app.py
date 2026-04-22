import streamlit as st
import requests

st.set_page_config(page_title="GreitaZita AI", page_icon="💅")

st.title("💅 GreitaZita AI Finance Tracker")
st.markdown("*AI-powered finance tracker for beauty salons*")

# Sidebar
salon_id = st.sidebar.selectbox("Select Salon", [1, 2, 3], format_func=lambda x: f"Salon {x}")
st.sidebar.markdown("---")
st.sidebar.info("💡 **Example messages:**\n- Rent 1200€\n- Haircut services 5000€\n- Supplies 300€")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Send me your 3-month expenses & earnings."}]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Call API
    with st.chat_message("assistant"):
        with st.spinner("AI is analyzing..."):
            try:
                response = requests.post(
                    "http://localhost:8000/chat",
                    json={"salon_id": salon_id, "message": prompt}
                )
                ai_response = response.json()["response"]
                st.write(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except:
                st.error("❌ Backend not running! Start with: python run_api.py")
