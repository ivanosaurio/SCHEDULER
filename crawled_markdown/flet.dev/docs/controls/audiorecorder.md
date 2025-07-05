[Skip to main content](https://flet.dev/docs/controls/audiorecorder/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/audiorecorder/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
      * [Audio](https://flet.dev/docs/controls/audio)
      * [AudioRecorder](https://flet.dev/docs/controls/audiorecorder)
      * [Draggable](https://flet.dev/docs/controls/draggable)
      * [DragTarget](https://flet.dev/docs/controls/dragtarget)
      * [FilePicker](https://flet.dev/docs/controls/filepicker)
      * [Flashlight](https://flet.dev/docs/controls/flashlight)
      * [FletApp](https://flet.dev/docs/controls/fletapp)
      * [Geolocator](https://flet.dev/docs/controls/geolocator)
      * [GestureDetector](https://flet.dev/docs/controls/gesturedetector)
      * [HapticFeedback](https://flet.dev/docs/controls/hapticfeedback)
      * [InteractiveViewer](https://flet.dev/docs/controls/interactiveviewer)
      * [MergeSemantics](https://flet.dev/docs/controls/mergesemantics)
      * [PermissionHandler](https://flet.dev/docs/controls/permissionhandler)
      * [SelectionArea](https://flet.dev/docs/controls/selectionarea)
      * [Semantics](https://flet.dev/docs/controls/semantics)
      * [SemanticsService](https://flet.dev/docs/controls/semanticsservice)
      * [ShaderMask](https://flet.dev/docs/controls/shadermask)
      * [ShakeDetector](https://flet.dev/docs/controls/shakedetector)
      * [TransparentPointer](https://flet.dev/docs/controls/transparentpointer)
      * [Video](https://flet.dev/docs/controls/video)
      * [WindowDragArea](https://flet.dev/docs/controls/windowdragarea)
  * [Cookbook](https://flet.dev/docs/controls/audiorecorder/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * AudioRecorder


On this page
# AudioRecorder
Audio recorder from microphone to a given file path. Works on macOS, Linux, Windows, iOS, Android and web. Based on the [record](https://pub.dev/packages/record) Dart/Flutter package.
note
On Linux, encoding is provided by [fmedia](https://stsaz.github.io/fmedia/) which must be installed separately.
AudioRecorder control is non-visual and should be added to `page.overlay` list.
Packaging
To build your Flet app that uses `AudioRecorder` control add `flet-audio-recorder` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-audio-recorder==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/audiorecorder/#examples "Direct link to Examples")
### Basic Example[​](https://flet.dev/docs/controls/audiorecorder/#basic-example "Direct link to Basic Example")
python/controls/utility/audio-recorder/audio-recorder-example.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/audio-recorder/audio-recorder-example.py)
## Properties[​](https://flet.dev/docs/controls/audiorecorder/#properties "Direct link to Properties")
note
Not all properties are supported on all platforms. Please check this [platform-feature parity matrix](https://pub.dev/packages/record#platform-feature-parity-matrix) for more information on which properties are supported on which platforms.
### `audio_encoder`[​](https://flet.dev/docs/controls/audiorecorder/#audio_encoder "Direct link to audio_encoder")
The audio encoder to be used for recording.
Value is of type [`AudioEncoder`](https://flet.dev/docs/reference/types/audioencoder) and defaults to [`AudioEncoder.WAV`](https://flet.dev/docs/reference/types/audioencoder#wav).
See [`this`](https://pub.dev/packages/record#file) for a detailed overview on the encodings supported by each platform.
### `auto_gain`[​](https://flet.dev/docs/controls/audiorecorder/#auto_gain "Direct link to auto_gain")
The recorder will try to auto adjust recording volume in a limited range.
Value is of type `bool` and defaults to `False`.
### `bit_rate`[​](https://flet.dev/docs/controls/audiorecorder/#bit_rate "Direct link to bit_rate")
The audio encoding bit rate in bits per second.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `128000`.
### `cancel_echo`[​](https://flet.dev/docs/controls/audiorecorder/#cancel_echo "Direct link to cancel_echo")
The recorder will try to reduce echo.
Value is of type `bool` defaults to `False`.
### `channels_num`[​](https://flet.dev/docs/controls/audiorecorder/#channels_num "Direct link to channels_num")
The numbers of channels for the recording. `1` = mono, `2` = stereo.
Defaults to `2`.
### `sample_rate`[​](https://flet.dev/docs/controls/audiorecorder/#sample_rate "Direct link to sample_rate")
The sample rate for audio in samples per second.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `44100`.
### `suppress_noise`[​](https://flet.dev/docs/controls/audiorecorder/#suppress_noise "Direct link to suppress_noise")
The recorder will try to negates the input noise.
Value is of type `bool` and defaults to `False`.
## Methods[​](https://flet.dev/docs/controls/audiorecorder/#methods "Direct link to Methods")
### `cancel_recording()`[​](https://flet.dev/docs/controls/audiorecorder/#cancel_recording "Direct link to cancel_recording")
Stops and discards/deletes the file/blob.
### `get_input_devices()`[​](https://flet.dev/docs/controls/audiorecorder/#get_input_devices "Direct link to get_input_devices")
Returns a dictionary whose values are the input devices available on the platform.
### `has_permission()`[​](https://flet.dev/docs/controls/audiorecorder/#has_permission "Direct link to has_permission")
Checks (and optionally requests) for audio record permission.
### `is_paused()`[​](https://flet.dev/docs/controls/audiorecorder/#is_paused "Direct link to is_paused")
Checks if recording session is paused.
### `is_recording()`[​](https://flet.dev/docs/controls/audiorecorder/#is_recording "Direct link to is_recording")
Checks if there's a valid recording session. Note that if the recording session is paused, this method will still return `True`.
### `is_supported_encoder(encoder)`[​](https://flet.dev/docs/controls/audiorecorder/#is_supported_encoderencoder "Direct link to is_supported_encoderencoder")
Checks if the given `encoder` is supported on the current platform.
### `pause()`[​](https://flet.dev/docs/controls/audiorecorder/#pause "Direct link to pause")
Pauses recording session.
### `resume()`[​](https://flet.dev/docs/controls/audiorecorder/#resume "Direct link to resume")
Resumes recording session after pause.
### `seek(position_milliseconds)`[​](https://flet.dev/docs/controls/audiorecorder/#seekposition_milliseconds "Direct link to seekposition_milliseconds")
Moves the cursor to the desired position.
### `start_recording(output_path)`[​](https://flet.dev/docs/controls/audiorecorder/#start_recordingoutput_path "Direct link to start_recordingoutput_path")
Starts new recording session on the specified `output_path`. On platforms other than web, the `output_path` must be provided.
### `stop_recording()`[​](https://flet.dev/docs/controls/audiorecorder/#stop_recording "Direct link to stop_recording")
Stops recording session and release internal recorder resource. It returns a string which is the location of the recorded file. On web, it returns the blob which could be opened using [`page.lauch_url()`](https://flet.dev/docs/controls/page#launch_urlurl). On other platforms, it returns the path to the file which is the `output_path` parameter passed to `start_recording()` method.
## Events[​](https://flet.dev/docs/controls/audiorecorder/#events "Direct link to Events")
### `on_state_changed`[​](https://flet.dev/docs/controls/audiorecorder/#on_state_changed "Direct link to on_state_changed")
Fires when audio recorder's state changes.
Event handler argument is of type [`AudioRecorderStateChangeEvent`](https://flet.dev/docs/reference/types/audiorecorderstatechangeevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/audiorecorder.md)
[PreviousAudio](https://flet.dev/docs/controls/audio)[NextDraggable](https://flet.dev/docs/controls/draggable)
  * [Examples](https://flet.dev/docs/controls/audiorecorder/#examples)
    * [Basic Example](https://flet.dev/docs/controls/audiorecorder/#basic-example)
  * [Properties](https://flet.dev/docs/controls/audiorecorder/#properties)
    * [`audio_encoder`](https://flet.dev/docs/controls/audiorecorder/#audio_encoder)
    * [`auto_gain`](https://flet.dev/docs/controls/audiorecorder/#auto_gain)
    * [`bit_rate`](https://flet.dev/docs/controls/audiorecorder/#bit_rate)
    * [`cancel_echo`](https://flet.dev/docs/controls/audiorecorder/#cancel_echo)
    * [`channels_num`](https://flet.dev/docs/controls/audiorecorder/#channels_num)
    * [`sample_rate`](https://flet.dev/docs/controls/audiorecorder/#sample_rate)
    * [`suppress_noise`](https://flet.dev/docs/controls/audiorecorder/#suppress_noise)
  * [Methods](https://flet.dev/docs/controls/audiorecorder/#methods)
    * [`cancel_recording()`](https://flet.dev/docs/controls/audiorecorder/#cancel_recording)
    * [`get_input_devices()`](https://flet.dev/docs/controls/audiorecorder/#get_input_devices)
    * [`has_permission()`](https://flet.dev/docs/controls/audiorecorder/#has_permission)
    * [`is_paused()`](https://flet.dev/docs/controls/audiorecorder/#is_paused)
    * [`is_recording()`](https://flet.dev/docs/controls/audiorecorder/#is_recording)
    * [`is_supported_encoder(encoder)`](https://flet.dev/docs/controls/audiorecorder/#is_supported_encoderencoder)
    * [`pause()`](https://flet.dev/docs/controls/audiorecorder/#pause)
    * [`resume()`](https://flet.dev/docs/controls/audiorecorder/#resume)
    * [`seek(position_milliseconds)`](https://flet.dev/docs/controls/audiorecorder/#seekposition_milliseconds)
    * [`start_recording(output_path)`](https://flet.dev/docs/controls/audiorecorder/#start_recordingoutput_path)
    * [`stop_recording()`](https://flet.dev/docs/controls/audiorecorder/#stop_recording)
  * [Events](https://flet.dev/docs/controls/audiorecorder/#events)
    * [`on_state_changed`](https://flet.dev/docs/controls/audiorecorder/#on_state_changed)


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
