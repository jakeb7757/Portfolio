# Portfolio Gallery 🎨

A modern art gallery-style portfolio website built with Flask, designed to showcase Master's program projects as "art exhibits."

## Features

- **Gallery Theme**: Modern, minimalist art gallery aesthetic
- **Project Exhibits**: Each project displayed as an art exhibit with detailed views
- **Category Filtering**: Filter projects by category (Cloud Architecture, Data Analytics, etc.)
- **Responsive Design**: Works beautifully on all devices
- **Cloud Run Ready**: Configured for easy deployment to Google Cloud Run

## Project Structure

```
Portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Container configuration
├── cloudbuild.yaml       # Google Cloud Build config
├── .dockerignore         # Docker ignore patterns
├── static/
│   ├── css/
│   │   └── style.css     # Gallery styling
│   ├── js/
│   │   └── main.js       # Interactive features
│   └── images/           # Project images
└── templates/
    ├── base.html         # Base template
    ├── gallery.html      # Main gallery page
    ├── exhibit.html      # Individual project view
    ├── about.html        # About page
    ├── contact.html      # Contact page
    └── 404.html          # Error page
```

## Local Development

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Visit `http://localhost:8080`

## Adding New Projects

Edit `app.py` and add new entries to the `EXHIBITS` list:

```python
{
    "id": "your-project-id",
    "title": "Your Project Title",
    "category": "Category Name",
    "description": "Project description...",
    "technologies": ["Tech1", "Tech2", "Tech3"],
    "image": "your-image.svg",
    "status": "Live",  # or "In Development", "In Progress"
    "link": "https://your-project-url.com",
    "github": "https://github.com/your/repo"
}
```

## Deployment to Google Cloud Run

### Prerequisites
- Google Cloud SDK installed
- A GCP project with billing enabled
- Cloud Run API enabled

### Deploy with Cloud Build (Recommended)

```bash
# Submit build to Cloud Build
gcloud builds submit --config cloudbuild.yaml

# Your app will be deployed to:
# https://portfolio-gallery-XXXXXX-uc.a.run.app
```

### Manual Deployment

```bash
# Set your project
gcloud config set project YOUR_PROJECT_ID

# Build and push the container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/portfolio-gallery

# Deploy to Cloud Run
gcloud run deploy portfolio-gallery \
  --image gcr.io/YOUR_PROJECT_ID/portfolio-gallery \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Customization

### Colors
Edit the CSS custom properties in `static/css/style.css`:

```css
:root {
    --color-accent: #c9a86c;  /* Gold accent color */
    --color-bg: #0a0a0a;      /* Background color */
    /* ... more variables */
}
```

### Fonts
The site uses:
- **Playfair Display** for headings (elegant, serif)
- **Inter** for body text (clean, modern)

### Adding Categories
Update the `CATEGORIES` list in `app.py`:

```python
CATEGORIES = ["All", "Cloud Architecture", "Data Analytics", "Machine Learning", "Web Development"]
```

## Technologies Used

- **Flask** - Python web framework
- **Gunicorn** - Production WSGI server
- **Docker** - Containerization
- **Google Cloud Run** - Serverless deployment

## License

MIT License - Feel free to use this as a template for your own portfolio!
