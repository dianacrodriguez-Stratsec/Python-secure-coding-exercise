
📊 Superstore Data Visualization Project
Analysis of the superstore_dataset2012.csv dataset using Pandas, Matplotlib, and Seaborn.

🎯 Project Objectives
Load and explore the dataset.

Perform univariate, bivariate, and multivariate visualizations.

Create a Matplotlib figure with four subplots.

Save at least one visualization as an image file.

Provide conclusions based on the visual analysis.

📁 Project Structure
Código
visualizacion_superstore/
│
├── visualizacion_superstore.ipynb
├── superstore_dataset2012.csv
├── figuras/
│   ├── heatmap_correlaciones_superstore.png
│   ├── subplots_superstore.png
│   ├── histograma_ventas.png
│   └── dispersion_ventas_beneficio.png
└── README.md
📈 Visualizations Included
🔹 1. Sales Histogram
Univariate visualization using Matplotlib.

🔹 2. Profit Boxplot by Category
Univariate visualization using Seaborn.

🔹 3. Sales vs Profit Scatter Plot
Bivariate visualization using Matplotlib.

🔹 4. Regression Plot (Sales vs Profit)
Bivariate visualization using Seaborn.

🔹 5. Correlation Heatmap
Multivariate visualization using Seaborn.
📁 Saved as: figuras/heatmap_correlaciones_superstore.png

🔹 6. Four-Panel Subplot Figure
Matplotlib figure containing histogram, boxplot, scatter plot, and bar chart.
📁 Saved as: figuras/subplots_superstore.png

🧠 Key Insights
There is a positive correlation between Sales and Profit, indicating that higher sales generally lead to higher profitability.

Product quantity does not strongly correlate with profit, suggesting that selling more units does not always guarantee higher earnings.

Category-level analysis shows that high sales categories are not always the most profitable.

The heatmap provides a clear overview of relationships between numerical variables.

The subplot figure offers a consolidated view of the dataset’s behavior across multiple dimensions.

🔐 ISO 27001 vs DORA Mapping Table
Professional compliance-style table aligned with your cybersecurity background.

🛠 Technologies Used
Python 3.x

Pandas

Matplotlib

Seaborn

Jupyter Notebook
