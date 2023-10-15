from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.static_folder = 'static'
JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco',
    'salary': '$120,000'
}, {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Chicago',
    'salary': '$110,000'
}, {
    'id': 4,
    'title': 'Machine Learning Engineer',
    'location': 'Los Angeles',
    'salary': '$140,000'
}]


@app.route("/")
def hello_world():
  # return "Hello, World"
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
