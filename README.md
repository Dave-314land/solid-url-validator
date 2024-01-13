# solid-url-validator

This project is based on a recent coding challenge I took. I was tasked with building a URL validator with certain criteria that I have outlined below, as well as in main.py. After the timed portion of the challenge was completed, I wanted to build this out further to practice SOLID principles.

Criteria: 
Build a basic URL Validator.
Returns a list of responses.
Basic GET and POSTS requests validated.
If GET request contains valid token, return VALID and user name parameter.
If GET request does not contain valid token, return INVALID
If POST request contains valid token and contains valid CSRF token, return VALID and user name parameter.