# File 3: Poker Data Visualization Dashboard
# This script creates a Streamlit-based dashboard to visualize poker analytics.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_processed_data(file_path):
    """Loads the processed poker data."""
    return pd.read_csv(file_path)

def plot_hand_strength_distribution(data):
    """Plots the distribution of hand strengths."""
    plt.figure(figsize=(10, 6))
    plt.hist(data['hand_strength'], bins=30, alpha=0.7, color='blue')
    plt.title('Hand Strength Distribution')
    plt.xlabel('Hand Strength')
    plt.ylabel('Frequency')
    st.pyplot(plt)

def visualize_win_probability(data):
    """Plots win probabilities for selected scenarios."""
    st.write("Win Probability Simulation")
    st.write(data[['hand_strength', 'effective_stack']])

def main():
    st.title("Poker Data Analytics Dashboard")

    # Load data
    file_path = "processed_poker_data.csv"
    data = load_processed_data(file_path)

    # Hand Strength Distribution
    st.header("Hand Strength Distribution")
    plot_hand_strength_distribution(data)

    # Win Probability Visualization
    st.header("Win Probability Simulation")
    visualize_win_probability(data)

if __name__ == "__main__":
    main()
