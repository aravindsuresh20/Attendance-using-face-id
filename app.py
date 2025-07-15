from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute/<filename>')
def execute_file(filename):
    try:
        subprocess.run(['python', f'{filename}.py'])
        return f'Successfully executed: {filename}.py'
    except Exception as e:
        return f'Error executing {filename}.py: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)

