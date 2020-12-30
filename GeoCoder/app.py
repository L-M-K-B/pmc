from flask import Flask, render_template, request

from add_geo_data import process_content

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/result/", methods=['POST'])
def result_page():
    if request.method == 'POST':
        original_file = request.files["toBeUploaded"]

        if not original_file:
            return render_template("index.html", text="Please choose a file prior to pushing the upload button.")

        if not original_file.content_type == "text/csv":
            return render_template("index.html", text="Please only upload CSV files.")

        updated_file = process_content(original_file)
        print(updated_file)

        return render_template("result.html")

        # return render_template("index.html", text="Please make sure there is an address column in your file.")


if __name__ == "__main__":
    app.debug = True
    app.run()
