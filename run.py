from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing/landing-page.html')


@app.route('/processor')
def processor():
    return render_template('processor/processor.html')

@app.route('/user')
def user():
    return render_template('processor/user.html')


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		print(request.files['file'].filename)
	return redirect(url_for('processor'))

@app.route('/upload')
def upload_page():
	return render_template('processor/upload.html')