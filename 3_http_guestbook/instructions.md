- As before, the goal of this activity is further conceptual understanding of
  HTTP and how servers work, and none of the code here should be used a
  template for anything you will be doing for homework or project work.

- This activity represents a "refactored" or improved upon version of the
  previous activity.

Challenge 1
------------------

Get the code running, and figure out how to see the server and the pages its
serving up. Hint: It is the same steps as before.


Challenge 2
------------------

- In addition to adding a print to every file you are editing, another good
  habit to get into when learning a new web framework is adding a print
  statement to each "view function".

- Observe the effects of the print in the `index()` and `contact_me()`
  functions

- Add one to the `about_me()` function and observe its effects

TIP: When making changes to a server file, you will have to stop the server
with Ctrl+C, and start it again, for the change to be used.



Challenge 3
------------------

Time to add a new page to this website! Follow the same pattern you see below,
add a new page called "Bio" at "/bio".

- What's on the new page is up to you (perhaps: "I want to be the very best"?)

- HINT: In total, you'll have to do the following:
    1. Create a new function
    2. A new if statement in the routing
    3. A new `<a href...> link</a>` in the homepage.


Challenge 4
------------------

Make a "magic 8-ball" page. Follow the same procedure as Challenge 3, but this
time make your "magic 8-ball page" randomly say one of 2 or 3 messages.

Stuck? See a code hint at the bottom of this file.


Challenge 5
------------------

Visit the contact page. Examine the terminal output every time you submit data
on the contact page. Try typing different messages.

Can you "extract" the name from the URL? Print the user's name to the terminal
whenever they submit

HINT: Try the following line:

    other_crap, name = path.split('=')


Challenge 6
------------------

In Python create a list called "guestbook". Append the name to this list every
time they hit Submit. Print the contents of this list so you know it's working.


Challenge 7
------------------

Generate an HTML list using `<li>` etc to show the guest list as a list of
bullet points.



Fun Bonus
------------------

You might be able to connect from one computer to another's webserver, assuming
you are both on the same WiFi network, by going to
http://COMPUTERNAME.local:8080 (e.g., if another computer name is
"magnificent", then you can go to: http://magnificent.local:8080 )


Advanced Bonus Challenge 1
------------------

Make a link or button "X" next to each guestbook item that, when clicked, will
delete each individual guestbook item.


Advanced Bonus Challenge 2
------------------

- The HTTP protocol standards says that servers should only respond with "200
  OK" if everything went fine.
- If something a file is not found, it should respond with "HTTP/1.0 404 Not
  Found"
- Improve the server to give back "proper" 404 error pages



---------------------


Challenge 4 - Hint
--------------------

Hint: Partial Python code to randomly respond with one of 3 messages:

    messages = [
        'You bet',
        'Not likely',
        'Impossible',
    ]
    message = random.choice(messages)
    return message

