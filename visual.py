import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dashboard_page():
    st.title("Customer Churn Dashboard Page")
    
    # Load the data
    data = pd.read_csv("data/traindata.csv")

    # Data Overview
    st.header("Data Overview")
    st.write("Here is a quick summary of the dataset")
    st.dataframe(data.head())

    # Calculate KPIs
    total_customers = len(data)
    churn_rate = round((data['Churn'].value_counts().iloc[1] / total_customers) * 100, 2)
    avg_tenure = round(data['tenure'].mean(), 2)

    # Display KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Customers", total_customers)
    with col2:
        st.metric("Churn Rate", f"{churn_rate}%")
    with col3:
        st.metric("Average Tenure", f"{avg_tenure} months")

    # Interactive Scatter Plot
    st.subheader("Interactive Visualization")
    variable = st.selectbox("Select a variable", options=["tenure", "MonthlyCharges", "TotalCharges"])

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=variable, y="TotalCharges", hue="Churn", data=data, palette="coolwarm")
    plt.title(f"Total Charges vs. {variable} by Churn Status")
    st.pyplot(plt)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    corr = data[["tenure", "MonthlyCharges", "TotalCharges"]].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation of Key Features")
    st.pyplot(plt)

    # Violin Plot of Churn vs Total Charges
    st.subheader("Total Charges by Churn Status")
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="Churn", y="TotalCharges", data=data, palette="muted", split=True)
    plt.title("Distribution of Total Charges by Churn Status")
    st.pyplot(plt)

    # Countplot for Internet Service
    st.subheader("Internet Service Types Distribution")
    plt.figure(figsize=(8, 5))
    sns.countplot(x="InternetService", data=data, palette="viridis")
    plt.title("Distribution of Internet Service Types")
    st.pyplot(plt)

    # Scatter Plot of Tenure vs Monthly Charges
    st.subheader("Monthly Charges vs Tenure by Churn Status")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="tenure", y="MonthlyCharges", hue="Churn", data=data, palette="coolwarm")
    plt.title("Monthly Charges vs. Tenure by Churn Status")
    st.pyplot(plt)

    # Boxplot of Tenure by Contract Type
    st.subheader("Tenure Distribution by Contract Type")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Contract", y="tenure", data=data, palette="coolwarm")
    plt.title("Tenure by Contract Type")
    st.pyplot(plt)

# Call the dashboard function
if __name__ == "__main__":
    dashboard_page()
