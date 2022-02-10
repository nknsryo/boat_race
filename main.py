from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/main", methods=["GET"])
def get_race_track():
    return render_template("main.html")


@app.route("/main", methods=["POST"])
def post_race_track():
    tracks = request.form.getlist("track")
    rate1 = request.form["rate-01"]
    rate2 = request.form["rate-02"]
    bet_price = request.form["bet"]
    deposit_price = request.form["deposit"]
    message = "登録が完了しました！"
    return render_template("main.html", tracks=tracks, rate1=rate1, rate2=rate2, bet_price=bet_price,
                           deposit_price=deposit_price, message=message)


if __name__ == '__main__':
    app.run(debug=True)

