# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import time
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load Dataset

df = pd.read_csv("order_products__prior.csv")

# Transform Transactions

products_df = pd.read_csv("products.csv")
df_merged = pd.merge(df, products_df[['product_id', 'product_name']], on='product_id', how='left')

transactions = df_merged.groupby('order_id')['product_name'].apply(list).values.tolist()

print("Total Transactions", len(transactions))

# One Hot Encoding Basket

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket = pd.DataFrame(te_array, columns=te.columns_)

# Apriori Itemsets

start = time.time()
apriori_itemsets = apriori(basket, min_support=0.002, use_colnames=True)
apriori_time = time.time() - start
print("Apriori done in:", apriori_time)
apriori_itemsets.head()

# Association Rules

rules = association_rules(apriori_itemsets, metric="lift", min_threshold=1)
print("Association rules", rules.shape)
print(rules.sort_values("confidence", ascending=False).head(10))

# Filter Strong Rules

rules_filtered = rules[(rules["confidence"] >= 0.5) & (rules["lift"] > 1.2)]
print("Strong rules:", rules_filtered.shape)
print(rules_filtered.sort_values("lift", ascending=False).head(10))

# Network Graph

G = nx.DiGraph()
top_rules = rules_filtered.sort_values("lift", ascending=False).head(15)

for _, row in top_rules.iterrows():
    for a in row["antecedents"]:
        for c in row["consequents"]:
            G.add_edge(a, c, weight=row["lift"])

communities = greedy_modularity_communities(G)

communities = [list(c) for c in communities]

color_map = {}
colors = cm.Set2(range(len(communities)))

for color, community in zip(colors, communities):
    for node in community:
        color_map[node] = color

node_colors = [color_map[node] for node in G.nodes()]

pos = nx.spring_layout(G, k=1.4, iterations=120, seed=42)

node_sizes = [basket[node].sum() * 10 for node in G.nodes()]
edge_widths = [G[u][v]["weight"] * 1.2 for u, v in G.edges()]

plt.figure(figsize=(12, 8))

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)
nx.draw_networkx_labels(
    G, pos, font_size=8, bbox=dict(facecolor="white", edgecolor="none", alpha=0.7)
)
nx.draw_networkx_edges(G, pos, width=edge_widths, arrows=False, edge_color="green")

plt.title("Product Association Network")
plt.axis("off")
plt.show()

plt.savefig("product_association_network.png", dpi=300, bbox_inches="tight")
