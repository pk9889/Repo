from flask import Flask, render_template
import getpass
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def htop():
    name = "Your Full Name"
    username = getpass.getuser()
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")
    try:
        top_output = subprocess.run(
            "top -b -n 1 | head -10", 
            shell=True, 
            capture_output=True, 
            text=True,
            check=True
        ).stdout
    except subprocess.CalledProcessError as e:
        top_output = f"Error running top command: {e}"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>System Info - htop</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            h1 {{
                color: #333;
            }}
            .info {{
                background: #fff;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }}
            pre {{
                background: #222;
                color: #0f0;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>

        <h1>System Info</h1>
        <div class="info">
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {time_str}</p>
        </div>

        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
