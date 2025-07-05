[Skip to main content](https://flet.dev/docs/cookbook/large-lists/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/large-lists/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/large-lists/)
    * [Theming](https://flet.dev/docs/cookbook/theming)
    * [Keyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)
    * [Large lists](https://flet.dev/docs/cookbook/large-lists)
    * [Drag and drop](https://flet.dev/docs/cookbook/drag-and-drop)
    * [File picker and uploads](https://flet.dev/docs/cookbook/file-picker-and-uploads)
    * [Animations](https://flet.dev/docs/cookbook/animations)
    * [Authentication](https://flet.dev/docs/cookbook/authentication)
    * [Assets](https://flet.dev/docs/cookbook/assets)
    * [Fonts](https://flet.dev/docs/cookbook/fonts)
    * [Read and write files](https://flet.dev/docs/cookbook/read-and-write-files)
    * [Client storage](https://flet.dev/docs/cookbook/client-storage)
    * [Session storage](https://flet.dev/docs/cookbook/session-storage)
    * [Encrypting sensitive data](https://flet.dev/docs/cookbook/encrypting-sensitive-data)
    * [PubSub](https://flet.dev/docs/cookbook/pub-sub)
    * [Control Refs](https://flet.dev/docs/cookbook/control-refs)
    * [Accessibility](https://flet.dev/docs/cookbook/accessibility)
    * [Logging](https://flet.dev/docs/cookbook/logging)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Cookbook
  * Large lists


On this page
# Large lists
You can use [`Column`](https://flet.dev/docs/controls/column) and [`Row`](https://flet.dev/docs/controls/row) controls to display lists in the most cases, but if the list contains hundreds or thousands of items `Column` and `Row` will be ineffective with lagging UI as they render all items at once even they are not visible at the current scrolling position.
In the following example we are adding 5,000 text controls to a page. Page uses `Column` as a default layout container:
```
import flet as ftdefmain(page: ft.Page):for i inrange(5000):    page.controls.append(ft.Text(f"Line {i}"))  page.scroll ="always"  page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Run the program and notice that it's not just it takes a couple of seconds to initially load and render all text lines on a page, but scrolling is slow and laggy too:
![](https://flet.dev/img/docs/getting-started/scroll-column.gif)
For displaying lists with a lot of items use [`ListView`](https://flet.dev/docs/controls/listview) and [`GridView`](https://flet.dev/docs/controls/gridview) controls which render items on demand, visible at the current scrolling position only.
## ListView[​](https://flet.dev/docs/cookbook/large-lists/#listview "Direct link to ListView")
[`ListView`](https://flet.dev/docs/controls/listview) could be either vertical (default) or horizontal. ListView items are displayed one after another in the scroll direction.
ListView already implements effective on demand rendering of its children, but scrolling performance could be further improved if you can set the same fixed height or width (for `horizontal` ListView) for all items ("extent"). This could be done by either setting absolute extent with `item_extent` property or making the extent of all children equal to the extent of the first child by setting `first_item_prototype` to `True`.
Let's output a list of 5,000 items using ListView control:
```
import flet as ftdefmain(page: ft.Page):  lv = ft.ListView(expand=True, spacing=10)for i inrange(5000):    lv.controls.append(ft.Text(f"Line {i}"))  page.add(lv)ft.app(main, view=ft.AppView.WEB_BROWSER)
```

Now the scrolling is smooth and fast enough to follow mouse movements:
![](https://flet.dev/img/docs/getting-started/scroll-listview.gif)
note
We used `expand=True` in ListView constructor. In order to function properly, ListView must have a height (or width if `horizontal`) specified. You could set an absolute size, e.g. `ListView(height=300, spacing=10)`, but in the example above we make ListView to take all available space on the page, i.e. expand. Read more about [`Control.expand`](https://flet.dev/docs/controls#expand) property.
## GridView[​](https://flet.dev/docs/cookbook/large-lists/#gridview "Direct link to GridView")
[`GridView`](https://flet.dev/docs/controls/gridview) allows arranging controls into a scrollable grid.
You can make a "grid" with `ft.Column(wrap=True)` or `ft.Row(wrap=True)`, for example:
```
import osimport flet as ftos.environ["FLET_WS_MAX_MESSAGE_SIZE"]="8000000"defmain(page: ft.Page):  r = ft.Row(wrap=True, scroll="always", expand=True)  page.add(r)for i inrange(5000):    r.controls.append(      ft.Container(        ft.Text(f"Item {i}"),        width=100,        height=100,        alignment=ft.alignment.center,        bgcolor=ft.Colors.AMBER_100,        border=ft.border.all(1, ft.Colors.AMBER_400),        border_radius=ft.border_radius.all(5),))  page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/row-wrap-as-grid.png)
Try scrolling and resizing the browser window - everything works, but very laggy.
note
At the start of the program we are setting the value of `FLET_WS_MAX_MESSAGE_SIZE` environment variable to `8000000` - this is the maximum size of WebSocket message in bytes that can be received by Flet Server rendering the page. Default size is 1 MB, but the size of JSON message describing 5,000 container controls would exceed 1 MB, so we are increasing allowed size to 8 MB.
Squeezing large messages through WebSocket channel is, generally, not a good idea, so use [batched updates](https://flet.dev/docs/cookbook/large-lists/#batch-updates) approach to control channel load.
GridView, similar to ListView, is very effective to render a lot of children. Let's implement the example above using GridView:
```
import osimport flet as ftos.environ["FLET_WS_MAX_MESSAGE_SIZE"]="8000000"defmain(page: ft.Page):  gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)  page.add(gv)for i inrange(5000):    gv.controls.append(      ft.Container(        ft.Text(f"Item {i}"),        alignment=ft.alignment.center,        bgcolor=ft.Colors.AMBER_100,        border=ft.border.all(1, ft.Colors.AMBER_400),        border_radius=ft.border_radius.all(5),))  page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/grid-view.png)
With GridView scrolling and window resizing are smooth and responsive!
You can specify either fixed number of rows or columns (runs) with `runs_count` property or the maximum size of a "tile" with `max_extent` property, so the number of runs can vary automatically. In our example we set the maximum tile size to 150 pixels and set its shape to "square" with `child_aspect_ratio=1`. `child_aspect_ratio` is the ratio of the cross-axis to the main-axis extent of each child. Try changing it to `0.5` or `2`.
## Batch updates[​](https://flet.dev/docs/cookbook/large-lists/#batch-updates "Direct link to Batch updates")
When `page.update()` is called a message is being sent to Flet server over WebSockets containing page updates since the last `page.update()`. Sending a large message with thousands of added controls could make a user waiting for a few seconds until the messages is fully received and controls rendered.
To increase usability of your program and present the results to a user as soon as possible you can send page updates in batches. For example, the following program adds 5,100 child controls to a ListView in batches of 500 items:
```
import flet as ftdefmain(page: ft.Page):# add ListView to a page first  lv = ft.ListView(expand=1, spacing=10, item_extent=50)  page.add(lv)for i inrange(5100):    lv.controls.append(ft.Text(f"Line {i}"))# send page to a pageif i %500==0:      page.update()# send the rest to a page  page.update()ft.app(main, view=ft.AppView.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/sending-page-updates-in-batches.png)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/large-lists.md)
[PreviousKeyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)[NextDrag and drop](https://flet.dev/docs/cookbook/drag-and-drop)
  * [ListView](https://flet.dev/docs/cookbook/large-lists/#listview)
  * [GridView](https://flet.dev/docs/cookbook/large-lists/#gridview)
  * [Batch updates](https://flet.dev/docs/cookbook/large-lists/#batch-updates)


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
