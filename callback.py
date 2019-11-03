import PySimpleGUI as sg

# This design pattern simulates button callbacks
# Note that callbacks are NOT a part of the package's interface to the
# caller intentionally.  The underlying implementation actually does use
# tkinter callbacks.  They are simply hidden from the user.

# The callback functions
def button1():
    print('Button 1 callback')

def button2():
    print('Button 2 callback')

# Lookup dictionary that maps button to function to call
func_dict = {'1':button1, '2':button2}

# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Quit()]]

# Show the Window to the user
window = sg.Window('Button callback example', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.Read()
    if event in ('Quit', None):
        break
    # Lookup event in function dictionary
    try:
        func_to_call = func_dict[event]   # look for a match in the function dictionary
        func_to_call()                    # if successfully found a match, call the function found
    except:
        pass

window.Close()

    # All done!
sg.PopupOK('Done') 