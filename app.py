"""
Grocery Sales Forecasting App - Guayaquil Stores
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import pickle
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Grocery Sales Forecasting",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🛒 Grocery Sales Forecasting</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Corporación Favorita - Guayaquil Stores | Q1 2014</div>', unsafe_allow_html=True)

# Load model registry
@st.cache_data
def load_registry():
    with open('data/model_registry.json', 'r') as f:
        return json.load(f)

registry = load_registry()

# Sidebar
st.sidebar.header("📊 Forecast Configuration")

# Store selection
stores = sorted(list(set([r['store_nbr'] for r in registry])))
selected_store = st.sidebar.selectbox(
    "Select Store",
    stores,
    format_func=lambda x: f"Store {x}"
)

# Family selection
families = [r['family'] for r in registry if r['store_nbr'] == selected_store]
selected_family = st.sidebar.selectbox(
    "Select Product Family",
    families
)

# Forecast horizon
forecast_days = st.sidebar.slider(
    "Forecast Days",
    min_value=7,
    max_value=90,
    value=90,
    step=7
)

# Load forecast
@st.cache_data
def load_forecast(store, family):
    file_path = f'data/forecast_store{store}_{family}.csv'
    return pd.read_csv(file_path, parse_dates=['date'])

forecast_df = load_forecast(selected_store, selected_family)
forecast_df = forecast_df.head(forecast_days)

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Store", f"{selected_store}")

with col2:
    st.metric("Product Family", selected_family)

with col3:
    avg_forecast = forecast_df['unit_sales'].mean()
    st.metric("Avg Daily Forecast", f"{avg_forecast:,.0f}")

with col4:
    total_forecast = forecast_df['unit_sales'].sum()
    st.metric("Total Forecast", f"{total_forecast:,.0f}")

st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 Forecast", "📊 Statistics", "📥 Data"])

with tab1:
    st.subheader("Sales Forecast Visualization")
    
    # Create plot
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=forecast_df['date'],
        y=forecast_df['unit_sales'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#ff7f0e', width=2),
        marker=dict(size=4)
    ))
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Unit Sales",
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weekly aggregation
    st.subheader("Weekly Aggregation")
    forecast_weekly = forecast_df.copy()
    forecast_weekly['week'] = forecast_weekly['date'].dt.to_period('W')
    weekly_agg = forecast_weekly.groupby('week')['unit_sales'].sum().reset_index()
    weekly_agg['week'] = weekly_agg['week'].astype(str)
    
    fig_weekly = go.Figure(data=[
        go.Bar(x=weekly_agg['week'], y=weekly_agg['unit_sales'], marker_color='steelblue')
    ])
    fig_weekly.update_layout(
        xaxis_title="Week",
        yaxis_title="Total Sales",
        height=400
    )
    st.plotly_chart(fig_weekly, use_container_width=True)

with tab2:
    st.subheader("Forecast Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Summary")
        stats_df = pd.DataFrame({
            'Metric': ['Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Total'],
            'Value': [
                f"{forecast_df['unit_sales'].mean():,.2f}",
                f"{forecast_df['unit_sales'].median():,.2f}",
                f"{forecast_df['unit_sales'].std():,.2f}",
                f"{forecast_df['unit_sales'].min():,.2f}",
                f"{forecast_df['unit_sales'].max():,.2f}",
                f"{forecast_df['unit_sales'].sum():,.2f}"
            ]
        })
        st.dataframe(stats_df, hide_index=True, use_container_width=True)
    
    with col2:
        st.markdown("### Monthly Breakdown")
        monthly_df = forecast_df.copy()
        monthly_df['month'] = monthly_df['date'].dt.strftime('%Y-%m')
        monthly_summary = monthly_df.groupby('month')['unit_sales'].agg([
            ('Total', 'sum'),
            ('Average', 'mean'),
            ('Days', 'count')
        ]).reset_index()
        st.dataframe(monthly_summary, hide_index=True, use_container_width=True)

with tab3:
    st.subheader("Forecast Data")
    
    display_df = forecast_df[['date', 'unit_sales']].copy()
    display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
    display_df.columns = ['Date', 'Forecasted Sales']
    display_df['Cumulative'] = display_df['Forecasted Sales'].cumsum()
    
    st.dataframe(display_df, hide_index=True, use_container_width=True, height=400)
    
    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name=f"forecast_store{selected_store}_{selected_family}.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p><b>Corporación Favorita - Grocery Sales Forecasting System</b></p>
    <p>Guayaquil, Guayas Province | Q1 2014 Forecast | Model: LightGBM</p>
</div>
""", unsafe_allow_html=True)
