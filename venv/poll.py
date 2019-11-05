from flask import Flask,render_template
import os
poll_data={
    'question':'which web framework do you use?',
    'fields':['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject']
    }

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('poll.html',data=poll_data)

if __name__ == "__main__":
    app.run(debug=True)    