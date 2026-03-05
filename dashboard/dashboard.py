import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Food Delivery Customer Satisfaction Analysis")


df = pd.read_csv('data/processed/delivery_master_clean.csv')

#question 1: At what specific minute do customers get angry about waiting for their food?
grouped_real = df.groupby('Delivery Duration (in minutes)')['Realistic Rating Order Time'].mean()
st.header("At what specific minute do customers get angry about waiting for their food?")
fig1, ax1 = plt.subplots()
ax1.plot(grouped_real.index, grouped_real.values, marker='o')
ax1.set_xlabel('Delivery Duration (in minutes)')
ax1.set_ylabel('Average Rating')
ax1.set_title('Average Rating vs. Delivery Duration')
ax1.grid(True)
st.pyplot(fig1)

#question 2: Which cities have the most problems?
grouped_cities = df.groupby('Order_City')['Customer_Rating_Cities'].mean().sort_values()
st.header("Which cities have the most problems?")
fig2, ax2 = plt.subplots()
ax2.bar(grouped_cities.index, grouped_cities.values, color='tomato')
ax2.set_xlabel('City')
ax2.set_ylabel('Average Rating')
ax2.set_title('Average Rating by City')
plt.xticks(rotation=45)
st.pyplot(fig2)

# question 3: Which restaurants have the most problems?
grouped_restaurants = df.groupby('Restaurant Type')['Customer_Rating_Restaurants'].mean().sort_values(ascending=True)
st.header("Which restaurants have the most problems?")
fig3, ax3 = plt.subplots()
ax3.bar(grouped_restaurants.index, grouped_restaurants.values, color='lightblue')
ax3.set_xlabel('Restaurant Type')
ax3.set_ylabel('Average Rating')
ax3.set_title('Average Rating by Restaurant Type')
plt.xticks(rotation=45)
st.pyplot(fig3)

#question 4: At what time are customers most likely to be less tolerant of longer delivery times?
df['Order_Hour'] = pd.to_datetime(df['Order Date and Time']).dt.hour
grouped_order_time = df.groupby('Order_Hour')['Customer_Rating_Order_Time'].mean().sort_values()
st.header("At what time are customers most likely to be less tolerant of longer delivery times?")
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(grouped_order_time.index, grouped_order_time.values, marker='o', color='royalblue')
ax.set_xlabel('Order Hour')
ax.set_ylabel('Average Rating')
ax.set_title('Average Rating by Order Hour')
ax.grid(True)
plt.xticks(grouped_order_time.index)
st.pyplot(fig)

#question 5: Does the amount of money spent on the order influence customers' tolerance for long delivery waits?

#plotting a scatter plot to visualize the relationship between total bill and customer rating for money spent
st.header("Does the amount of money spent on the order influence customers' tolerance for long delivery waits?")
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Total Bill (in Saudi Riyals)'], df['Customer_Rating_Money_Spent'], alpha=0.5, color='teal')
ax.set_xlabel('Total Bill (in Saudi Riyals)')
ax.set_ylabel('Customer Rating Money Spent')
ax.set_title('Customer Rating vs. Total Bill')
ax.grid(True)
st.pyplot(fig)

#plotting a line plot to show the average rating for money spent across different total bill ranges
df['Bill_Range'] = pd.cut(df['Total Bill (in Saudi Riyals)'], bins=10)
grouped = df.groupby('Bill_Range')['Customer_Rating_Money_Spent'].mean()
st.header("Average Rating by Total Bill Range")
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(grouped.index.astype(str), grouped.values, marker='o', color='orange')
ax.set_xlabel('Total Bill Range (in Saudi Riyals)')
ax.set_ylabel('Average Rating')
ax.set_title('Average Rating by Total Bill Range')
plt.xticks(rotation=45)
ax.grid(True)
st.pyplot(fig)

# Conclusions Section
st.header("Key Insights and Conclusions")

st.markdown("""
**1) At what specific minute do customers get angry about waiting for their food?**

Based on the line chart, we observe that customer ratings begin to drop significantly after the 16th minute of delivery duration. However, it is important to note that the dataset is synthetic and was engineered so that lower ratings correspond to longer delivery times. This trend should be validated with real-world data for more accurate business decisions.

**2) Which cities have the most problems?**

The analysis shows no significant differences in average customer ratings across cities. This lack of variability is likely due to the synthetic nature of the data, which does not reflect real operational challenges or customer satisfaction differences between locations.

**3) Which restaurants have the most problems?**

Similarly, the average ratings for restaurant types are nearly identical, indicating no particular restaurant type stands out as problematic. Again, this is a limitation of working with synthetic data, and real data may reveal more actionable insights.

**4) At what time are customers most likely to be less tolerant of longer delivery times?**

The chart suggests that customers tend to be less tolerant of longer delivery times in the morning, particularly around 8 AM. This insight could help operations teams prioritize efficiency during peak morning hours to improve customer satisfaction.

**5) Does the amount of money spent on the order influence customers' tolerance for long delivery waits?**

Two visualizations were used to explore this question. The scatter plot shows that customer ratings are distributed horizontally, with no clear relationship between the amount spent and the rating. The line chart of average ratings by bill range also reveals no trend or pattern. Therefore, we conclude that the amount spent on an order does not influence customer tolerance for delivery duration in this dataset.
""")

