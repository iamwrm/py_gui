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


layout = [[sg.Text('Persistent window')],
          [sg.Input(key='IN_1')],
          [sg.Input(key='IN_2')],
          [sg.Button('Read'), sg.Exit()],
          [sg.Button('Touch'), sg.Button('Clear')]
          ]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Touch':
        exe_cmd_wr('touch a b c')
    if event == 'Clear':
        exe_cmd_wr('rm -f a b c')

window.Close()
