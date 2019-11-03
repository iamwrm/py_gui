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


layout = [[sg.Text('Scheduling Alogrithm Visualization Tool')],
          [sg.Button('Generate Random Tasks', font=("Helvetica", 10))],
          [sg.Multiline(
              default_text='This is the default Text should you decide not to type anything', size=(35, 3), key="Tasks Input")],
          [sg.Button('Read'), sg.Exit()],
          [sg.Button('Touch'), sg.Button('Clear')],
          [sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],
          ]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()

    keys_entered = ""
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Generate Random Tasks':
        keys_entered="GRT"
        window.Element('Tasks Input').Update(keys_entered)
        print(values)
    if event == 'Touch':
        exe_cmd_wr('echo touched')
    if event == 'Clear':
        exe_cmd_wr('echo cleared')


window.Close()
