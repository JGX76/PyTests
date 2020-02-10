import PySimpleGUI as sg
from random import randint

nb_dice = 3
contents = [[sg.Button('Roll your dice')],
            [sg.Button('-', size=(2,2), disabled=True, pad=(0,0), key=i) for i in range(nb_dice)],
            [sg.Text(0, size=(24,1), key='-SCORE-', background_color='gray' )],
            [sg.Text(0, size=(6,1), key='-P1 SCORE-'), sg.Text(0, size=(6,1), key='-P2 SCORE-')],]

layout = [[sg.Col(contents, element_justification='c')]]        # Put into a column so can center everything

window = sg.Window('Window Title', layout, margins=(0,0), text_justification='center', font='Any 14', element_padding=(5,5))

player = p1_score = p2_score = score = 0
fixed_dice = [0]*nb_dice
while True:                     # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if str(event).startswith('Roll'):           # roll button
        roll_all = 0 not in fixed_dice
        for i in range(nb_dice):
            if roll_all or not fixed_dice[i]:
                window[i].update(randint(1,6), disabled=False)
    else:                                       # clicked on a dice
        window[event].update(disabled=True)
        fixed_dice[event] = int(window[event].GetText())
        if 0 not in fixed_dice:                 # end of players turn... determine score
            score += sum(fixed_dice)
            fixed_dice = [0]*nb_dice
            if player:
                player = 0
                p2_score += score
            else:
                player = 1
                p1_score += score
            window['-SCORE-'].update(score)
            window['-P1 SCORE-'].update(p1_score)
            window['-P2 SCORE-'].update(p2_score)
window.close()
