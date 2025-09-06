# app.py

import streamlit as st
import pandas as pd
import duckdb  # 🦆 DuckDB!
from agent_sql import generate_sql_query

st.set_page_config(page_title="SQL Chatbot from CSV", layout="wide")
st.title("📊 Upload CSV and Ask Questions in Natural Language")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     df.columns = df.columns.str.strip()
#      # DEBUG: Show all column names
#     st.write("🧾 Column names:", df.columns.tolist())

#     # # Optional: Clean BasePay or other currency columns
#     if "BasePay" in df.columns:
#     #     st.write("🔍 Cleaning BasePay column...")
#     #     df["BasePay"] = df["BasePay"].replace('[\$,]', '', regex=True)
#         df["BasePay"] = pd.to_numeric(df["BasePay"], errors="coerce")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()  # Clean column names

    st.write("🧾 Column names:", df.columns.tolist())

    # Automatically clean and convert numeric-like columns
    for col in df.columns:
        if df[col].dtype == 'object':  # Process only text-based columns
            # Step 1: Strip unwanted characters like '$', ',' and whitespace
            cleaned = (
                df[col]
                .astype(str)
                .str.replace(r'[\$,]', '', regex=True)
                .str.strip()
            )

            # Step 2: Try to convert to numeric (invalid values will become NaN)
            converted = pd.to_numeric(cleaned, errors='coerce')

            # Step 3: If more than 50% values are valid numbers, use the converted column
            if converted.notna().mean() > 0.5:
                df[col] = converted
    
    st.write("📄 Here's a preview of your data:")
    st.dataframe(df)

    # # DEBUG: Show BasePay type and values
    # if "BasePay" in df.columns:
    #     st.write("🧬 BasePay dtype:", df["BasePay"].dtype)
    #     st.write("📊 First 10 BasePay values (non-null):", df["BasePay"].dropna().head(10))

    #     # DuckDB test run
    #     try:
    #         test_result = duckdb.query("SELECT MAX(BasePay) AS MaxBasePay FROM df").to_df()
    #         st.write("🧪 DuckDB test: MAX(BasePay):", test_result)
    #     except Exception as e:
    #         st.error(f"❌ DuckDB test query failed: {str(e)}")

    # Let user ask question
    st.markdown("---")
    query = st.text_input("💬 Ask a question about your uploaded data")

    if query:
        with st.spinner("Analyzing and executing..."):
            try:
                # Generate SQL using Ollama
                sql_query = generate_sql_query(query, "df", df.head(5))
                st.code(sql_query, language="sql")

                # Execute the SQL query using DuckDB
                result = duckdb.query(sql_query).to_df()


                 # Handle result
                if result.empty:
                    st.warning("⚠️ The query returned no data.")
                elif result.shape == (1, 1):
                    value = result.iat[0, 0]
                    if pd.isna(value) or value is None:
                        st.warning("⚠️ Query result is NULL — possibly due to invalid/missing data.")
                    else:
                        st.success("✅ Answer:")
                        st.write(f"📌 {value}")
                else:
                    st.success("✅ Answer:")
                    st.dataframe(result)

            except Exception as e:
                st.error(f"❌ Error running SQL query: {str(e)}")
