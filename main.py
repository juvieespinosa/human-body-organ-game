import turtle
import pandas

screen = turtle.Screen()
screen.title("INTERNAL STRUCTURE OF THE HUMAN BODY")
image = "human body organ.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("body_organs.csv")
all_parts = data.part.to_list()
guessed_parts = []

while len(guessed_parts) < 8:
    answer_part = screen.textinput(title=f"{len(guessed_parts)}/8 Body Organs Correct",
                                   prompt="What's another body organs name?").title()
    if answer_part == "Exit":
        missing_parts = []
        for part in all_parts:
            if part not in guessed_parts:
                missing_parts.append(part)
        new_data = pandas.DataFrame(missing_parts)
        new_data.to_csv("parts_to_learn.csv")
        break
    if answer_part in all_parts:
        guessed_parts.append(answer_part)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        part_data = data[data.part == answer_part]
        t.goto(int(part_data.x), int(part_data.y))
        t.write(answer_part)

screen.exitonclick()
