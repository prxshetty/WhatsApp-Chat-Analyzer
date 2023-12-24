import streamlit as st
import helper
import preprocessor

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf_8")
    df=preprocessor.preprocess(data)
    st.dataframe(df)
    #fetches unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.remove('You joined a group via invite in the community')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user=st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages,words=helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4=st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)