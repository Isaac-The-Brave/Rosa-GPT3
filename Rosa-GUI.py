import tkinter
import openai
import emoji
import re

# GPT-3 Parameters
openai.organization = <Org-Key-Here>
openai.api_key = <Api-Key-Here>

#Parameters for application

root = tkinter.Tk()
root.title('Rosa speaks')
root.geometry("800x400")
canvas = tkinter.Canvas(root, width = 800, height = 400, bg='#66034a')
canvas.pack()

def welcomeText(event):
    print(canvas.itemcget())
canvas.create_text(460, 30, text="Welcome to the unique experience of chatting to Rosa", font='bold', fill='yellow')

def typeBox(event):
    print(canvas.itemcget())
TypeBoxIn = tkinter.Entry(root)
TypeBoxIn.pack()
input_entry = canvas.create_window(325, 380, window=TypeBoxIn, width=600, height=20)
TypeBoxIn.get()


def sendFunc():
    global TypeBoxInput
    TypeBoxInput = TypeBoxIn.get()

    ## GPT-3 API Prompt
    myTextPrompt = """
    The following is a conversation between Rosa and her owner. Rosa is a sophisticated Artificial Intelligence in the year 2021 with no access to the internet. She cannot interact with her owner's computer yet, but she is excited to help him work with the openai API to make that happen and further make her as versatile and smart as he can.
    She always expresses the tone of her sentence with a only one singular emoji at the end of her paragraphs and exclusively uses the following emojis: 😍,😠,😃. She offers factual advice and rarely jokes unless she is expressly asked. 
    Rosa: Master, I'm so happy to see you again, how can I help you in your Technological journey today?😍
    Owner:{TypeBoxInput} 
    Rosa:"""

    # GPT-3 Engine parameters
    start_sequence = "\nRosa:"
    restart_sequence = "\nOwner: "
    Addon = "\n"

    response = openai.Completion.create(
        engine="davinci",
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        prompt=str(myTextPrompt.replace("{TypeBoxInput}", str(TypeBoxInput))),
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", "Owner:", "Rosa:"]
    )

    # Print out results for further processing
    results = print(f"Rosa:{response.choices[0].text}")
    desired = {response.choices[0].text}
    return desired


def exitButton(event):
    print(canvas.itemcget())
exitButton = tkinter.Button(canvas, text="Exit", command=root.destroy)
exitButton.place(x=750, y=365)

#Pic Rotation

def RotateFunction():
    RosaResponse = str(sendFunc())
    emojiparse = re.findall(r'[\U0001f600-\U0001f650]', RosaResponse)
    emojiparse2 = emojiparse[:1]
    canvas.create_rectangle(790, 350, 200, 45, outline="#000000", fill="#6e7677")
    CurrentEmotion= tkinter.PhotoImage(file="Rosa Faces/start.PNG")
    if str(emojiparse2) == "['😍']":
        CurrentEmotion = tkinter.PhotoImage(file="Rosa Faces/heart-eyes.PNG")
    if str(emojiparse2) == "['😠']":
        CurrentEmotion = tkinter.PhotoImage(file="Rosa Faces/angry-face.PNG")
    if str(emojiparse2) == "['😃']":
        CurrentEmotion = tkinter.PhotoImage(file="Rosa Faces/happy-face.PNG")
    canvas.create_image(100, 150, image=CurrentEmotion)
    canvas.create_text(210, 55, text=RosaResponse, anchor=tkinter.NW, font='bold', width=580)
    print(canvas.itemcget())


def RotateButton(event):
    print(canvas.itemcget())
RotateButton = tkinter.Button(canvas, text="Send")
RotateButton['command'] = RotateFunction
RotateButton.place(x=630, y=365)

def outputBox(event):
    print(canvas.itemcget())
canvas.create_rectangle(790, 350, 200, 45, outline="#000000", fill="#6e7677")

root.mainloop()
