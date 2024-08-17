import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# 🏡 Gurugram Real Estate 🏡")
st.markdown('"Informed Choices for Your Dream Home - **Predict Prices; Analyze Markets; Receive Recommendations**"')
image_path = "images/real_estate_pic.jpg"
st.image(image_path, use_column_width=True)
st.markdown("[Connect with me on Linkedin](https://www.linkedin.com/in/mihir-srivastava50/)")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">📝 Project Overview 📝</p>', unsafe_allow_html=True)
st.markdown("""
- **Objective**: Gain practical experience in the end-to-end machine learning lifecycle in the real estate domain.
- **Modules**: Price Prediction, Data Analysis and Recommendation Systems.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🌐 Web Scraping Challenges 🌐</p>', unsafe_allow_html=True)
st.markdown("""
1. **Blocked IPs** 🚫
   - Website blocked our IP addresses.
   - Limited access to pages.
2. **Data Quantity & Distribution** 📊
   - Gathered only 3000 data points initially.
   - Data unevenly distributed across areas.
3. **Solution** ✅
   - Scraped data separately for major city areas.
   - Result: 6800 data points, covering all major areas.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🧹 Data Cleaning 🧹</p>', unsafe_allow_html=True)
st.markdown("""
- **Manual cleaning**: Fixed spelling mistakes and focused on major areas.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">📊 Outlier Detection & Removal 📊</p>', unsafe_allow_html=True)
st.markdown("""
- Some manual work due to index position mismatches.
- Tailored approaches for dealing with outliers in specific cases.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🛠️ Feature Engineering 🛠️</p>', unsafe_allow_html=True)
st.markdown("""
- Resolving errors in the built-up area column.
- Modified luxury score column for clarity and accuracy.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🧩 Additional Code Development 🧩</p>', unsafe_allow_html=True)
st.markdown("""
- The recommender module required additional code for implementation.
- I took the initiative to develop code for apartment data collection and map visualization.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🏘️ Recommender System Challenges 🏘️</p>', unsafe_allow_html=True)
st.markdown("""
- **Goal**: Generate recommendations based on landmarks.
- Complex due to multiple variations of landmarks.
- Manual data consolidation; narrowed down to top 250 landmarks for better recommendations.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<p style="font-size: 20px; font-weight: bold;">🚀 Deployment 🚀</p>', unsafe_allow_html=True)
st.markdown("""
- Ongoing project with limitless scope for improvement.
""")

st.markdown("<br>", unsafe_allow_html=True)
if st.button('**Click Here for Detailed Explanation**'):
    st.markdown("""
    In this comprehensive Project, the primary focus was on leveraging data science techniques to provide insights,
    predictions, and recommendations in the real estate domain. The project unfolds through various stages, covering data
    gathering, cleaning, exploratory analysis, modeling, recommendation systems, and the deployment of a user-friendly
    application.
    
    1. **Data Gathering**: 
                        The project commenced with the collection of real estate data, which was self-scraped from the
                        99acres website. Similar datasets from other property listing websites were also explored,
                        ensuring a diverse and representative dataset.
                        
    2. **Data Cleaning and Merging**: 
                        To prepare the dataset for analysis, a meticulous data cleaning process was undertaken, handling
                        missing values and ensuring consistency. The data was then merged, bringing together
                        information on houses and flats into a unified dataset.
                        
    3. **Feature Engineering**: 
                        The dataset underwent feature engineering to enhance its richness and informativeness. New
                        features, such as additional room indicators, area with type specifications, age of possession,
                        furnish details, and a luxury score, were introduced to provide a more detailed representation of
                        the properties.
                        
    4. **Exploratory Data Analysis (EDA)**:
                        Univariate and multivariate analyses were conducted to uncover patterns and relationships within
                        the data. The use of Pandas Profiling facilitated a deeper understanding of data distribution and
                        structure.
                        
    5. **Outlier Detection, Missing Value Imputation**:
                        Outliers were identified and removed to ensure the robustness of subsequent analyses. Missing
                        values, particularly in critical columns like area and bedroom, were addressed using appropriate
                        imputation techniques.
                        
    6. **Feature Selection**:
                        Multiple feature selection techniques were employed to identify the most impactful variables for
                        modeling. These included correlation analysis, random forest and gradient boosting feature
                        importance, permutation importance, LASSO, recursive feature elimination, and SHAP
                        (Explainable Al).
    
    7. **Model Selection & Productionalization**:
                        In the Model Selection and Productionalization phase, an exhaustive comparison of various
                        regression models was conducted to determine the most effective model for predicting property
                        prices. The process involved implementing a detailed price prediction pipeline that incorporated
                        encoding methods, ensuring the robustness and accuracy of the chosen model. The selected
                        model was then deployed using Streamlit, creating an intuitive and user-friendly web interface
                        for end-users.
                        
        The regression models considered in the comparison included
        - Linear Regression: A foundational regression model that assumes a linear relationship between the input features and the target variable.
        
        - Support Vector Regression (SVR): A regression technique that leverages support vector machines to find a hyperplane that best fits the data, allowing for non-linear relationships.
        
        - Random Forest Regressor: An ensemble learning method that builds a multitude of decision trees during training and outputs the average
          prediction of the individual trees.
        
        - Multi-layer Perceptron (MLP): A type of artificial neural network that consists of multiple layers of nodes and is capable of learning complex patterns.
        
        - LASSO Regression: A linear regression technique that incorporates L1 regularization, encouraging sparsity 
          in the coefficient estimates.
        
        - Ridge Regression: A linear regression technique with L2 regularization, which helps prevent 
          multicollinearity and stabilizes the model.
        
        - Gradient Boosting Regressor: An ensemble learning method that builds trees sequentially, with each tree 
          correcting the errors of the previous ones.
        
        - Decision Tree Regressor: A non-linear regression model that splits the dataset into subsets based on the 
          most significant attribute at each node.
        
        - K-Nearest Neighbors Regressor: A regression model that predicts the target variable by averaging the values of its k-nearest neighbors.
        
        - ElasticNet Regression: A linear regression technique that combines L1 and L2 regularization terms.
        
        The comparison involved assessing the performance of each model on relevant evaluation metrics, considering factors
        such as accuracy, precision, and recall. After careful evaluation, the most suitable regression model was selected based on
        its overall performance and ability to generalize to new data.
        
        The chosen regression model was then integrated into a comprehensive price prediction pipeline, which included
        preprocessing steps, encoding methods, and handling of various features to ensure optimal performance. The final model
        was deployed using Streamlit, creating an interactive and user-friendly web interface for predicting property prices. This
        productionalization step made the model accessible to end-users, allowing them to make informed decisions in the real
        estate domain.
                        
    8. **Building the Analytics Module**:
                        An analytics module was developed to visually represent key insights about the real estate data. Geographical maps, word
                        clouds for amenities, scatter plots, pie charts, and box plots were employed to offer users a comprehensive understanding
                        of the market.
    
    9. **Building the Recommender System**:
                        In the process of building the Recommender System, three distinct recommendation models were developed, each
                        focusing on different aspects of the real estate dataset: top facilities, price details, and location advantages. The goal was
                        to provide users with personalized recommendations tailored to their preferences and priorities. Additionally, a user-
                        friendly recommendation interface was crafted using Streamlit, enhancing the accessibility of the recommendation
                        systems.
                        
    10. **Deploying the Application on AWS**:
                        The entire application, encompassing prediction, analytics, and recommendation functionalities, was deployed on Amazon
                        Web Services (AWS). This step ensured the scalability and accessibility of the project.
                        
                        This capstone project not only demonstrates proficiency in data science techniques such as feature engineering,
                        exploratory analysis, and model building but also showcases the deployment of a real-world application, making valuable
                        insights and recommendations accessible to end-users.

""")


st.sidebar.success("Select a demo above.")