from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/')
def home_view():
    return render_template('first.html')


@app.route('/s')
def second_view():
    res = make_response(render_template('second.html'))
    res.set_cookie('fd', request.args.get('fd'))
    return res


@app.route('/t')
def third_view():
    res = make_response(render_template('third.html'))
    res.set_cookie('sd', request.args.get('sd'))
    return res


@app.route('/final')
def final_view():
    return render_template('final.html')


if __name__ == '__main__':
    app.run(debug=True)
