from flask import Flask, redirect, url_for, render_template, request, send_from_directory

app = Flask(__name__, static_url_path='')


@app.route("/")
def home():
	return render_template("index.html")

@app.route('/<path>')
def fetch(path):
	try: return send_from_directory("/static/img", path+".png")
	except:
		try: return send_from_directory("/static/img", path+".gif")
		except:
			try: return redirect("https://aaerialys.cf/emotes/"+path+".png")
			except: return redirect("https://aaerialys.cf/emotes/"+path+".gif")

if __name__ == "__main__":
	app.run(debug=True)