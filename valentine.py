from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Be My Valentine 💖</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      background: #0f172a;
      color: white;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      background: white;
      color: black;
      padding: 40px;
      border-radius: 20px;
      text-align: center;
      width: 350px;
    }

    h1 span {
      color: #22c55e;
    }

    .bear {
      width: 120px;
      margin: 10px 0;
    }

    .buttons {
      margin-top: 20px;
    }

    button {
      font-size: 18px;
      padding: 10px 25px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      margin: 0 10px;
    }

    .yes-button {
      background: #ec4899;
      color: white;
      font-size: 20px;
    }

    .no-button {
      background: #e5e7eb;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Be My <span>Valentine</span></h1>
    <img src="https://i.imgur.com/3ZQ3Z5k.png" class="bear" />
    <p>Will you be my Valentine?</p>

    <div class="buttons">
      <button class="yes-button" onclick="handleYesClick()">Yes</button>
      <button class="no-button" onclick="handleNoClick()">No</button>
    </div>
  </div>

  <script>
    let messageIndex = 0;
    const messages = [
      "No 😢",
      "Are you sure?",
      "Pleaseee 🥺",
      "Don't break my heart 💔",
      "Last chance 😭",
      "Say yes already ❤️"
    ];

    function handleNoClick() {
      const noButton = document.querySelector(".no-button");
      const yesButton = document.querySelector(".yes-button");

      noButton.textContent = messages[messageIndex];
      messageIndex = (messageIndex + 1) % messages.length;

      const currentSize = parseFloat(
        window.getComputedStyle(yesButton).fontSize
      );
      yesButton.style.fontSize = `${currentSize * 1.3}px`;
    }

    function handleYesClick() {
      window.location.href = "/yes";
    }
  </script>
</body>
</html>
"""

yes_html = """
<!DOCTYPE html>
<html>
<head>
  <title>Yay 💖</title>
  <style>
    body {
      background: #ffe4e6;
      font-family: Arial;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      text-align: center;
    }
    h1 {
      color: #ec4899;
      font-size: 50px;
    }
  </style>
</head>
<body>
  <h1>Yayyy! 💕 I knew it 😍</h1>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(index_html)

@app.route("/yes")
def yes():
    return render_template_string(yes_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
