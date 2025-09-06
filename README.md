# SQL Chatbot from CSV using Streamlit + Ollama (Mistral)
This repository contains a Streamlit application powered by Ollama and the Mistral LLM.
It allows you to upload a CSV dataset and query it in plain English.

Under the hood:

Mistral LLM (via Ollama) converts your natural language question into an SQL query.

DuckDB executes the query directly on your uploaded CSV.

Streamlit displays results in a clean, interactive web interface.

Everything runs locally, ensuring data privacy and speed. 🚀

✨ Features

Upload any CSV file

Ask questions in natural language (e.g., “What is the average salary per department?”)

Automatic SQL generation by Mistral LLM

Query execution with DuckDB

Interactive result display (single value or full table)

Local & privacy-preserving with Ollama

🛠️ Installation
Prerequisites

Python 3.9+

 [Ollama](https://ollama.ai/download) 
 installed locally

Pull the Mistral model:

ollama pull mistral

Setup

Clone the repo and install Python dependencies:

git clone https://github.com/LakshmiManaswini-7/sql-chatbot-streamlit.git

cd sql-chatbot-streamlit

pip install -r requirements.txt

Run
streamlit run single_app.py


Then open http://localhost:8501
 

📂 Project Structure
├── agent_sql.py        # Handles prompt → SQL using Ollama + Mistral
├── single_app.py       # Streamlit frontend app
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md

📖 Example

Suppose you upload a salaries.csv file with a column BasePay.
You ask:

What is the maximum BasePay?


The model generates SQL:

SELECT MAX(BasePay) FROM df;


And the app outputs:

120000.0

🤖 Why Mistral?

Efficient → Runs smoothly on local hardware

Open weights → Transparent and flexible for developers

Strong reasoning → Great at natural language → SQL mapping

Privacy-friendly → Works fully offline via Ollama

