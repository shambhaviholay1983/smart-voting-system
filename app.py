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
import voting_manager

# This function will run every time your app starts/restarts
def setup_database():
    try:
        conn = voting_manager.get_db_connection()
        cur = conn.cursor()
        # Create tables if they don't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Aadhaar_Master (
                aadhaar_number VARCHAR(12) PRIMARY KEY,
                full_name VARCHAR(100)
            );
            CREATE TABLE IF NOT EXISTS EPIC_Master (
                epic_id VARCHAR(20) PRIMARY KEY,
                voter_name VARCHAR(100)
            );
            CREATE TABLE IF NOT EXISTS Aadhaar_EPIC_Link (
                aadhaar_number VARCHAR(12),
                epic_id VARCHAR(20),
                PRIMARY KEY (aadhaar_number, epic_id)
            );
            
            -- Insert test data
            INSERT INTO Aadhaar_Master (aadhaar_number, full_name) 
            VALUES ('123412341234', 'Test User') ON CONFLICT DO NOTHING;
            INSERT INTO EPIC_Master (epic_id, voter_name) 
            VALUES ('ABC1234567', 'Test User') ON CONFLICT DO NOTHING;
        ''')
        conn.commit()
        cur.close()
        conn.close()
        print("Database auto-setup complete!")
    except Exception as e:
        print(f"Auto-setup failed: {e}")

# Run the setup before the app starts
setup_database()

# ... rest of your Flask app code (app = Flask(__name__), etc.)
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
