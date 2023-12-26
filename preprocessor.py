import re
import pandas as pd
# installed with streamlit in the venv
def preprocess(data):

    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
    # chats where in m.d.y format, so i had to alter the code language as well,
    # another approach to fix that was maybe use the errors='coerce'  to declare those values
    # NaT which cause problems while parsing but would reduce the rows
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    special_message = "You joined a group via invite in the community"
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if special_message in message:
            users.append('group_notification')
            messages.append(special_message)
        elif entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    # Make sure both lists have the same length
    if len(messages) < len(df):
        messages.append(None)  # Add a placeholder value for the extra row

    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    period=[]
    for hour in df[['day_name','hour']]['hour']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str(hour)+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period

    return df