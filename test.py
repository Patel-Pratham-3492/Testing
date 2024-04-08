import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.header("This :red[page] is :blue[testing] :violet[purpose] only :green[!]")

name = st.text_input("Enter Name: ")
email = st.text_input("Enter Email: ")
message = "This is testing purpose only!"

def send_email(receiver_email, message):
	# Email configuration
	sender_email = "prathampatel8320@gmail.com"
	password = "vdtz gfex tcoq odbc"  # Prompt for email password	
	smtp_server = "smtp.gmail.com"  # Change according to your email provider
	smtp_port = 587  # Change according to your email provider

	# Create message
	email = MIMEMultipart()
	email["From"] = sender_email
	email["To"] = receiver_email
	email["Subject"] = "Subject"  # You can customize the subject here
	email.attach(MIMEText(message, "plain"))

	# Connect to SMTP server and send email
	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(sender_email, password)
		text = email.as_string()
		server.sendmail(sender_email, receiver_email, text)
		st.write("Email sent successfully!")
	except Exception as e:
		st.write(f"Error: {e}")
	finally:
		server.quit()


if st.button("submit"):
	if (name == "" or email ==""):
		st.error("fill details properly")
	else:
		send_email(str(email),message)
		st.success("Done!")
