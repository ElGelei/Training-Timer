from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return redirect(url_for('create_routine'))

@app.route('/create', methods=['GET', 'POST'])
def create_routine():
    if request.method == 'POST':
        exercises = request.form.getlist('exercise')
        durations = request.form.getlist('duration')
        session['routine'] = list(zip(exercises, durations))
        return redirect(url_for('start_training'))
    return render_template('create.html')

@app.route('/train', methods=['GET'])
def start_training():
    routine = session.get('routine', [])
    return render_template('train.html', routine=routine)

if __name__ == '__main__':
    app.run(debug=True)