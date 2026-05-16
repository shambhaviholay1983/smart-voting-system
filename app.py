# from flask import Flask, render_template

# ही ओळ तपासा. 'app' हे नाव लहान अक्षरात (lowercase) असणे आवश्यक आहे.
#app = Flask(__name__) 

#@app.route('/')
#def index():
#    return "Hello World phd"

# This imports everything or specific items from your voting_manager.py file
from flask import Flask, render_template
# This imports everything or specific items from your voting_manager.py file
import voting_manager 
# OR: from voting_manager import verify_voter_biometrics, initialize_voting_db

app = Flask(__name__)

@app.route('/verify-vote')
def verify():
    # Example of accessing a function inside voting_manager
    # success = verify_voter_biometrics(voter_id)
    return "Verification Page"
