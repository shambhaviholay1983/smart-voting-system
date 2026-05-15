from flask import Flask

# ही ओळ तपासा. 'app' हे नाव लहान अक्षरात (lowercase) असणे आवश्यक आहे.
app = Flask(__name__) 

@app.route('/')
def index():
    return "Hello World phd"
