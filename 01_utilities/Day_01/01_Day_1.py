"""
Challenge - Self-Intro Script Generator

Create a pyhton script that interacts with the user and generates a personalized self introduction.

your program should :
1. Ask the user for their name, age, city, profession and favourite hobby.
2. Format this data into a warm, friendly paragraph of self introdution.
3. print the final paragraph in a clean and readable format.

Example :-
If the user inputs:
    Name: Ritzz
    Age: 23
    City: Indore
    profession: Software Engineer
    Favourite hobby: Reading

Your Script might output:
"Hello! My name is Ritzz. I'm 23 year old and live in indore. I work as a Software Engineer and
I absolutly enjoy reading in my free time. Nice to meet you!."

Bonus:
-Add the current date to the end of the paragraph like:
"Logged on: 2025-06-14"
-Wrap the printed message with a decorative border of stars(*)
"""

import datetime
name = input("What is your name ? ").strip()

age = input("How old are you ? ").strip()

city = input("Which city do you live in ? ").strip()

profession = input("What is your profession ? ").strip()

hobby = input("What is your hobby ? ").strip()

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}"
    f"I work as a {profession} and i absolutly enjoy {hobby} in my free time."
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)

 