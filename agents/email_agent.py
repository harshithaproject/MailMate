import streamlit as st
import openai

client  = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_email_response(email_content, tone):
    prompt = f"Generate a {tone.lower()} response to the following email:\n\n{email_content}\n\nResponse:"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant that helps generate email responses."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()