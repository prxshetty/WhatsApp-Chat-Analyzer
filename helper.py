from urlextract import URLExtract
extract = URLExtract();
def fetch_stats(selected_user,df):

    #used to  tell info about the selected user
    if selected_user!='Overall':
        df = df[df['user'] == selected_user]

    #fetches the no of messages
    num_messages = df.shape[0]

    #fetches the total number of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    #fetches the number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]
    #no_media_messages = df['message'].str.contains('<Media omitted>', case=False).sum()

    #fetches the number of links shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)












