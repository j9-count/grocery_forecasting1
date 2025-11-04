# Grocery Sales Forecasting - Streamlit App

## Corporación Favorita Sales Forecasting
Interactive forecasting application for Guayaquil stores, deployed on Streamlit Cloud.

**🌐 Live App:** [Your App URL Here](https://your-app.streamlit.app)

---

##  Features

- **Interactive Forecasting**: Select store and product family combinations
- **Customizable Horizon**: Choose forecast length (7-90 days)
- **Visual Analytics**: Interactive line charts and weekly aggregations
- **Detailed Statistics**: Summary metrics and monthly breakdowns
- **Export**: Download forecasts as CSV for further analysis

---

##  Project Overview

- **Forecast Period**: January - March 2014 (Q1 2014)
- **Location**: Guayaquil, Guayas Province, Ecuador
- **Model**: LightGBM with engineered features
- **Deployment**: Streamlit Cloud

---

##  Model Performance

**Best Model:** LightGBM Gradient Boosting

- **MAE**: 750-1,000 units (varies by store-family combination)
- **Features Used**: 
  - Lag features (1, 7, 14, 28 days)
  - Rolling statistics (mean, std, min, max)
  - Holiday indicators
  - Payday effects (15th and last day of month)
  - Oil prices
  - Promotional activities
  - Transaction counts

**Model Comparison:**
- Naive Seasonal Baseline: Benchmark model
- Prophet (Facebook): Good for interpretability
- **LightGBM**: Best accuracy (Production model) 

---

##  Deployment

###  Streamlit Cloud 

**Live App:** Deployed at [share.streamlit.io](https://share.streamlit.io)



---

## 💻 Local Development

Want to run this app locally? Follow these steps:

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/grocery_forecasting1.git
cd grocery_forecasting1
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run app.py
```

4. **Open browser:**
Navigate to http://localhost:8501

---

##  Project Structure
```
grocery_forecasting1/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
│
├── data/                    # Data files (forecasts & configs)
│   ├── model_registry.json  # Model metadata
│   ├── forecast_metadata.json
│   ├── selected_combinations.json
│   └── forecast_store*.csv  # Pre-generated forecasts
│
└── models/                  # Trained ML models 
    ├── lgb_store*.pkl       # LightGBM models
    └── config_store*.json   # Model configurations
```

---

##  How to Use the App

### 1. Select Store
Choose from available Guayaquil stores (Store 44, 45, 47, etc.)

### 2. Select Product Family
Pick a product category (GROCERY, BEVERAGES, CLEANING, etc.)

### 3. Set Forecast Horizon
Use the slider to select how many days to forecast (7-90 days)

### 4. View Results
- **Forecast Tab**: Interactive time series visualization
- **Statistics Tab**: Summary metrics and monthly breakdown
- **Data Tab**: Detailed daily forecasts with download option

### 5. Download Forecasts
Click the "Download Forecast CSV" button to export data

---

##  Technical Stack

**Frontend:**
- Streamlit 1.29.0
- Plotly 5.18.0 (interactive charts)

**Data Processing:**
- Pandas 2.1.4
- NumPy 1.26.2

**Machine Learning:**
- LightGBM 4.1.0 (if models included)
- Scikit-learn 1.3.2

**Deployment:**
- Streamlit Cloud (Free tier)
- GitHub (Version control)

---

##  Data Sources

- **Historical Sales Data**: Corporación Favorita (Kaggle competition)
- **Training Period**: 2013 full year
- **Stores**: Guayaquil, Guayas Province locations only
- **Products**: Multiple product families across stores

**External Factors:**
- Ecuador oil prices (dcoilwtico)
- Holiday calendar (national & regional)
- Transaction counts
- Promotional activities

---

##  Updates & Maintenance

### Automated Deployment
- Any push to `main` branch triggers automatic redeployment
- Streamlit Cloud rebuilds the app (~2-3 minutes)

### Manual Updates
1. Make changes locally
2. Commit and push to GitHub
3. Streamlit Cloud auto-deploys

### Model Updates
To update forecasts with new data:
1. Retrain models with updated data
2. Generate new forecasts
3. Replace files in `data/` folder
4. Push to GitHub

---

##  Known Limitations

- **Forecast Period**: Currently limited to Jan-Mar 2014
- **Historical Data**: Based on 2013 data only
- **Model Size**: Large model files may be stored externally (Google Drive)
- **Free Tier**: Subject to Streamlit Cloud resource limits

---

##  Contributing

This is a demonstration project for a time series forecasting system. 

**Potential Improvements:**
- Add more store-family combinations
- Implement real-time forecasting
- Add confidence intervals
- Include model retraining pipeline
- Add user authentication

---

##  Support & Contact

**Issues?** 
- Check the [GitHub Issues](https://github.com/YOUR-USERNAME/grocery_forecasting1/issues)
- Review Streamlit Cloud logs (Manage App → Logs)

**Questions?**
- Email: your.email@example.com
- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

---

##  License

This project is for educational and demonstration purposes.

**Data Source:** Corporación Favorita Grocery Sales Forecasting (Kaggle)

---

##  Acknowledgments

- **Corporación Favorita** for the dataset
- **Streamlit** for the amazing framework
- **LightGBM** for the powerful ML library
- Demand planners in Guayaquil for inspiration

---

## 🔗 Quick Links

- **Live App**: [Your Streamlit App URL](https://your-app.streamlit.app)
- **GitHub Repo**: [grocery_forecasting1](https://github.com/YOUR-USERNAME/grocery_forecasting1)
- **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
- **Documentation**: See project notebooks 

---

**Version:** 1.0.0  
**Last Updated:** November 2024  
**Status:** 🟢 Active & Deployed

---

Built with ❤️ for demand planners in Guayaquil, Ecuador
"""
