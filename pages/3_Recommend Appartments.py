import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Appartments")

# importing dataset --> contain every apartment distance from every landmark
location_df = pickle.load(open('datasets/location_distance.pkl','rb'))

# importing cosine similarity
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl','rb'))

# function which recommend property
def recommend_properties_with_scores(property_name, top_n=247):
    # cosine similarity matrix
    cosine_sim_matrix = (0.5 * cosine_sim1 + 0.3 * cosine_sim2 + 1 * cosine_sim3)
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    return recommendations_df.head(5)


# Initialize session state for storing selected values and results
if 'selected_appartment' not in st.session_state:
    st.session_state.selected_appartment = None

if 'result_ser' not in st.session_state:
    st.session_state.result_ser = None

# Title and input fields
st.title('Select Location and Radius')

# Default values
default_location = 'Huda City Centre Metro Station'
default_radius = 7

# Location selection with default value
selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()),
                                 index=sorted(location_df.columns.to_list()).index(default_location))

# Radius input with default value
radius = st.number_input('Radius (in Kms)', min_value=0, value=default_radius)

# Search button
if st.button('Search'):
    # Filter and sort properties based on the selected location and radius
    st.session_state.result_ser = location_df[location_df[selected_location] < radius * 1000][
        selected_location].sort_values()

# Display search results or a message if no properties are found
if st.session_state.result_ser is not None:
    if st.session_state.result_ser.empty:
        st.text("No properties found within the selected radius.")
        st.session_state.selected_appartment = None
    else:
        for key, value in st.session_state.result_ser.items():
            st.text(f"{key}  -->  {round(value / 1000)} kms")

        st.markdown("<br><br>", unsafe_allow_html=True)
        # Use Markdown to display a bold label for the selectbox
        st.markdown(
            """
            <style>
            .custom-label {
                font-size: 30px;  /* Increase font size */
                font-weight: bold; /* Make text bold */
                margin-bottom: 5px; /* Adjust margin below label */
            }
            </style>
            <div class="custom-label">
                Select an Apartment (Recommend Apartments)
            </div>
            """,
            unsafe_allow_html=True
        )
        # Allow user to select a property from the search results
        st.session_state.selected_appartment = st.selectbox('', sorted(st.session_state.result_ser.index.to_list()),
                                                            index=0)

        # Recommend button
        if st.button('Recommend'):
            if st.session_state.selected_appartment:
                # Get recommendations based on the selected property
                recommendation_df = recommend_properties_with_scores(st.session_state.selected_appartment)
                st.dataframe(recommendation_df)
            else:
                st.text("Please select a property to get recommendations.")