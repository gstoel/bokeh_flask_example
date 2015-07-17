from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Bokeh example</h1><a href=/plot>Go to plot page</a>'

@app.route('/plot/')
@app.route('/plot/<color>')
def hello(color='red'):
    return render_template('bokeh.html', col=color)


if __name__ == '__main__':
	app.run(debug=True)
