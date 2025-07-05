[Skip to main content](https://flet.dev/docs/getting-started/custom-controls/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/getting-started/custom-controls/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/custom-controls/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Custom controls


On this page
# Custom controls
While Flet provides 100+ built-in controls that can be used on their own, the real beauty of programming with Flet is that all those controls can be utilized for creating your own reusable UI components using Python object-oriented programming concepts.
You can create custom controls in Python by styling and/or combining existing Flet controls.
## Styled controls[​](https://flet.dev/docs/getting-started/custom-controls/#styled-controls "Direct link to Styled controls")
The most simple custom control you can create is a styled control, for example, a button of a certain color and behaviour that will be used multiple times throughout your app.
To create a styled control, you need to create a new class in Python that inherits from the Flet control you are going to customize, `ElevatedButton` in this case:
```
classMyButton(ft.ElevatedButton):def__init__(self, text):super().__init__()    self.bgcolor = ft.Colors.ORANGE_300    self.color = ft.Colors.GREEN_800    self.text = text   
```

Your control has a constructor to customize properties and events and pass custom data. Note that you must call `super().__init__()` in your own constructor to have access to the properties and methods of the Flet control from which you inherit.
Now you can use your brand-new control in your app:
```
import flet as ftdefmain(page: ft.Page):  page.add(MyButton(text="OK"), MyButton(text="Cancel"))ft.app(main)
```

![](https://flet.dev/img/docs/custom-controls/styled-controls.png)
See example of using styled controls in [Calculator App tutorial](https://flet.dev/docs/tutorials/python-calculator#styled-controls).
### Handling events[​](https://flet.dev/docs/getting-started/custom-controls/#handling-events "Direct link to Handling events")
Similar to properties, you can pass event handlers as parameters into your custom control class constructor:
```
import flet as ftclassMyButton(ft.ElevatedButton):def__init__(self, text, on_click):super().__init__()    self.bgcolor = ft.Colors.ORANGE_300    self.color = ft.Colors.GREEN_800    self.text = text    self.on_click = on_clickdefmain(page: ft.Page):defok_clicked(e):print("OK clicked")defcancel_clicked(e):print("Cancel clicked")  page.add(    MyButton(text="OK", on_click=ok_clicked),    MyButton(text="Cancel", on_click=cancel_clicked),)ft.app(main)
```

## Composite controls[​](https://flet.dev/docs/getting-started/custom-controls/#composite-controls "Direct link to Composite controls")
Composite custom controls inherit from container controls such as `Column`, `Row`, `Stack` or even `View` to combine multiple Flet controls. The example below is a `Task` control that can be used in a To-Do app:
```
import flet as ftclassTask(ft.Row):def__init__(self, text):super().__init__()    self.text_view = ft.Text(text)    self.text_edit = ft.TextField(text, visible=False)    self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)    self.save_button = ft.IconButton(      visible=False, icon=ft.Icons.SAVE, on_click=self.save)    self.controls =[      ft.Checkbox(),      self.text_view,      self.text_edit,      self.edit_button,      self.save_button,]defedit(self, e):    self.edit_button.visible =False    self.save_button.visible =True    self.text_view.visible =False    self.text_edit.visible =True    self.update()defsave(self, e):    self.edit_button.visible =True    self.save_button.visible =False    self.text_view.visible =True    self.text_edit.visible =False    self.text_view.value = self.text_edit.value    self.update()defmain(page: ft.Page):  page.add(    Task(text="Do laundry"),    Task(text="Cook dinner"),)ft.app(main)
```

![](https://flet.dev/img/docs/custom-controls/composite-controls.gif)
You can find more examples of composite custom controls in [community examples](https://github.com/flet-dev/examples/tree/main/python/community) and [flet-contrib](https://github.com/flet-dev/flet-contrib/tree/main/flet_contrib) repos.
## Life-cycle methods[​](https://flet.dev/docs/getting-started/custom-controls/#life-cycle-methods "Direct link to Life-cycle methods")
Custom controls provide life-cycle "hook" methods that you may need to use for different use cases in your app.
### `build()`[​](https://flet.dev/docs/getting-started/custom-controls/#build "Direct link to build")
`build()` method is called when the control is being created and assigned its `self.page`.
Override `build()` method if you need to implement logic that cannot be executed in control's constructor because it requires access to the `self.page`. For example, choose the right icon depending on `self.page.platform` for your [adaptive app](https://flet.dev/docs/getting-started/adaptive-apps/#custom-adaptive-controls).
### `did_mount()`[​](https://flet.dev/docs/getting-started/custom-controls/#did_mount "Direct link to did_mount")
`did_mount()` method is called after the control is added to the page and assigned transient `uid`.
Override `did_mount()` method if you need to implement logic that needs to be executed after the control was added to the page, for example [Weather widget](https://github.com/flet-dev/examples/tree/main/python/community/weather_widget) which calls Open Weather API every minute to update itself with the new weather conditions.
### `will_unmount()`[​](https://flet.dev/docs/getting-started/custom-controls/#will_unmount "Direct link to will_unmount")
`will_unmount()` method is called before the control is removed from the page.
Override `will_unmount()` method to execute clean-up code.
### `before_update()`[​](https://flet.dev/docs/getting-started/custom-controls/#before_update "Direct link to before_update")
`before_update()` method is called every time when the control is being updated.
Make sure not to call `update()` method within `before_update()`.
## Isolated controls[​](https://flet.dev/docs/getting-started/custom-controls/#isolated-controls "Direct link to Isolated controls")
Custom control has `is_isolated` property which defaults to `False`.
If you set `is_isolated` to `True`, your control will be isolated from outside layout, i.e. when `update()` method is called for the parent control, the control itself will be updated but any changes to the controls' children are not included into the update digest. Isolated controls should call `self.update()` to push its changes to a Flet page.
As a best practice, any custom control that calls `self.update()` inside its class methods should be isolated.
In the above examples, simple styled `MyButton` doesn't need to be isolated, but the `Task` should be:
```
classTask(ft.Row):def__init__(self, text):super().__init__()defis_isolated(self):returnTrue
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/custom-controls.md)
[PreviousFlet controls](https://flet.dev/docs/getting-started/flet-controls)[NextAdaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)
  * [Styled controls](https://flet.dev/docs/getting-started/custom-controls/#styled-controls)
    * [Handling events](https://flet.dev/docs/getting-started/custom-controls/#handling-events)
  * [Composite controls](https://flet.dev/docs/getting-started/custom-controls/#composite-controls)
  * [Life-cycle methods](https://flet.dev/docs/getting-started/custom-controls/#life-cycle-methods)
    * [`build()`](https://flet.dev/docs/getting-started/custom-controls/#build)
    * [`did_mount()`](https://flet.dev/docs/getting-started/custom-controls/#did_mount)
    * [`will_unmount()`](https://flet.dev/docs/getting-started/custom-controls/#will_unmount)
    * [`before_update()`](https://flet.dev/docs/getting-started/custom-controls/#before_update)
  * [Isolated controls](https://flet.dev/docs/getting-started/custom-controls/#isolated-controls)


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
