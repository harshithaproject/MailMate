import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="Email Agent", page_icon="📧");
st.title("📧 Email Agent")


email_text = st.text_area("Enter the email content:", height=200)
recipient_email = st.text_input("Recipient's Email Address:")
tone = st.selectbox("Select the tone of the response:", ["Formal", "Informal", "Friendly", "Professional"])


if st.button("Generate Response"):
    if not recipient_email:
        st.warning("Please enter the recipient's email address.")
    else:
        with st.spinner("Generating response..."):
            response = generate_email_response(email_text, tone)
            send_status = send_email(recipient_email, response)
            st.subheader("Generated Response:")
            st.markdown(response, unsafe_allow_html=True)
            if send_status:
                st.success("Email sent successfully!")
            else:
                st.error("Failed to send email.")