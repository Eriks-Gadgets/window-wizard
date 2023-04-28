#importing pysimpleGUI in order to make GUI function
import PySimpleGUI as sg

#start of the event log, used for debugging
print("Window Wizard event log")

#sets the theme of the window
sg.theme("DarkBlue17")

#sets in_Library to False
in_library = False

#text for the first window
loading_window = sg.Popup("Window Wizard\n© Erik's Gadgets, 2023")

#text for the second window
win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("New Window")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
textnum = 0 
proper_pretzel = []
temp_text = []
#while the window is open, this code will run.
while True:
    event, values = win_window.read()
    print(event) #every event will be printed in the event log
    
    #when the exit button is pressed, the window will close.
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    
    #creates a new window when the button is pressed
    if event == "New Window":
        win_window.close() #closing the main window
        win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("Temporary"), sg.Text("Will not create a file.")],[sg.Button("Return [1]")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    
    #creates a temporary window that will not be saved
    if event == "Temporary":
        dialogue = 1
        win_window.close() #closing the main window
        win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Text("! Are you sure you want to create a temporary window? !\n! Your Changes will not be saved !")],[sg.Button("Yes"), sg.Button("No")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

    #closes the window and returns you to the previous window
    if event == "Return [1]" or event == "No":
        if event == "No" and dialogue == 1 or event == "Return [1]":
            win_window.close()
            win_window = sg.Window(title="Menu", layout=[[sg.Text("Window Wizard")],[sg.Button("New Window")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
    
    #creates your custom window
    if event == "Yes":
        win_window.close() 
        my_custom_margins = [200, 150]
        my_custom_title = "MyWindow"
        my_layout_temp=[[]]
        objects = [sg.Button("Title"), sg.Button("Margins")]
        my_custom_window_temp = sg.Window(title=my_custom_title + " (Preview)", layout=my_layout_temp, margins=my_custom_margins).read()
        win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

    #adjust will adjust what your window contains
    if event == "Adjust":

        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust", layout=[[sg.Text("Window Wizard")],[sg.Button("Title"), sg.Button("Margins")],[sg.Button("Return [2]")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
            post_objects = objects
            del objects
            objects = post_objects
            del post_objects

    #brings up text library
    if event == "Adjust Text Items":
        pretzel = []
        for i in temp_text:
            in_library = True
            proper_pretzel.append(sg.Button(i))
            pretzel.append(i)
            win_window.close()
            print(temp_text)
            win_window = sg.Window(title="Window Wizard Menu", layout=[x for x in proper_pretzel], margins=(100, 50))


    if in_library == True:
        if event in pretzel:
            #quick text configuration
            position_pretzel = 0
            for i in pretzel:
                if event == i:
                    break
                else:
                    position_pretzel += 1
            win_window.close()
            win_window = sg.Window(title="Add Text Item: ", layout=[[sg.Input(event)],[sg.Button("Edit Text Item")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
        else:
            in_library = False

    #Edits text item
    if event == "Edit Text Item":
        pretzel[position_pretzel] = values[0]
        win_window.close()
        if my_layout_temp == [[]]:
            my_layout_temp.append([sg.Text(values[0])])
        else:
            my_layout_temp.append([sg.Text(values[0])],)
            my_layout_temp[-1] = [sg.Text(values[0])]
            temp_text.append(values[0])
            text = values[0]
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))


    #brings you to the previous window
    if event == "Return [2]":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

    #opens title menu
    if event == "Title":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust Title (" + my_custom_title + ")", layout=[[sg.Text("Window Wizard")],[sg.Input(my_custom_title)],[sg.Button("Adjust Title")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

    #opens margin menu
    if event == "Margins":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Adjust Margins " + str(my_custom_margins), layout=[[sg.Text("Window Wizard")],[sg.Text("Margins {X}"), sg.Input(str(my_custom_margins[0]))], [sg.Text("Margins {Y}"), sg.Input(str(my_custom_margins[1]))],[sg.Button("Adjust Margins")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

    #adjusts margins of the window
    if event == "Adjust Margins":
        if dialogue == 1:
            win_window.close()
            my_custom_margins = (values[0], values[1])
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50)) 
            
            #adjusts the title of the window
    if event == "Adjust Title":
        if dialogue == 1:
            win_window.close()
            my_custom_title = values[0]
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

            #adds an item to the window
    if event == "Add":
        if dialogue == 1:
            win_window.close()
            win_window = sg.Window(title="Add Item to '" + str(my_custom_title) + "'", layout=[[sg.Text("Window Wizard")],[sg.Button("Text")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

            #Opens the text menu
    if event == "Text":
        if dialogue == 1:
            win_window.close()
            textnum += 1
            objects.append(sg.Button("Text" + str(textnum)))
            additem = 1
            win_window = sg.Window(title="Add Text Item: ", layout=[[sg.Input()],[sg.Button("Add Text Item")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))
            
            #adds a text item to the window
    if event == "Add Text Item":
        if additem == 1:
            win_window.close()
            if my_layout_temp == [[]]:
                my_layout_temp.append([sg.Text(values[0])])
            else:
                my_layout_temp.append([sg.Text(values[0])],)
            my_layout_temp[-1] = [sg.Text(values[0])]
            temp_text.append(values[0])
            text = values[0]
            win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))

            #Preview your window
    if event == "Preview":
        if dialogue == 1:
             string_cheese = "" #makes it look like there is a new layout every time preview is run in order to prevent errors
             for i in temp_text:
                 string_cheese += i
                 string_cheese += "\n"
             post_objects = objects
             objects = post_objects
             win_window.close()
             testing = 1
             title2 = ""
             if "~" in my_custom_title:
                 for i in my_custom_title:
                     if i == "~":
                         break
                     else:
                         title2 += i
             else:
                 title2 = my_custom_title + " (Preview)"
             my_custom_window_temp = sg.Window(title=title2, layout=[[sg.Text(string_cheese)]], margins=tuple(my_custom_margins)).read()
             win_window = sg.Window(title="Window Wizard Menu", layout=[[sg.Menu([['File', ['Exit']],['Configurations', ['Add', 'Adjust', 'Delete']],])],[sg.Button("Preview")],[sg.Button("Exit")],[sg.Text("© Erik's Gadgets")]], margins=(100, 50))


win_window.close()
