[Skip to main content](https://flet.dev/docs/tutorials/python-todo/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/tutorials/python-todo/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/tutorials/python-todo/)
  * [Tutorials](https://flet.dev/docs/tutorials)
    * [To-Do app](https://flet.dev/docs/tutorials/python-todo)
    * [Calculator app](https://flet.dev/docs/tutorials/python-calculator)
    * [Trello clone](https://flet.dev/docs/tutorials/trello-clone)
    * [Solitaire game](https://flet.dev/docs/tutorials/python-solitaire)
    * [Chat app](https://flet.dev/docs/tutorials/python-chat)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * To-Do app


On this page
# Create To-Do app in Python with Flet
In this tutorial we will show you, step-by-step, how to create a To-Do app in Python using Flet framework and then publish it as a desktop, mobile or web app. The app is a single-file console program of just [172 lines (formatted!) of Python code](https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py), yet it is a multi-platform application with rich, responsive UI:
![](https://flet.dev/img/docs/tutorial/todo-complete-demo-web.gif)
You can see the live demo [here](https://gallery.flet.dev/todo/).
We chose a To-Do app for the tutorial, because it covers all of the basic concepts you would need to create a Flet app: building a page layout, adding controls, handling events, displaying and editing lists, making reusable UI components, and publishing options.
The tutorial consists of the following steps:
  * [Getting started with Flet](https://flet.dev/docs/tutorials/python-todo/#getting-started-with-flet)
  * [Adding page controls and handling events](https://flet.dev/docs/tutorials/python-todo/#adding-page-controls-and-handling-events)
  * [View, edit and delete list items](https://flet.dev/docs/tutorials/python-todo/#view-edit-and-delete-list-items)
  * [Filtering list items](https://flet.dev/docs/tutorials/python-todo/#filtering-list-items)
  * [Final touches](https://flet.dev/docs/tutorials/python-todo/#final-touches)
  * [Publishing the app](https://flet.dev/docs/tutorials/python-todo/#publishing-the-app)


## Getting started with Flet[​](https://flet.dev/docs/tutorials/python-todo/#getting-started-with-flet "Direct link to Getting started with Flet")
To create a multi-platform app in Python with Flet, you don't need to know HTML, CSS or JavaScript, but you do need a basic knowledge of Python and object-oriented programming.
Before you can create your first Flet app, you need to [setup your development environment](https://flet.dev/docs/getting-started/), which requires Python 3.9 or above and `flet` package.
Once you have Flet installed, let's [create](https://flet.dev/docs/getting-started/create-flet-app) a simple hello-world app.
Create `hello.py` with the following contents:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(value="Hello, world!"))ft.app(main)
```

Run this app and you will see a new window with a greeting:
![](https://flet.dev/img/docs/tutorial/todo-app-hello-world.png)
## Adding page controls and handling events[​](https://flet.dev/docs/tutorials/python-todo/#adding-page-controls-and-handling-events "Direct link to Adding page controls and handling events")
Now we're ready to create a multi-user To-Do app.
To start, we'll need a [TextField](https://flet.dev/docs/controls/textfield) for entering a task name, and an "+" [FloatingActionButton](https://flet.dev/docs/controls/floatingactionbutton) with an event handler that will display a [Checkbox](https://flet.dev/docs/controls/checkbox) with a new task.
Create `todo.py` with the following contents:
```
import flet as ftdefmain(page: ft.Page):defadd_clicked(e):    page.add(ft.Checkbox(label=new_task.value))    new_task.value =""    page.update()  new_task = ft.TextField(hint_text="What's needs to be done?")  page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))ft.app(main)
```

Run the app and you should see a page like this:
![](https://flet.dev/img/docs/tutorial/todo-app-1.png)
### Page layout[​](https://flet.dev/docs/tutorials/python-todo/#page-layout "Direct link to Page layout")
Now let's make the app look nice! We want the entire app to be at the top center of the page, taking up 600 px width. The TextField and the "+" button should be aligned horizontally, and take up full app width:
![](https://flet.dev/img/docs/tutorial/todo-diagram-1.svg)
[`Row`](https://flet.dev/docs/controls/row) is a control that is used to lay its children controls out horizontally on a page. [`Column`](https://flet.dev/docs/controls/column) is a control that is used to lay its children controls out vertically on a page.
Replace `todo.py` contents with the following:
```
import flet as ftdefmain(page: ft.Page):defadd_clicked(e):    tasks_view.controls.append(ft.Checkbox(label=new_task.value))    new_task.value =""    view.update()  new_task = ft.TextField(hint_text="What needs to be done?", expand=True)  tasks_view = ft.Column()  view=ft.Column(    width=600,    controls=[      ft.Row(        controls=[          new_task,          ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),],),      tasks_view,],)  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.add(view)ft.app(main)
```

Run the app and you should see a page like this:
![](https://flet.dev/img/docs/tutorial/todo-app-2.png)
### Reusable UI components[​](https://flet.dev/docs/tutorials/python-todo/#reusable-ui-components "Direct link to Reusable UI components")
While we could continue writing our app in the `main` function, the best practice would be to create a [reusable UI component](https://flet.dev/docs/getting-started/custom-controls). Imagine you are working on an app header, a side menu, or UI that will be a part of a larger project. Even if you can't think of such uses right now, we still recommend creating all your Flet apps with composability and reusability in mind.
To make a reusable To-Do app component, we are going to encapsulate its state and presentation logic in a separate class:
```
import flet as ftclassTodoApp(ft.Column):# application's root control is a Column containing all other controlsdef__init__(self):super().__init__()    self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)    self.tasks_view = ft.Column()    self.width =600    self.controls =[      ft.Row(        controls=[          self.new_task,          ft.FloatingActionButton(            icon=ft.Icons.ADD, on_click=self.add_clicked),],),      self.tasks_view,]defadd_clicked(self, e):    self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))    self.new_task.value =""    self.update()defmain(page: ft.Page):  page.title ="To-Do App"  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.update()# create application instance  todo = TodoApp()# add application's root control to the page  page.add(todo)ft.app(main)
```

note
Try adding two `TodoApp` components to the page:
```
# create application instanceapp1 = TodoApp()app2 = TodoApp()# add application's root control to the pagepage.add(app1, app2)
```

## View, edit and delete list items[​](https://flet.dev/docs/tutorials/python-todo/#view-edit-and-delete-list-items "Direct link to View, edit and delete list items")
In the [previous step](https://flet.dev/docs/tutorials/python-todo/#adding-page-controls-and-handling-events), we created a basic To-Do app with task items shown as checkboxes. Let's improve the app by adding "Edit" and "Delete" buttons next to a task name. The "Edit" button will switch a task item to edit mode.
![](https://flet.dev/img/docs/tutorial/todo-diagram-2.svg)
Each task item is represented by two rows: `display_view` row with Checkbox, "Edit" and "Delete" buttons and `edit_view` row with TextField and "Save" button. `view` column serves as a container for both `display_view` and `edit_view` rows.
Before this step, the code was short enough to be fully included in the tutorial. Going forward, we will be highlighting only the changes introduced in a step.
Copy the entire code for this step from [here](https://github.com/flet-dev/examples/blob/main/python/tutorials/todo/to-do-4.py). Below we will explain the changes we've done to implement view, edit, and delete tasks.
To encapsulate task item views and actions, we introduced a new `Task` class:
```
classTask(ft.Column):def__init__(self, task_name, task_delete):super().__init__()    self.task_name = task_name    self.task_delete = task_delete    self.display_task = ft.Checkbox(value=False, label=self.task_name)    self.edit_name = ft.TextField(expand=1)    self.display_view = ft.Row(      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,      vertical_alignment=ft.CrossAxisAlignment.CENTER,      controls=[        self.display_task,        ft.Row(          spacing=0,          controls=[            ft.IconButton(              icon=ft.Icons.CREATE_OUTLINED,              tooltip="Edit To-Do",              on_click=self.edit_clicked,),            ft.IconButton(              ft.Icons.DELETE_OUTLINE,              tooltip="Delete To-Do",              on_click=self.delete_clicked,),],),],)    self.edit_view = ft.Row(      visible=False,      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,      vertical_alignment=ft.CrossAxisAlignment.CENTER,      controls=[        self.edit_name,        ft.IconButton(          icon=ft.Icons.DONE_OUTLINE_OUTLINED,          icon_color=ft.Colors.GREEN,          tooltip="Update To-Do",          on_click=self.save_clicked,),],)    self.controls =[self.display_view, self.edit_view]defedit_clicked(self, e):    self.edit_name.value = self.display_task.label    self.display_view.visible =False    self.edit_view.visible =True    self.update()defsave_clicked(self, e):    self.display_task.label = self.edit_name.value    self.display_view.visible =True    self.edit_view.visible =False    self.update()defdelete_clicked(self, e):    self.task_delete(self)
```

Additionally, we changed `TodoApp` class to create and hold `Task` instances when the "Add" button is clicked:
```
classTodoApp(ft.Column):# application's root control is a Column containing all other controlsdef__init__(self):super().__init__()    self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)    self.tasks = ft.Column()    self.width =600    self.controls =[      ft.Row(        controls=[          self.new_task,          ft.FloatingActionButton(            icon=ft.Icons.ADD, on_click=self.add_clicked),],),      self.tasks,]defadd_clicked(self, e):    task = Task(self.new_task.value, self.task_delete)    self.tasks.controls.append(task)    self.new_task.value =""    self.update()deftask_delete(self, task):    self.tasks.controls.remove(task)    self.update()
```

For "Delete" task operation, we implemented `task_delete()` method in `TodoApp` class which accepts task control instance as a parameter.
Then, we passed a reference to `task_delete` method into Task constructor and called it on "Delete" button event handler.
Run the app and try to edit and delete tasks:
![](https://flet.dev/img/docs/tutorial/view-edit-delete.gif)
## Filtering list items[​](https://flet.dev/docs/tutorials/python-todo/#filtering-list-items "Direct link to Filtering list items")
We already have a functional To-Do app where we can create, edit, and delete tasks. To be even more productive, we want to be able to filter tasks by their status.
Copy the entire code for this step from [here](https://github.com/flet-dev/examples/blob/main/python/tutorials/todo/to-do-5.py). Below we will explain the changes we've done to implement filtering.
`Tabs` control is used to display filter:
```
# ...classTodoApp(ft.Column):# application's root control is a Column containing all other controlsdef__init__(self):super().__init__()    self.new_task = ft.TextField(hint_text="What's needs to be done?", expand=True)    self.tasks = ft.Column()    self.filter= ft.Tabs(      selected_index=0,      on_change=self.tabs_changed,      tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],)# ....
```

To display different lists of tasks depending on their statuses, we could maintain three lists with "All", "Active" and "Completed" tasks. We, however, chose an easier approach where we maintain the same list and only change a task's visibility depending on its status.
In `TodoApp` class we overrided [`before_update()`](https://flet.dev/docs/getting-started/custom-controls#before_update) method alled every time when the control is being updated. It iterates through all the tasks and updates their `visible` property depending on the status of the task:
```
classTodoApp(ft.Column):# ...defbefore_update(self):    status = self.filter.tabs[self.filter.selected_index].textfor task in self.tasks.controls:      task.visible =(        status =="all"or(status =="active"and task.completed ==False)or(status =="completed"and task.completed))
```

Filtering should occur when we click on a tab or change a task status. `TodoApp.before_update()` method is called when Tabs selected value is changed or Task item checkbox is clicked:
```
classTodoApp(ft.Column):# ...deftabs_changed(self, e):    self.update()deftask_status_change(self, e):    self.update()defadd_clicked(self, e):    task = Task(self.new_task.value, self.task_status_change, self.task_delete)# ...classTask(ft.Column):def__init__(self, task_name, task_status_change, task_delete):super().__init__()    self.completed =False    self.task_name = task_name    self.task_status_change = task_status_change    self.task_delete = task_delete    self.display_task = ft.Checkbox(      value=False, label=self.task_name, on_change=self.status_changed)# ...defstatus_changed(self, e):    self.completed = self.display_task.value    self.task_status_change()
```

Run the app and try filtering tasks by clicking on the tabs:
![](https://flet.dev/img/docs/tutorial/todo-app-filtering.gif)
## Final touches[​](https://flet.dev/docs/tutorials/python-todo/#final-touches "Direct link to Final touches")
Our Todo app is almost complete now. As a final touch, we will add a footer (`Column` control) displaying the number of incomplete tasks (`Text` control) and a "Clear completed" button.
Copy the entire code for this step from [here](https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py). Below we highlighted the changes we've done to implement the footer:
```
classTodoApp():def__init__(self):# ...    self.items_left = ft.Text("0 items left")    self.width =600    self.controls =[      ft.Row([ft.Text(value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],        alignment=ft.MainAxisAlignment.CENTER,),      ft.Row(        controls=[          self.new_task,          ft.FloatingActionButton(            icon=ft.Icons.ADD, on_click=self.add_clicked),],),      ft.Column(        spacing=25,        controls=[          self.filter,          self.tasks,          ft.Row(            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,            vertical_alignment=ft.CrossAxisAlignment.CENTER,            controls=[              self.items_left,              ft.OutlinedButton(                text="Clear completed", on_click=self.clear_clicked),],),],),]# ...defclear_clicked(self, e):for task in self.tasks.controls[:]:if task.completed:        self.task_delete(task)defbefore_update(self):    status = self.filter.tabs[self.filter.selected_index].text    count =0for task in self.tasks.controls:      task.visible =(        status =="all"or(status =="active"and task.completed ==False)or(status =="completed"and task.completed))ifnot task.completed:        count +=1    self.items_left.value =f"{count} active item(s) left"
```

Run the app:
![](https://flet.dev/img/docs/tutorial/todo-app-4.png)
## Publishing the app[​](https://flet.dev/docs/tutorials/python-todo/#publishing-the-app "Direct link to Publishing the app")
Congratulations! You have created your first Python app with Flet, and it looks awesome!
Now it's time to share your app with the world!
[Follow these instructions](https://flet.dev/docs/publish) to publish your Flet app as a mobile, desktop or web app.
## Summary[​](https://flet.dev/docs/tutorials/python-todo/#summary "Direct link to Summary")
In this tutorial, you have learnt how to:
  * Create a simple Flet app;
  * Work with [Reusable UI components](https://flet.dev/docs/getting-started/custom-controls);
  * Design UI layout using `Column` and `Row` controls;
  * Work with lists: view, edit and delete items, filtering;
  * [Publish](https://flet.dev/docs/publish/) your Flet app to multiple platforms;


For further reading you can explore [controls](https://flet.dev/docs/controls) and [examples repository](https://github.com/flet-dev/examples/tree/main/python).
We would love to hear your feedback! Please drop us an email, join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/tutorials/python-todo.md)
[PreviousTutorials](https://flet.dev/docs/tutorials)[NextCalculator app](https://flet.dev/docs/tutorials/python-calculator)
  * [Getting started with Flet](https://flet.dev/docs/tutorials/python-todo/#getting-started-with-flet)
  * [Adding page controls and handling events](https://flet.dev/docs/tutorials/python-todo/#adding-page-controls-and-handling-events)
    * [Page layout](https://flet.dev/docs/tutorials/python-todo/#page-layout)
    * [Reusable UI components](https://flet.dev/docs/tutorials/python-todo/#reusable-ui-components)
  * [View, edit and delete list items](https://flet.dev/docs/tutorials/python-todo/#view-edit-and-delete-list-items)
  * [Filtering list items](https://flet.dev/docs/tutorials/python-todo/#filtering-list-items)
  * [Final touches](https://flet.dev/docs/tutorials/python-todo/#final-touches)
  * [Publishing the app](https://flet.dev/docs/tutorials/python-todo/#publishing-the-app)
  * [Summary](https://flet.dev/docs/tutorials/python-todo/#summary)


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
