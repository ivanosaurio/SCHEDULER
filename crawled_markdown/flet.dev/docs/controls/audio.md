[Skip to main content](https://flet.dev/docs/controls/audio/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/audio/)
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
  * [Cookbook](https://flet.dev/docs/controls/audio/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * Audio


On this page
# Audio
A control to simultaneously play multiple audio files. Works on macOS, Linux, Windows, iOS, Android and web. Based on [audioplayers](https://pub.dev/packages/audioplayers) Flutter widget.
Audio control is non-visual and should be added to `page.overlay` list.
Packaging
To build your Flet app that uses `Audio` control add `flet-audio` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-audio==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/audio/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/utility/audio)
### Autoplay audio[​](https://flet.dev/docs/controls/audio/#autoplay-audio "Direct link to Autoplay audio")
note
Autoplay works in desktop, mobile apps and Safari browser, but doesn't work in Chrome/Edge.
python/controls/utility/audio/audio-autoplay.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/audio/audio-autoplay.py)
### Audio with playback controls[​](https://flet.dev/docs/controls/audio/#audio-with-playback-controls "Direct link to Audio with playback controls")
python/controls/utility/audio/audio-player.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/audio/audio-player.py)
## Properties[​](https://flet.dev/docs/controls/audio/#properties "Direct link to Properties")
### `autoplay`[​](https://flet.dev/docs/controls/audio/#autoplay "Direct link to autoplay")
Starts playing audio as soon as audio control is added to a page.
Value is of type `bool` and defaults to `False`.
note
Autoplay works in desktop, mobile apps and Safari browser, but doesn't work in Chrome/Edge.
### `balance`[​](https://flet.dev/docs/controls/audio/#balance "Direct link to balance")
Sets the stereo balance.
-1 - The left channel is at full volume; the right channel is silent. 1 - The right channel is at full volume; the left channel is silent. 0 - Both channels are at the same volume.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
note
Setting balance is supported on Windows and Linux only.
### `playback_rate`[​](https://flet.dev/docs/controls/audio/#playback_rate "Direct link to playback_rate")
Sets the playback rate. iOS and macOS have limits between 0.5 and 2x Android SDK version should be 23 or higher.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
### `release_mode`[​](https://flet.dev/docs/controls/audio/#release_mode "Direct link to release_mode")
Sets the release mode.
Value is of type [`ReleaseMode`](https://flet.dev/docs/reference/types/releasemode) and defaults to `ReleaseMode.RELEASE`.
### `src`[​](https://flet.dev/docs/controls/audio/#src "Direct link to src")
The audio source. Can be a URL or a local [asset file](https://flet.dev/docs/cookbook/assets).
note
[Here](https://github.com/bluefireteam/audioplayers/blob/main/troubleshooting.md#supported-formats--encodings) is a list of supported audio formats.
### `src_base64`[​](https://flet.dev/docs/controls/audio/#src_base64 "Direct link to src_base64")
Sets the contents of audio file encoded in base-64 format.
Value is of type `str`.
### `volume`[​](https://flet.dev/docs/controls/audio/#volume "Direct link to volume")
Sets the volume (amplitude).
0 is mute and 1 is the max volume. The values between 0 and 1 are linearly interpolated.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
## Methods[​](https://flet.dev/docs/controls/audio/#methods "Direct link to Methods")
### `get_current_position()`[​](https://flet.dev/docs/controls/audio/#get_current_position "Direct link to get_current_position")
Returns the current position in milliseconds.
### `get_duration()`[​](https://flet.dev/docs/controls/audio/#get_duration "Direct link to get_duration")
Returns the duration of audio in milliseconds.
### `pause()`[​](https://flet.dev/docs/controls/audio/#pause "Direct link to pause")
Stops playing audio.
### `play()`[​](https://flet.dev/docs/controls/audio/#play "Direct link to play")
Starts playing audio for the beginning.
### `release()`[​](https://flet.dev/docs/controls/audio/#release "Direct link to release")
Stops playing and releases the resources associated with this audio control. The resources are going to be fetched or buffered again as soon as you call `resume()` or change the source.
### `resume()`[​](https://flet.dev/docs/controls/audio/#resume "Direct link to resume")
Resumes playing audio from the current position.
### `seek()`[​](https://flet.dev/docs/controls/audio/#seek "Direct link to seek")
Moves the cursor to the desired position.
Method arguments:
  * `position_milliseconds` - desired position in milliseconds.


## Events[​](https://flet.dev/docs/controls/audio/#events "Direct link to Events")
### `on_duration_changed`[​](https://flet.dev/docs/controls/audio/#on_duration_changed "Direct link to on_duration_changed")
Fires as soon as audio duration is available (it might take a while to download or buffer it).
Event handler argument is of type [`AudioDurationChangeEvent`](https://flet.dev/docs/reference/types/audiodurationchangeevent).
### `on_loaded`[​](https://flet.dev/docs/controls/audio/#on_loaded "Direct link to on_loaded")
Fires when an audio is loaded/buffered.
### `on_position_changed`[​](https://flet.dev/docs/controls/audio/#on_position_changed "Direct link to on_position_changed")
Fires when audio position is changed. Will continuously update the position of the playback every 1 second if the status is playing. Can be used for a progress bar.
Event handler argument is of type [`AudioPositionChangeEvent`](https://flet.dev/docs/reference/types/audiopositionchangeevent).
### `on_seek_complete`[​](https://flet.dev/docs/controls/audio/#on_seek_complete "Direct link to on_seek_complete")
Fires on seek completions. An event is going to be sent as soon as the audio seek is finished.
### `on_state_changed`[​](https://flet.dev/docs/controls/audio/#on_state_changed "Direct link to on_state_changed")
Fires when audio player state changes.
Event handler argument is of type [`AudioStateChangeEvent`](https://flet.dev/docs/reference/types/audiostatechangeevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/audio.md)
[PreviousUtility](https://flet.dev/docs/controls/utility)[NextAudioRecorder](https://flet.dev/docs/controls/audiorecorder)
  * [Examples](https://flet.dev/docs/controls/audio/#examples)
    * [Autoplay audio](https://flet.dev/docs/controls/audio/#autoplay-audio)
    * [Audio with playback controls](https://flet.dev/docs/controls/audio/#audio-with-playback-controls)
  * [Properties](https://flet.dev/docs/controls/audio/#properties)
    * [`autoplay`](https://flet.dev/docs/controls/audio/#autoplay)
    * [`balance`](https://flet.dev/docs/controls/audio/#balance)
    * [`playback_rate`](https://flet.dev/docs/controls/audio/#playback_rate)
    * [`release_mode`](https://flet.dev/docs/controls/audio/#release_mode)
    * [`src`](https://flet.dev/docs/controls/audio/#src)
    * [`src_base64`](https://flet.dev/docs/controls/audio/#src_base64)
    * [`volume`](https://flet.dev/docs/controls/audio/#volume)
  * [Methods](https://flet.dev/docs/controls/audio/#methods)
    * [`get_current_position()`](https://flet.dev/docs/controls/audio/#get_current_position)
    * [`get_duration()`](https://flet.dev/docs/controls/audio/#get_duration)
    * [`pause()`](https://flet.dev/docs/controls/audio/#pause)
    * [`play()`](https://flet.dev/docs/controls/audio/#play)
    * [`release()`](https://flet.dev/docs/controls/audio/#release)
    * [`resume()`](https://flet.dev/docs/controls/audio/#resume)
    * [`seek()`](https://flet.dev/docs/controls/audio/#seek)
  * [Events](https://flet.dev/docs/controls/audio/#events)
    * [`on_duration_changed`](https://flet.dev/docs/controls/audio/#on_duration_changed)
    * [`on_loaded`](https://flet.dev/docs/controls/audio/#on_loaded)
    * [`on_position_changed`](https://flet.dev/docs/controls/audio/#on_position_changed)
    * [`on_seek_complete`](https://flet.dev/docs/controls/audio/#on_seek_complete)
    * [`on_state_changed`](https://flet.dev/docs/controls/audio/#on_state_changed)


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
