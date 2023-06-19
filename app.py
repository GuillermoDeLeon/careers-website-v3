from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Benaluru, India',
    'salary': '$110,000'
  },
    {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'San Antonio, TX',
    'salary': '$90,000'
  },
    {
    'id': 3,
    'title': 'Baseball Pitcher',
    'location': 'Helotes, TX',
    'salary': '$35,500'
  },
    {
    'id': 4,
    'title': 'Rock Climber',
    'location': 'New York, NY',
    'salary': '$11,000'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Guillermo D Careers')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)