[Skip to main content](https://flet.dev/docs/cookbook/animations/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/animations/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/animations/)
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
  * Animations


On this page
# Animations
## Implicit animations[​](https://flet.dev/docs/cookbook/animations/#implicit-animations "Direct link to Implicit animations")
With implicit animations, you can animate a control property by setting a target value; whenever that target value changes, the control animates the property from the old value to the new one. Animation produces interpolated values between the old and the new value over the given _duration_. By default, the animation is _linearly_ increasing the animation value, however, a _curve_ can be applied to the animation which changes the value according to the provided curve. For example, `easeOutCubic` curve increases the animation value quickly at the beginning of the animation and then slows down until the target value is reached:
Each `Control` provides a number of `animate_{something}` properties, described below, to enable implicit animation of its appearance:
  * `animate_opacity`
  * `animate_rotation`
  * `animate_scale`
  * `animate_offset`
  * `animate_position`
  * `animate` (Container)


`animate_*` properties could have one of the following values:
  * Instance of `animation.Animation` class - allows configuring the duration (in milliseconds) and the curve of the animation, for example `animate_rotation=ft.animation.Animation(duration=300, curve="bounceOut")`. See [Curves](https://api.flutter.dev/flutter/animation/Curves-class.html) in Flutter docs for possible values. Default is `linear`.
  * `int` value - enables animation with specified duration in milliseconds and `linear` curve.
  * `bool` value - enables animation with the duration of 1000 milliseconds and `linear` curve.


### Opacity animation[​](https://flet.dev/docs/cookbook/animations/#opacity-animation "Direct link to Opacity animation")
Setting control's `animate_opacity` to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of [`Control.opacity`](https://flet.dev/docs/controls#opacity) property.
![](https://flet.dev/img/docs/getting-started/animations/animate-opacity.gif)
```
import flet as ftdefmain(page: ft.Page):  c = ft.Container(    width=150,    height=150,    bgcolor="blue",    border_radius=10,    animate_opacity=300,)defanimate_opacity(e):    c.opacity =0if c.opacity ==1else1    c.update()  page.add(    c,    ft.ElevatedButton("Animate opacity",      on_click=animate_opacity,),)ft.app(main)
```

### Rotation animation[​](https://flet.dev/docs/cookbook/animations/#rotation-animation "Direct link to Rotation animation")
Setting control's `animate_rotation` to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of [`Control.rotate`](https://flet.dev/docs/controls#rotate) property.
![](https://flet.dev/img/docs/getting-started/animations/animate-rotation.gif)
```
from math import piimport flet as ftdefmain(page: ft.Page):  c = ft.Container(    width=100,    height=70,    bgcolor="blue",    border_radius=5,    rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),    animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),)defanimate(e):    c.rotate.angle += pi /2    page.update()  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.spacing =30  page.add(    c,    ft.ElevatedButton("Animate!", on_click=animate),)ft.app(main)
```

### Scale animation[​](https://flet.dev/docs/cookbook/animations/#scale-animation "Direct link to Scale animation")
Setting control's `animate_scale` to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of [`Control.scale`](https://flet.dev/docs/controls#scale) property.
![](https://flet.dev/img/docs/getting-started/animations/animate-scale.gif)
```
import flet as ftdefmain(page: ft.Page):  c = ft.Container(    width=100,    height=100,    bgcolor="blue",    border_radius=5,    scale=ft.transform.Scale(scale=1),    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),)defanimate(e):    c.scale =2    page.update()  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.spacing =30  page.add(    c,    ft.ElevatedButton("Animate!", on_click=animate),)ft.app(main)
```

### Offset animation[​](https://flet.dev/docs/cookbook/animations/#offset-animation "Direct link to Offset animation")
Setting control's `animate_offset` to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of `Control.offset` property.
`offset` property is an instance of `transform.Offset` class which specifies horizontal `x` and vertical `y` offset of a control scaled to control's size. For example, an offset `transform.Offset(-0.25, 0)` will result in a horizontal translation of one quarter the width of the control.
Offset animation is used for various sliding effects:
![](https://flet.dev/img/docs/getting-started/animations/animate-offset.gif)
```
import flet as ftdefmain(page: ft.Page):  c = ft.Container(    width=150,    height=150,    bgcolor="blue",    border_radius=10,    offset=ft.transform.Offset(-2,0),    animate_offset=ft.animation.Animation(1000),)defanimate(e):    c.offset = ft.transform.Offset(0,0)    c.update()  page.add(    c,    ft.ElevatedButton("Reveal!", on_click=animate),)ft.app(main)
```

### Position animation[​](https://flet.dev/docs/cookbook/animations/#position-animation "Direct link to Position animation")
Setting control's `animate_position` to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of [Control's `left`, `top`, `right` and `bottom` properties](https://flet.dev/docs/controls#left).
Please note Control position works inside `Stack` control only.
![](https://flet.dev/img/docs/getting-started/animations/animate-position.gif)
```
import flet as ftdefmain(page: ft.Page):  c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=1000)  c2 = ft.Container(    width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500)  c3 = ft.Container(    width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000)defanimate_container(e):    c1.top =20    c1.left =200    c2.top =100    c2.left =40    c3.top =180    c3.left =100    page.update()  page.add(    ft.Stack([c1, c2, c3], height=250),    ft.ElevatedButton("Animate!", on_click=animate_container),)ft.app(main)
```

### Animated container[​](https://flet.dev/docs/cookbook/animations/#animated-container "Direct link to Animated container")
Setting [`Container.animate`](https://flet.dev/docs/controls/container#animate) to either `True`, number or an instance of `animation.Animation` class (see above) enables implicit animation of container properties such as size, background color, border style, gradient.
![](https://flet.dev/img/docs/getting-started/animations/animate-container.gif)
```
import flet as ftdefmain(page: ft.Page):  c = ft.Container(    width=150,    height=150,    bgcolor="red",    animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),)defanimate_container(e):    c.width =100if c.width ==150else150    c.height =50if c.height ==150else150    c.bgcolor ="blue"if c.bgcolor =="red"else"red"    c.update()  page.add(c, ft.ElevatedButton("Animate container", on_click=animate_container))ft.app(main)
```

### Animated content switcher[​](https://flet.dev/docs/cookbook/animations/#animated-content-switcher "Direct link to Animated content switcher")
[`AnimatedSwitcher`](https://flet.dev/docs/controls/animatedswitcher) allows animated transition between a new control and the control previously set on the AnimatedSwitcher as a `content`.
![](https://flet.dev/img/docs/getting-started/animations/animated-switcher-images.gif)
```
import timeimport flet as ftdefmain(page: ft.Page):  i = ft.Image(src="https://picsum.photos/150/150", width=150, height=150)defanimate(e):    sw.content = ft.Image(      src=f"https://picsum.photos/150/150?{time.time()}", width=150, height=150)    page.update()  sw = ft.AnimatedSwitcher(    i,    transition=ft.AnimatedSwitcherTransition.SCALE,    duration=500,    reverse_duration=500,    switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,    switch_out_curve=ft.AnimationCurve.BOUNCE_IN,)  page.add(    sw,    ft.ElevatedButton("Animate!", on_click=animate),)ft.app(main)
```

### Animation end callback[​](https://flet.dev/docs/cookbook/animations/#animation-end-callback "Direct link to Animation end callback")
All controls with `animate_*` properties have `on_animation_end` event handler which is called when animation complete and can be used to chain multiple animations.
Event's object `data` field contains the name of animation:
  * `opacity`
  * `rotation`
  * `scale`
  * `offset`
  * `position`
  * `container`


For example:
```
 c = ft.Container(    ft.Text("Animate me!"),# ...    animate=ft.animation.Animation(1000,"bounceOut"),    on_animation_end=lambda e:print("Container animation end:", e.data))
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/animations.md)
[PreviousFile picker and uploads](https://flet.dev/docs/cookbook/file-picker-and-uploads)[NextAuthentication](https://flet.dev/docs/cookbook/authentication)
  * [Implicit animations](https://flet.dev/docs/cookbook/animations/#implicit-animations)
    * [Opacity animation](https://flet.dev/docs/cookbook/animations/#opacity-animation)
    * [Rotation animation](https://flet.dev/docs/cookbook/animations/#rotation-animation)
    * [Scale animation](https://flet.dev/docs/cookbook/animations/#scale-animation)
    * [Offset animation](https://flet.dev/docs/cookbook/animations/#offset-animation)
    * [Position animation](https://flet.dev/docs/cookbook/animations/#position-animation)
    * [Animated container](https://flet.dev/docs/cookbook/animations/#animated-container)
    * [Animated content switcher](https://flet.dev/docs/cookbook/animations/#animated-content-switcher)
    * [Animation end callback](https://flet.dev/docs/cookbook/animations/#animation-end-callback)


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
