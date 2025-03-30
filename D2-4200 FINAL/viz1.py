import pandas as pd
import altair as alt

df = pd.read_csv("cleaned_costco_data.csv")

bar_chart = (
    alt.Chart(df)
    .mark_bar(color="#0060a9")
    .encode(
        x=alt.X("Sub Category:N", title="Product Category", sort="-y", axis=alt.Axis(labelAngle=-45)),
        y=alt.Y("count():Q", title="Number of Products"),
        tooltip=["Sub Category", "count()"]
    )
    .properties(title="Number of Products in Each Category", width=800, height=500)
)

# Save to HTML file
bar_chart.save("bar_chart.html")
