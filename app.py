"""
Portfolio Website - Modern Art Gallery Style
A Flask application to showcase Master's program projects as art exhibits
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)

# Project/Exhibit data - easily expandable
EXHIBITS = [
    {
        "id": "flask-gcr-app",
        "title": "Flask on Google Cloud Run",
        "category": "Cloud Architecture",
        "description": "A production Flask application deployed on Google Cloud Run, demonstrating containerization, CI/CD pipelines, and serverless architecture.",
        "technologies": ["Python", "Flask", "Docker", "Google Cloud Run", "Cloud Build"],
        "image": "flask-app.svg",
        "status": "Live",
        "link": "#",  # Add your actual link
        "github": "#"  # Add your GitHub link
    },
    {
        "id": "django-gcr-app",
        "title": "Django Cloud Application",
        "category": "Cloud Architecture",
        "description": "A Django web application showcasing full-stack development with cloud-native deployment strategies.",
        "technologies": ["Python", "Django", "Docker", "Google Cloud Run", "PostgreSQL"],
        "image": "django-app.svg",
        "status": "In Development",
        "link": "#",
        "github": "#"
    },
    {
        "id": "data-analytics-1",
        "title": "Data Analytics Project",
        "category": "Data Analytics",
        "description": "Exploratory data analysis and visualization project demonstrating statistical analysis and insights extraction.",
        "technologies": ["Python", "Pandas", "Matplotlib", "Seaborn", "Jupyter"],
        "image": "analytics.svg",
        "status": "In Progress",
        "link": "#",
        "github": "#"
    },
]

CATEGORIES = ["All", "Cloud Architecture", "Data Analytics", "Machine Learning", "Web Development"]


@app.route("/")
def gallery():
    """Main gallery view - the landing page"""
    return render_template("gallery.html", exhibits=EXHIBITS, categories=CATEGORIES)


@app.route("/exhibit/<exhibit_id>")
def exhibit(exhibit_id):
    """Individual exhibit/project detail view"""
    exhibit_data = next((e for e in EXHIBITS if e["id"] == exhibit_id), None)
    if exhibit_data is None:
        return render_template("404.html"), 404
    return render_template("exhibit.html", exhibit=exhibit_data)


@app.route("/about")
def about():
    """About page - your background and program info"""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Contact page"""
    return render_template("contact.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
