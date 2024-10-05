from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key='YOUR API KEY')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image', methods=['POST'])
def generate_image():

    prompt = request.form.get('image')

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )

    image = response.data[0].url

    return render_template('index.html', image=image, prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)