from flask import Flask, render_template, session, redirect, url_for, request
import random
import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = 'super_secure_secret_key'

DATA_FILE = 'interaction_log.csv'

# Create CSV file with headers if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'ip', 'user', 'version', 'button_id'])

@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        if not name:
            # Optional: you can pass an error message to your intro.html if you want
            return render_template('intro.html', error="Please enter your name.")
        session['name'] = name
        session['version'] = random.choice(['a', 'b'])  # lowercase to match template logic
        return redirect(url_for('home'))
    return render_template('intro.html')

@app.route('/home')
def home():
    if 'name' not in session:
        return redirect(url_for('intro'))

    version = session.get('version', 'a')
    name = session.get('name')

    if version == 'a':
        return render_template('version_a.html', name=name)
    else:
        return render_template('version_b.html', name=name)

@app.route('/track', methods=['POST'])
def track():
    data = {
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'ip': request.remote_addr,
        'user': session.get('name', 'anonymous'),
        'version': session.get('version', 'unknown'),
        'button_id': request.form.get('button_id', 'unknown')
    }

    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data['timestamp'], data['ip'], data['user'], data['version'], data['button_id']])

    return '', 204  # No Content

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('intro'))

# Optional: Add a simple results page to show summary counts
@app.route('/results')
def results():
    counts = {'btnA': 0, 'btnB': 0}
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                btn = row['button_id']
                if btn in counts:
                    counts[btn] += 1
    except FileNotFoundError:
        pass

    total = counts['btnA'] + counts['btnB']
    return render_template('results.html', counts=counts, total=total)

if __name__ == '__main__':
    app.run(debug=True)
