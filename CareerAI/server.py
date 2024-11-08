from flask import Flask, render_template, request


app = Flask("Resume LLMs")

@app.route("/")
def render_index_page():
   
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000)
