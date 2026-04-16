import streamlit as st
import pandas as pd
import plotly.express as px

# 1 Page settings
st.set_page_config(page_title="Vehicle Analyzer", layout="wide")

# 2. Loading and cleaning function with cache


@st.cache_data
def load_and_clean_data():
    try:
        df = pd.read_csv('vehicles_us.csv')

        # Limpieza básica
        df['odometer'] = df['odometer'].fillna(df['odometer'].median())
        df['model_year'] = df['model_year'].fillna(0).astype(int)
        df['brand'] = df['model'].apply(
            lambda x: str(x).split()[0].capitalize())

        return df
    except FileNotFoundError:
        st.error(
            "¡Ups! No encontré el archivo 'vehicles_us.csv'. Revisa si el nombre está bien escrito.")
        return None


df = load_and_clean_data()

# 3. Sidebar for interactivity
st.sidebar.header("Comparison Options")
available_brands = sorted(df['brand'].unique())
selected_brands = st.sidebar.multiselect(
    "Select brands to compare:",
    options=available_brands,
    default=available_brands[:3]
)

# 4. Data filtering

df_filtered = df[df['brand'].isin(selected_brands)]
# Special DataFrame for time-dependent visualizations (avoids year 0)
df_visualization = df_filtered[df_filtered['model_year'] > 0]

# 5. Main header
st.title('Exploratory Analysis of Vehicle Data')
st.write("Analyze the relationship between price, mileage, and model year by brand.")

# --- GRAPHICS SECTION ---

col1, col2 = st.columns(2)

with col1:
    # Bar chart: Average price per brand
    st.subheader('Average Price per Brand')
    avg_price = df_filtered.groupby('brand')['price'].mean().reset_index()
    fig_bar = px.bar(
        avg_price,
        x='brand',
        y='price',
        color='brand',
        title="Average Price per Selection",
        labels={'price': 'Average Price ($)', 'brand': 'Brand'}
    )
    st.plotly_chart(fig_bar, width='stretch')

with col2:
    # Line chart: Evolution of prices by year
    st.subheader('Evolution of Prices by Year')
    if not df_visualization.empty:
        avg_price_year = df_visualization.groupby(
            'model_year')['price'].mean().reset_index()
        fig_line = px.line(
            avg_price_year,
            x='model_year',
            y='price',
            title="Historical Price Trends",
            labels={'model_year': 'Model Year',
                    'price': 'Average Price ($)'}
        )
        st.plotly_chart(fig_line, width='stretch')
    else:
        st.info("There is no year data for these brands.")

# Scatter plot at the bottom (full width)
st.divider()
st.subheader('Relationship: Mileage vs. Price')
fig_scatter = px.scatter(
    df_visualization,
    x='odometer',
    y='price',
    color='brand',
    hover_data=['model', 'model_year'],
    title="Depreciation Analysis: Mileage vs. Price",
    labels={'odometer': 'Mileage', 'price': 'Price ($)'}
)
st.plotly_chart(fig_scatter, width='stretch')
