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
