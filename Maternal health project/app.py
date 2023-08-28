from flask import Flask, render_template, request, redirect, url_for
import africastalking

app = Flask(__name__)

# Configure Africa's Talking credentials
africastalking_username = ""
africastalking_api_key = ""

africastalking.initialize(africastalking_username, africastalking_api_key)
sms = africastalking.SMS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST', 'GET'])
def send_sms():
    recipient_phone = request.form.get('recipient_phone')
    message = "Welcome to Well Mother. We are glad you have joined us. This is how you will be receiving daily updates on maternal health."

    try:
        # Send SMS using Africa's Talking API
        response = sms.send(message, [recipient_phone])
        return f"SMS sent successfully to {recipient_phone}. Message ID: {response['SMSMessageData']['Message']['Id']}"
    except Exception as e:
        return f"Failed to send SMS: {str(e)}"

@app.route('/static/css/<path:filename>')
def css_file(filename):
    return send_from_directory('static/css', filename), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    app.run(debug=True)


