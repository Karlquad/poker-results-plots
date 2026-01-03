import os

# This finds the folder where THIS file lives (The Project Root)
# This works on every computer (Windows/Mac/Linux) automatically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("adsf",BASE_DIR)


# Construct paths relative to the project root
DATA_PATH = os.path.join(BASE_DIR, "poker_data.csv")
RULES_PATH = os.path.join(BASE_DIR, "poker_rules.json")

# --- Plot Styling (from your notebook) ---
COLUMN_WIDTH_MM = 85
COLUMN_WIDTH_DBL_MM = 178
COLUMN_WIDTH_INCH = COLUMN_WIDTH_MM / 25.4
COLUMN_WIDTH_DBL_INCH = COLUMN_WIDTH_DBL_MM / 25.4

# Font Sizes
FS_TITLE = 14
FS_LABEL = 12
FS_TICK = 10

# --- Color Palette ---
# You can define standard colors here so all your plots look the same
COLOR_NET_POSITIVE = '#2ca02c'  # Green
COLOR_NET_NEGATIVE = '#d62728'  # Red