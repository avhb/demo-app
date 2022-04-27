# ReadMe

python -m venv venv310
- activate venv: (windows) `. venv310/Scripts/Activate.ps1` or (linux) `. venv310/bin/activate`
- install requirements: `pip install -r requirements.txt`

test

POM

---

Root page: /

When I navigate to the root page
Then I should see Hello world

---

Home page: /home

Given I'm on the homepage
When I click the about page link
Then I should redirect to the about page

---

About page: /about

Given I'm on the about page
When I click the homepage link
Then I should redirect to the homepage
