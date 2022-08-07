from flask import Flask, render_template
import random

app = Flask(__name__)

# Copy Image Address
images = [
    "https://www.adorama.com/alc/wp-content/uploads/2021/05/bird-wings-flying-feature.gif",
    "https://i.pinimg.com/originals/42/1d/80/421d8028549bb25e1f1e09ebe606d7c4.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
