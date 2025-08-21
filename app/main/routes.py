from flask import Blueprint, render_template

# Blueprint Configuration
main = Blueprint(
    'main', __name__,
    template_folder='../templates',
    static_folder='../static'
)

@main.route('/')
def index():
    """Homepage."""
    return render_template('index.html')