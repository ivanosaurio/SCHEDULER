[Skip to main content](https://flet.dev/blog/canvas/#__docusaurus_skipToContent_fallback)
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


# Canvas
April 26, 2023 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Unleash your inner artist 🧑‍🎨 and boost your Flet creativity with brand-new [Canvas](https://flet.dev/docs/controls/canvas) control just released in [Flet 0.6.0](https://pypi.org/project/flet/)!
Canvas enables you to draw arbitrary graphics using a set of primitives, or "shapes", such as line, circle, arc, path and text. I bet you can even implement your own version of [charts](https://flet.dev/blog/flet-charts) using Canvas control!
Combine Canvas with [GestureDetector](https://flet.dev/docs/controls/gesturedetector) and you get a free-hand drawing app - Flet Brush 😀!
![](https://flet.dev/img/docs/controls/canvas/canvas-flet-brush.gif)
[Example source](https://github.com/flet-dev/examples/blob/main/python/controls/canvas/canvas-flet-brush.py)
`Canvas` control is located in `flet.canvas` package. You need another import to use it:
```
import flet.canvas as cv
```

Here's a simple program drawing a smiley face with [`Circle`](https://flet.dev/docs/controls/canvas#circle-shape-properties) and [`Arc`](https://flet.dev/docs/controls/canvas#arc-shape-properties) shapes using filled and stroke [`Paint`](https://flet.dev/docs/reference/types/paint):
```
import mathimport flet as ftimport flet.canvas as cvdefmain(page: ft.Page):  stroke_paint = paint = ft.Paint(stroke_width=2, style=ft.PaintingStyle.STROKE)  fill_paint = paint = ft.Paint(style=ft.PaintingStyle.FILL)  cp = cv.Canvas([      cv.Circle(100,100,50, stroke_paint),      cv.Circle(80,90,10, stroke_paint),      cv.Circle(84,87,5, fill_paint),      cv.Circle(120,90,10, stroke_paint),      cv.Circle(124,87,5, fill_paint),      cv.Arc(70,95,60,40,0, math.pi, paint=stroke_paint),],    width=float("inf"),    expand=True,)  page.add(cp)ft.app(main)
```

![](https://flet.dev/img/docs/controls/canvas/canvas-face.png)
Read more about Canvas in [docs](https://flet.dev/docs/controls/canvas) and explore [Canvas examples](https://github.com/flet-dev/examples/tree/main/python/controls/canvas)!
## Other changes[​](https://flet.dev/blog/canvas/#other-changes "Direct link to Other changes")
### Rich text support[​](https://flet.dev/blog/canvas/#rich-text-support "Direct link to Rich text support")
While working on [drawing text on Canvas](https://flet.dev/docs/controls/canvas#drawing-text), as a bonus to this release, we implemented a new [`TextSpan`](https://flet.dev/docs/reference/types/textspan) control which can now be used with [`Text.spans`](https://flet.dev/docs/controls/text#spans) to output rich text.
![](https://flet.dev/img/docs/controls/text/richtext-borders-stroke.png)
Check rich text examples: [one](https://flet.dev/docs/controls/text#rich-text-basics), [two](https://flet.dev/docs/controls/text#rich-text-with-borders-and-stroke) and [three](https://flet.dev/docs/controls/text#rich-text-with-gradient).
### `url` property for buttons[​](https://flet.dev/blog/canvas/#url-property-for-buttons "Direct link to url-property-for-buttons")
If you need to open a URL by clicking on a button or any other control with `on_click` event you can just provide that URL in `url` instead of doing that in the code with [`page.launch_url()`](https://flet.dev/docs/controls/page#launch_urlurl) method.
Instead of that:
```
ft.ElevatedButton("Go to Google", on_click=lambda e: e.page.launch_url("https://google.com"))
```

you can just do this:
```
ft.ElevatedButton("Go to Google", url="https://google.com")
```

A new `url` property also solves [blocked window on Safari](https://github.com/flet-dev/flet/issues/1105) issue.
### Auto-follow links in `Markdown`[​](https://flet.dev/blog/canvas/#auto-follow-links-in-markdown "Direct link to auto-follow-links-in-markdown")
As a continuation of `url` property `Markdown` control can now be enabled to auto-follow URLs in the document:
```
import flet as ftmd ="""[Go to Google](https://www.google.com)"""defmain(page: ft.Page):  page.add(    ft.Markdown(      md,      extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,      auto_follow_links=True,))ft.app(main)
```

### Better web support[​](https://flet.dev/blog/canvas/#better-web-support "Direct link to Better web support")
In this release we also did some improvements to web support like [capturing user info in `page.client_id` and `page.client_user_agent`](https://github.com/flet-dev/flet/pull/1302) as well as fixing nasty [#1333](https://github.com/flet-dev/flet/pull/1333) and [#1289](https://github.com/flet-dev/flet/pull/1289) bugs related to routing.
That's all for today!
Upgrade Flet module to the latest version (`pip install flet --upgrade`), give canvas and rich text a try and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-04-26-canvas.md)
[Newer postScrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)[Older postFlet Charts](https://flet.dev/blog/flet-charts)
  * [Other changes](https://flet.dev/blog/canvas/#other-changes)
    * [Rich text support](https://flet.dev/blog/canvas/#rich-text-support)
    * [`url` property for buttons](https://flet.dev/blog/canvas/#url-property-for-buttons)
    * [Auto-follow links in `Markdown`](https://flet.dev/blog/canvas/#auto-follow-links-in-markdown)
    * [Better web support](https://flet.dev/blog/canvas/#better-web-support)


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
