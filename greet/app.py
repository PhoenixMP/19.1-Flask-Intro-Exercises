from flask import Flask, request

app = Flask(__name__)
print('hi')


@app.route('/')  # this is a decorator
def home_page():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p> This is the Greet App </p>
            
        </body>
    </html>
    """
    return html


@app.route('/welcome')
def say_welcome():
    html = """
     <h1>Welcome</h1>
    """
    return html


greetings = {
    "home": "welcome home",
    "back": "welcome back"
}


@app.route('/welcome/<greeting>')
def do_a_greet(greeting):
    greet = greetings[greeting]
    html = f"""
     <h1>{greet}</h1>
    """
    return html
