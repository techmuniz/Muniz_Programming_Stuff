Whenever we are sourcing candidates in LinkedIn Recruiter Projects, we have 3 options we when open a profile:

- Save candidate -> Move to the next candidate
- Hide candidate -> Move to the next candidate
- Activate the 'Show More' experience button

What is this tool for?

Automate those steps using a script.

How?

You assign an Alphanumeric key to each of those steps, and the script will find do all the clicking for you.

Technically speaking:

I use OpenCV to find the respective buttons image in the active page, once it founds, it clicks on it. Simple as that.


Known Bugs:

Some functions only work when browser zoom is 100% /n
Rarely (1 out of 50, probably) program saves the "Similar Profiles" in the side, instead of the current candidate in the screeen
If you try to insert more than one letter as a key, it will break the program 
Program will probably break if you do something that you should not do it :D
