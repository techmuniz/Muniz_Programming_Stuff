Here we got a few personal projects & some exercises that I like to play with.

Regarding projects, there's one called Muniz Recruiter Helper (Lack of better name). Why I created?

Whenever we are sourcing candidates in LinkedIn Recruiter's Projects, we have three options when we open a profile:

**Save candidate** -> Move to the next candidate
**Hide candidate** -> Move to the next candidate
Activate the **'Show More'** experience button

**What is this tool for?**
Automating these steps using a script.

**How?**
You assign an alphanumeric key to each of these steps, and the script will do all the clicking for you.

**Technically speaking:**
I use OpenCV to find the respective button's image on the active page, and once it's found, it clicks on it. It's as simple as that. OpenCV to find the respective button's image onOpenCV

**Known Bugs:**
Some functions only work when the browser zoom is at 100%.
Rarely (probably 1 out of 50 times), the program saves the "Similar Profiles" on the side instead of the current candidate on the screen.
If you try to insert more than one letter as a key, it will break the program.
The program will probably break if you do something you shouldn't do :D


**I'm also developing a script with similar properties for our internal Turing ATS - the "Matching" project**
