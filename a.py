import PySimpleGUI as sg
import subprocess


def exe_cmd_wr(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass


text_input_def = 'You can either input your own tasks or press the button above to get random number'

drop_down_button_tuple = ('Select Algorithm', 'Round Robin',
                          'First Come First Serve', 'Shortest Job First')

dropdown_algorithms = sg.Drop(values=drop_down_button_tuple, auto_size_text=True, size=(
    20, 1))

text_tasks_input = sg.Multiline(default_text=text_input_def,
                                size=(100, 3), key="Tasks Input")


str_button_rand = 'Generate Random Tasks'
str_button_vis = 'Schedule and Visualize'

button_rand_gen = sg.Button(str_button_rand, font=(
    "Helvetica", 10), button_color=('white', 'green'))

button_visulize = sg.Button(str_button_vis,font=(
    "Helvetica", 15), size=(20, 3),button_color=('white','orange'))



layout = [[sg.Text('Scheduling Alogrithm Visualization Tool')],
          [button_rand_gen, ],
          [text_tasks_input],
          [dropdown_algorithms, button_visulize],
          [sg.Button('Touch'), sg.Button('Clear'),
           sg.Button('Read'), sg.Exit()],
          ]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()

    keys_entered = ""
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Generate Random Tasks':
        keys_entered = "(5,2,1), (2,1,1), (4,32,1)"
        window.Element('Tasks Input').Update(keys_entered)
    if event == 'Touch':
        exe_cmd_wr('echo touched')
    if event == 'Clear':
        exe_cmd_wr('echo cleared')


window.Close()
