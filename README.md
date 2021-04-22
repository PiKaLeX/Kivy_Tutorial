# Kivy_Tutorial
https://realpython.com/mobile-app-kivy-python/

# Understanding the Kivy Framework
Kivy was first released in early 2011. This cross-platform Python framework can be deployed to Windows, Mac, Linux, and Raspberry Pi. It supports multitouch events in addition to regular keyboard and mouse inputs. Kivy even supports GPU acceleration of its graphics, since they’re built using OpenGL ES2. The project uses the MIT license, so you can use this library for free and commercial software.

When you create an application with Kivy, you’re creating a Natural User Interface or NUI. The idea behind a Natural User Interface is that the user can easily learn how to use your software with little to no instruction.

Kivy does not attempt to use native controls or widgets. All of its widgets are custom-drawn. This means that Kivy applications will look the same across all platforms. However, it also means that your app’s look and feel will differ from your user’s native applications. This could be a benefit or a drawback, depending on your audience.

# Installing Kivy
Kivy has many dependencies, so it’s recommended that you install it into a Python virtual environment. You can use either Python’s built-in venv library or the virtualenv package.

Here’s how you can create a Python virtual environment:

Shell
```shell
$ python3 -m venv my_kivy_project
```
This will copy your Python 3 executable into a folder called my_kivy_project and add a few other subfolders to that directory.

To use your virtual environment, you need to activate it. On Mac and Linux, you can do that by executing the following while inside the my_kivy_project folder:

Shell
```shell
$ source bin/activate
```
The command for Windows is similar, but the location of the activate script is inside of the Scripts folder instead of bin.

Now that you have an activated Python virtual environment, you can run pip to install Kivy. On Linux and Mac, you’ll run the following command:

Shell
```shell
$ python -m pip install kivy
```

If you run into any issues installing Kivy on your platform, then see the Kivy download page for additional instructions.

# Working With Kivy Widgets
A **widget** is an onscreen control that the user will interact with. All graphical user interface toolkits come with a set of widgets. Some common widgets that you may have used include buttons, combo boxes, and tabs. Kivy has many widgets built into its framework.

## Running a “Hello, Kivy!” Program
To see how Kivy works, take a look at the following “Hello, World!” application:

Python
```python
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()
```

Every Kivy application needs to subclass _App_ and override _build()_. This is where you’ll put your UI code or make calls to other functions that define your UI code. In this case, you create a _Label_ widget and pass in its _text_, _size_hint_, and _pos_hint_. These last two arguments are not required.

size_hint tells Kivy the proportions to use when creating the widget. It takes two numbers:

The first number is the x size hint and refers to the width of the control.
The second number is the y size hint and refers to the height of the control.
Both of these numbers can be anywhere between 0 and 1. The default value for both hints is 1. You can also use pos_hint to position the widget. In the code block above, you tell Kivy to center the widget on the x and y axes.

To make the application run, you instantiate your MainApp class and then call run(). When you do so, you should see the following on your screen:
![Image of Hello Kivy App](https://files.realpython.com/media/01_mdriscoll_hello_kivy.879d11e41080.png)

## Displaying an Image
Kivy has a couple of different image-related widgets to choose from. You can use Image to load local images from your hard drive or AsyncImage to load an image from a URL. For this example, you’ll stick with the standard Image class:

Python
```Python
from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source='/path/to/real_python.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
```

In this code, you import Image from the kivy.uix.image sub-package. The Image class takes a lot of different parameters, but the one that you want to use is source. This tells Kivy which image to load. Here, you pass a fully-qualified path to the image. The rest of the code is the same as what you saw in the previous example.

When you run this code, you’ll see something like the following:
![Hello world Image](https://files.realpython.com/media/02_mdriscoll_hello_image.607fbd03a04d.png)

# Laying Out the UI
Each GUI framework that you use has its own method of arranging widgets. For example, in wxPython you’ll use sizers, while in Tkinter you use a layout or geometry manager. With Kivy, you’ll use **__Layouts__**. There are several different types of Layouts that you can use. Here are some of the most common ones:

* BoxLayout
* FloatLayout
* GridLayout

You can search Kivy’s documentation for a full list of available Layouts. You can also look in kivy.uix for the actual source code.

Try out the BoxLayout with this code:

Python
```Python
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
```

Here, you import BoxLayout from kivy.uix.boxlayout and instantiate it. Then you create a list of colors, which are themselves lists of Red-Blue-Green (RGB) colors. Finally, you loop over a range of 5, creating a button btn for each iteration. To make things a bit more fun, you set the background_color of the button to a random color. You then add the button to your layout with layout.add_widget(btn).

When you run this code, you’ll see something like this:
![Image of BoxLayout example](https://files.realpython.com/media/kivy_hboxlayout.a8ac0394109e.png)

There are 5 randomly-colored buttons, one for each iteration of your for loop.

When you create a layout, there are a few arguments you should know:

* padding: You can specify the padding in pixels between the layout and its children in one of three ways:
    1. A four-argument list: [padding_left, padding_top, padding_right, padding_bottom]
    1. A two-argument list: [padding_horizontal, padding_vertical]
    1. A singular argument: padding=10
* spacing: You can add space between the children widgets with this argument.
* orientation: You can change the default orientation of the BoxLayout from horizontal to vertical.

# Adding Events
Like most GUI toolkits, Kivy is mostly **event-based**. The framework responds to user keypresses, mouse events, and touch events. Kivy has the concept of a **Clock** that you can use to schedule function calls for some time in the future.

Kivy also has the concept of __Properties__, which works with the __EventDispatcher__. Properties help you do validation checking. They also let you fire events whenever a widget changes its size or position.

Let’s add a **button event** to your button code from earlier:
Python
```Python
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('You pressed the button!')

if __name__ == '__main__':
    app = MainApp()
    app.run()
```

In this code, you call _button.bind()_ and link the _on_press_ event to MainApp.on_press_button(). This method implicitly takes in the widget _instance_, which is the _button_ object itself. Finally, a message will print to _stdout_ whenever the user presses your button.

# Using the KV Language
Kivy also provides a design language called **KV** that you can use with your Kivy applications. The KV language lets you separate your interface design from the application’s logic. This follows the separation of concerns principle and is part of the Model-View-Controller architectural pattern. You can update the previous example to use the KV language:

Python
```Python
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
```
This code might look a bit odd at first glance, as it creates a Button without setting any of its attributes or binding it to any events. What’s happening here is that Kivy will automatically look for a file that has the same name as the class in lowercase, without the App part of the class name.

In this case, the class name is ButtonApp, so Kivy will look for a file named button.kv. If that file exists and is properly formatted, then Kivy will use it to load up the UI. Go ahead and create this file and add the following code:

Text
```
<Button>:
    text: 'Press me'
    size_hint: (.5, .5)
    pos_hint: {'center_x': .5, 'center_y': .5}
    on_press: app.on_press_button()
```

Here’s what each line does:
* **Line 1** matches the Button call in your Python code. It tells Kivy to look into the instantiated object for a button definition.
* **Line 2** sets the button’s __text__.
* **Line 3** sets the width and height with __size_hint__.
* **Line 4** sets the button’s position with __pos_hint__.
* **Line 5** sets the on_press event handler. To tell Kivy where the event handler is, you use __app.on_press_button()__. Here, Kivy knows will look in the Application class for a method called .__on_press_button()__.

You can set up all of your widgets and layouts inside one or more KV language files. The KV language also supports importing Python modules in KV, creating dynamic classes, and much more. For full details, check out Kivy’s guide to the KV Language.

Now you’re ready to create a real application!

# Creating a Kivy Application
One of the best ways to learn a new skill is by creating something useful. With that in mind, you’ll use Kivy to build a calculator that supports the following operations:

* Addition
* Subtraction
* Multiplication
* Division

For this application, you’ll need a series of buttons in some kind of layout. You’ll also need a box along the top of your app to display the equations and their results. Here’s a sketch of your calculator:

![Image of calculator final result](https://files.realpython.com/media/kvcalc_mock.637f132ddd19.png)

Now that you have a goal for the UI, you can go ahead and write the code:

Python
```Python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout
```
Here’s how your calculator code works:

* **In lines 8 to 10**, you create a list of operators and a couple of handy values, last_was_operator and last_button, that you’ll use later on.
* **In lines 11 to 15**, you create a top-level layout main_layout and add a read-only TextInput widget to it.
* **In lines 16 to 21**, you create a nested list of lists containing most of your buttons for the calculator.
* **In line 22**, you start a for loop over those buttons. For each nested list you’ll do the following:
    * **In line 23**, you create a BoxLayout with a horizontal orientation.
    * **In line 24**, you start another for loop over the items in the nested list.
    * **In lines 25 to 39**, you create the buttons for the row, bind them to an event handler, and add the buttons to the horizontal BoxLayout from line 23.
    * **In line 31**, you add this layout to main_layout.
* **In lines 33 to 37**, you create the equals button (=), bind it to an event handler, and add it to main_layout.
The next step is to create the .on_button_press() event handler. Here’s what that code looks like:

Python
```Python
def on_button_press(self, instance):
    current = self.solution.text
    button_text = instance.text

    if button_text == "C":
        # Clear the solution widget
        self.solution.text = ""
    else:
        if current and (
            self.last_was_operator and button_text in self.operators):
            # Don't add two operators right after each other
            return
        elif current == "" and button_text in self.operators:
            # First character cannot be an operator
            return
        else:
            new_text = current + button_text
            self.solution.text = new_text
    self.last_button = button_text
    self.last_was_operator = self.last_button in self.operators
```

Most of the widgets in your application will call .on_button_press(). Here’s how it works:

* **Line 41** takes the instance argument so you can access which widget called the function.

* **Lines 42** and 43 extract and store the value of the solution and the button text.

* **Lines 45** to 47 check to see which button was pressed. If the user pressed C, then you’ll clear the solution. Otherwise, move on to the else statement.

* **Line 49** checks if the solution has any pre-existing value.

* **Line 50 to 52** check if the last button pressed was an operator button. If it was, then solution won’t be updated. This is to prevent the user from having two operators in a row. For example, 1 */ is not a valid statement.

* **Lines 53 to 55** check to see if the first character is an operator. If it is, then solution won’t be updated, since the first value can’t be an operator value.

* **Lines 56 to 58** drop to the else clause. If none of the previous conditions are met, then update solution.

* **Line 59** sets last_button to the label of the last button pressed.

* **Line 60** sets last_was_operator to True or False depending on whether or not it was an operator character.

The last bit of code to write is .on_solution():

Python
```Python
def on_solution(self, instance):
    text = self.solution.text
    if text:
        solution = str(eval(self.solution.text))
        self.solution.text = solution
```

Once again, you grab the current text from solution and use Python’s built-in eval() to execute it. If the user created a formula like 1+2, then eval() will run your code and return the result. Finally, you set the result as the new value for the solution widget.

> Note: eval() is somewhat dangerous because it can run arbitrary code. Most developers avoid using it because of that fact. However, since you’re only allowing integers, operators, and the period as input to eval(), it’s safe to use in this context.

When you run this code, your application will look like this on a desktop computer:

![Image of actual result](https://files.realpython.com/media/kvcalc.20e9d0008d8f.png)


<details>
  <summary>
  Complete Code Example
  </summary>

  Here’s the full code for the calculator:

  Python
  ```Python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
  ```
</details>


# Packaging Your App for Android

Now that you’ve finished the code for your application, you can share it with others. One great way to do that is to turn your code into an application that can run on your Android phone. To accomplish this, first you’ll need to install a package called buildozer with pip:

shell
```Shell
$ pip install buildozer
```

Then, create a new folder and navigate to it in your terminal. Once you’re there, you’ll need to run the following command:


shell
```Shell
$ buildozer init
```

This will create a buildozer.spec file that you’ll use to configure your build. For this example, you can edit the first few lines of the spec file as follows:

Text
```
[app]

# (str) Title of your application
title = KvCalc

# (str) Package name
package.name = kvcalc

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kvcalc
```

Feel free to browse the rest of the file to see what else you can change.

At this point, you’re almost ready to build your application, but first, you’ll want to install the dependencies for buildozer. Once those are installed, copy your calculator application into your new folder and rename it to main.py. This is required by buildozer. If you don’t have the file named correctly, then the build will fail.

Now you can run the following command:

shell
```Shell
$ buildozer -v android debug
```

--- Pouin Pouin... Buildzoer n'est pas compatible avec Windows... Il faut passer par une machine virtuelle de Linux...