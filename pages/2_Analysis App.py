import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import ast

st.set_page_config(page_title='Analysis')

st.title('Analysis')

new_df = pd.read_csv('datasets/data_viz1.csv')
# feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))
wordcloud_df = pd.read_csv('datasets/wordcloud_df.xls')

# Select Box
def create_select_box(key_suffix):
    sector_options = new_df['sector'].unique().tolist()
    sector_options.insert(0, 'overall')
    selected_sector = st.selectbox(label='Select Sector', options=sector_options, key=key_suffix)
    return selected_sector

## Geographical Map
group_df = new_df.groupby('sector').mean()[['price','price_per_sqft','built_up_area','latitude','longitude']]

st.markdown('<p style="font-size: 30px; font-weight: bold;">Geographical Map (Sector Price per Sqft)</p>', unsafe_allow_html=True)
st.markdown("""
  - **Color**: average price per square feet of every sector
  - **Size**: average area of the flat
""")

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10.5,
                  mapbox_style="open-street-map",width=1000,height=650,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

## Wordcloud
def wordcloud_every_sector(sector):
    main = []
    if sector == 'overall':
        for item in wordcloud_df['features'].dropna().apply(ast.literal_eval):
            main.extend(item)
    else:
        individual_sector_df = wordcloud_df[wordcloud_df['sector'] == sector]
        for item in individual_sector_df['features'].dropna().apply(ast.literal_eval):
            main.extend(item)

    feature_text = ' '.join(main)
    return feature_text

st.header('Features Wordcloud (for amenities)')

# sector_options = new_df['sector'].unique().tolist()
# sector_options.insert(0,'overall')
# selected_sector = st.selectbox('Select Sector', sector_options)
selected_sector_wordcloud = create_select_box(key_suffix='wordcloud')
feature_text = wordcloud_every_sector(selected_sector_wordcloud)

wordcloud = WordCloud(width=800, height=800,
                      background_color='black',
                      stopwords=set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size=10).generate(feature_text)

fig, ax = plt.subplots(figsize=(6, 4), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)


## Scatter Plot (Area VS Price)
st.header('Area Vs Price')

def scatter_plot(sector):
    if sector == 'overall':
        fig1 = px.scatter(new_df, x="built_up_area", y="price", color="bedRoom")
    else:
        fig1 = px.scatter(new_df[new_df['sector'] == sector], x="built_up_area", y="price", color="bedRoom")
    return fig1
selected_sector_scatter = create_select_box(key_suffix='scatter')
st.plotly_chart(scatter_plot(selected_sector_scatter), use_container_width=True)

## Pie Chart
st.header('BHK Pie Chart')

selected_sector_pie = create_select_box(key_suffix='pie')
if selected_sector_pie == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector_pie], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

## Boxplot --> for BHK price comparison
st.header('Side by Side BHK Price Comparison')

# fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price')
# st.plotly_chart(fig3, use_container_width=True)

selected_sector_box = create_select_box(key_suffix='box')
less_than_4_bedroom_df = new_df[new_df['bedRoom'] <= 5]

if selected_sector_box == 'overall':
    fig3 = px.box(less_than_4_bedroom_df, x='bedRoom', y='price')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.box(less_than_4_bedroom_df[less_than_4_bedroom_df['sector'] == selected_sector_box], x='bedRoom',y='price')
    st.plotly_chart(fig3, use_container_width=True)


## Distplot of Property Type
st.header('Side by Side Distplot for property type')

fig4 = plt.figure(figsize=(10, 4))

sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig4)