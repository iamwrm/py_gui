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


def print_to_file_wr(file_dir, mode_input, text):
    with open(file_dir, mode_input) as f:
        print(text, file=f)


text_guide_txt = 'Please input the tasks in the format of (length, arrive time, priority)'
text_guide = sg.Text(text_guide_txt)

text_input_def = 'You can either input your own tasks or press the button above to get random number'

drop_down_button_tuple = ('Select Algorithm', 'Round Robin',
                          'First Come First Serve', 'Shortest Job First')

dropdown_algorithms = sg.Drop(values=drop_down_button_tuple, auto_size_text=True, size=(
    20, 1),key='dropdown_algo')

text_tasks_input = sg.Multiline(default_text=text_input_def,
                                size=(100, 3), key="Tasks Input")


str_button_rand = 'Generate Random Tasks'
str_button_vis = 'Schedule and Visualize'
str_button_clear = 'Clear'

button_rand_gen = sg.Button(str_button_rand, font=(
    "Helvetica", 10), button_color=('white', 'green'))

button_visulize = sg.Button(str_button_vis, font=(
    "Helvetica", 15), size=(20, 3), button_color=('white', 'orange'))

button_clear = sg.Button(str_button_clear)

str_image_result = 'image_result'
image_sche_result = sg.Image(filename=r'./assets/1.png', key=str_image_result)

layout = [[sg.Text('Scheduling Alogrithm Visualization Tool')],
          [text_guide],
          [button_rand_gen, button_clear],
          [text_tasks_input],
          [dropdown_algorithms, button_visulize],
          [image_sche_result],
          [sg.Exit()],
          ]

window = sg.Window('Window that stays open', layout)

state = 1

while True:
    event, values = window.Read()

    keys_entered = ""
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Generate Random Tasks':
        keys_entered = "(5,2,1), (2,1,1), (4,32,1)"
        window.Element('Tasks Input').Update(keys_entered)
    if event == 'Clear':
        window.Element('Tasks Input').Update("")
    if event == str_button_vis:
        window.Element(str_image_result).Update('./s1.png')
        # exe_cmd_wr("")
        print_to_file_wr('./a_out.txt', 'w+', values['dropdown_algo'])
        print_to_file_wr('./a_out.txt', 'a+', values['Tasks Input'])


window.Close()
