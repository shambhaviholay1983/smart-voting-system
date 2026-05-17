import os
from flask import Flask, render_template, request
import voting_manager # This is your updated, non-Tkinter file

app = Flask(__name__)

@app.route('/')
def index():
    # Show a simple input page instead of a Tkinter window
    return '''
        <form action="/link" method="post">
            <input type="text" name="aadhaar" placeholder="Aadhaar Number">
            <input type="text" name="epic" placeholder="EPIC ID">
            <button type="submit">Link Identities</button>
        </form>
    '''

@app.route('/link', methods=['POST'])
def link():
    aadhaar = request.form.get('aadhaar')
    epic = request.form.get('epic')
    
    # Use the function from your voting_manager.py
    success, message = voting_manager.process_linking(aadhaar, epic)
    
    if success:
        return f"<h1>Success!</h1><p>{message}</p>"
    else:
        return f"<h1>Error</h1><p>{message}</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
