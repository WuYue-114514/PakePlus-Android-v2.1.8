import webview
import os
def load_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()
if __name__ == '__main__':
    html = load_html()
    window = webview.create_window(
        'MC服务器状态查询器',
        html=html,
        width=1400,
        height=800,
        min_size=(800, 600),
        resizable=True
    )
    webview.start()