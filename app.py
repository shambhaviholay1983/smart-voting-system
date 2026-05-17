from flask import Flask
# ... other imports ...

app = Flask(__name__) # <--- This variable MUST be named 'app'

# ... your routes ...

if __name__ == "__main__":
    app.run()
