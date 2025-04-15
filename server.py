from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file, Response

from src.download_mp3 import download_mp3_from_youtube


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    """
    Standard route ('/') when entering the website. Will return the template index.html.

    :returns: html file of index
    """

    return render_template('index.html')


@app.route('/downloadMP3', methods=['POST'])
def downloadMP3():
    print("DEINE MOM")

    link = request.get_json()["ytLink"]

    print(link)

    download_mp3_from_youtube(link)

    return send_file(f"output/currentSong.mp3", mimetype='audio/mpeg', as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)
