# File 5: Expected Value (EV) Calculator for Poker Decisions
# This script calculates the expected value (EV) of poker decisions based on input scenarios.
import pandas as pd

# Calculate EV for a specific decision
def calculate_ev(win_probability, pot_size, bet_amount):
    """Calculates the expected value (EV) of a decision.
    EV = (Win Probability * Pot Size) - (Lose Probability * Bet Amount)
    """
    lose_probability = 1 - win_probability
    ev = (win_probability * pot_size) - (lose_probability * bet_amount)
    return ev

# Evaluate multiple decisions

def evaluate_decisions(decision_scenarios):
    """Evaluates EV for multiple decisions and returns a DataFrame of results."""
    results = []
    for scenario in decision_scenarios:
        ev = calculate_ev(scenario['win_probability'], scenario['pot_size'], scenario['bet_amount'])
        results.append({
            'Decision': scenario['decision'],
            'Win Probability': scenario['win_probability'],
            'Pot Size': scenario['pot_size'],
            'Bet Amount': scenario['bet_amount'],
            'Expected Value (EV)': ev
        })
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Example decision scenarios
    decision_scenarios = [
        {'decision': 'Call', 'win_probability': 0.5, 'pot_size': 100, 'bet_amount': 50},
        {'decision': 'Raise', 'win_probability': 0.7, 'pot_size': 100, 'bet_amount': 80},
        {'decision': 'Fold', 'win_probability': 0.0, 'pot_size': 100, 'bet_amount': 0},
    ]

    # Evaluate decisions
    results = evaluate_decisions(decision_scenarios)
    
    # Display results
    print(results)
    
    # Save results to CSV
    results.to_csv("decision_ev_results.csv", index=False)
    print("EV results saved to 'decision_ev_results.csv'.")
