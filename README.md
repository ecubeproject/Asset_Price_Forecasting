# 📈 Asset Price Forecasting using VAR

A web-based forecasting application built with **Gradio** and powered by a **Vector Autoregression (VAR)** model.  
It forecasts future prices of **Bitcoin**, **Gold**, and the **S&P 500** based on historical weekly data.

---

## 🚀 Live Demo

[![Gradio App](https://img.shields.io/badge/Launch-App-blue)](https://huggingface.co/spaces/your-username/Asset_Price_Forecasting)

---

## 🧠 Features

- VAR-based multivariate time series forecasting
- Choose forecasting horizon from 4 to 12 weeks
- Select any combination of assets: Bitcoin, Gold, and S&P 500
- Forecast plot with **95% confidence intervals**
- Forecast table available for export
- Built with Gradio UI for interactivity

---

## 📊 Dataset

| Asset     | Source                     | Ticker     | Date Range           |
|-----------|----------------------------|------------|----------------------|
| Bitcoin   | [Yahoo Finance](https://finance.yahoo.com) | `BTC-USD`   | Jan 1, 2021 – May 31, 2025 |
| Gold      | [Yahoo Finance](https://finance.yahoo.com) | `GC=F`      | Jan 1, 2021 – May 31, 2025 |
| S&P 500   | [Yahoo Finance](https://finance.yahoo.com) | `^GSPC`     | Jan 1, 2021 – May 31, 2025 |

All data was manually downloaded due to API limitations and resampled to **weekly frequency**.

---

## 🛠️ Tech Stack

| Layer          | Tool / Library            |
|----------------|---------------------------|
| Frontend UI    | Gradio                    |
| Modeling       | statsmodels (VAR)         |
| Data Handling  | pandas, numpy             |
| Visualization  | matplotlib                |
| Deployment     | Hugging Face Spaces (Gradio) |

---

## 🧩 Future Enhancements

- 🔁 **Forecast-based lag optimization** (grid search using out-of-sample accuracy)
- 🤖 **Compare VAR with VECM, LSTM, or Prophet**
- 💡 **Add macroeconomic indicators** like:
  - Interest rates
  - VIX (volatility index)
  - Federal Reserve policy variables
- 📦 Deploy as **Dockerized microservice** for production use

---

## 📌 Instructions

### ▶️ Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/Asset_Price_Forecasting.git
   cd Asset_Price_Forecasting

2. Install dependencies
   pip install -r requirements.txt
3. Run the app
   python app.py
🙋 Author
Your Name: Tejas Desai
Feel free to connect: LinkedIn: https://www.linkedin.com/in/tejasddesaiindia/          GitHub:https://github.com/ecubeproject/

---

📜 License

MIT License © 2025
