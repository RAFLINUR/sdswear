from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def handle_contact(data=None):
    """Handle contact form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'subject']
        if not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'message': 'Semua field harus diisi'
            }), 400
        
        # In a real app, you would save this to a database
        # For now, we'll just acknowledge receipt
        print(f"Contact form submission: {data}")
        
        return jsonify({
            'success': True,
            'message': 'Pesan Anda telah diterima. Kami akan segera menghubungi Anda!'
        }), 200
        
    except Exception as e:
        print(f"Error in contact form: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Terjadi kesalahan. Silakan coba lagi.'
        }), 500

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
