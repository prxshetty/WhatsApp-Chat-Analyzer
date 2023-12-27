import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px



with open( "./style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)
st.markdown(
    """
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
    <style>
    .sidebar {
        position: fixed;
        background-color: rgba(24, 119, 242, 0.7);
        color: white;
        padding: 20px;
        width: 200px;
        height: 100%;
    }
    .sidebar a {
        color: white;
        text-decoration: underline;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: rgba(24, 119, 242, 0.7);
        color: white;
    }
    .footer a {
        color: white;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,

)
st.markdown(
    """
    <style>
    .main-content {
        margin-left: 220px; /* Adjust the margin to make space for the sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("logos/whatsapp_logo.png", width=50)
st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf_8")
    df = preprocessor.preprocess(data)

    # fetches unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words, num_media_messages, no_of_links = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media")
            st.title(num_media_messages)
        with col4:
            st.header("Total Links")
            st.title(no_of_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig = px.line(timeline, x='time', y='message',labels={'message': 'Number of Messages'})
        st.plotly_chart(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        fig=px.line(daily_timeline, x='only_date', y='message',labels={'message':'Number of Messages'})
        st.plotly_chart(fig)

        # activity monitor
        st.title("Activity Map")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig=px.bar(busy_day,x=busy_day.index, y=busy_day.values, labels={'y':'Number of Messages'})
            st.plotly_chart(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig=px.bar(busy_month,x=busy_month.index, y=busy_month.values, labels={'y':'Number of Messages'})
            st.plotly_chart(fig)

        # Heatmap Weekly
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig,transparent=True)


        # finding the busiest user in the group(Group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_user(df)
            col1 = st.columns(1)
            st.dataframe(new_df)
            fig = px.bar(x,x=x.index,y=x.values, labels={'y':'Number of Messages'})
            st.plotly_chart(fig)

        # wordCloud
        st.title("WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig,transparent=True)

        # most common words without punctuation marks
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()

        fig=px.bar(most_common_df, x=1, y=0,orientation='h',
                   labels={'x': 'Number of Occurrences'})
        fig.update_traces(marker_color='#575fe8')
        st.plotly_chart(fig)
        st.title("Most Common Words")


        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2=st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig = go.Figure(data=[go.Pie(labels=emoji_df['Emoji'], values=emoji_df['Count'])])
            fig.update_layout(title_text='Top 10 Emoji Analysis')
            st.plotly_chart(fig)

collaborations_name = "<i>Suggestions are always Welcomed!<i>"
github_link = "https://github.com/prxshetty"
linkedin_link = "https://www.linkedin.com/in/prxshetty"
twitter_link = "https://www.x.com/prxshetty"
# st.markdown(
#     f'<div class="footer">{collaborations_name}: <a href="{github_link}" target="_blank">GitHub</a> | '
#     f'<a href="{linkedin_link}" target="_blank">LinkedIn</a> | <a href="{twitter_link}" target="_blank">Twitter</a></div>',
#     unsafe_allow_html=True
# )

st.sidebar.markdown(
    f'<div class="footer">{collaborations_name} <a href="{github_link}" target="_blank">GitHub</a> | '
    f'<a href="{linkedin_link}" target="_blank">LinkedIn</a> | <a href="{twitter_link}" target="_blank">Twitter</a></div>',
    unsafe_allow_html=True
)