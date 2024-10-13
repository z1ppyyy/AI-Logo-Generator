## AI Logo Generator 🌍

## **AI Logo Generator** is a web-based application that allows users to generate logos for their company or personal projects using AI-based image generation models. The user can simply input a prompt describing the desired logo, and the application will return a custom logo design based on the input.

## Table of Contents

- [Demo](#demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Demo


https://github.com/user-attachments/assets/bc7cd7d7-9f1d-46e4-9ce3-ff7ca1b00752



## Requirements
- Python 3.12 or later
- An OpenAI API key (for DALL-E)

## Installation
To run this project locally, follow these steps:

Setup Instructions
1. Clone the repository:

```
git clone https://github.com/yourusername/ai-logo-generator.git
```

Navigate to the project directory:

```
cd ai-logo-generator
```

Paste your API KEY obtained from the https://platform.openai.com/
```
client = OpenAI(api_key='YOUR API KEY')
```

Run the application:

```
flask run
```

The app will be available at http://127.0.0.1:5000/.

## Usage
1. Open the browser and navigate to http://127.0.0.1:5000/.
2. Enter a prompt describing your desired logo, e.g., "A modern tech logo for a startup.".
3. Click on Generate and wait for the AI to create a custom logo for you.
4. The generated logo will be displayed below the input form.


## License
This project is licensed under the MIT License. See the LICENSE file for more details.
