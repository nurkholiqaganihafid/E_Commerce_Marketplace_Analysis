import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import streamlit as st
from babel.numbers import format_currency
from matplotlib.colors import LinearSegmentedColormap

sns.set_style('darkgrid')

# Load Data
all_df = pd.read_csv('https://raw.githubusercontent.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/main/dashboard/all_data.csv')
geo_df = pd.read_csv('https://raw.githubusercontent.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/main/dashboard/geolocation.csv')

def display_dataframe(df, option):
    selected_product = df[df['product_category_name_english'].isin(option)]

    if not option:
        col1, col2 = st.columns(2)

        # Number of orders
        with col1:
            total_orders = df.order_id.nunique()
            st.metric('#Orders', value=total_orders)

        # Number of revenue
        with col2:
            total_revenue = df.payment_value.sum()
            formatted_revenue = format_currency(total_revenue, 'BRL', locale='pt_BR')
            st.metric('#Revenue', value=formatted_revenue)

        # Mean review score
        col3 = st.columns(1)
        with col3[0]:
            mean_review = df.review_score.mean().round(2)
            st.metric('#Mean Review', value=mean_review)

        st.dataframe(df)
    else:
        col1, col2 = st.columns(2)

        with col1:
            total_orders = selected_product.order_id.nunique()
            st.metric('#Orders', value=total_orders)

        with col2:
            total_revenue = selected_product.payment_value.sum()
            formatted_revenue = format_currency(total_revenue, 'BRL', locale='pt_BR')
            st.metric('#Revenue', value=formatted_revenue)

        col3 = st.columns(1)
        with col3[0]:
            mean_review = selected_product.review_score.mean().round(2)
            st.metric('#Mean Review', value=mean_review)

        st.dataframe(selected_product)

def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_approved_at').agg({
        'order_id': 'nunique',
        'order_item_id': 'sum',
        'payment_value': 'sum'
    })

    daily_orders_df = daily_orders_df.reset_index()

    daily_orders_df.rename(columns={
        'order_id': 'order_count',
        'order_item_id': 'order_item_count',
        'payment_value': 'revenue'
    }, inplace=True)

    return daily_orders_df

def plot_total_orders_and_revenue(daily_orders_df):
    total_orders = daily_orders_df.order_count.sum()
    total_revenue = format_currency(daily_orders_df.revenue.sum(), 'BRL', locale='pt_BR')

    st.metric('#Total Orders', value=total_orders)
    st.metric('#Total Revenue', value=total_revenue)

def plot_daily_orders(daily_orders_df, min_date):
    if min_date <= daily_orders_df['order_approved_at'].max() - pd.DateOffset(days=60):
        x = daily_orders_df['order_approved_at']
        y = daily_orders_df['order_count']

        fig, ax = plt.subplots(figsize=(20, 8))
        ax.plot(x, y, linewidth=2, color='#577fd7')
        ax.tick_params(axis='x', labelsize=16)
        ax.tick_params(axis='y', labelsize=16)

        st.pyplot(fig)
    else:
        x = daily_orders_df['order_approved_at']
        y = daily_orders_df['order_count']

        fig, ax = plt.subplots(figsize=(20, 8))
        ax.plot(x, y, linewidth=2, color='#577fd7')
        ax.tick_params(axis='x', labelsize=16)
        ax.tick_params(axis='y', labelsize=16)

        for i in range(len(daily_orders_df)):
            plt.text(
                x[i],
                daily_orders_df['order_count'][i] + 0.5,
                daily_orders_df['order_count'][i],
                ha='left',
                va='bottom',
                fontsize=12
            )

        st.pyplot(fig)

def plot_best_worst_performing_product(df):
    sum_order_items_df = df.groupby(by='product_category_name_english') \
        .order_item_id.sum() \
        .sort_values(ascending=False).reset_index()

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(28, 10))

    colors = ['#577fd7', '#bcccef', '#bcccef', '#bcccef', '#bcccef']

    # First plot
    sns.barplot(
        x='order_item_id',
        y='product_category_name_english',
        data=sum_order_items_df.head(5),
        palette=colors,
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel('Number of Sales', fontsize=28, labelpad=15)
    ax[0].set_title('Best Performing Product', loc='center', fontsize=36, pad=15)
    ax[0].tick_params(axis='y', labelsize=30)
    ax[0].tick_params(axis='x', labelsize=26)

    for i in range(len(sum_order_items_df.head(5))):
        ax[0].text(
            sum_order_items_df['order_item_id'].iloc[i],
            i,
            sum_order_items_df['order_item_id'].iloc[i],
            va='center',
            fontsize=20
        )

    # Second plot
    asc_sum_order = sum_order_items_df.sort_values(
        by='order_item_id', ascending=True
    ).head(5)

    sns.barplot(
        x='order_item_id',
        y='product_category_name_english',
        data=asc_sum_order,
        palette=colors,
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel('Number of Sales', fontsize=28, labelpad=15)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position('right')
    ax[1].yaxis.tick_right()
    ax[1].set_title('Worst Performing Product', loc='center', fontsize=36, pad=15)
    ax[1].tick_params(axis='y', labelsize=30)
    ax[1].tick_params(axis='x', labelsize=26)

    for i, value in enumerate(asc_sum_order['order_item_id']):
        ax[1].text(
            value,
            i,
            value,
            va='center',
            ha='right',
            fontsize=20
        )

    st.pyplot(fig)

def plot_review_scores_distribution(df):
    review_scores = df['review_score'].value_counts().sort_values(ascending=False)

    col1, col2 = st.columns(2)

    # By number of review scores
    with col1:
        fig, ax = plt.subplots(figsize=(8, 7))
        sns.barplot(
            x=review_scores.index,
            y=review_scores.values,
            order=review_scores.index,
            palette=['#577fd7', '#bcccef', '#bcccef', '#bcccef', '#bcccef']
        )

        ax.set_title('Distribution of Review Scores', fontsize=20, pad=15)
        ax.set_ylabel(None)
        ax.set_xlabel('Rating', fontsize=16)
        ax.tick_params(axis='x', labelsize=16)
        ax.tick_params(axis='y', labelsize=16)

        for i, value in enumerate(review_scores.values):
            ax.text(
                y=value,
                x=i,
                s=value,
                ha='center',
                fontsize=14
            )

        st.pyplot(fig)

    # By percentage review score
    with col2:
        review_colors = {
            5: '#577fd7',
            4: '#bcccef',
            3: '#bcccef',
            2: '#bcccef',
            1: '#bcccef'
        }

        fig, ax = plt.subplots(figsize=(10, 8.7))
        percentages = (review_scores / review_scores.sum()) * 100

        wedges, label_texts, value_texts = ax.pie(
            percentages,
            labels=percentages.index.astype(int),
            colors=[review_colors[key] for key in percentages.index.astype(int)],
            autopct='%1.1f%%',
            labeldistance=1.05
        )
        ax.set_title('Percentage of Products with Review Score', fontsize=20, pad=15)
        ax.axis('equal')

        for text in label_texts:
            text.set_fontsize(20)

        for value_text in value_texts:
            value_text.set_fontsize(17)

        st.pyplot(fig)

def plot_delivery_times_distribution(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(
        data=df,
        x='order_delivery_time',
        kde=True, bins=20, edgecolor='black',
        color='#577fd7'
    )
    ax.set_xlabel('Delivery Time (Days)', fontsize=12, labelpad=10)
    ax.set_ylabel('Frequency', fontsize=12, labelpad=10)

    st.pyplot(fig)

def plot_demographic_characteristics(df):
    # By customer state
    bystate_df = df.groupby(by='customer_state').order_id.nunique() \
        .sort_values(ascending=False) \
        .reset_index()

    order_value_max = bystate_df.loc[bystate_df['order_id'].idxmax(), 'customer_state']

    colors_ = [
        '#bcccef' if state != order_value_max else '#577fd7'
        for state in bystate_df['customer_state']
    ]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.barplot(
        x=bystate_df['customer_state'],
        y=bystate_df['order_id'],
        palette=colors_
    )
    ax.set_title('Number of Orders by Customer State', fontsize=16, pad=12)
    ax.set_xlabel(None)
    ax.set_ylabel(None)

    for i, value in enumerate(bystate_df['order_id']):
        ax.text(
            i,
            value,
            str(value),
            ha='center',
            fontsize=7
        )

    st.pyplot(fig)

    col1, col2 = st.columns(2)
    # By customer city
    with col1:
        bycity_df = df.groupby(by='customer_city').order_id.nunique() \
            .sort_values(ascending=False) \
            .reset_index().head(10)

        fig, ax = plt.subplots(figsize=(14, 11))
        sns.barplot(x='order_id', y='customer_city', data=bycity_df, palette=colors_)
        ax.set_title('Top 10 Cities by Number of Orders', fontsize=38, pad=15)
        ax.set_xlabel(None)
        ax.set_ylabel(None)
        ax.tick_params(axis='x', labelsize=34)
        ax.tick_params(axis='y', labelsize=34)

        for i, value in enumerate(bycity_df['order_id']):
            ax.text(value, i, str(value), ha='left', va='center', fontsize=30)

        st.pyplot(fig)

    # By payment type
    with col2:
        bypayment_type_df = df.groupby(by='payment_type') \
            .order_id.nunique() \
            .sort_values(ascending=False).reset_index()

        fig, ax = plt.subplots(figsize=(10, 6.3))
        sns.barplot(
            x='order_id',
            y='payment_type',
            data=bypayment_type_df,
            palette=['#577fd7', '#bcccef', '#bcccef', '#bcccef', '#bcccef']
        )
        ax.set_title('Number of Orders by Payment Type', fontsize=26, pad=15)
        ax.set_xlabel(None)
        ax.set_ylabel(None)
        ax.tick_params(axis='x', labelsize=22)
        ax.tick_params(axis='y', labelsize=22)

        for i, value in enumerate(bypayment_type_df['order_id']):
            ax.text(value, i, str(value), ha='left', va='center', fontsize=20)

        st.pyplot(fig)

def plot_correlation_matrix(df):
    # Select numerical columns only
    numeric_columns = df.select_dtypes(include=[np.number])

    threshold = st.slider("Select threshold", -1.0, 1.0, 0.0, step=0.1)
    correlation_matrix = numeric_columns.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        correlation_matrix,
        vmin=-1.,
        vmax=1.,
        annot=False,
        cmap='coolwarm',
        linewidths=0.5,
        mask=correlation_matrix.abs() < threshold
    )
    ax.set_title('E-Commerce Marketplace Data Correlation', fontsize=20, pad=12)
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)

    st.pyplot(fig, clear_figure=True)

    price_checkbox = st.checkbox("Displays correlation based on price")
    if price_checkbox:
        correlation_matrix['price']

def plot_geolocation_distribution(geo_df):
    gdf = gpd.GeoDataFrame(
        geo_df,
        geometry=gpd.points_from_xy(geo_df.geolocation_lng, geo_df.geolocation_lat)
    )

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    min_val = geo_df['geolocation_zip_code_prefix'].min()
    max_val = geo_df['geolocation_zip_code_prefix'].max()
    cmap = LinearSegmentedColormap.from_list('custom_cmap', ['#fee6e6', '#f40907'])

    threshold = st.slider(
        "Select Geolocation Zip Code Prefix Threshold",
        min_val, max_val,
        (min_val, max_val)
    )

    fig, ax = plt.subplots(figsize=(18, 14))
    world.boundary.plot(ax=ax, linewidth=0.5, color='gray')
    gdf.plot(
        ax=ax,
        markersize=10,
        column='geolocation_zip_code_prefix',
        cmap=cmap,
        legend=True,
        vmin=threshold[0],
        vmax=threshold[1]
    )
    ax.set_title('Geolocation Distribution', fontsize=18, pad=14)
    ax.set_xlabel('Longitude', fontsize=14, labelpad=12)
    ax.set_ylabel('Latitude', fontsize=14, labelpad=12)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    st.pyplot(fig)

# Sort and convert to datetime
datetime_cols = [
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "order_purchase_timestamp",
    "shipping_limit_date"
]

for column in datetime_cols:
    all_df[column] = pd.to_datetime(all_df[column])

# Create Filter Components by Date
min_date = all_df["order_approved_at"].min()
max_date = all_df["order_approved_at"].max()

with st.sidebar:
    st.image('https://raw.githubusercontent.com/nurkholiqaganihafid/E_Commerce_Marketplace_Analysis/main/dashboard/mecoliq.png')

    start_date, end_date = st.date_input(
        label='Select Time Range',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Main Data
main_df = all_df[
    (all_df['order_approved_at'] >= str(start_date)) &
    (all_df['order_approved_at'] <= str(end_date))
]

# Streamlit App
st.header(':chart_with_upwards_trend: E-Commerce Marketplace Dashboard :chart_with_upwards_trend:')
st.subheader('Detail Data')

expander = st.expander('DataFrame')
with expander:
    option = st.multiselect(
        'Select Product Category',
        main_df['product_category_name_english'].unique()
    )
    display_dataframe(main_df, option)

st.subheader('Daily Orders')
daily_orders_df = create_daily_orders_df(main_df)

plot_total_orders_and_revenue(daily_orders_df)
plot_daily_orders(daily_orders_df, min_date)

st.subheader('Best and Worst Performing Product by Number of Sales')
plot_best_worst_performing_product(main_df)

st.subheader('Distribution of Review Scores on Products Sold')
plot_review_scores_distribution(main_df)

st.subheader('Distribution of Product Delivery Times')
plot_delivery_times_distribution(main_df)

st.subheader('Demographic Characteristics')
plot_demographic_characteristics(main_df)

st.subheader('E-Commerce Marketplace Correlation')
plot_correlation_matrix(main_df)

st.subheader('Geolocation distribution based on latitude and longitude')
plot_geolocation_distribution(geo_df)

st.caption('Copyright 2023 | Author: Nurkholiq Agani Hafid')