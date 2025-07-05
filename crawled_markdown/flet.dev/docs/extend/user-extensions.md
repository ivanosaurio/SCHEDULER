[Skip to main content](https://flet.dev/docs/extend/user-extensions/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/extend/built-in-extensions)
    * [Built-in extensions](https://flet.dev/docs/extend/built-in-extensions)
    * [User extensions](https://flet.dev/docs/extend/user-extensions)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Extending Flet
  * User extensions


On this page
# Creating Flet extension for existing Flutter package
## Introduction[​](https://flet.dev/docs/extend/user-extensions/#introduction "Direct link to Introduction")
While Flet controls leverage many built-in Flutter widgets, enabling the creation of complex applications, not all Flutter widgets or third-party packages can be directly supported by the Flet team or included within the core Flet framework.
To address this, the Flet framework provides an extensibility mechanism. This allows you to incorporate widgets and APIs from your own custom Flutter packages or [third-party libraries](https://pub.dev/packages?sort=popularity) directly into your Flet application.
In this guide, you will learn how to create Flet extension from template and then customize it to integrate 3rd-party Flutter package into your Flet app or share it with community.
### Prerequisites[​](https://flet.dev/docs/extend/user-extensions/#prerequisites "Direct link to Prerequisites")
To integrate custom Flutter package into Flet you need to have basic understanding of how to create Flutter apps and packages in Dart language and have Flutter development environment configured. See [Flutter Getting Started](https://docs.flutter.dev/get-started/install) for more information about Flutter and Dart.
## Create Flet extension from template[​](https://flet.dev/docs/extend/user-extensions/#create-flet-extension-from-template "Direct link to Create Flet extension from template")
Flet now makes it easy to create and build projects with your custom controls based on Flutter widgets or Flutter 3rd-party packages. In the example below, we will be creating a custom Flet extension based on the [flutter_spinkit](https://pub.dev/packages/flutter_spinkit) package.
  1. Create new virtual enviroment and [install Flet](https://flet.dev/docs/getting-started/#virtual-environment) there.
  2. Create new Flet extension project from template:


```
flet create --template extension --project-name flet-spinkit
```

A project with new FletSpinkit control will be created. The control is just a Flutter Text widget with text property, which we will customize later.
  1. Build your app.


Flet project created from extension template has `examples/flet_spinkit_example` folder with the example app.
When in the folder where your `pyproject.toml` for the app is (`examples/flet_spinkit_example`), run `flet build` command, for example, for macos:
```
flet build macos -v
```

Open the app and see the new custom Flet Control:
```
open build/macos/flet-spinkit-example.app
```

![](https://flet.dev/img/docs/extending-flet/example.png)
  1. Change your app.


Once the project was built for desktop once, you can make changes to your python files and run it without re-building.
First, if you are not using uv, install dependencies from pyproject.toml:
```
pip install .
```

or
```
poetry install
```

Now you can make changes to your example app main.py:
```
import flet as ftfrom flet_spinkit import FletSpinkitdef main(page: ft.Page):  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.add(    ft.Container(      height=150,      width=300,      alignment=ft.alignment.center,      bgcolor=ft.Colors.PINK_200,      content=FletSpinkit(        tooltip="My new PINK FletSpinkit Control tooltip",        value="My new PINK FletSpinkit Flet Control",      ),    ),  )ft.app(main)
```

and run:
```
flet run
```

![](https://flet.dev/img/docs/extending-flet/example-pink.png)
  1. Re-build your app.


When you make any changes to your flutter package, you need to re-build:
```
flet build macos -v
```

If you need to debug, run this command:
```
build/macos/flet-spinkit-example.app/Contents/MacOS/flet-spinkit-example --debug
```

## Integrate 3rd-party Flutter package[​](https://flet.dev/docs/extend/user-extensions/#integrate-3rd-party-flutter-package "Direct link to Integrate 3rd-party Flutter package")
Let's integrate [flutter_spinkit](https://pub.dev/packages/flutter_spinkit) package into our Flet app.
  1. Add dependency.


Go to `src/flutter/flet_spinkit` folder and run this command to add dependency to `flutter_spinkit` to `pubspec.yaml`:
```
flutter pub add flutter_spinkit
```

Read more information about using Flutter packages [here](https://docs.flutter.dev/packages-and-plugins/using-packages).
  1. Modify `dart` file.


In the `src/flutter/flet_spinkit/lib/src/flet_spinkit.dart` file, add import statement and replace Text widget with `SpinKitRotatingCircle` widget:
```
import 'package:flet/flet.dart';import 'package:flutter/material.dart';import 'package:flutter_spinkit/flutter_spinkit.dart';class FletSpinkitControl extends StatelessWidget { final Control? parent; final Control control; const FletSpinkitControl({  super.key,  required this.parent,  required this.control, }); @override Widget build(BuildContext context) {  Widget myControl = SpinKitRotatingCircle(   color: Colors.red,   size: 100.0,  );  return constrainedControl(context, myControl, parent, control); }}
```

  1. Rebuild your example app.


Go to `examples/flet_spinkit_example`, clear cache and rebuild your app:
```
flet build macos -v
```

  1. Run your app:

![](https://flet.dev/img/docs/extending-flet/spinkit1.gif)
## Flet extension structure[​](https://flet.dev/docs/extend/user-extensions/#flet-extension-structure "Direct link to Flet extension structure")
After creating new Flet project from extension template, you will see the following folder structure:
```
├── LICENSE├── mkdocs.yml├── README.md├── docs│  └── index.md│  └── FletSpinkit.md├── examples│  └── flet_spinkit_example│    ├── README.md│    ├── pyproject.toml│    └── src│      └── main.py├── pyproject.toml└── src  ├── flet_spinkit  │  ├── __init__.py  │  └── flet_spinkit.py  └── flutter    └── flet_spinkit      ├── CHANGELOG.md      ├── LICENSE      ├── README.md      ├── lib      │  ├── flet_spinkit.dart      │  └── src      │    ├── create_control.dart      │    └── flet_spinkit.dart      └── pubspec.yaml
```

Flet extension consists of:
  * **package** , located in `src` folder
  * **example app** , located in `examples/flet-spinkit_example` folder
  * **docs** , located in `docs` folder


### Package[​](https://flet.dev/docs/extend/user-extensions/#package "Direct link to Package")
Package is the component that will be used in your app. It contists of two parts: Python and Flutter.
#### Python[​](https://flet.dev/docs/extend/user-extensions/#python "Direct link to Python")
##### flet_spinkit.py[​](https://flet.dev/docs/extend/user-extensions/#flet_spinkitpy "Direct link to flet_spinkit.py")
Here you create Flet Python control - a Python class that you use in your Flet app.
The minumal requirements for this class is that it has to be inherited from Flet `Control` and it has to have `_get_control_name` method that will return the control name. This name should be the same as `args.control.type` we check in the `create_control.dart` file.
#### Flutter[​](https://flet.dev/docs/extend/user-extensions/#flutter "Direct link to Flutter")
##### pubspec.yaml[​](https://flet.dev/docs/extend/user-extensions/#pubspecyaml "Direct link to pubspec.yaml")
A yaml file containing metadata that specifies the package's dependencies.
There is already a dependency to `flet` created from template. You need to add there a dependency to Flutter package for which you are creating your extension.
##### flet_spinkit.dart[​](https://flet.dev/docs/extend/user-extensions/#flet_spinkitdart "Direct link to flet_spinkit.dart")
Two methods are exported:
  * `createControl` - called to create a widget that corresponds to a control on Python side.
  * `ensureInitialized` - called once on Flet program start.


##### src/create_control.dart[​](https://flet.dev/docs/extend/user-extensions/#srccreate_controldart "Direct link to src/create_control.dart")
Creates Flutter widget based on control names returned by the Control's `_get_control_name()` function. This mechanism iterates through all third-party packages and returns the first matching widget.
##### src/flet_spinkit.dart[​](https://flet.dev/docs/extend/user-extensions/#srcflet_spinkitdart "Direct link to src/flet_spinkit.dart")
Here you create Flutter "wrapper" widget that will build Flutter widget or API that you want to use in your Flet app.
Wrapper widget passes the state of Python control down to a Flutter widget, that will be displayed on a page, and provides an API to route events from Flutter widget back to Python control.
### Example app[​](https://flet.dev/docs/extend/user-extensions/#example-app "Direct link to Example app")
##### src/main.py[​](https://flet.dev/docs/extend/user-extensions/#srcmainpy "Direct link to src/main.py")
Python program that uses Flet Python control.
##### pyproject.toml[​](https://flet.dev/docs/extend/user-extensions/#pyprojecttoml "Direct link to pyproject.toml")
Here you specify dependency to your package, which can be:
  * **Path dependency**


Absolute path to your Flet extension folder, for example:
```
dependencies = [ "flet-spinkit @ file:///Users/user-name/projects/flet-spinkit", "flet>=0.26.0",]
```

  * **Git dependency**


Link to git repository, for example:
```
dependencies = [ "flet-ads @ git+https://github.com/flet-dev/flet-ads.git", "flet>=0.26.0",]
```

  * **PyPi dependency**


Name of the package published on pypi.org, for example:
```
dependencies = [ "flet-ads", "flet>=0.26.0",]
```

### Docs[​](https://flet.dev/docs/extend/user-extensions/#docs "Direct link to Docs")
If you are planning to share your extension with community, you can easily generate documenation from your source code using [mkdocs](https://www.mkdocs.org/).
Flet extension comes with `docs` folder containing initial files for your documentation and `mkdocs.yml`.
Run the following command to see how your docs look locally:
```
mkdocs serve
```

Open <http://127.0.0.1:8000> in your browser:
![](https://flet.dev/img/docs/extending-flet/mkdocs.png)
Once your documentation is ready, if your package is hosted on GitHub, your can run the following command to host your documentation on GitHub pages:
```
mkdocs gh-deploy
```

You may find [this guide](https://realpython.com/python-project-documentation-with-mkdocs/#step-5-build-your-documentation-with-mkdocs) helpful to get started with mkdocs.
## Customize properties[​](https://flet.dev/docs/extend/user-extensions/#customize-properties "Direct link to Customize properties")
In the example above, Spinkit control creates a hardcoded Flutter widget. Now let's customize its properties.
### Common properties[​](https://flet.dev/docs/extend/user-extensions/#common-properties "Direct link to Common properties")
Generally, there are two types of controls in Flet:
  1. Visual controls that are added to the app/page surface, such as FletSpinkit.
  2. Non-visual controls that can be:
     * popup controls (dialogs, pickers, panels etc.).
     * services that are added to `overlay`, such as Video or Audio.


Flet `Control` class has properties common for all controls such as `visible`, `opacity` and `tooltip`, to name a few.
Flet `ConstrainedControl` class is inherited from `Control` and has many additional properties such as `top` and `left` for its position within Stack and a bunch of animation properties.
When creating non-visual control, your Python control should be inherited from ['Control](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/control.py). Then, to be able to use `Control` properties in your app, you need to add them to the constructor of your Python Control. In its dart counterpart (`src/flet_spinkit.dart`) use `baseControl()` to wrap your Flutter widget.
When creating visual control, your Python control should be inherited from [`ConstrainedControl`](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/constrained_control.py). In its dart counterpart (`src/flet_spinkit.dart`) use `constrainedControl()` to wrap your Flutter widget.
Then, to be able to use `Control` and `ConstrainedControl` properties in your app, you need to add them to the constructor of your Python Control.
See reference for the common Control properties [here](https://flet.dev/docs/controls).
If you have created your extension project from Flet extension template, your Python Control is already inherited from `ConstrainedControl` and you can use its properties in your example app:
```
import flet as ftfrom flet_spinkit import FletSpinkitdefmain(page: ft.Page):  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.add(    ft.Stack([        ft.Container(height=200, width=200, bgcolor=ft.Colors.BLUE_100),        FletSpinkit(opacity=0.5, tooltip="Spinkit tooltip", top=0, left=0),]))ft.app(main)
```

![](https://flet.dev/img/docs/extending-flet/spinkit2.gif)
### Control-specific properties[​](https://flet.dev/docs/extend/user-extensions/#control-specific-properties "Direct link to Control-specific properties")
Now that you have taken full advantage of the properties Flet `Control` and `ConstrainedControl` offer, let's define the properties that are specific to the new Control you are building.
In the FletSpinkit example, let's define its `color` and `size`.
In Python class, define new `color` and `size` properties:
```
from enum import Enumfrom typing import Any, Optionalfrom flet.core.constrained_control import ConstrainedControlfrom flet.core.control import OptionalNumberfrom flet.core.types import ColorEnums, ColorValueclassFletSpinkit(ConstrainedControl):"""  FletSpinkit Control.  """def__init__(    self,## Control#    opacity: OptionalNumber =None,    tooltip: Optional[str]=None,    visible: Optional[bool]=None,    data: Any =None,## ConstrainedControl#    left: OptionalNumber =None,    top: OptionalNumber =None,    right: OptionalNumber =None,    bottom: OptionalNumber =None,## FletSpinkit specific#    color: Optional[ColorValue]=None,    size: OptionalNumber =None,):    ConstrainedControl.__init__(      self,      tooltip=tooltip,      opacity=opacity,      visible=visible,      data=data,      left=left,      top=top,      right=right,      bottom=bottom,)    self.color = color    self.size = sizedef_get_control_name(self):return"flet_spinkit"# color@propertydefcolor(self)-> Optional[ColorValue]:return self.__color@color.setterdefcolor(self, value: Optional[ColorValue]):    self.__color = value    self._set_enum_attr("color", value, ColorEnums)# size@propertydefsize(self):return self._get_attr("size")@size.setterdefsize(self, value):    self._set_attr("size", value)
```

In `src/flet_spinkit.dart` file, use helper methods `attrColor` and `attrDouble` to access color and size values:
```
import 'package:flet/flet.dart';import 'package:flutter/material.dart';import 'package:flutter_spinkit/flutter_spinkit.dart';class FletSpinkitControl extends StatelessWidget { final Control? parent; final Control control; const FletSpinkitControl({  super.key,  required this.parent,  required this.control, }); @override Widget build(BuildContext context) {  var color = control.attrColor("color", context);  var size = control.attrDouble("size");  Widget myControl = SpinKitRotatingCircle(   color: color,   size: size ?? 100,  );  return constrainedControl(context, myControl, parent, control); }}
```

Use `color` and `size` properties in your app:
```
import flet as ftfrom flet_spinkit import FletSpinkitdefmain(page: ft.Page):  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.add(    ft.Stack([        ft.Container(height=200, width=200, bgcolor=ft.Colors.BLUE_100),        FletSpinkit(          opacity=0.5,          tooltip="Spinkit tooltip",          top=0,          left=0,          color=ft.Colors.YELLOW,          size=150,),]))ft.app(main)
```

Re-build and run:
![](https://flet.dev/img/docs/extending-flet/spinkit3.gif)
You can find source code for this example [here](https://github.com/flet-dev/flet-spinkit).
#### Examples for different types of properties and events[​](https://flet.dev/docs/extend/user-extensions/#examples-for-different-types-of-properties-and-events "Direct link to Examples for different types of properties and events")
##### Enum properties[​](https://flet.dev/docs/extend/user-extensions/#enum-properties "Direct link to Enum properties")
For example, `clip_behaviour` for `AppBar`.
In [Python](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/app_bar.py):
```
# clip_behavior@propertydefclip_behavior(self)-> Optional[ClipBehavior]:return self._get_attr("clipBehavior")@clip_behavior.setterdefclip_behavior(self, value: Optional[ClipBehavior]):  self._set_attr("clipBehavior",    value.value ifisinstance(value, ClipBehavior)else value,)
```

In [Dart](https://github.com/flet-dev/flet/blob/main/packages/flet/lib/src/controls/app_bar.dart):
```
var clipBehavior = Clip.values.firstWhere(  (e) =>    e.name.toLowerCase() ==    widget.control.attrString("clipBehavior", "")!.toLowerCase(),  orElse: () => Clip.none);
```

##### Json properties[​](https://flet.dev/docs/extend/user-extensions/#json-properties "Direct link to Json properties")
For example, `shape` property for `Card`.
In [Python](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/card.py):
```
defbefore_update(self):super().before_update()  self._set_attr_json("shape", self.__shape)# shape@propertydefshape(self)-> Optional[OutlinedBorder]:return self.__shape@shape.setterdefshape(self, value: Optional[OutlinedBorder]):  self.__shape = value
```

In [Dart](https://github.com/flet-dev/flet/blob/main/packages/flet/lib/src/controls/card.dart):
```
var shape = parseOutlinedBorder(control, "shape")
```

##### Children[​](https://flet.dev/docs/extend/user-extensions/#children "Direct link to Children")
For example, `content` for `AlertDialog`:
In [Python](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/alert_dialog.py):
```
def_get_children(self):    children =[]if self.__content:      self.__content._set_attr_internal("n","content")      children.append(self.__content)return children
```

In [Dart](https://github.com/flet-dev/flet/blob/main/packages/flet/lib/src/controls/alert_dialog.dart):
```
  var contentCtrls =    widget.children.where((c) => c.name == "content" && c.isVisible);
```

##### Events[​](https://flet.dev/docs/extend/user-extensions/#events "Direct link to Events")
For example, `on_click` event for `ElevatedButton`.
In [Python](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet/src/flet/core/elevated_button.py):
```
# on_click@propertydefon_click(self):return self._get_event_handler("click")@on_click.setterdefon_click(self, handler):  self._add_event_handler("click", handler)
```

In [Dart](https://github.com/flet-dev/flet/blob/main/packages/flet/lib/src/controls/elevated_button.dart):
```
Function()? onPressed = !disabled  ? () {    debugPrint("Button ${widget.control.id} clicked!");    if (url != "") {    openWebBrowser(url,      webWindowName: widget.control.attrString("urlTarget"));    }    widget.backend.triggerControlEvent(widget.control.id, "click");  }  : null;
```

## Examples[​](https://flet.dev/docs/extend/user-extensions/#examples "Direct link to Examples")
Flet has controls that are implemented as [built-in extensions](https://flet.dev/docs/extend/built-in-extensions) and could serve as a starting point for your own controls.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/extend/user-extensions.md)
[PreviousBuilt-in extensions](https://flet.dev/docs/extend/built-in-extensions)[NextControls reference](https://flet.dev/docs/controls)
  * [Introduction](https://flet.dev/docs/extend/user-extensions/#introduction)
    * [Prerequisites](https://flet.dev/docs/extend/user-extensions/#prerequisites)
  * [Create Flet extension from template](https://flet.dev/docs/extend/user-extensions/#create-flet-extension-from-template)
  * [Integrate 3rd-party Flutter package](https://flet.dev/docs/extend/user-extensions/#integrate-3rd-party-flutter-package)
  * [Flet extension structure](https://flet.dev/docs/extend/user-extensions/#flet-extension-structure)
    * [Package](https://flet.dev/docs/extend/user-extensions/#package)
    * [Example app](https://flet.dev/docs/extend/user-extensions/#example-app)
    * [Docs](https://flet.dev/docs/extend/user-extensions/#docs)
  * [Customize properties](https://flet.dev/docs/extend/user-extensions/#customize-properties)
    * [Common properties](https://flet.dev/docs/extend/user-extensions/#common-properties)
    * [Control-specific properties](https://flet.dev/docs/extend/user-extensions/#control-specific-properties)
  * [Examples](https://flet.dev/docs/extend/user-extensions/#examples)


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
