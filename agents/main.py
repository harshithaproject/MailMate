import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="Email Agent", page_icon="📧");
st.title("📧 Email Agent")


email_text = st.text_area("Enter the email content:", height=200)
recipient_email = st.text_input("Recipient's Email Address:")
tone = st.selectbox("Select the tone of the response:", ["Formal", "Informal", "Friendly", "Professional"])
if st.button("Generate Response"):
    if email_text and recipient_email:
        with st.spinner("Generating response..."):
            response = generate_email_response(email_text, tone)
            st.subheader("Generated Response:")
            st.write(response)

            if st.button("Send Email"):
                with st.spinner("Sending email..."):
                    send_email(recipient_email, "Response to Your Email", response)
                    st.success("Email sent successfully!")
    else:
        st.error("Please enter the email content and recipient's email address.")