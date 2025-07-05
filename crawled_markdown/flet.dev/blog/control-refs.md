[Skip to main content](https://flet.dev/blog/control-refs/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
All posts
### 2025
  * [Introducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)
  * [Tap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
  * [Flet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
  * [Flet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)


### 2024
  * [Flet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
  * [pyproject.toml support for flet build command](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command)
  * [Flet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)
  * [Flet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)
  * [Flet v0.23.0 Release Announcement](https://flet.dev/blog/flet-v-0-23-release-announcement)
  * [Flet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)
  * [Flet packaging update](https://flet.dev/blog/flet-packaging-update)
  * [Controls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)
  * [Flet FastAPI and async API improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements)
  * [Flet adaptive UI and custom controls release](https://flet.dev/blog/flet-adaptive-and-custom-controls)


### 2023
  * [Packaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)
  * [Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)
  * [Flet for Android](https://flet.dev/blog/flet-for-android)
  * [Flet for iOS](https://flet.dev/blog/flet-for-ios)
  * [Scrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)
  * [Canvas](https://flet.dev/blog/canvas)
  * [Flet Charts](https://flet.dev/blog/flet-charts)
  * [Standalone Flet web apps with Pyodide](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide)
  * [Packaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)


### 2022
  * [Flet mobile update](https://flet.dev/blog/flet-mobile-update)
  * [Flet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)
  * [ResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)
  * [Matplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts)
  * [Gesture detector](https://flet.dev/blog/gesture-detector)
  * [User authentication](https://flet.dev/blog/user-authentication)
  * [File picker and uploads](https://flet.dev/blog/file-picker-and-uploads)
  * [Fun with animations](https://flet.dev/blog/fun-with-animations)
  * [Beautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)
  * [Control Refs](https://flet.dev/blog/control-refs)
  * [Flet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)
  * [Navigation and Routing](https://flet.dev/blog/navigation-and-routing)
  * [New release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)
  * [Using custom fonts in a Flet app](https://flet.dev/blog/using-custom-fonts-in-flet-app)
  * [Introducing Flet](https://flet.dev/blog/introducing-flet)


# Control Refs
August 3, 2022 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet controls are objects and to access their properties we need to keep references (variables) to those objects.
Consider the following example:
```
import flet as ftdefmain(page):  first_name = ft.TextField(label="First name", autofocus=True)  last_name = ft.TextField(label="Last name")  greetings = ft.Column()defbtn_click(e):    greetings.controls.append(ft.Text(f"Hello, {first_name.value}{last_name.value}!"))    first_name.value =""    last_name.value =""    page.update()    first_name.focus()  page.add(    first_name,    last_name,    ft.ElevatedButton("Say hello!", on_click=btn_click),    greetings,)ft.app(target=main)
```

In the very beginning of `main()` method we create three controls which we are going to use in button's `on_click` handler: two `TextField` for first and last names and a `Column` - container for greeting messages. We create controls with all their properties set and in the end of `main()` method, in `page.add()` call, we use their references (variables).
When more and mode controls and event handlers added it becomes challenging to keep all control definitions in one place, so they become scattered across `main()` body. Glancing at `page.add()` parameters it's hard to imagine (without constant jumping to variable definitions in IDE) what would the end form look like:
```
  page.add(    first_name,    last_name,    ft.ElevatedButton("Say hello!", on_click=btn_click),    greetings,)
```

Is `first_name` a TextField, does it have autofocus set? Is greetings a `Row` or a `Column`?
## `Ref` class[​](https://flet.dev/blog/control-refs/#ref-class "Direct link to ref-class")
Flet provides `Ref` utility class which allows to define a reference to the control, use that reference in event handlers and set the reference to a real control later, while building a tree. The idea comes from [React](https://reactjs.org/docs/refs-and-the-dom.html).
To define a new typed control reference:
```
first_name = ft.Ref[ft.TextField]()
```

To access referenced control (control de-reference) use `Ref.current` property:
```
# empty first namefirst_name.current.value =""
```

To assign control to a reference set `Control.ref` property to a reference:
```
page.add(  ft.TextField(ref=first_name, label="First name", autofocus=True))
```

note
All Flet controls have `ref` property.
We could re-write our program to use references:
```
import flet as ftdefmain(page):  first_name = ft.Ref[ft.TextField]()  last_name = ft.Ref[ft.TextField]()  greetings = ft.Ref[ft.Column]()defbtn_click(e):    greetings.current.controls.append(      ft.Text(f"Hello, {first_name.current.value}{last_name.current.value}!"))    first_name.current.value =""    last_name.current.value =""    page.update()    first_name.current.focus()  page.add(    ft.TextField(ref=first_name, label="First name", autofocus=True),    ft.TextField(ref=last_name, label="Last name"),    ft.ElevatedButton("Say hello!", on_click=btn_click),    ft.Column(ref=greetings),)ft.app(target=main)
```

Now we can clearly see in `page.add()` the structure of the page and all the controls it's built of.
Yes, the logic becomes a little bit more verbose as you need to add `.current.` to access ref's control, but it's a matter of personal preference :)
[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [how-to](https://flet.dev/blog/tags/how-to)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-08-03-control-refs.md)
[Newer postBeautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)[Older postFlet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)
  * [`Ref` class](https://flet.dev/blog/control-refs/#ref-class)


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
