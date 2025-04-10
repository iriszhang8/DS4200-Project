import pandas as pd
import altair as alt

# Load the data
df = pd.read_csv("cleaned_costco_data.csv")
# Map subcategories to categories
category_mapping = {
    "Bakery & Desserts": "Food",
    "Breakfast": "Food",
    "Candy": "Food",
    "Deli": "Food",
    "Meat & Seafood": "Food",
    "Pantry & Dry Goods" : "Food",
    "Poultry": "Food",
    "Seafood": "Food",
    "Snacks": "Food",
    "Organic": "Food",
    "Kirkland Signature Grocery": "Food",
    "Beverages & Water": "Beverages",
    "Coffee": "Beverages",
    "Cleaning Supplies": "Household",
    "Laundry Detergent & Supplies": "Household",
    "Paper & Plastic Products": "Household",
    "Household": "Household",
    "Gift Baskets": "Other",
    "Floral": "Other"
}

# Add the new category column
df["Category"] = df["Sub Category"].map(category_mapping)
# Bar chart showing the number of products in each category
custom_colors = {
    "Food": "#0060a9",
    "Beverages": "#e32a36",
    "Household": "green",
    "Other": "orange"
}

bar_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Sub Category:N", title="Product Sub Category", sort="-y", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("count():Q", title="Number of Products"),
        color=alt.Color("Category:N", title="Category", scale=alt.Scale(domain=list(custom_colors.keys()), range=list(custom_colors.values()))),
        tooltip=["Category", "Sub Category", "count()"]
    )
    .properties(title="Number of Products in Each Sub Category, by Category", width=800, height=500)
)

bar_chart
# Save to HTML file
bar_chart.save("bar_chart.html")
