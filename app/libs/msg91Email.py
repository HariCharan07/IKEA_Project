import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendmail(toAddress, fromName, fromAddress, subject, body):
    try:
    
        # Set up SMTP server details
        smtp_server = 'smtp.mailer91.com'
        smtp_port = 587

        # Set up email account details
        sender_email = 'emailer@delivery.koneqto.com'
        sender_password = 'cr0pg6TwpCng4D7O'

        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = f'{fromName} <{fromAddress}>'
        # print(f'{0}{1}'.format(fromName, fromAddress))
        message['To'] = toAddress
        message['Subject'] = subject
        # print("test")

        # Add body text to the message
        message.attach(MIMEText(body, 'plain'))
        # print("body")

        # Connect to the SMTP server
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()  # Enable TLS encryption

        # Login to the email account
        smtp_connection.login(sender_email, sender_password)

        # Send the email
        smtp_connection.sendmail(fromAddress, toAddress, message.as_string())

        # Close the connection
        smtp_connection.quit()
        print("mail sent successfully to" + toAddress)
        # return "mail sent successfully to" + toAddress
    except Exception as e:
        return str(e)


# sendmail('vikas50572kushwaha@gmail.com', 'Vikas Kushwaha', 'info@koneqto.com', 'Test Subject', 'This is a test body')