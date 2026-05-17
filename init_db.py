import psycopg2
import os

# Use your EXTERNAL Connection String from Render here for a one-time setup
conn = psycopg2.connect("your_external_url_here")
cur = conn.cursor()

# Create the tables your voting_manager expects
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
''')

# Add one test record so you can test the linking logic
cur.execute("INSERT INTO Aadhaar_Master (aadhaar_number, full_name) VALUES ('123412341234', 'Test User') ON CONFLICT DO NOTHING;")
cur.execute("INSERT INTO EPIC_Master (epic_id, voter_name) VALUES ('ABC1234567', 'Test User') ON CONFLICT DO NOTHING;")

conn.commit()
print("Tables created successfully!")
cur.close()
conn.close()
