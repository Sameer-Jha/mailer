import smtplib, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from secrets import user
from secrets import password


def simple_mail():
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}

    This is a test e-mail message."""

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(user,  password)
        server.sendmail(sender, receiver, message)


def embedded_mail():
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = "Private Person <from@example.com>"
    message["To"] = "A Test User <to@example.com>"
    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a>
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(user,  password)
        server.sendmail(sender, receiver, message.as_string())


def attachment_mail():
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"
    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "from@example.com"
    receiver_email = "to@example.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "document.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(user,  password)
        server.sendmail(sender, receiver, text)


if __name__ == "__main__":
    simple_mail()

## Mutimailer can be easily developed using csv or json data input
