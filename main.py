from flask import Flask, render_template
import pafy

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/music")
def music():
	url = "https://www.youtube.com/watch?v=3EmUmbhDRiY"
	video = pafy.new(url)
	audio = video.getbestaudio()
	audio_url = audio.url
	return render_template("music.html", audio_url=audio_url)

if __name__ == "__main__":
	app.run(debug=True)
