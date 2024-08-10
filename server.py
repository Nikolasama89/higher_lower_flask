from flask import Flask
import random

# SETTING AND THE PRINTING THE RANDOM NUMBER
random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


# SETTING THE HOMEPAGE
@app.route("/")
def homepage():
    return ("<div style='text-align: center;'>"
            "<h1>Guess a number between 0 and 9!</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
            "</div>")

# USER GUESSING THROUGH THE URL AND PROGRAM GIVES FEEDBACK IF ITS HIGH OR LOW
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: purple'>Too high, try again!</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXhpNjFwaW95NDVncWp3YzZnZWU1cnVvb281ZHdwY2FocGgyY3hhbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cMJlmcleA6CO3CddGv/giphy.gif'/>"
                "</div>")

    elif guess < random_number:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
                "</div>")
    else:
        return ("<div style='text-align: center;'>"
                "<h1 style='color: yellow'>You found it!</h1>"
                "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDBxaXZjbTB1NjM2ZWRpNnAyMjNid3ZwYzh6b3Izbm5hZ21iZTI1byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dudcZA9e14HIY/giphy.gif'/>"
                "</div>")






if __name__ == "__main__":
    app.run()
