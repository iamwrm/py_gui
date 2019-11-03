import PySimpleGUI as sg
import subprocess
import random

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

drop_down_button_tuple = (
    'Select Algorithm', 'Round Robin', 'First Come First Serve')

dropdown_algorithms = sg.Drop(values=drop_down_button_tuple, auto_size_text=True, size=(
    20, 1), key='dropdown_algo')

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
str_image_waiting = 'image_waiting'
str_image_num_left = 'image_numleft'

image_sche_result = sg.Image(filename=r'./assets/1.png', key=str_image_result)

image_waiting_time = sg.Image(
    filename=r'./assets/1.png', key=str_image_waiting)

image_num_left = sg.Image(filename=r'./assets/1.png', key=str_image_num_left)

layout = [[sg.Text('Scheduling Alogrithm Visualization Tool')],
          [text_guide],
          [button_rand_gen, button_clear],
          [text_tasks_input],
          [dropdown_algorithms, button_visulize],
          [image_sche_result],
          [image_waiting_time, image_num_left],
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
        keys_entered = "(50,2,1), (80,3,1), (30,30,1)"
        keys_entered = ""
        for i in range(5):
            length = int(random.uniform(2, 38))
            arri = int(random.uniform(0,100))
            str_job = ""
            if i > 0:
                str_job += ', '
            str_job+='('+str(length)+','+str(arri)+',1)'

            keys_entered += str_job



        window.Element('Tasks Input').Update(keys_entered)
    if event == 'Clear':
        window.Element('Tasks Input').Update("")
    if event == str_button_vis:
        # exe_cmd_wr("")
        print_to_file_wr('./a_out.txt', 'w+', values['dropdown_algo'])
        print_to_file_wr('./a_out.txt', 'a+', values['Tasks Input'])
        exe_cmd_wr('python3 sche.py')
        window.Element(str_image_result).Update('./a.png')
        window.Element(str_image_waiting).Update('./ba.png')
        window.Element(str_image_num_left).Update('./ca.png')


window.Close()
