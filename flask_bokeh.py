from flask import Flask, render_template
from bokeh.plotting import figure, output_notebook, show
from bokeh import embed
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Bokeh example</h1><a href=/plot>Go to plot page</a>'

def make_my_plot(col):
    # this col_from_web has been added to the example and should be updated by the col attribute coming in through /plot/<col>
    col_from_web ="green"
    a = 10
    # prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x]
    y1 = [a**i for i in x]
    y2 = [a**(i**2) for i in x]

    # create a new plot
    p = figure(
       tools="",
       y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
       x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x")
    p.circle(x, x, legend="y=x", fill_color="white", size=8)
    p.line(x, y0, legend="y=x^2", line_width=3)
    p.line(x, y1, legend="y=10^x", line_color=col)
    p.circle(x, y1, legend="y=10^x", fill_color=col, line_color=col, size=6)
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

    # show the results
    return p

@app.route('/plot/')
@app.route('/plot/<color>')
def hello(color='red'):
    plot = make_my_plot(color)
    script, div = embed.components(plot)
    return render_template(
        'bokeh.html',
        script=script,
        div=div
        )


if __name__ == '__main__':
	app.run(debug=True)
