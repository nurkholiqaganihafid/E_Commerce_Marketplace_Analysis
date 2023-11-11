<div id="top"></div>

# 📌E_Commerce_Marketplace_Analysis
- __*Brazilian E-Commerce Marketplace*__ is a real commercial dataset containing information about 100 thousand orders from 2016 to 2018 in various markets in Brazil. Analysis that can be performed includes __order status, price, payment, delivery, customer location, product attributes, and customer reviews__.
- __The goal of this analysis__ is to provide valuable insights to e-commerce businesses on optimizing sales strategies, increasing customer satisfaction, and optimizing product delivery.
- This database consists of nine tables, including __customers_dataset, geolocation_dataset, order_items_dataset, order_payments_dataset, order_reviews_dataset, orders_dataset, product_category_name_translation, products_dataset, and sellers_dataset__. [Dataset source](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- This project uses a data analysis cycle, namely:
  - Question (Business Questions)
  - Data Wrangling
  - Exploratory Data Analysis (EDA)
  - Data Visualization and Explanatory
  - Draw Conclusion and Recommendation
  - Project Result Link: [Click here](https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/blob/main/E_Commerce_Marketplace_Analysis.ipynb)

# 📌Outline
- [Business Questions](#business-questions) 
- [Results](#results)
  - [Deploy Streamlit App](#deploy-streamlit-app)
  - [Streamlit Dashboard](#streamlit-dashboard)
  - [My Analysis Results](#my-analysis-results)
    - [Merging all Data](#merging-all-data)
    - [Data Visualization](#data-visualization)
      - [1st Question](#1st-question)
      - [2nd Question](#2nd-question)
      - [3rd Question](#3rd-question)
      - [4th Question](#4th-question)
      - [5th Question](#5th-question)
      - [6th Question](#6th-question)
      - [7th Question](#7th-question)
- [Conclusions and Recommendations](#conclusions-and-recommendations)

# 🎯Business Questions
[👆](#outline)
Business questions that will be answered through this data analysis include:
1. How are the sales performance, number of ordered items, and revenue on E-Commerce in the last few months?
2. What products sell the most and least?
3. How is the distribution of review scores on products sold and what is the percentage for each review?
4. How is the product delivery time distributed?
5. What are the demographic characteristics of customers in the e-commerce marketplace sector?
6. Is there a correlation between product price and shipping costs (freight_value)?
7. How is the distribution of geolocation based on latitude and longitude in Brazil?

# 🎯Results
## 💻Deploy Streamlit App
[👆](#outline)
Requirements to deploy dashboard.py on streamlit.
- Make sure the `virtualenv` is ready to run for this project.
- Install all the required libraries using the following command.
```
pip install streamlit Babel geopandas matplotlib numpy pandas seaborn streamlit
```
- Prepare `requirements.txt` file

```
pip install pipreqs
```
This package is used to generate the `requirements.txt` file which contains a list of all the packages used in this project.

```
pipreqs
```
This command will automatically create a `requirements.txt` file with a list of all packages used in this project.

- Run the streamlit application
```
streamlit run dashboard.py
```
This is the command to run the Streamlit application with the `dashboard.py` file.

## 📊Streamlit Dashboard
[👆](#outline)
Link Streamlit Dashboard: [E-Commerce Marketplace Dashboard](https://nurkholiq-ecommerce-marketplace-analysis.streamlit.app/)

<p align="center">
  <img alt="E-Commerce Marketplace Dashboard" title="E-Commerce Marketplace Dashboard" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/c6e2b4f6-64a9-442a-ac38-26a0140a667b" width="750">
</p>

## 📈My Analysis Results
### Merging all Data
[👆](#outline) Total Data from the Merge Results
<p align="center">
  <img alt="Data Frame" title="Data Frame" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/67c126d9-4bf6-4e04-bc90-6420e2fd0ae3" width="400">
</p>

### Data Visualization
#### 1st Question
[👆](#outline)
How are the sales performance, number of ordered items, and revenue on E-Commerce in the last few months?
- By orders & items
<p align="center">
  <img alt="Number of Orders per Month (Last 12 Months)" title="Number of Orders per Month (Last 12 Months)" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/97e9a660-c6f3-463d-b715-6312b4cb6ab3" width="750">
</p>

- By revenue
<p align="center">
  <img alt="Total Revenue per Month (Last 12 Months)" title="Total Revenue per Month (Last 12 Months)" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/00f14915-555f-4e01-8224-808bcf92b0fc" width="750">
</p>

#### 2nd Question
[👆](#outline)
What products sell the most and least?
<p align="center">
  <img alt="Best and Worst Performing Product by Number of Sales" title="Best and Worst Performing Product by Number of Sales" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/e5255e33-2b71-4d3e-b4af-f2f38a91fc58" width="750">
</p>

#### 3rd Question
[👆](#outline)
How is the distribution of review scores on products sold and what is the percentage for each review?
- By number of review scores
<p align="center">
  <img alt="Distribution of Review Scores" title="Distribution of Review Scores" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/9f5e9a34-9cbf-44b3-ba73-efab408b5848" width="750">
</p>

- By percentage review score
<p align="center">
  <img alt="Percentage of Products with Review Score" title="Percentage of Products with Review Score" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/5b521f26-006d-4c73-a152-015552224ab7" width="750">
</p>

#### 4th Question
[👆](#outline)
How is the product delivery time distributed?
<p align="center">
  <img alt="Distribution of Order Delivery Time" title="Distribution of Order Delivery Time" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/b6e55350-91d3-4ce4-b403-02383f866036" width="750">
</p>

#### 5th Question
[👆](#outline)
What are the demographic characteristics of customers in the e-commerce marketplace sector?
- By customer state
<p align="center">
  <img alt="Number of Orders by Customer State" title="Number of Orders by Customer State" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/614db033-2ed0-4710-8674-e00b0e583939" width="750">
</p>

- By customer city
<p align="center">
  <img alt="Top 10 Cities by Number of Orders" title="Top 10 Cities by Number of Orders" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/6c115cc8-d8fc-4794-8469-d57711c88528" width="750">
</p>

- By payment type
<p align="center">
  <img alt="Number of Orders by Payment Type" title="Number of Orders by Payment Type" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/dac985a6-b253-4b64-b308-5c21e1372aee" width="750">
</p>

#### 6th Question
[👆](#outline)
Is there a correlation between product price and shipping costs (freight_value)?
<p align="center">
  <img alt="E-Commerce Marketplace Data Correlation" title="E-Commerce Marketplace Data Correlation" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/4c73e43f-cd84-4033-9e6d-2d8ff3695fe9" width="750">
</p>

#### 7th Question
[👆](#outline)
How is the distribution of geolocation based on latitude and longitude in Brazil?
<p align="center">
  <img alt="Geolocation Distribution" title="Geolocation Distribution" src="https://github.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/assets/89395541/498fcd8b-db17-44ea-b001-01637b963329" width="750">
</p>


# 📚Conclusions and Recommendations
- Conclusions
    - Based on the results of the analysis carried out on the E-Commerce Marketplace, there are several important findings. First, __sales performance, number of ordered items, and revenue__ on e-commerce in recent months have been very volatile. __November 2017__ showed __excellent__ performance, with a high number of __orders and revenue__. However, there was a drastic decline in __September 2018__, which had the potential to have a __negative__ impact on future profits.

    - Furthermore, the product that __sells the most__ is the `Bed Bath Table`, while the `Security and Services` product has the __lowest sales__. This shows that products in the `Bed Bath Table` category have high popularity among customers.

    - In terms of __review score__ distribution, __a score of 5__ dominates the total of __66,264__ reviews with a __percentage of 56.5%__, indicating that the majority of customers gave very good reviews to the products they purchased. This shows a high level of customer satisfaction.

    - The distribution of product __delivery times__ tends to be in the __range of 1 to 50 days__, with some other cases of delivery taking longer. However, delivery times that take this long are very rare.

    - In terms of customer __demographic characteristics__, the state of __SP__ has the __largest number of orders__, one of which is the city of __Sao Paulo__ which has the largest number of orders. The __most commonly__ used payment method is `credit_card`, while `debit_card` has a __very small__ number of transactions.

    - There is a __fairly strong positive correlation__ between __product prices and shipping costs__, indicating that the higher the product price, the higher the shipping costs. In addition, there is a __strong positive correlation__ between __product price and payment value__, indicating that the higher the product price, the higher the value of payments made by customers.

    - Meanwhile, the __geolocation distribution__ shows the __SP state__ that occupies the __most geolocation__ point positions, and the state with the __least distribution__ is `geolocation_state` __AP__. However, it is important to note that to understand geolocation distribution patterns in more depth, further analysis is required.

- Recommendations
> Based on these findings, several recommendations can be made. First, further analysis needs to be carried out to find out the __causes of the decline__ in performance in __September 2018__. Factors such as the existence of competitors and marketing campaigns need to be considered. In addition, marketing efforts need to be increased for products with low sales, such as `Security and Services`.

> In terms of __product delivery__, care needs to be taken to ensure that delivery is carried out __on time__ in order to meet customer expectations. In addition, it is worth considering offering __alternative payment methods__ that are more attractive to customers, besides `credit_card`.

<p align="right"><a href="#top">Back to top</a></p>
