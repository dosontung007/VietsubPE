from flask import Flask, render_template
app = Flask(__name__)


@app.route("/problem=<pr>")
def render(pr):
    return render_template('Problem_{}.html'.format(pr))


if __name__ == '__main__':
    app.run(debug=True)
