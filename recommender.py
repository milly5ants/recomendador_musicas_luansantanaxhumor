# streamlit_recommender_ranking.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

# --- Inicialização ---
nltk.download('stopwords')
stopwords_pt = stopwords.words('portuguese')

# --- Ler CSV ---
df = pd.read_csv("data/processed/musicas_limpa.csv", encoding="utf-8")

# --- TF-IDF ---
vectorizer = TfidfVectorizer(stop_words=stopwords_pt)
X = vectorizer.fit_transform(df['letra_limpa'])

# --- Humores ---
humores = {
    'romântico': ['amor', 'paixão', 'coração', 'beijo', 'carinho'],
    'triste': ['sozinho', 'triste', 'choro', 'adeus', 'solidão'],
    'animado': ['dança', 'festa', 'alegria', 'sorriso'],
    'saudade': ['lembrança', 'falta', 'distância', 'saudade'],
    'reflexivo': ['pensamento', 'vida', 'aprendizado', 'caminho', 'reflexão'],
    'alegre': ['feliz', 'risada', 'brilho', 'otimismo', 'contentamento'],
    'melancólico': ['silêncio', 'choro', 'saudade', 'tristeza', 'nostalgia']
}

# --- Função recomendação ---
def recomendar(humor, df, vectorizer, X, top_n=15):
    palavras = humores[humor]
    query = " ".join(palavras)
    query_vec = vectorizer.transform([query])
    similaridade = cosine_similarity(query_vec, X).flatten()
    df['score'] = similaridade
    recomendadas = df.sort_values(by='score', ascending=False).head(top_n)
    return recomendadas[['titulo', 'score']]

# --- Interface Streamlit ---
st.set_page_config(page_title="🎶 Recomendador de Luan Santana", layout="wide")
st.title("🎵 Recomendador de Músicas do Luan por Humor (Ranking)")

humor_usuario = st.selectbox("Escolha seu humor:", list(humores.keys()))

if st.button("🎯 Recomendar"):
    resultado = recomendar(humor_usuario, df, vectorizer, X)
    st.subheader(f"🎵 Top {len(resultado)} músicas para '{humor_usuario}'")
    st.dataframe(resultado.reset_index(drop=True))
