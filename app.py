from project import app

@app.route("/")
def index():
	return ("<h1>POC<h1>")


if __name__ == "__main__":
	app.run(debug=True)