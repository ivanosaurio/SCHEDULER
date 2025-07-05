[Skip to main content](https://flet.dev/docs/getting-started/navigation-and-routing/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/getting-started/navigation-and-routing/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/navigation-and-routing/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Navigation and routing


On this page
# Navigation and routing
Navigation and routing is an essential feature of Single Page Applications (SPA) which allows organizing application user interface into virtual pages (views) and "navigate" between them while application URL reflects the current state of the app.
For mobile apps navigation and routing serves as a [deep linking](https://docs.flutter.dev/development/ui/navigation/deep-linking) to specific application parts.
Well, it took [more efforts](https://github.com/flet-dev/flet/pull/95/files) than expected to add navigation and routing into Flet as the implementation is based on [Navigator 2.0](https://medium.com/flutter/learning-flutters-new-navigation-and-routing-system-7c9068155ade) Flutter API and required to replace Flet's "Page" abstraction with "Page and Views". Flutter's newer navigation and routing API has substantial improvements such as:
  1. Programmatic control over history stack.
  2. An easy way to intercept a call to "Back" button in AppBar.
  3. Robust synchronization with browser history.

![](https://flet.dev/img/docs/navigation-routing/routing-app-example.gif)
Explore [source code](https://github.com/flet-dev/examples/blob/main/python/apps/routing-navigation/building-views-on-route-change.py) of the example above.
## Page route[​](https://flet.dev/docs/getting-started/navigation-and-routing/#page-route "Direct link to Page route")
Page route is a portion of application URL after `#` symbol:
![](https://flet.dev/img/docs/navigation-routing/page-address-route.png)
Default application route, if not set in application URL by the user, is `/`. All routes start with `/`, for example `/store`, `/authors/1/books/2`.
Application route can be obtained by reading `page.route` property, for example:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Grab application URL, open a new browser tab, paste the URL, modify its part after `#` to `/test` and hit enter. You should see "Initial route: /test".
Every time the route in the URL is changed (by editing the URL or navigating browser history with Back/Forward buttons) Flet calls `page.on_route_change` event handler:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))defroute_change(e: ft.RouteChangeEvent):    page.add(ft.Text(f"New route: {e.route}"))  page.on_route_change = route_change  page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Now try updating URL hash a few times and then use Back/Forward buttons! You should see a new message added to a page each time the route changes:
![](https://flet.dev/img/docs/navigation-routing/page-route-change-event.gif)
Route can be changed programmatically, by updating `page.route` property:
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text(f"Initial route: {page.route}"))defroute_change(e: ft.RouteChangeEvent):    page.add(ft.Text(f"New route: {e.route}"))defgo_store(e):    page.route ="/store"    page.update()  page.on_route_change = route_change  page.add(ft.ElevatedButton("Go to Store", on_click=go_store))ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Click "Go to Store" button and you'll see application URL is changed and a new item is pushed in a browser history. You can use browser "Back" button to navigate to a previous route.
## Page views[​](https://flet.dev/docs/getting-started/navigation-and-routing/#page-views "Direct link to Page views")
Flet's [Page](https://flet.dev/docs/controls/page) now is not just a single page, but a container for [View](https://flet.dev/docs/controls/view) layered on top of each other like a sandwich:
![](https://flet.dev/img/docs/navigation-routing/page-views.svg)
A collection of views represents navigator history. Page has [`page.views`](https://flet.dev/docs/controls/page#views) property to access views collection.
The last view in the list is the one currently displayed on a page. Views list must have at least one element (root view).
To simulate a transition between pages change `page.route` and add a new `View` in the end of `page.view` list.
Pop the last view from the collection and change route to a "previous" one in [`page.on_view_pop`](https://flet.dev/docs/controls/page#on_view_pop) event handler to go back.
## Building views on route change[​](https://flet.dev/docs/getting-started/navigation-and-routing/#building-views-on-route-change "Direct link to Building views on route change")
To build a reliable navigation there must be a single place in the program which builds a list of views depending on the current route. Other words, navigation history stack (represented by the list of views) must be a function of a route.
This place is [`page.on_route_change`](https://flet.dev/docs/controls/page#on_route_change) event handler.
Let's put everything together into a complete example which allows navigating between two pages:
```
import flet as ftdefmain(page: ft.Page):  page.title ="Routes Example"defroute_change(route):    page.views.clear()    page.views.append(      ft.View("/",[          ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),          ft.ElevatedButton("Visit Store", on_click=lambda_: page.go("/store")),],))if page.route =="/store":      page.views.append(        ft.View("/store",[            ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),            ft.ElevatedButton("Go Home", on_click=lambda_: page.go("/")),],))    page.update()defview_pop(view):    page.views.pop()    top_view = page.views[-1]    page.go(top_view.route)  page.on_route_change = route_change  page.on_view_pop = view_pop  page.go(page.route)ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Try navigating between pages using "Visit Store" and "Go Home" buttons, Back/Forward browser buttons, manually changing route in the URL - it works no matter what! :)
note
To "navigate" between pages we used [`page.go(route)`](https://flet.dev/docs/controls/page#goroute) - a helper method that updates [`page.route`](https://flet.dev/docs/controls/page#route), calls [`page.on_route_change`](https://flet.dev/docs/controls/page#on_route_change) event handler to update views and finally calls `page.update()`.
Notice the usage of [`page.on_view_pop`](https://flet.dev/docs/controls/page#on_view_pop) event handler. It fires when the user clicks automatic "Back" button in [`AppBar`](https://flet.dev/docs/controls/appbar) control. In the handler we remove the last element from views collection and navigate to view's root "under" it.
## Route templates[​](https://flet.dev/docs/getting-started/navigation-and-routing/#route-templates "Direct link to Route templates")
Flet offers [`TemplateRoute`](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet-core/src/flet_core/template_route.py) - an utility class based on [repath](https://github.com/nickcoutsos/python-repath) library which allows matching ExpressJS-like routes and parsing their parameters, for example `/account/:account_id/orders/:order_id`.
`TemplateRoute` plays great with route change event:
```
troute = TemplateRoute(page.route)if troute.match("/books/:id"):print("Book view ID:", troute.id)elif troute.match("/account/:account_id/orders/:order_id"):print("Account:", troute.account_id,"Order:", troute.order_id)else:print("Unknown route")
```

You can read more about template syntax supported by `repath` library [here](https://github.com/nickcoutsos/python-repath#parameters).
## URL strategy for web[​](https://flet.dev/docs/getting-started/navigation-and-routing/#url-strategy-for-web "Direct link to URL strategy for web")
Flet web apps support two ways of configuring URL-based routing:
  * **Path** (default) - paths are read and written without a hash. For example, `fletapp.dev/path/to/view`.
  * **Hash** - paths are read and written to the [hash fragment](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax). For example, `fletapp.dev/#/path/to/view`.


To change URL strategy use `route_url_strategy` parameter of `flet.app()` method, for example:
```
ft.app(main, route_url_strategy="hash")
```

URL strategy for Flet Server can be configured with `FLET_ROUTE_URL_STRATEGY` environment variable which could be set to either `path` (default) or `hash`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/navigation-and-routing.md)
[PreviousAdaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)[NextTesting on iOS](https://flet.dev/docs/getting-started/testing-on-ios)
  * [Page route](https://flet.dev/docs/getting-started/navigation-and-routing/#page-route)
  * [Page views](https://flet.dev/docs/getting-started/navigation-and-routing/#page-views)
  * [Building views on route change](https://flet.dev/docs/getting-started/navigation-and-routing/#building-views-on-route-change)
  * [Route templates](https://flet.dev/docs/getting-started/navigation-and-routing/#route-templates)
  * [URL strategy for web](https://flet.dev/docs/getting-started/navigation-and-routing/#url-strategy-for-web)


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
