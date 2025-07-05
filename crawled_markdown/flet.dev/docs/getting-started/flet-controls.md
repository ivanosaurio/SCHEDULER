[Skip to main content](https://flet.dev/docs/getting-started/flet-controls/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
    * [Create a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)
    * [Running Flet app](https://flet.dev/docs/getting-started/running-app)
    * [Flet controls](https://flet.dev/docs/getting-started/flet-controls)
    * [Custom controls](https://flet.dev/docs/getting-started/custom-controls)
    * [Adaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)
    * [Navigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)
    * [Testing on iOS](https://flet.dev/docs/getting-started/testing-on-ios)
    * [Testing on Android](https://flet.dev/docs/getting-started/testing-on-android)
    * [Async apps](https://flet.dev/docs/getting-started/async-apps)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/getting-started/flet-controls/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/flet-controls/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Flet controls


On this page
# Flet controls
User interface is made of **Controls** (aka widgets). To make controls visible to a user they must be added to a `Page` or inside other controls. Page is the top-most control. Nesting controls into each other could be represented as a tree with Page as a root.
Controls are just regular Python classes. Create control instances via constructors with parameters matching their properties, for example:
```
t = ft.Text(value="Hello, world!", color="green")
```

To display control on a page add it to `controls` list of a Page and call `page.update()` to send page changes to a browser or desktop client:
```
import flet as ftdefmain(page: ft.Page):  t = ft.Text(value="Hello, world!", color="green")  page.controls.append(t)  page.update()ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/controls-text.png)
note
In the following examples we will be showing just the contents of `main` function.
You can modify control properties and the UI will be updated on the next `page.update()`:
```
t = ft.Text()page.add(t)# it's a shortcut for page.controls.append(t) and then page.update()for i inrange(10):  t.value =f"Step {i}"  page.update()  time.sleep(1)
```

Some controls are "container" controls (like Page) which could contain other controls. For example, `Row` control allows arranging other controls in a row one-by-one:
```
page.add(  ft.Row(controls=[    ft.Text("A"),    ft.Text("B"),    ft.Text("C")]))
```

or `TextField` and `ElevatedButton` next to it:
```
page.add(  ft.Row(controls=[    ft.TextField(label="Your name"),    ft.ElevatedButton(text="Say my name!")]))
```

`page.update()` is smart enough to send only the changes made since its last call, so you can add a couple of new controls to the page, remove some of them, change other controls' properties and then call `page.update()` to do a batched update, for example:
```
for i inrange(10):  page.controls.append(ft.Text(f"Line {i}"))if i >4:    page.controls.pop(0)  page.update()  time.sleep(0.3)
```

Some controls, like buttons, could have event handlers reacting on a user input, for example `ElevatedButton.on_click`:
```
defbutton_clicked(e):  page.add(ft.Text("Clicked!"))page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
```

and more advanced example for a simple To-Do:
```
import flet as ftdefmain(page):defadd_clicked(e):    page.add(ft.Checkbox(label=new_task.value))    new_task.value =""    new_task.focus()    new_task.update()  new_task = ft.TextField(hint_text="What's needs to be done?", width=300)  page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/simple-ToDo.png)
info
Flet implements _imperative_ UI model where you "manually" build application UI with stateful controls and then mutate it by updating control properties. Flutter implements _declarative_ model where UI is automatically re-built on application data changes. Managing application state in modern frontend applications is inherently complex task and Flet's "old-school" approach could be more attractive to programmers without frontend experience.
### `visible` property[​](https://flet.dev/docs/getting-started/flet-controls/#visible-property "Direct link to visible-property")
Every control has `visible` property which is `true` by default - control is rendered on the page. Setting `visible` to `false` completely prevents control (and all its children if any) from rendering on a page canvas. Hidden controls cannot be focused or selected with a keyboard or mouse and they do not emit any events.
### `disabled` property[​](https://flet.dev/docs/getting-started/flet-controls/#disabled-property "Direct link to disabled-property")
Every control has `disabled` property which is `false` by default - control and all its children are enabled. `disabled` property is mostly used with data entry controls like `TextField`, `Dropdown`, `Checkbox`, buttons. However, `disabled` could be set to a parent control and its value will be propagated down to all children recursively.
For example, if you have a form with multiple entry control you can set `disabled` property for each control individually:
```
first_name = ft.TextField()last_name = ft.TextField()first_name.disabled =Truelast_name.disabled =Truepage.add(first_name, last_name)
```

or you can put form controls into container, e.g. `Column` and then set `disabled` for the column:
```
first_name = ft.TextField()last_name = ft.TextField()c = ft.Column(controls=[  first_name,  last_name])c.disabled =Truepage.add(c)
```

## Buttons[​](https://flet.dev/docs/getting-started/flet-controls/#buttons "Direct link to Buttons")
`Button` is the most essential input control which generates `click` event when pressed:
```
btn = ft.ElevatedButton("Click me!")page.add(btn)
```

![](https://flet.dev/img/docs/getting-started/getting-user-input-elevated-button.png)
All events generated by controls on a web page are continuously sent back to your script, so how do you respond to a button click?
## Event handlers[​](https://flet.dev/docs/getting-started/flet-controls/#event-handlers "Direct link to Event handlers")
Buttons with events in "Counter" app:
```
import flet as ftdefmain(page: ft.Page):  page.title ="Flet counter example"  page.vertical_alignment = ft.MainAxisAlignment.CENTER  txt_number = ft.TextField(value="0", text_align="right", width=100)defminus_click(e):    txt_number.value =str(int(txt_number.value)-1)    page.update()defplus_click(e):    txt_number.value =str(int(txt_number.value)+1)    page.update()  page.add(    ft.Row([        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),        txt_number,        ft.IconButton(ft.Icons.ADD, on_click=plus_click),],      alignment=ft.MainAxisAlignment.CENTER,))ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/getting-user-input-event-handlers.png)
## Textbox[​](https://flet.dev/docs/getting-started/flet-controls/#textbox "Direct link to Textbox")
Flet provides a number of [controls](https://flet.dev/docs/controls) for building forms: [TextField](https://flet.dev/docs/controls/textfield), [Checkbox](https://flet.dev/docs/controls/checkbox), [Dropdown](https://flet.dev/docs/controls/dropdown), [ElevatedButton](https://flet.dev/docs/controls/elevatedbutton).
Let's ask a user for a name:
```
import flet as ftdefmain(page):defbtn_click(e):ifnot txt_name.value:      txt_name.error_text ="Please enter your name"      page.update()else:      name = txt_name.value      page.clean()      page.add(ft.Text(f"Hello, {name}!"))  txt_name = ft.TextField(label="Your name")  page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/getting-user-input-textbox.png)
## Checkbox[​](https://flet.dev/docs/getting-started/flet-controls/#checkbox "Direct link to Checkbox")
The [Checkbox](https://flet.dev/docs/controls/checkbox) control provides you with various properties and events emmiters for ease of use.
Let's create a one checkbox ToDo:
```
import flet as ftdefmain(page):defcheckbox_changed(e):    output_text.value =(f"You have learned how to ski : {todo_check.value}.")    page.update()  output_text = ft.Text()  todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)  page.add(todo_check, output_text)ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/getting-user-input-checkbox.png)
## Dropdown[​](https://flet.dev/docs/getting-started/flet-controls/#dropdown "Direct link to Dropdown")
```
import flet as ftdefmain(page: ft.Page):defbutton_clicked(e):    output_text.value =f"Dropdown value is: {color_dropdown.value}"    page.update()  output_text = ft.Text()  submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)  color_dropdown = ft.Dropdown(    width=100,    options=[      ft.dropdown.Option("Red"),      ft.dropdown.Option("Green"),      ft.dropdown.Option("Blue"),],)  page.add(color_dropdown, submit_btn, output_text)ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/getting-user-input-dropdown.png)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/flet-controls.md)
[PreviousRunning Flet app](https://flet.dev/docs/getting-started/running-app)[NextCustom controls](https://flet.dev/docs/getting-started/custom-controls)
  * [`visible` property](https://flet.dev/docs/getting-started/flet-controls/#visible-property)
  * [`disabled` property](https://flet.dev/docs/getting-started/flet-controls/#disabled-property)
  * [Buttons](https://flet.dev/docs/getting-started/flet-controls/#buttons)
  * [Event handlers](https://flet.dev/docs/getting-started/flet-controls/#event-handlers)
  * [Textbox](https://flet.dev/docs/getting-started/flet-controls/#textbox)
  * [Checkbox](https://flet.dev/docs/getting-started/flet-controls/#checkbox)
  * [Dropdown](https://flet.dev/docs/getting-started/flet-controls/#dropdown)


Docs
  * [Introduction](https://flet.dev/docs)
  * [Controls reference](https://flet.dev/docs/controls)


Community
  * [Discord](https://discord.gg/dzWXP8SHG8)
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/flet)
  * [X](https://x.com/fletdev)
  * [Bluesky](https://bsky.app/profile/fletdev.bsky.social)


More
  * [Blog](https://flet.dev/blog)
  * [GitHub](https://github.com/flet-dev/flet)
  * [Support](https://flet.dev/support)


Legal
  * [Privacy policy](https://flet.dev/privacy-policy)


Copyright © 2025 Appveyor Systems Inc. Built with Docusaurus.
