from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload-csv", methods=["GET", "POST"])
def uplaod_csv():

    if request.method == "POST":

        if  request.files:

            csv = request.files["csv"]

            path = "this should be dynamic"
            csv.save(os.path.join(path, csv.filename))

            return redirect(request.url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd

app = Flask(__name__)

@app.route("/")
def x():
    return render_template("index.html")


@app.route("/upload-csv", methods=["GET", "POST"])
def upload_csv():

    if request.method == "POST":

        if request.files:

            csv_upload = request.files["csv"]
            filename = csv_upload.filename
            csv_upload.save(os.path.join("uploads", csv_upload.filename))

            path = os.path.join("uploads", csv_upload.filename)
            df = pd.read_csv(path)
            new_column = range(12343)
            df['new_column'] = new_column
            df.to_csv(os.path.join("downloads", filename))

            return redirect(url_for('uploaded_file', filename=filename))

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    filename_processed = 'processed' + '-' + filename
    return send_from_directory("downloads", filename, as_attachment=True, attachment_filename=filename_processed)


if __name__ == "__main__":
    app.run(debug=True)