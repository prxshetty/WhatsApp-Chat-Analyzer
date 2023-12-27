mkdir -p ~/.streamlit/

echo "[theme]\n\
primaryColor = '#575fe8'\n\
backgroundColor = '#f5f7f3'\n\
secondaryBackgroundColor = '#c9eab8'\n\
textColor = '#262730'\n\
font = 'sans serif'\n\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml


