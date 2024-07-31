from flask import Flask, request, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Remplacez 'your_secret_key' par une clé secrète sécurisée

@app.route('/')
def home():
    return redirect('/create')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        exercise = request.form.get('exercise')
        duration = request.form.get('duration')
        if 'routine' not in session:
            session['routine'] = []
        # Ajouter l'exercice à la session
        session['routine'].append((exercise, duration))
        session.modified = True  # Marquer la session comme modifiée
        return redirect('/create')
    return render_template('create.html', routine=session.get('routine', []))

@app.route('/train')
def train():
    routine = session.get('routine', [])
    return render_template('train.html', routine=routine)

@app.route('/remove/<int:index>', methods=['POST'])
def remove(index):
    if 'routine' in session and 0 <= index < len(session['routine']):
        del session['routine'][index]
        session.modified = True  # Marquer la session comme modifiée
    return redirect('/create')

if __name__ == '__main__':
    app.run(debug=True)