import pandas as pd
import numpy as np
import gradio as gr
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR

# Load your cleaned data (weekly price data from 2021 to 2025)
df = pd.read_csv("df_clean.csv", index_col=0, parse_dates=True)

# Resample to weekly frequency and drop missing
weekly_df = df.resample("W").last().dropna()

# Differencing to make stationary
df_diff = weekly_df.diff().dropna()

# Fit model once globally
model = VAR(df_diff)
model_fit = model.fit(20)  # use optimal lag identified earlier

# Forecasting function
def forecast_VAR(n_forecast, assets):
    forecast = model_fit.forecast(model_fit.endog, steps=n_forecast)
    forecast_index = pd.date_range(df.index[-1], periods=n_forecast + 1, freq="W")[1:]

    forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=df.columns)

    # Convert from differenced values to actual forecast
    last_values = weekly_df.iloc[-1]
    forecast_cumsum = forecast_df.cumsum()
    forecast_values = forecast_cumsum.add(last_values)

    # Plot selected assets
    plt.figure(figsize=(12, 6))
    for col in assets:
        plt.plot(weekly_df[col][-12:], label=f"Actual {col}")
        plt.plot(forecast_values[col], linestyle="--", label=f"Forecast {col}")

    plt.title("Forecast from VAR Model")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.tight_layout()
    
    # Return plot and forecast table
    return plt, forecast_values[assets]

# Gradio UI
def gradio_interface(n_forecast, bitcoin, gold, sp500):
    selected_assets = []
    if bitcoin:
        selected_assets.append("Bitcoin")
    if gold:
        selected_assets.append("Gold")
    if sp500:
        selected_assets.append("S&P500")

    fig, table = forecast_VAR(n_forecast, selected_assets)
    return fig, table

with gr.Blocks() as demo:
    gr.Markdown("## VAR-Based Forecasting for Bitcoin, Gold, and S&P 500")

    with gr.Row():
        n_weeks = gr.Dropdown(choices=list(range(4, 13)), label="Weeks to Forecast", value=4)
        bitcoin = gr.Checkbox(label="Bitcoin", value=True)
        gold = gr.Checkbox(label="Gold", value=True)
        sp500 = gr.Checkbox(label="S&P500", value=True)

    with gr.Row():
        plot_output = gr.Plot(label="Forecast Plot")
        table_output = gr.Dataframe(label="Forecast Table")

    btn = gr.Button("Generate Forecast")
    btn.click(fn=gradio_interface, inputs=[n_weeks, bitcoin, gold, sp500], outputs=[plot_output, table_output])

# Launch app
demo.launch()
