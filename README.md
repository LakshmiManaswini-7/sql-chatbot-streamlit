# SQL Chatbot from CSV using Streamlit + Ollama (Mistral)
This repo hosts a Streamlit app powered by Ollama and the Mistral LLM. Upload a CSV and ask questions in plain English the model converts them into SQL queries, executed on your data via DuckDB. Get instant, interactive answers in a simple web interface, all running locally for privacy.
SQL Chatbot from CSV using Streamlit + Ollama (Mistral)

This project is a natural language to SQL chatbot that lets you:

Upload any CSV file

Ask questions in plain English

Automatically generate SQL queries using an LLM (Mistral) via Ollama

Execute the SQL on your data with DuckDB

View results directly in a Streamlit web app

🚀 Tech Stack

Streamlit
 → Web interface for CSV upload + chatbot

DuckDB
 → In-memory SQL engine to query uploaded data

Ollama
 → Runs LLMs locally on your machine

Mistral
 → Open-weight language model used to generate SQL

🧠 How it Works

User uploads a CSV file.

User asks a question in natural language (e.g., “What is the average salary per department?”).

The app calls Ollama → Mistral LLM, which generates an SQL query.

The SQL query is executed on the uploaded CSV using DuckDB.

Results are displayed in the app.

🛠️ Installation
Prerequisites

Python 3.9+

Ollama
 installed and running

Mistral model pulled locally:

ollama pull mistral

Clone & Setup
git clone https://github.com/YOUR-USERNAME/sql-chatbot-streamlit.git
cd sql-chatbot-streamlit
pip install -r requirements.txt

▶️ Run the App
streamlit run single_app.py


Then open: http://localhost:8501

 Project Structure
├── agent_sql.py        # Handles prompt → SQL using Ollama + Mistral
├── single_app.py       # Streamlit frontend app
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md

Example

Upload a salaries.csv with a column BasePay, then ask:

"What is the maximum BasePay?"

The app will generate something like:

SELECT MAX(BasePay) FROM df;


And return the result.
