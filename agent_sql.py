# agent_sql.py

import sqlite3
import subprocess
import pandas as pd

# def generate_sql_query(prompt: str, table_name: str, sample_data: pd.DataFrame) -> str:
#     # Format the prompt for SQL generation
#     full_prompt = f"""
# You are a helpful AI assistant that generates SQLite SQL queries.

# Table: {table_name}
# Here are the first few rows:
# {sample_data.to_string(index=False)}

# User question:
# {prompt}

# Only output the SQL query. Do not explain anything.
# """

#     result = subprocess.run(
#         ['ollama', 'run', 'mistral'],
#         input=full_prompt.encode('utf-8'),
#         stdout=subprocess.PIPE
#     )

#     return result.stdout.decode('utf-8').strip()
def generate_sql_query(prompt: str, table_name: str, sample_data: pd.DataFrame) -> str:
    column_list = ", ".join(sample_data.columns.tolist())

    full_prompt = f"""
You are a helpful assistant that writes SQLite SQL queries.

Table name: {table_name}
Columns: {column_list}

Here are a few sample rows from the table:
{sample_data.to_string(index=False)}

User question:
{prompt}

Only return the SQL query. Do not explain anything.
"""

    result = subprocess.run(
        ['ollama', 'run', 'mistral'],
        input=full_prompt.encode('utf-8'),
        stdout=subprocess.PIPE
    )

    return result.stdout.decode('utf-8').strip()

