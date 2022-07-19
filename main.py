from flask import Flask, render_template, request
import requests
import smtplib


OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/60bc08b7d4f5f0a7c80f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    blog_url = "https://api.npoint.io/60bc08b7d4f5f0a7c80f"
    response = requests.get(blog_url)
    all_posts = response.json()
    for blog_post in all_posts:
        if blog_post["id"] == post_id:
            current_post = blog_post
    return render_template("post.html", post=current_post)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    global data
    if request.method == "POST":
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL,
                            to_addrs=OWN_EMAIL,
                            msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
