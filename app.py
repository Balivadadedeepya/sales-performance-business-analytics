import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Performance Business Analytics")
st.write("Upload your sales CSV file to explore business performance and generate insights.")

uploaded_file = st.file_uploader(
    "📁 Upload Sales Data",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Sales data loaded successfully!")

    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Identify common columns
    sales_column = next(
        (col for col in df.columns if col.lower() in ["sales", "revenue", "amount"]),
        None
    )

    profit_column = next(
        (col for col in df.columns if col.lower() == "profit"),
        None
    )

    # Key metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("📦 Total Records", len(df))

    if sales_column:
        col2.metric(
            "💰 Total Sales",
            f"{df[sales_column].sum():,.2f}"
        )

        col3.metric(
            "📈 Average Sales",
            f"{df[sales_column].mean():,.2f}"
        )

    if profit_column:
        st.metric(
            "💵 Total Profit",
            f"{df[profit_column].sum():,.2f}"
        )

    # Sales distribution
    if sales_column:
        st.subheader("📊 Sales Distribution")

        fig = px.histogram(
            df,
            x=sales_column,
            title="Sales Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Profit analysis
    if sales_column and profit_column:
        st.subheader("💰 Sales vs Profit")

        fig = px.scatter(
            df,
            x=sales_column,
            y=profit_column,
            title="Sales vs Profit"
        )

        st.plotly_chart(fig, use_container_width=True)

    # Automatic insights
    st.subheader("💡 Business Insights")

    if sales_column:
        highest_sale = df[sales_column].max()
        average_sale = df[sales_column].mean()

        st.write(
            f"• Highest recorded sale: **{highest_sale:,.2f}**"
        )

        st.write(
            f"• Average sale value: **{average_sale:,.2f}**"
        )

    if profit_column:
        total_profit = df[profit_column].sum()

        if total_profit > 0:
            st.success("📈 Overall profit is positive.")
        elif total_profit < 0:
            st.warning("⚠️ Overall profit is negative.")
        else:
            st.info("Profit is currently at break-even.")

else:
    st.info("👆 Upload a CSV file to start analyzing sales performance.")
