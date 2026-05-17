import os
import psycopg2
from psycopg2 import extras

# This function connects to your Render PostgreSQL database

def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    try:
        # Added sslmode='require' for Render security
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        return conn
    except Exception as e:
        print(f"DATABASE ERROR: {e}") # This will show up in your Render Logs
        return None

def process_linking(aadhaar, epic):
    """
    Handles the logic of linking Aadhaar and EPIC.
    Returns a tuple: (Success Status [True/False], Message)
    """
    
    # 1. Basic Validation
    if not aadhaar or not epic:
        return False, "Please provide both Aadhaar Number and EPIC ID."

    connection = get_db_connection()
    if not connection:
        return False, "Database connection failed. Please try again later."

    try:
        cursor = connection.cursor(cursor_factory=extras.RealDictCursor)
        
        # 2. Verify Aadhaar in Master Table
        # Using %s to prevent SQL Injection
        cursor.execute("SELECT full_name FROM Aadhaar_Master WHERE aadhaar_number = %s", (aadhaar,))
        if not cursor.fetchone():
            return False, "The Aadhaar ID provided is not present in the Master Database."

        # 3. Verify EPIC ID in Master Table
        cursor.execute("SELECT epic_id FROM EPIC_Master WHERE epic_id = %s", (epic,))
        if not cursor.fetchone():
            return False, f"The EPIC ID '{epic}' was not found in the Voter List."

        # 4. Check for Existing Link (Duplicate Prevention)
        cursor.execute("SELECT * FROM Aadhaar_EPIC_Link WHERE aadhaar_number = %s OR epic_id = %s", (aadhaar, epic))
        if cursor.fetchone():
            return False, "Security Alert: This Aadhaar or EPIC ID is already linked."

        # 5. Finalize the Database Link
        query = "INSERT INTO Aadhaar_EPIC_Link (aadhaar_number, epic_id) VALUES (%s, %s)"
        cursor.execute(query, (aadhaar, epic))
        connection.commit()
        
        return True, "Identity Authentication Successful! Records have been linked."

    except Exception as e:
        return False, f"System failure: {str(e)}"
    
    finally:
        cursor.close()
        connection.close()
