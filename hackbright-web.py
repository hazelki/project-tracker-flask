from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    print first, last, github

    project_results = hackbright.get_grades_by_github(github)



    html = render_template('student_info.html', first=first, last=last, github=github, project_results=project_results)

    return html


@app.route('/')    
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    html = render_template('student_info.html', first=first, last=last, github=github)

    return html

@app.route("/project")
def get_project():
    """List information about the project"""
    title = request.args.get('title')
    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("project_info.html", title=title, description=description, max_grade=max_grade)

    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
