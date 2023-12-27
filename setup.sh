mkdir -p ~/.streamlit/

echo "\[theme]
primaryColor = '#575fe8'
backgroundColor = '#f5f7f3'
secondaryBackgroundColor = '#c9eab8'
textColor = '#262730'
font = 'sans serif'
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml


