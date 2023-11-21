import turtle
import pandas

states_added = []
states_need_to_remember_list = []
written_states = []

# Reading data from csv
states_data = pandas.read_csv('50_states.csv')
list_of_states = states_data['state'].to_list()


def is_states_written(state_name, added_states_list):
    if state_name in added_states_list:
        return True
    else:
        return False


def is_state_available(state_name, state_list):
    if state_name in state_list:
        return True
    else:
        return False


def is_state_remembered(state_name, remembered_state_list):
    if state_name in remembered_state_list:
        return True
    else:
        return False


def write_on_screen(text, x_cor, y_cor):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x_cor, y_cor)
    writer.pendown()
    writer.write(arg=text, align='center', font=('Arial', 15, 'normal'))


# Screen Initialization
image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)

# Game Starting
is_game_on = True

while is_game_on:
    user_choice = screen.textinput(title='Guess the state', prompt='Enter the state name').title()
    # Checking if state is available in list of states in USA
    if is_state_available(user_choice, list_of_states):
        # Checking if state is written on screen or not
        if not is_states_written(user_choice, written_states):
            state_row_data = states_data[states_data.state == user_choice]
            write_on_screen(user_choice, int(state_row_data.x), int(state_row_data.y))
            written_states.append(user_choice)
            # Now checking if state is added to the list of states or not
            if not is_state_remembered(user_choice, states_added):
                states_added.append(user_choice)
        else:
            continue

    elif user_choice == 'Exit':
        is_game_on = False
        for each_states in list_of_states:
            if each_states in states_added:
                continue
            else:
                states_need_to_remember_list.append(each_states)
        states_should_remember_dict = {'states_name': states_need_to_remember_list}
        need_to_remember_states_data = pandas.DataFrame(states_should_remember_dict)
        need_to_remember_states_data.to_csv('should_remember.csv')
