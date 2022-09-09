from flask import Flask
from utility.Sites import Sites
from flask import Flask, render_template, request

app = Flask(__name__)
site_builder = Sites()


@app.route("/", methods=['GET'])
def form():
    return render_template("form.html")


@app.route("/site", methods=['GET'])
def home():
    print(request.args.get("size", ""))
    new_site = site_builder.create_site(int(request.args.get("size", "")))

    return render_template("site.html", site=new_site)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
