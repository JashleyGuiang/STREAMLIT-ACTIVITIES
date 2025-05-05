import streamlit as st
import pandas as pd

# Title of the app
st.title('DataFrame Viewer')

# Upload CSV file using st.file_uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the CSV file using pandas
    df = pd.read_csv(uploaded_file)

    # Show the DataFrame with st.dataframe
    st.write("### Data Preview")
    st.dataframe(df)

    # Checkbox to toggle viewing raw data
    show_raw_data = st.checkbox("Show Raw Data", value=False)
    if show_raw_data:
        st.write("### Raw Data")
        st.write(df)

    # Selectbox to filter by a column
    if df.shape[1] >= 5:
        column_to_filter = st.selectbox("Select a column to filter by", df.columns)

        # Allow users to filter by unique values in the chosen column
        unique_values = df[column_to_filter].unique()
        selected_value = st.selectbox(f"Select a value to filter by {column_to_filter}", unique_values)

        # Filter the dataframe based on the selected value
        filtered_df = df[df[column_to_filter] == selected_value]
        st.write(f"### Filtered Data by {column_to_filter} = {selected_value}")
        st.dataframe(filtered_df)

else:
    st.write("Please upload a CSV file to proceed.")
