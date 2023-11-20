import PySimpleGUI as sg

# Define PySimpleGUI settings
sg.theme('DarkAmber')

# Define the layout of the GUI
logo = sg.Image('/Users/zec/Desktop/Jack1/HKU4.png', size=(300, 350))

layout = [
    [sg.Column([[logo]], justification='center')], 
    [sg.Text('Log In', size=(18, 1), font=('Any', 18),
             text_color='#FFFFFF', justification='center')],
    [sg.Button('😊', size=(5, 1), key='face_button'), sg.Button('EXIT')],
    [sg.Text('Username:', justification='right', size=(10, 1)), sg.Input(key='username')],
    [sg.Text('Password:', justification='right', size=(10, 1)), sg.Input(key='password', password_char='*')],
    [sg.Text('Fingerprint', justification='right', size=(10, 1)), sg.Slider(range=(0, 100), orientation='h',
                                                                resolution=1, default_value=60, size=(15, 15), key='fingerprint')],
    [sg.Column([[sg.Button('Phone Authentication'), sg.Text('Forgot Password?')]], justification='center')]
]

# Create the window
window = sg.Window('ICMS Portal',
                   default_element_size=(21, 1),
                   element_justification='c',
                   text_justification='right',
                   auto_size_text=False).Layout(layout)

# Read events and values from the window
event, values = window.Read()

# Process the events
if event is None or event == 'EXIT':
    exit()

# Get the value of the fingerprint slider
gui_fingerprint = values["fingerprint"]
win_started = False

# Get the values of the username and password inputs
username = values['username']
password = values['password']

# Close the window
window.Close()