#This solution takes concepts, which are introduced later in the book and uses them. 
#For a solution for an exercise similiar to this, look at own_list.py
friends = """Coral Alfaro
Phillip Ryan
Alfred Odling
Cohan Gardner
Bradley Fisher
Jenny Marshall
Meredith Connolly
Cassia Simons
Maegan Terrell
Fox Branch
Nichola Hale
Saskia Allison
Calista Brennan
Petra Naylor
Anita Lane
Patrik Guy
Lillia Salgado
Hadiya Mcbride
Ashton Mcdonnell
Rex Chambers
Sama Rios
Jarrad Sweet
Jokubas Davenport
Kathy Cooke
Alison Duke
Aneesa Garner
Dalia Bartlett
Yisroel Griffiths
Yara Redfern
Wiktoria Kearney
Alex Cooley
Sylvie Todd
Eren Moon
Aya Pitt
Lynda Banks
Lola Lucas
Eve Shah
""".split()
for i in range(int(len(friends)/2)):
    print("Hello " + friends[2*i] + " " + friends[2*i+1]+ "! How are you?")