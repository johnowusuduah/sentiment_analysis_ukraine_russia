import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

# add style
st.markdown(
    """<style>.main{background-color: #F5F5F5;}</style>""", unsafe_allow_html=True
)

# caching ingestion of data
# put code we only want to run once in a function
@st.cache
def get_data(file_path):
    taxi_data = pd.read_csv(file_path)
    return taxi_data


with header:
    st.title("Welcome to Our Data Science Project")
    st.text(
        "In this project I look into the transactions of taxis in NYC in January of 2020"
    )

with dataset:
    st.header("NYC taxi dataset")
    st.text("I found this dataset on City of New York TLC Trip Record Data")
    taxi_data = get_data("./data_2.0/taxi_data.csv")
    st.write(taxi_data.head())

    st.subheader("Pick-up Location ID Distribution in January, 2022 ")
    pulocation_dist = pd.DataFrame(taxi_data["PULocationID"].value_counts())
    st.bar_chart(pulocation_dist)

with features:
    st.header("The features created")
    st.markdown("* **First feature:** I created this feature because of ...")
    st.markdown("* **Second feature:** I created this feature because of ...")

with model_training:
    st.header("Time to train the model")
    # create columns
    # to place widgets in columns, refer to column variables below
    sel_col, disp_col = st.columns(2)

    # get input from user
    max_depth = sel_col.slider(
        "What should be the max_depth of the model?",
        min_value=10,
        max_value=100,
        value=5,
        step=1,
    )
    no_estimators = sel_col.selectbox(
        "How many trees should there be?", options=[100, 200, 300, "No limit"], index=0
    )

    sel_col.text("Here is a list of features in my data:")
    sel_col.write(taxi_data.columns)

    input_feature = sel_col.text_input(
        "Which feature should be used as the input feature", "PULocationID"
    )

    # instantiate random forest regressor
    if no_estimators == "No limit":
        regr = RandomForestRegressor(max_depth=max_depth)
    else:
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators=no_estimators)

    # training data
    X = taxi_data[[input_feature]]
    y = taxi_data[["trip_distance"]]

    # fit model to training data
    regr.fit(X, y)
    prediction = regr.predict(y)

    disp_col.subheader("Mean absolute error of the model is:")
    disp_col.write(mean_absolute_error(y, prediction))

    disp_col.subheader("Mean squared error of the model is:")
    disp_col.write(mean_squared_error(y, prediction))

    disp_col.subheader("R squared score of the model is:")
    disp_col.write(r2_score(y, prediction))
