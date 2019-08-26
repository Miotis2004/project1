from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
        post = get_posts()
        posts = []
        for po in post:
            posts.append((po['userName'], po['userPost']))
        #jposts = jsonify(posts['userName'], posts['userPost'])
        return render_template('index.html', posts=posts)
    if request.method == 'GET':
        post = get_posts()
        posts = []
        for po in post:
            posts.append((po['userName'], po['userPost']))
        return render_template('index.html', posts=posts)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(debug=True)

