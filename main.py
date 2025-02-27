import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

def main():
    st.title("Market Research Bot")
    st.write("Upload a CSV file to analyze market trends.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.write("### Data Preview:")
        st.dataframe(df.head())
        
        st.write("### Basic Statistics:")
        st.write(df.describe())
        
        numeric_columns = df.select_dtypes(include=['number']).columns
        if len(numeric_columns) > 0:
            st.write("### Data Visualization:")
            selected_col = st.selectbox("Select a column to visualize", numeric_columns)
            
            fig, ax = plt.subplots()
            df[selected_col].hist(ax=ax, bins=20)
            ax.set_title(f"Distribution of {selected_col}")
            st.pyplot(fig)
        
        search_term = st.text_input("Search for a product or keyword:")
        if search_term:
            filtered_df = df[df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)]
            st.write("### Search Results:")
            st.dataframe(filtered_df)
        
        st.write("### Advanced Analysis:")
        if st.checkbox("Show Correlation Matrix"):
            st.write(df.corr())
        
        if st.checkbox("Show Missing Values"):
            st.write(df.isnull().sum())
        
        if st.checkbox("Show Top Categories"):
            category_column = st.selectbox("Select a categorical column", df.select_dtypes(include=['object']).columns)
            st.write(df[category_column].value_counts().head(10))

if __name__ == "__main__":
    main()
