# Operational Analysis of Food Delivery in Saudi Arabia

🚀 **[Click here to view the Interactive Streamlit Dashboard](https://operational-analysis-of-food-delivery-bmpfhr2jrxmpgutpdjlxuu.streamlit.app/)**

## Project Overview
This project aims to provide actionable insights into the operational performance of a food delivery service in Saudi Arabia. The analysis focuses on understanding customer satisfaction, delivery times, and identifying potential areas for improvement in the delivery process. The results are presented in an interactive dashboard to facilitate decision-making for operations teams and business stakeholders.

## Purpose
The main goal is to answer key business questions that help optimize delivery operations and enhance customer experience. Although the dataset used is synthetic, the methodology and analytical approach are designed to be applicable to real-world scenarios.

## Data Availability
The dataset used in this project is synthetic and is included in the repository. It contains realistic food delivery records, but does not represent real customer information. The file size is small (486 KB), making it easy to download and reproduce the analysis. You can find the data in the `data/raw/` folder.

## Tools and Technologies
- **Pandas**: Data manipulation and aggregation
- **Matplotlib**: Data visualization
- **Streamlit**: Interactive dashboard development
- **Jupyter Notebook**: Exploratory data analysis and prototyping

## 💡 Key Business Insights
Instead of simply asking questions, this project revealed practical operational metrics:

1. **The Wait Time Critical Point:** It was discovered that customer tolerance plummets after **16 minutes**, where average ratings drop from **4.75 stars to 3 stars**. (Note: Because the original synthetic dataset lacked a logical correlation between delivery duration and customer satisfaction, this metric was simulated using a custom Python function to apply real-world business logic and demonstrate feature engineering capabilities).

2. **Geographic Bottlenecks:** No single city was identified as the most problematic area, as all cities had roughly the same average rating. (Note: This perfect uniformity is likely an artifact of the synthetic nature of the data generation process)

3. **Restaurant Type Performance:** No single restaurant type was found to have more issues with delivery times, as all restaurant types had roughly the same average rating. This may be due to the synthetic nature of the data. (Note: Similar to geography, this lack of variance is likely due to the dataset's synthetic nature).

4. **Time Sensitivity:** Data indicates that customers who place orders at **8:00 AM** and **10:00 PM** are significantly less tolerant of delays, which directly impacts their ratings.

5. **Value vs. Patience:** Analysis revealed that higher-value orders **do not show greater or lesser tolerance** for delivery delays compared to lower-value orders. (Note: Attributed to the uniform random distribution in the synthetic dataset).

## Sample Results
Below are some sample charts generated during the analysis:

![Average Rating by Order Hour](images/average_rating_hour.png)
*Figure 1. Distribution of delivery times by hour. This graph shows the times when customers are least likely to wait longer to receive food delivery.*

![Customer Rating vs Total Bill](images/rating_total_bill.png)
*Figure 2. Distribution of customer ratings in relation to total bill. This chart shows if there is any relationship between customer rating and delivery cost*

## How to Use
- All data processing and analysis are performed in Jupyter Notebooks located in the `notebooks` folder.
- The final results and visualizations are available in the Streamlit dashboard (`dashboard/dashboard.py`).
- To run the dashboard, use the following command:
  ```bash
  streamlit run dashboard/dashboard.py
  ```

For any questions or feedback, feel free to contact me via GitHub.
