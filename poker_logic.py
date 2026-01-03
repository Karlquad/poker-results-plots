import pandas as pd
import json


def load_config(path):
    """
    Loads the rules from a JSON file and converts string keys back to integers.
    """
    with open(path, 'r') as f:
        # We convert keys back to integers because JSON keys are always strings in JSON
        return {int(k): v for k, v in json.load(f).items()}


def load_data(path):  # <--- Add 'path' here
    return pd.read_csv(path)


def compute_net(df, year, all_rules):
    # Filter data for the specific year
    year_df = df[df['Year'] == year].copy()
    r = all_rules[year]

    # Calculation logic remains the same
    year_df['Cost'] = (r['buyin'] + r['bounty'] +
                       year_df['Rebuy'] * r['rebuy_cost'] +
                       year_df['Addon'] * r['addon_cost'])

    # Map payouts (ensure rank is treated as string for dict lookup if needed)
    payouts = {int(k): v for k, v in r['payouts'].items()}
    year_df['Winnings'] = year_df['Rank'].map(payouts).fillna(0)
    year_df['Bounty_Earned'] = year_df['Knockouts'] * r['ko_value']
    year_df['Net_Earnings'] = year_df['Winnings'] + year_df['Bounty_Earned'] - year_df['Cost']

    return year_df