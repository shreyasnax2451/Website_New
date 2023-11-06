from flask import Flask, render_template, jsonify

app = Flask(__name__)

MOVIES = [
    {
    'id':1,
    'name':'REWRITING MALLORY - A SHORT FILM REVIEW',
    'review':'Rewriting Mallory is an excellent short that takes the audience on an emotional rollercoaster.'
    },
    {
        'id':2,
        'name':'SISYPHUS UNBOUND',
        'review':'"Sisyphus Unbound" is an excellent showcase for debut director Ryan Fleming displaying his talent for story telling.'

    }
]

@app.route("/")
def hello():
    return render_template('home.html', movies = MOVIES) 

@app.route("/api/reviews")
def list_jobs():
    return jsonify(MOVIES)

if __name__ == '__main__':
    app.run(debug=True) 