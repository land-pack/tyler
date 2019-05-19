from flask import Flask
from flask import render_template


app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return render_template("edusmart/index.html")

@app.route("/about")
def about():
    return render_template("edusmart/about-us.html")


@app.route("/contact")
def contact():
    return render_template("edusmart/contact.html")

@app.route("/courses")
def courses():
    return render_template("edusmart/courses.html")

@app.route("/course")
def course_detail():
    return render_template("edusmart/course-details.html")
    # return render_template("edusmart/courses.html")

@app.route("/blogs")
def blogs():
    return render_template("edusmart/course-details.html")
    # return render_template("edusmart/courses.html")

@app.route("/single_blog")
def single_blog():
    return render_template("edusmart/course-details.html")
    # return render_template("edusmart/courses.html")
@app.route("/elements")
def elements():
    return render_template("edusmart/elements.html")

@app.route("/bases/map")
def bases_map():
    return render_template("bases/map.html")

if __name__ == '__main__':
    app.run(debug=True, port=5180)