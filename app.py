from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

class Todo(db.Model):
	id = db.Coloumn(db.Integer, primary_key=True)
	content = db.Coloumn(db.String(200), nullable=False)
	date_created = db.Coloumn(db.DateTime, default = datetime.utcnow)
	

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True)