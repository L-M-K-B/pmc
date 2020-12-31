from flask import Flask, render_template, request, send_from_directory

from handle_data import process_content

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

        new_file_name, html_table = process_content(original_file)

        return render_template("result.html", table=html_table, download_link=f'/converted_files/{new_file_name}')

        # return render_template("index.html", text="Please make sure there is an address column in your file.")


@app.route('/converted_files/<path:filename>')
def send_file(filename):
    return send_from_directory('converted_files', filename)


if __name__ == "__main__":
    app.debug = True
    app.run()
