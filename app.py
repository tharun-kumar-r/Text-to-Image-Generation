from flask import Flask, render_template, request
import requests
from io import BytesIO
import base64

app = Flask(__name__)

API_KEY = "e1eef6c98ac5d97555103d5effd1641797af967d19b089a1ecbc7b42c5135f2493d70fbe7fabe79847427843dad0676b"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
                          files={'prompt': (None, prompt, 'text/plain')},
                          headers={'x-api-key': API_KEY})
        if r.ok:
            image_base64 = base64.b64encode(r.content).decode('utf-8')
            return render_template('index.html', image_data=image_base64)
        else:
            return render_template('index.html', error=r.text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
