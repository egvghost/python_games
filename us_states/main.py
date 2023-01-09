from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(725, 491)
screen.title("🇺🇸 U.S. 50 States GAME 📍")
screen.bgpic("blank_states_img.gif")

states = pandas.read_csv("./50_states.csv")
# print(states.state)
all_states = states.state.to_list()
found_states = []

label = Turtle()
label.hideturtle()
label.penup()
label.color("black")
counter = Turtle()
counter.hideturtle()
counter.penup()
counter.color("black")
counter.goto(-360, 210)
counter.write(arg=f"{len(found_states)}/50", font=("Arial", 30, "bold"))

while len(found_states) < 50:
  player_input = screen.textinput("US States", "Enter the name of the State").title()
  if player_input == "Exit":
    missing_states = [state for state in all_states if state not in found_states]
    # print(missing_states)
    my_dict = {
      "Missing States": missing_states  
    }
    data_frame = pandas.DataFrame(missing_states)
    data_frame.to_csv("./missing_states.csv")
    break
  elif player_input in all_states and player_input not in found_states:
    label.goto(int(states[states.state == player_input].x), int(states[states.state == player_input].y))
    label.write(arg=player_input, font=("Arial", 15, "normal"))
    found_states.append(player_input)
    counter.clear()
    counter.goto(-360, 210)
    counter.write(arg=f"{len(found_states)}/50", font=("Arial", 30, "bold"))
