import numpy as np
import streamlit as st
from openai import OpenAI
from sentence_transformers import SentenceTransformer

documents = [
    "The top 5 most expensive car brands from the dataset are: Lamorghini, Bently, Porsche, Land-Rover and Jaguar",
    "On average diesel cars has a better milage than petrol cars",
    "The larger the CC the engine the greater the power",
    "The majoirty of cars manafactured are manual. The amount of automatics has increase in recent years",
    "The more expensive the car the greater the power"
]

model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = model.encode(documents)
client = OpenAI()

st.title('Car stats chatbot')
user_question = st.chat_input('Ask a question...')

def cosine_similarity(a, b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

if user_question:
    question_emb = model.encode([user_question])[0]
    scores = [cosine_similarity(question_emb, e) for e in doc_embeddings]
    best_index = np.argmax(scores)
    retrieved_context = documents[best_index]
    
    prompt = f'''
    You are a helpful assistant. 
    Use ONLY the context below to answer the question.

    Context:
    {retrieved_context}

    Question:
    {user_question}

    If the answer is not in the context, say 'I do not know.'.
    '''

    response = client.chat.completions.create(
        model='gpt-4.1-mini',
        messages=[{'role': 'user', 'content': prompt}]
    )

    answer = response.choices[0].message.content

    st.markdown(f'**Question:** {user_question}')
    st.markdown(f'**Answer:**  {answer}')