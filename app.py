from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key='YOUR API KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logo', methods=['GET','POST'])
def generate_image():
    if request.method == 'POST':
        user_prompt = request.form['logo']

        response = client.images.generate(
            model="dall-e-3",
            prompt = f"You're a professional logo designer. Create a logo based on the following description: {user_prompt}",
            size="1024x1024",
            quality="standard",
            n=1,
            )

        image = response.data[0].url
        return render_template('logo.html', image=image, prompt=user_prompt)

    return render_template('logo.html')

@app.route('/download')
def download_logo():
    # TODO implement download button 
    pass


if __name__ == '__main__':
    app.run(debug=True)