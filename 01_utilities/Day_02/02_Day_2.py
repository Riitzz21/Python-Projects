"""
Challenge : Stylish Bio Generator for Instagram/Twitter

Create a python utility that ask the user for a few key details and generates a short, stylish, bio that
could be used for social media profiles like Instagram or Twitter.

Your program should:
1. prompt the user to enter their :
- Name 
- Profession
- one - liner passion or goal
- Favourite emoji (optional)
- website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise and catchy.

3. Add optional hashtags or emojis for flair.

Example :

Input :

Name : Ritzz
Profession : Designer
passion - Making things beautiful.
emoji : 🎨
website : ritzz.design

Output :

🎨 Ritzz | Designer
💎 Making things beautiful.
🌈 ritzz.design

Bonus :

- Let the user pick from 2-3 different layout style.
- Ask the user if they want to save the result into a '.txt' file.

"""
import textwrap

name = input("Enter your name : ").strip()
profession = input("Enter your profession : ").strip()
passion = input("Enter your passion : ").strip()
emoji = input("Enter your favourite emoji : ").strip()
website = input("Enter your website name : ").strip()

print("\nChoose your style : ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3 : ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n🌀 {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name} \n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji * 3} \n {name} - {profession}\n {passion} \n {website} \n {emoji*3}"

bio = generate_bio(style)

print("\n Your Stylish Bio:\n")
print("*" * 50)

print(textwrap.dedent(bio))
print("*" * 50)

save = input("do you want to save this bio to a .txt file? (yes/no) : ").lower()

if save == "yes":
    filename = f"{name.lower().replace(' ', ' _')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File saved")