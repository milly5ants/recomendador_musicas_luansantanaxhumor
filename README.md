# 🎶 Recomendador de Músicas do Luan Santana por Humor

Este projeto usa **Python + NLP** para recomendar músicas do **Luan Santana** de acordo com o **estado de espírito do usuário** (ex.: "tô apaixonado", "tô triste").  

A ideia é mostrar na prática como aplicar **tratamento de dados**, **processamento de linguagem natural (NLP)** e **automação** em um problema divertido e acessível, mas que reflete cenários reais de **sistemas de recomendação** usados em empresas (Netflix, Spotify, e-commerce, etc).

---

## 🚀 Objetivos do Projeto
- Coletar e organizar letras de músicas do Luan Santana.
- Tratar o texto (limpeza, tokenização, embeddings).
- Classificar músicas por emoção (romântico, animado, nostálgico, triste).
- Criar um recomendador que sugere músicas conforme o humor informado.
- Disponibilizar o sistema em uma interface simples (app web ou bot no Telegram).

---

## 📂 Estrutura do Projeto

recomendador-luan-santana/
│── data/ # dados brutos e tratados
│ ├── raw/
│ ├── processed/
│
│── notebooks/ # análises exploratórias
│ ├── 01_scraping.ipynb
│ ├── 02_preprocessing.ipynb
│ ├── 03_modelo_classificacao.ipynb
│ ├── 04_recomendador.ipynb
│
│── src/ # código principal
│ ├── scraping.py
│ ├── preprocessing.py
│ ├── model.py
│ ├── recommender.py
│
│── app/ # interfaces
│ ├── streamlit_app.py
│ ├── telegram_bot.py
│
│── tests/ # testes unitários
│
│── requirements.txt # dependências
│── README.md # documentação principal
│── .gitignore # arquivos ignorados no Git

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/recomendador-luan-santana.git
   cd recomendador-luan-santana

2. Crie e ative um ambiente virtual:
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. Instale as dependências:
pip install -r requirements.txt

▶️ Como Rodar

1. Coletar letras 
python src/scraping.py

2. Tratar e preparar dataset
python src/preprocessing.py

3. Treinar modelo
python src/model.py

4. Testar recomendador
python src/recommender.py --mood "apaixonado"

5. Rodar aplicação web (Streamlit)
streamlit run app/streamlit_app.py

🧰 Tecnologias Usadas

- Python 3.x
- BeautifulSoup / Requests → scraping das letras
- Pandas / NumPy → manipulação de dados
- NLTK / spaCy → processamento de texto
- Scikit-learn → classificação de emoções
- Streamlit → app web interativo
- python-telegram-bot → bot no Telegram (opcional)

📌 Status do Projeto

📍 Etapa atual: Montagem da estrutura inicial + coleta de dados (scraping).
👉 Próximos passos: limpeza dos textos e classificação inicial de emoções.

👨‍💻 Autor

Projeto desenvolvido por Jamily, com foco em aprendizado de Python, NLP e automações com IA.
