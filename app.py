from flask import Flask, render_template, request, jsonify
import sys
import webbrowser
import threading
import time

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    message = 'Hello Flask! Return string by app.py'
    #return render_template('index.html')
    return render_template('index.html', message=message)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = f'Name: {name}, Email: {email}'
    return message

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/about_post', methods=['POST'])
def about_post():
    data = request.get_json()
    message = data['message']
    return jsonify({'result': 'You entered: ' + message})

@app.route('/about_new')
def about_new():
    return render_template('about_bootrap_5_3.html')

@app.route('/about_new_post', methods=['POST'])
def about_new_post():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = data['message']
    total_str = f'Name: {name}, Email: {email}, Message: {message} '
    return total_str   

def open_browser():
    #print(webbrowser._browsers)
    #the result is empty....
    
    webbrowser.open('http://127.0.0.1:5000')
    
'''
#not working....    
def check_browser_closed():
    time.sleep(1)
    while True:
        if webbrowser.BackgroundBrowser(webbrowser.get()).is_active:
            time.sleep(1)
        else:
            exit(0)
'''    
if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run()
    