from flask import Flask, render_template, request, redirect, escape, session, copy_current_request_context
from mysql.connector import Connect
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread


app = Flask(__name__)

app.secret_key = "NigdyNieZgadniesz"

app.config['dbconfig']={'host':'127.0.0.1',
                        'user': 'vsearch',
                        'password': 'password',
                        'database': 'vsearchlogDB',}


@app.route('/login')
def login():
    session['logged_in']=True
    return 'You are logged in'

@app.route('/logout')
def logout():
    session.pop('logged_in')
    return "You have logged off"

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        with UseDatabase(app.config['dbconfig']) as cursor:
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res, ))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('Logging failed with error ', str(err))
    return render_template('results.html', the_title='Welcome to search4letters', the_phrase=phrase, the_letters=letters, the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters')

@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    contents = []
    error_message = ""
    _SQL = """select phrase, letters, ip, browser_string, results from log"""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            cursor.execute(_SQL)
            contents = cursor.fetchall()
    except ConnectionError as err:
        error_message = "Failed to connect to db"            
        print("Is the database up and running?", str(err))
    except CredentialsError as err:
        error_message = "Invalid credentials for db logging"
        print("There is a problem with db credentials", str(err))
    except SQLError as err:
        error_message = "There is an issue with SQL command"
        print("Is your SQL query correct?", str(err))
    except Exception as err:
        error_message = "Some other problem"
        print("Something went wrong", str(err))
    titles = ('Phrase','Letters','Remote Address','Agent','Result')
    return render_template('viewlog.html',
                            the_title='Logs',
                            the_row_titles = titles,
                            the_data = contents,
                            the_message = error_message)

if __name__ == '__main__':
    app.run(debug=True)