# poker
poker equity data analytics
Integration Workflow

Data Preparation:

Use poker_data_preprocessing.py to clean and preprocess raw data. This step ensures data quality for subsequent analysis.

Probability Calculation:

Run poker_win_probability.py to compute win probabilities for specific scenarios or hands.

Visualization:

Use poker_visualization_ui.py to explore the data and insights through an interactive dashboard.

Opponent Behavior Modeling:

Train the opponent action prediction model using opponent_modeling.py.

Save the trained model for deployment in real-time decision-making systems.

Decision Evaluation:

Use poker_ev_calculator.py to calculate the EV of different decisions and assess profitability.

Example Usage Scenario

Preprocess a poker hand history dataset (raw_poker_data.csv) using poker_data_preprocessing.py.

Calculate win probabilities for a specific hand using poker_win_probability.py.

Visualize the processed data and probabilities using poker_visualization_ui.py.

Train a model to predict opponents' actions using opponent_modeling.py.

Evaluate the profitability of potential moves with poker_ev_calculator.py.
