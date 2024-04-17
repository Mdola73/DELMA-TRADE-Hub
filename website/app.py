from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'infos@delmatradehub.org'
app.config['MAIL_PASSWORD'] = 'your_password'
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')  #new roote for About Us page
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/contact', methods=['GET', 'POST'])
def Contact():
    if request.method == 'POST':
        print("Handling form submission...")
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"Reaceived form data - Name: {name}, Email: {email}, Message: {message}")
        msg = Message(subject='Feedback from Contact Form',
                      sender=email,
                      recipients=['infos@delmatradehub.org'])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        mail.send(msg)
        
        print("Form submission handled successfully")
        return redirect(url_for('thank_you()'))
    return render_template('contact.html')
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

#process the form submission(e.g, send email, store in database)
if __name__ == '__main__':
    app.run(debug=True)
    