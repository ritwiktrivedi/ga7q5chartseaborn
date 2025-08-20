# chart.py
# Author: Ritwik
# Visualization: Professional-grade Seaborn Barplot
# Output: chart.png (512x512)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic business data
# -----------------------------
np.random.seed(42)  # for reproducibility

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
categories = ["North", "South", "East", "West"]

data = []
for product in products:
    for region in categories:
        sales = np.random.randint(80, 200)  # realistic range of units sold
        data.append([product, region, sales])

df = pd.DataFrame(data, columns=["Product", "Region", "Sales"])

# -----------------------------
# 2. Seaborn styling
# -----------------------------
sns.set_style("whitegrid")              # clean background
sns.set_context("talk")                 # larger labels for clarity
palette = sns.color_palette("Set2")     # professional palette

# -----------------------------
# 3. Create barplot
# -----------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches * 64 dpi = 512x512 pixels

ax = sns.barplot(
    data=df,
    x="Product",
    y="Sales",
    hue="Region",
    palette=palette,
    errorbar="sd"
)

# -----------------------------
# 4. Styling: titles, labels, legends
# -----------------------------
ax.set_title("Average Sales Performance by Product and Region",
             fontsize=16, weight="bold")
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Average Sales (Units)", fontsize=14)
ax.legend(title="Region", fontsize=10, title_fontsize=11, loc="upper right")

# -----------------------------
# 5. Export chart
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 512x512
plt.close()
