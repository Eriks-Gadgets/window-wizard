import PySimpleGUI as sg
print("Window Wizard event log")
sg.theme("DarkBlue17")
loading_window = sg.Popup("Window Wizard\n© Erik's Gadgets, 2023")
win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("New Window")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
textnum = 0
while True:
    event, values = win_window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "New Window":
        win_window.close()
        win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("Temporary"), sg.Text("Will not create a file.")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Temporary":
        dialogue = 1
        win_window.close()
        win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Text("! Are you sure you want to create a temporary window? !\n! Your Changes will not be saved !")],[sg.Button("Yes"), sg.Button("No")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Return [1]" or event == "No":
        if event == "No" and dialogue == 1 or event == "Return [1]":
            win_window.close()
            win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("New Window")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Yes":
        win_window.close()
        my_custom_margins = [200, 150]
        my_custom_title = "MyWindow"
        my_layout_temp=[[]]
        objects = [sg.Button("Title"), sg.Button("Margins")]
        my_custom_window_temp = sg.Window(title=my_custom_title + " (Preview)", layout=my_layout_temp, margins=my_custom_margins).read()
        win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Adjust":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust", layout=[[sg.Text("Window Wizard")],objects,[sg.Button("Return [2]")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
            post_objects = objects
            del objects
            objects = post_objects
            del post_objects
    if event == "Return [2]":
        if dialogue == 1:
            objects = [sg.Button("Title"), sg.Button("Margins")]
            win_window.close()
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Title":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust Title (" + my_custom_title + ")", layout=[[sg.Text("Window Wizard")],[sg.Input(my_custom_title)],[sg.Button("Adjust Title")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Margins":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust Margins " + str(my_custom_margins), layout=[[sg.Text("Window Wizard")],[sg.Text("Margins {X}"), sg.Input(str(my_custom_margins[0]))], [sg.Text("Margins {Y}"), sg.Input(str(my_custom_margins[1]))],[sg.Button("Adjust Margins")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Adjust Margins":
        if dialogue == 1:
            win_window.close()
            objects = [sg.Button("Title"), sg.Button("Margins")]
            my_custom_margins = (values[0], values[1])
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))                                                                            
    if event == "Adjust Title":
        if dialogue == 1:
            win_window.close()
            objects = [sg.Button("Title"), sg.Button("Margins")]
            my_custom_title = values[0]
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Add":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Add Item to '" + str(my_custom_title) + "'", layout=[[sg.Text("Window Wizard")],[sg.Button("Text")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Text":
        if dialogue == 1:
            win_window.close()
            textnum += 1
            objects.append(sg.Button("Text" + str(dialogue)))
            additem = 1
            win_window = sg.Window(title="Add Text Item: ", layout=[[sg.Input()],[sg.Button("Add Text Item")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Add Text Item":
        if additem == 1:
            win_window.close()
            if my_layout_temp == [[]]:
                my_layout_temp.append([sg.Text(values[0])])
            else:
                my_layout_temp.append([sg.Text(values[0])],)
            my_layout_temp[-1] = [sg.Text(values[0])]
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    if event == "Preview":
        if dialogue == 1:
            post_objects = objects
            del objects
            objects = post_objects
            del post_objects
            win_window.close()
            del my_custom_window_temp
            my_custom_window_temp = sg.Window(title=my_custom_title + " (Preview)", layout=my_layout_temp, margins=tuple(my_custom_margins)).read()
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
win_window.close()
