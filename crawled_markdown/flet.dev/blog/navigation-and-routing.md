[Skip to main content](https://flet.dev/blog/navigation-and-routing/#__docusaurus_skipToContent_fallback)
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


# Navigation and Routing
July 23, 2022 · 5 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
[Flet 0.1.42](https://pypi.org/project/flet/0.1.42/) has been released with navigation and routing!
Navigation and routing is an essential feature of Single Page Applications (SPA) which allows organizing application user interface into virtual pages (views) and "navigate" between them while application URL reflects the current state of the app.
For mobile apps navigation and routing serves as a [deep linking](https://docs.flutter.dev/development/ui/navigation/deep-linking) to specific application parts.
Well, it took [more efforts](https://github.com/flet-dev/flet/pull/95/files) than expected to add navigation and routing into Flet as the implementation is based on [Navigator 2.0](https://medium.com/flutter/learning-flutters-new-navigation-and-routing-system-7c9068155ade) Flutter API and required to replace Flet's "Page" abstraction with "Page and Views". Flutter's newer navigation and routing API has substantial improvements such as:
  1. Programmatic control over history stack.
  2. An easy way to intercept a call to "Back" button in AppBar.
  3. Robust synchronization with browser history.

![](https://flet.dev/img/docs/navigation-routing/routing-app-example.gif)
Explore [source code](https://github.com/flet-dev/examples/blob/main/python/apps/routing-navigation/building-views-on-route-change.py) of the example above.
## Page route[​](https://flet.dev/blog/navigation-and-routing/#page-route "Direct link to Page route")
Page route is a portion of application URL after `#` symbol:
![](https://flet.dev/img/docs/navigation-routing/page-address-route.png)
Default application route, if not set in application URL by the user, is `/`. All routes start with `/`, for example `/store`, `/authors/1/books/2`.
Application route can be obtained by reading `page.route` property, for example:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

Grab application URL, open a new browser tab, paste the URL, modify its part after `#` to `/test` and hit enter. You should see "Initial route: /test".
Every time the route in the URL is changed (by editing the URL or navigating browser history with Back/Forward buttons) Flet calls `page.on_route_change` event handler:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))defroute_change(route):    page.add(ft.Text(f"New route: {route}"))  page.on_route_change = route_change  page.update()ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

Now try updating URL hash a few times and then use Back/Forward buttons! You should see a new message added to a page each time the route changes:
![](https://flet.dev/img/docs/navigation-routing/page-route-change-event.gif)
Route can be changed programmatically, by updating `page.route` property:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))defroute_change(route):    page.add(ft.Text(f"New route: {route}"))defgo_store(e):    page.route ="/store"    page.update()  page.on_route_change = route_change  page.add(ft.ElevatedButton("Go to Store", on_click=go_store))ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

Click "Go to Store" button and you'll see application URL is changed and a new item is pushed in a browser history. You can use browser "Back" button to navigate to a previous route.
## Page views[​](https://flet.dev/blog/navigation-and-routing/#page-views "Direct link to Page views")
Flet's [Page](https://flet.dev/docs/controls/page) now is not just a single page, but a container for [View](https://flet.dev/docs/controls/view) layered on top of each other like a sandwich:
![](https://flet.dev/img/docs/navigation-routing/page-views.svg)
A collection of views represents navigator history. Page has [`page.views`](https://flet.dev/docs/controls/page#views) property to access views collection.
The last view in the list is the one currently displayed on a page. Views list must have at least one element (root view).
To simulate a transition between pages change `page.route` and add a new `View` in the end of `page.view` list.
Pop the last view from the collection and change route to a "previous" one in [`page.on_view_pop`](https://flet.dev/docs/controls/page#on_view_pop) event handler to go back.
## Building views on route change[​](https://flet.dev/blog/navigation-and-routing/#building-views-on-route-change "Direct link to Building views on route change")
To build a reliable navigation there must be a single place in the program which builds a list of views depending on the current route. Other words, navigation history stack (represented by the list of views) must be a function of a route.
This place is [`page.on_route_change`](https://flet.dev/docs/controls/page#on_route_change) event handler.
Let's put everything together into a complete example which allows navigating between two pages:
```
import flet as ftdefmain(page: ft.Page):  page.title ="Routes Example"defroute_change(route):    page.views.clear()    page.views.append(      ft.View("/",[          ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_VARIANT),          ft.ElevatedButton("Visit Store", on_click=lambda_: page.go("/store")),],))if page.route =="/store":      page.views.append(        ft.View("/store",[            ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_VARIANT),            ft.ElevatedButton("Go Home", on_click=lambda_: page.go("/")),],))    page.update()defview_pop(view):    page.views.pop()    top_view = page.views[-1]    page.go(top_view.route)  page.on_route_change = route_change  page.on_view_pop = view_pop  page.go(page.route)ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

Try navigating between pages using "Visit Store" and "Go Home" buttons, Back/Forward browser buttons, manually changing route in the URL - it works no matter what! :)
note
To "navigate" between pages we used [`page.go(route)`](https://flet.dev/docs/controls/page#goroute) - a helper method that updates [`page.route`](https://flet.dev/docs/controls/page#route), calls [`page.on_route_change`](https://flet.dev/docs/controls/page#on_route_change) event handler to update views and finally calls `page.update()`.
Notice the usage of [`page.on_view_pop`](https://flet.dev/docs/controls/page#on_view_pop) event handler. It fires when the user clicks automatic "Back" button in [`AppBar`](https://flet.dev/docs/controls/appbar) control. In the handler we remove the last element from views collection and navigate to view's root "under" it.
## Route templates[​](https://flet.dev/blog/navigation-and-routing/#route-templates "Direct link to Route templates")
Flet offers [`TemplateRoute`](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet-core/src/flet_core/template_route.py) - an utility class based on [repath](https://github.com/nickcoutsos/python-repath) library which allows matching ExpressJS-like routes and parsing their parameters, for example `/account/:account_id/orders/:order_id`.
`TemplateRoute` plays great with route change event:
```
troute = TemplateRoute(page.route)if troute.match("/books/:id"):print("Book view ID:", troute.id)elif troute.match("/account/:account_id/orders/:order_id"):print("Account:", troute.account_id,"Order:", troute.order_id)else:print("Unknown route")
```

You can read more about template syntax supported by `repath` library [here](https://github.com/nickcoutsos/python-repath#parameters).
That's all for today!
[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-07-23-navigation-and-routing.md)
[Newer postFlet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)[Older postNew release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)
  * [Page route](https://flet.dev/blog/navigation-and-routing/#page-route)
  * [Page views](https://flet.dev/blog/navigation-and-routing/#page-views)
  * [Building views on route change](https://flet.dev/blog/navigation-and-routing/#building-views-on-route-change)
  * [Route templates](https://flet.dev/blog/navigation-and-routing/#route-templates)


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
