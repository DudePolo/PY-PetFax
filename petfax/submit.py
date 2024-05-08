from flask import ( Blueprint, render_template, request )
bp = Blueprint('submit', __name__, url_prefix='/facts')

@bp.route('/new', methods=('GET', 'POST'))
def new_fact():
    if request.method == 'POST':
        # Handle form submission here
        fact_text = request.form['fact_text']
        # Process the submitted data (e.g., save to database)
        return 'Fact submitted: {}'.format(fact_text)
    else:
        # Render the form template for GET requests
        return render_template('submitForm.html')