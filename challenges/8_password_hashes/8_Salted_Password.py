# You can add to this file in the editor 
import pyotp    # generates one-time passwords
import sqlite3  # database for username/passwords
import hashlib  # secure hashes and message digest
import uuid     # for creating universally unique identifiers
import os

from flask import Flask, request
app = Flask(__name__) # always use two underscores

db_name = 'odisee.db'

# flask code ot create web content at the root path
@app.route('/')
def index():
    return 'Welcome to the hands-on lab for an evolution of password systems!'

# Flask code to configure the server to store a username and password as a hash
################# Password Hashing######################
@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    ## connect to database
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    ## create the table with three colums, username, hash and salt
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH(USERNAME TEXT PRIMARY KEY NOT NULL,HASH TEXT NOT NULL, SALT TEXT NOT NULL);''')
    conn.commit()
    try:
        password = request.form['password'] # get password from the curl statement = requests in python
        salt = os.urandom(32) # generate the salt
        hash_value = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000) # create the hash with the salt combined
        c.execute("""INSERT INTO USER_HASH (USERNAME, HASH, SALT) VALUES (?,?,?);""",(request.form['username'], hash_value.hex(), salt)) # store the values in the database
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    print('username: ', request.form['username'], ' password: ',request.form['password'], ' hash: ', hash_value)
    return "signup success\n"

# verify if the username and password are stored as a hash, and only a hash
def verify_hash(username, password): # get username and password from the curl command = requests lib in python
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH, SALT FROM USER_HASH WHERE USERNAME ='{0}'".format(username) # select the hash and salt from the db for a specific username
    c.execute(query)
    records = c.fetchone() # store both values (hash and salt) in the records list
    conn.close()
    if not records:
        return False
    # recalculate the salted hash with the salt value from the database and the passwword input from the curl login statement
    # if that calcualation matches the salted hash stored in the db, the user can login.
    return records[0] == hashlib.pbkdf2_hmac('sha256', password.encode(), records[1], 100000).hex()

# read the parameters from the http post request
@app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = 'login success\n'
        else:
            error = 'Invalid username/password\n'
    else:
        error = 'Invalid Method\n'
    return error
    
# create local web service on port 5000 with a self signed TLS certificate
# ssl_context='adhoc' allows you to run an application over HTTPS without havint to use certificates
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')