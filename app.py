from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profiles = [
        {
            "name": "Mercy $ Jeremy",
            "bio": "Finding love on EliteSingles was like discovering a hidden treasure map.Mercy and Jeremy's  story proves that when two hearts unite with a common purpose, an extraordinary journey begins #ElitesMeet",
            "photo": "girl1.jpeg"
        },
        {
            "name": "Joean $ Edith" ,
            "bio": "Another succesful match for the books! Congratulations to Joean & Edith on their wedding,We love that you found love on our platform. #elitesmeet",
            "photo": "girl2.jpeg"
        },
    ]
    return render_template("index.html", profiles=profiles)

@app.route("/profiles")
def profiles():
    profiles = [
        {
            "name": "Profile 1",
            "Occupation": "Stable",
            "description": "Entrepreneur,Financially Stable • Loves travel and fine dining.",
            "photos": ["P1.jpeg"]
        },
        {
            "name": "Profile 2",
            "Occupation": "Doctor",
            "description": "Doctor,Fitness enthusiast • Business minded.",
            "photos": ["P3.jpeg"]
        },
        {
            "name": "Profile 3",
            "Occupation": "Business Man",
            "description": "Corporate professional • Family oriented.",
            "photos": ["P4.jpeg"]
        },
        {
            "name": "Profile 4",
            "Occupation": "Legal Job",
            "description": "Fashion lover,Working also financially stable • Outgoing personality.",
            "photos": ["P5.jpeg"]
        },
        {
            "name": "Profile 5",
            "Occupation": "Financially Stable",
            "description": "Creative mind,Doctor • Loves adventure.",
            "photos": ["P6.jpeg"]
        }
    ]

    return render_template("profiles.html", profiles=profiles)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
