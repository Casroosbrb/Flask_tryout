from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body>
            <p>Welkom op mijn Flask-website! Hieronder heb je de foto van de opdracht</p>
            <img src="/image" alt="Afbeelding">
        </body>
    </html>
    '''

@app.route('/image')
def serve_image():
    return send_from_directory('.', 'image.png')

if __name__ == "__main__":
    app.run(debug=True)
