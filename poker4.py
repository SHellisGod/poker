# File 4: Opponent Behavior Modeling
# This script models opponent behavior using machine learning.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load processed poker data
def load_processed_data(file_path):
    """Loads the processed poker data."""
    return pd.read_csv(file_path)

# Prepare data for modeling
def prepare_data(data):
    """Prepares features and labels for opponent modeling."""
    # Features: hand strength, effective stack, etc.
    features = data[['hand_strength', 'effective_stack']]

    # Labels: opponent action (e.g., fold, call, raise)
    labels = data['opponent_action']

    return train_test_split(features, labels, test_size=0.2, random_state=42)

# Train a machine learning model
def train_model(X_train, y_train):
    """Trains a Random Forest model on the poker data."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluates the trained model."""
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Accuracy: {acc * 100:.2f}%")
    print("Classification Report:\n", classification_report(y_test, predictions))

if __name__ == "__main__":
    # Load and prepare data
    file_path = "processed_poker_data.csv"
    data = load_processed_data(file_path)
    X_train, X_test, y_train, y_test = prepare_data(data)

    # Train and evaluate the model
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    # Save the model (optional)
    import joblib
    joblib.dump(model, "opponent_model.pkl")
    print("Opponent behavior model saved as 'opponent_model.pkl'.")
