[Skip to main content](https://flet.dev/blog/fun-with-animations/#__docusaurus_skipToContent_fallback)
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


# Fun with animations
August 21, 2022 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Despite Flet release debuting animations support was released some time ago, we've just finished documenting its new features! We all know if the feature is not documented it just doesn't exist! 😉
Flutter offers [multiple approaches](https://docs.flutter.dev/development/ui/animations) for creating animations such "implicit", "explicit", "tween", "stagered", "pre-canned" animations as well as displaying animation scenes prepared in Rive and Lottie editors.
We are starting with "implicit" animations which allows you to animate a control property by setting a target value; whenever that target value changes, the control animates the property from the old value to the new one.
## Demo time[​](https://flet.dev/blog/fun-with-animations/#demo-time "Direct link to Demo time")
[Check out this live demo!](https://flet-animation.herokuapp.com/)
[![](https://flet.dev/img/blog/animations/flet-animation-demo.gif)](https://flet-animation.herokuapp.com/)
[Explore demo sources](https://github.com/flet-dev/flet-heroku-app). The demo is hosted on Heroku, by the way, so you can use it as a starting point for your own deployments.
## Implicit animations[​](https://flet.dev/blog/fun-with-animations/#implicit-animations "Direct link to Implicit animations")
Implicit animations can be enabled for the following control properties:
  * [Opacity](https://flet.dev/docs/cookbook/animations#opacity-animation)
  * [Rotation](https://flet.dev/docs/cookbook/animations#rotation-animation) (new in this release)
  * [Scale](https://flet.dev/docs/cookbook/animations#scale-animation) (new in this release)
  * [Offset](https://flet.dev/docs/cookbook/animations#offset-animation) (new in this release)
  * [Position](https://flet.dev/docs/cookbook/animations#position-animation)


Additionally, all `Container` control properties [can be now animated](https://flet.dev/docs/cookbook/animations#animated-container) and there is a new [`AnimatedSwitcher`](https://flet.dev/docs/controls/animatedswitcher) control for animated transition between old a new content.
![](https://flet.dev/img/docs/controls/animated-switcher/animated-switcher.gif)
## Other new features[​](https://flet.dev/blog/fun-with-animations/#other-new-features "Direct link to Other new features")
### `Markdown` control[​](https://flet.dev/blog/fun-with-animations/#markdown-control "Direct link to markdown-control")
Allows to render text in Markdown format. Supports various extensions: `CommonMark`, `GitHub Web` and `GitHub Flavored`.
[See `Markdown` control docs](https://flet.dev/docs/controls/markdown) for more information and examples.
### URL launcher[​](https://flet.dev/blog/fun-with-animations/#url-launcher "Direct link to URL launcher")
`page.launch_url(url)` method allows programmatically opening a URL in a new browser window, for example:
```
page.launch_url("https://google.com")
```

It also works nice with `Markdown` control for opening links within markdown document.
### Keyboard shortcuts[​](https://flet.dev/blog/fun-with-animations/#keyboard-shortcuts "Direct link to Keyboard shortcuts")
`Page` now contains [`on_keyboard_event`](https://flet.dev/docs/controls/page#on_keyboard_event) event handlet to globally intercept all keystrokes.
Check this [simple usage example](https://github.com/flet-dev/examples/blob/main/python/controls/page/keyboard-events.py).
### Accessibility improvements[​](https://flet.dev/blog/fun-with-animations/#accessibility-improvements "Direct link to Accessibility improvements")
We added [Accessibility](https://flet.dev/docs/cookbook/accessibility) section to the docs covering semantics support for screen readers.
### `ShaderMark` control[​](https://flet.dev/blog/fun-with-animations/#shadermark-control "Direct link to shadermark-control")
A control that applies a mask generated by a shader to its content. Allows making nice effects like [gradually fading out images](https://flet.dev/docs/controls/shadermask#gradually-fade-out-image-to-the-bottom-edge).
That's it!
[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-08-21-fun-with-animations.md)
[Newer postFile picker and uploads](https://flet.dev/blog/file-picker-and-uploads)[Older postBeautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)
  * [Demo time](https://flet.dev/blog/fun-with-animations/#demo-time)
  * [Implicit animations](https://flet.dev/blog/fun-with-animations/#implicit-animations)
  * [Other new features](https://flet.dev/blog/fun-with-animations/#other-new-features)
    * [`Markdown` control](https://flet.dev/blog/fun-with-animations/#markdown-control)
    * [URL launcher](https://flet.dev/blog/fun-with-animations/#url-launcher)
    * [Keyboard shortcuts](https://flet.dev/blog/fun-with-animations/#keyboard-shortcuts)
    * [Accessibility improvements](https://flet.dev/blog/fun-with-animations/#accessibility-improvements)
    * [`ShaderMark` control](https://flet.dev/blog/fun-with-animations/#shadermark-control)


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
