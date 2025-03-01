from flask import Flask, render_template, send_from_directory
import os
import random
import math

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# Ensure the static/assets directory exists
os.makedirs(os.path.join(app.static_folder, 'assets'), exist_ok=True)

# Copy assets if they don't exist in static folder
assets = ['video.mp4', 'headshot.jpg', 'Prerna Singhal.pdf', 'image_1740700979888.png']
for asset in assets:
    src = os.path.join('attached_assets', asset)
    dst = os.path.join(app.static_folder, 'assets', asset)
    if os.path.exists(src) and not os.path.exists(dst):
        import shutil
        shutil.copy2(src, dst)

def generate_visualization_svg():
    """Generate a simple SVG visualization of actuarial data patterns"""
    width, height = 800, 400
    points = []

    # Generate sample data points
    for i in range(50):
        x = i * (width/50)
        y = height/2 + math.sin(i/5) * 50 + random.randint(-20, 20)
        points.append((x, y))

    # Create SVG content
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#212529"/>'

    # Add grid lines
    for i in range(0, width, 50):
        svg += f'<line x1="{i}" y1="0" x2="{i}" y2="{height}" stroke="#2c3136" stroke-width="1"/>'
    for i in range(0, height, 50):
        svg += f'<line x1="0" y1="{i}" x2="{width}" y2="{i}" stroke="#2c3136" stroke-width="1"/>'

    # Create path from points
    path = "M " + " L ".join([f"{x},{y}" for x, y in points])
    svg += f'<path d="{path}" fill="none" stroke="#0d6efd" stroke-width="2"/>'

    # Add data points
    for x, y in points:
        svg += f'<circle cx="{x}" cy="{y}" r="3" fill="#0d6efd"/>'

    svg += '</svg>'

    # Save the SVG
    svg_path = os.path.join(app.static_folder, 'assets', 'ai_visualization.svg')
    with open(svg_path, 'w') as f:
        f.write(svg)

# Generate the visualization on startup
generate_visualization_svg()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn-more')
def learn_more():
    return render_template('learn_more.html')

@app.route('/ai-content')
def ai_content():
    return render_template('ai_content.html')