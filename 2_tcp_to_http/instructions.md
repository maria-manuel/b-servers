- The goal of this activity is further conceptual understanding of HTTP and how
  servers work. It's a "from scratch" HTTP server. None of the code here should
  be used a template for anything you will be doing for homework or project
  work.

- The challenges here are mostly "code comprehension" focused. Only if you get
  to the Bonus Challenge will you be adding any substantial code.


Challenge 1
------------------

Get the code running.

- Run this with Python, then figure out how to access the server and see "Hello
  Server World!"

- Hint: Try going to http://localhost:8080/




Challenge 2
------------------

- Can you figure out which code you might need to change to make it reply with
  a different message than "Hello Server World"?

- Change it to say, `Welcome to my homepage`

- HINT: The code includes a lot of boilerplate to set up a TCP server.  The
  "good stuff" is 11 (reporting the requests back to the terminal), and lines
  18-19 (sending the response back).

- TIP: When making changes to a server file, you will have to stop the server
  with Ctrl+C, and start it again, for the change to be used.




Challenge 3
------------------

1. Examine the terminal output every time you visit the page.
2. Experiment by typing in different addresses in the address bar of your
browser and hitting enter.
3. For example, try the following:
    - http://localhost:8080/just-testing
    - http://localhost:8080/another/test/thing
    - http://localhost:8080/
4. See what different output appears in the terminal.



Challenge 4:
------------------
Right now, the application ONLY responds with "Hello Server World!" to all
requests coming in. Based on the pattern you established from Challenge 2,
write pseudocode for an application that shows a different page depending on
which page the user visits.




Bonus Challenge 1
------------------

Using the following pseudocode (and/or your own) as a reference, write code
to implement the bonus challenge.

Pseudo code:
- If the request we receive is for "/"
    - reply with the message "<h1>Welcome to my homepage!</h1>"
- If it is for "/about-me"
    - reply with the message "<h1>About me</h1>"
- If it is for "/contact-me"
    - reply with the message "<h1>Contact</h1>"
- Otherwise, it's a 404 error
    - reply with some sort of "file not found" message


Bonus Challenge 2
------------------

Refactor the solution you did for Bonus Challenge 1, so that the HTML of each
page is in the return value of a function, and the "if-statements" that you
likely wrote for Bonus Challenge 1 call those functions.

EXAMPLE:

    def about_me():
        return "<h1>About my page</h1>"

    # ... further down...

    if path == '/about-me':
        response_data = about_me()

