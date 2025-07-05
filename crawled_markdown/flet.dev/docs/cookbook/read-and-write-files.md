[Skip to main content](https://flet.dev/docs/cookbook/read-and-write-files/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/read-and-write-files/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/read-and-write-files/)
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
  * Read and write files


On this page
# Read and write files
In some cases, you need to read and write files to disk. For example, you might need to persist data across app launches, or download data from the internet and save it for later offline use.
Flet makes it easy to work with files and directories on the mobile/desktop device, as seen in the following example.
### Storage Paths[​](https://flet.dev/docs/cookbook/read-and-write-files/#storage-paths "Direct link to Storage Paths")
Flet provides two directory paths for data storage, available as environment variables: [`FLET_APP_STORAGE_DATA`](https://flet.dev/docs/reference/environment-variables/#flet_app_storage_data) and [`FLET_APP_STORAGE_TEMP`](https://flet.dev/docs/reference/environment-variables/#flet_app_storage_temp).
Their values can be gotten as follows:
```
import osapp_data_path = os.getenv("FLET_APP_STORAGE_DATA")app_temp_path = os.getenv("FLET_APP_STORAGE_TEMP")
```

### Writing to a File[​](https://flet.dev/docs/cookbook/read-and-write-files/#writing-to-a-file "Direct link to Writing to a File")
To write data to a new/existing file, you can use the built-in [`open`](https://docs.python.org/3/library/functions.html#open) function.
For example:
```
import osapp_data_path = os.getenv("FLET_APP_STORAGE_DATA")my_file_path = os.path.join(app_data_path,"test_file.txt")withopen(my_file_path,"w")as f:  f.write("Some file content...")
```

### Reading from a File[​](https://flet.dev/docs/cookbook/read-and-write-files/#reading-from-a-file "Direct link to Reading from a File")
To read data from an existing file, you can equally use the built-in [`open`](https://docs.python.org/3/library/functions.html#open) function.
For example:
```
import osapp_data_path = os.getenv("FLET_APP_STORAGE_DATA")my_file_path = os.path.join(app_data_path,"test_file.txt")withopen(my_file_path,"r")as f:  file_content = f.read()print(file_content)
```

Also, you can use the [`os`](https://docs.python.org/3/library/os.html) module (or any other out there) to perform various file operations like renaming, deleting, listing files present in the directory, etc.
## Example: Counter App[​](https://flet.dev/docs/cookbook/read-and-write-files/#example-counter-app "Direct link to Example: Counter App")
Below is an example that showcases a basic Counter application, whose value persists across app launches. This is made possible by writing the counter value to a file in the app's data storage directory and reading it when the app launches.
```
import osfrom datetime import datetimeimport flet as ft# constantsFLET_APP_STORAGE_DATA = os.getenv("FLET_APP_STORAGE_DATA")COUNTER_FILE_PATH = os.path.join(FLET_APP_STORAGE_DATA,"counter.txt")FLET_APP_CONSOLE = os.getenv("FLET_APP_CONSOLE")classCounter(ft.Text):def__init__(self, storage_path=COUNTER_FILE_PATH):super().__init__(theme_style=ft.TextThemeStyle.HEADLINE_LARGE)    self.storage_path = storage_path    self.count = self.__read_from_storage()defincrement(self):"""Increment the counter, store the new value, and return it."""    self.count +=1    self.update()    self.__write_to_storage()defbefore_update(self):super().before_update()    self.value =f"Button tapped {self.count} time{''if self.count ==1else's'}"def__log(self, action:str, value:int=None):"""Log executed action."""if value isNone:      value = self.countprint(f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} - {action} = {value}")def__read_from_storage(self):"""Read counter value. If an error occurs, use 0."""try:withopen(self.storage_path,"r")as f:        value =int(f.read().strip())except(FileNotFoundError, ValueError):# file does not exist or int parsing failed      value =0    self.__log("READ", value)return valuedef__write_to_storage(self):"""Write current counter value to storage."""withopen(self.storage_path,"w")as f:      f.write(str(self.count))    self.__log("WRITE")defmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.LIGHT  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTERdefshow_logs(e: ft.ControlEvent):if FLET_APP_CONSOLE isnotNone:withopen(FLET_APP_CONSOLE,"r")as f:        dlg = ft.AlertDialog(          title=ft.Text("App Logs"),          content=ft.Text(f.read()),          scrollable=True,)        page.open(dlg)  counter = Counter()  page.appbar = ft.AppBar(    title=ft.Text("Storage Playground", weight=ft.FontWeight.BOLD),    center_title=True,    bgcolor=ft.Colors.BLUE,    color=ft.Colors.WHITE,    adaptive=True,    actions=[      ft.IconButton(        icon=ft.Icons.REMOVE_RED_EYE,        tooltip="Show logs",        visible=FLET_APP_CONSOLE isnotNone,        on_click=show_logs,),],)  page.floating_action_button = ft.FloatingActionButton(    icon=ft.Icons.ADD,    text="Increment Counter",    foreground_color=ft.Colors.WHITE,    bgcolor=ft.Colors.BLUE,    on_click=lambda e: counter.increment(),)  page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT  page.add(ft.SafeArea(counter))ft.app(main)
```

  * `Counter` class is a custom control, which is a subclass/extension of the `Text` control. More information [here](https://flet.dev/docs/getting-started/custom-controls).
  * [`FLET_APP_CONSOLE`](https://flet.dev/docs/reference/environment-variables/#flet_app_console) is an environment variable that points to the application's console log file (`console.log`) which contains the app's [console output](https://flet.dev/docs/publish#console-output) (ex: `print()` statements). Its value is set in production mode.
  * If you have an android emulator or physical device, you can download and install this [apk](https://github.com/ndonkoHenri/flet-storage-cookbook/releases).
  * Follow [this](https://flet.dev/docs/publish) guide to package your app for all platforms.


[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/read-and-write-files.md)
[PreviousFonts](https://flet.dev/docs/cookbook/fonts)[NextClient storage](https://flet.dev/docs/cookbook/client-storage)
  * [Storage Paths](https://flet.dev/docs/cookbook/read-and-write-files/#storage-paths)
  * [Writing to a File](https://flet.dev/docs/cookbook/read-and-write-files/#writing-to-a-file)
  * [Reading from a File](https://flet.dev/docs/cookbook/read-and-write-files/#reading-from-a-file)
  * [Example: Counter App](https://flet.dev/docs/cookbook/read-and-write-files/#example-counter-app)


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
