[Skip to main content](https://flet.dev/docs/controls/video/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/video/)
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
  * [Cookbook](https://flet.dev/docs/controls/video/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * Video


On this page
# Video
Video playing control. Based on the [media_kit](https://pub.dev/packages/media_kit) Dart/Flutter package.
Prerequisites
On Linux, the [libmpv](https://mpv.io/) package must be installed. See [this section](https://flet.dev/docs/publish/linux#prerequisites) for more information.
Packaging
To build your Flet app that uses `Video` control add `flet-video` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-video==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/video/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/utility/video)
### Basic Example[​](https://flet.dev/docs/controls/video/#basic-example "Direct link to Basic Example")
python/controls/utility/video/video-example.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/video/video-example.py)
## Properties[​](https://flet.dev/docs/controls/video/#properties "Direct link to Properties")
### `alignment`[​](https://flet.dev/docs/controls/video/#alignment "Direct link to alignment")
Defines the Alignment of the viewport.
Value is of type [`Alignment`](https://flet.dev/docs/reference/types/alignment) and defaults to `alignment.center`.
### `aspect_ratio`[​](https://flet.dev/docs/controls/video/#aspect_ratio "Direct link to aspect_ratio")
Defines the aspect ratio of the video player.
### `autoplay`[​](https://flet.dev/docs/controls/video/#autoplay "Direct link to autoplay")
Whether the video should start playing automatically.
### `fit`[​](https://flet.dev/docs/controls/video/#fit "Direct link to fit")
Value is of type [`ImageFit`](https://flet.dev/docs/reference/types/imagefit) and defaults to `ImageFit.NONE`.
### `filter_quality`[​](https://flet.dev/docs/controls/video/#filter_quality "Direct link to filter_quality")
Filter quality of the texture used to render the video output.
Value is of type [`FilterQuality`](https://flet.dev/docs/reference/types/filterquality) and defaults to `FilterQuality.LOW`.
::: note Android was reported to show blurry images when using `FilterQuality.HIGH`. Prefer the usage of `FilterQuality.MEDIUM` on this platform. :::
### `fill_color`[​](https://flet.dev/docs/controls/video/#fill_color "Direct link to fill_color")
Defines the [color](https://flet.dev/docs/reference/colors) used to fill the video background.
### `muted`[​](https://flet.dev/docs/controls/video/#muted "Direct link to muted")
Defines whether the video player should be started in muted state.
Defaults to `False`.
### `resume_upon_entering_foreground_mode`[​](https://flet.dev/docs/controls/video/#resume_upon_entering_foreground_mode "Direct link to resume_upon_entering_foreground_mode")
Whether to resume the video when application enters foreground mode. Has effect only if `pause_upon_entering_background_mode` is also set to `True`.
### `show_controls`[​](https://flet.dev/docs/controls/video/#show_controls "Direct link to show_controls")
Whether to show the video player controls.
Defaults to `True`.
### `shuffle_playlist`[​](https://flet.dev/docs/controls/video/#shuffle_playlist "Direct link to shuffle_playlist")
Defines whether the playlist should be shuffled.
Defaults to `False`.
### `subtitle_configuration`[​](https://flet.dev/docs/controls/video/#subtitle_configuration "Direct link to subtitle_configuration")
Defines the subtitle configuration for the video player.
Value is of type [`VideoSubtitleConfiguration`](https://flet.dev/docs/reference/types/videosubtitleconfiguration).
### `title`[​](https://flet.dev/docs/controls/video/#title "Direct link to title")
Defines the name of the underlying window & process for native backend. This is visible inside the windows' volume mixer.
### `volume`[​](https://flet.dev/docs/controls/video/#volume "Direct link to volume")
Defines the volume of the video player.
Value ranges between `0.0` and `100.0` (default).
### `pause_upon_entering_background_mode`[​](https://flet.dev/docs/controls/video/#pause_upon_entering_background_mode "Direct link to pause_upon_entering_background_mode")
Whether to pause the video when application enters background mode.
### `pitch`[​](https://flet.dev/docs/controls/video/#pitch "Direct link to pitch")
Defines the relative pitch of the video player.
Defaults to `1.0`.
### `playback_rate`[​](https://flet.dev/docs/controls/video/#playback_rate "Direct link to playback_rate")
Defines the playback rate of the video player.
Defaults to `1.0`.
### `playlist`[​](https://flet.dev/docs/controls/video/#playlist "Direct link to playlist")
The video playlist consisting of `VideoMedia` objects. This property is read-only and can be set only once - at `Video` class instantiation. To modify it later on, use the `playlist_add(media)` and `playlist_remove(media_index)` methods.
### `playlist_mode`[​](https://flet.dev/docs/controls/video/#playlist_mode "Direct link to playlist_mode")
Represents the mode of playback for the `playlist`.
Value is of type [`PlaylistMode`](https://flet.dev/docs/reference/types/playlistmode).
### `wakelock`[​](https://flet.dev/docs/controls/video/#wakelock "Direct link to wakelock")
Whether to acquire wake lock while playing the video. When `True`, device's display will not go to standby/sleep while the video is playing.
Defaults to `False`.
## Methods[​](https://flet.dev/docs/controls/video/#methods "Direct link to Methods")
### `get_current_position()`[​](https://flet.dev/docs/controls/video/#get_current_position "Direct link to get_current_position")
Returns the current position of the video player in milliseconds.
### `get_duration()`[​](https://flet.dev/docs/controls/video/#get_duration "Direct link to get_duration")
Returns the duration of the currently playing `VideoMedia` in the `playlist` in milliseconds.
### `is_completed()`[​](https://flet.dev/docs/controls/video/#is_completed "Direct link to is_completed")
Returns `True` if the video player has reached the end of the currently playing `VideoMedia` in the `playlist`, `False` otherwise.
### `is_playing()`[​](https://flet.dev/docs/controls/video/#is_playing "Direct link to is_playing")
Returns `True` if the video player is currently playing, `False` otherwise.
### `jump_to(media_index)`[​](https://flet.dev/docs/controls/video/#jump_tomedia_index "Direct link to jump_tomedia_index")
Jumps to the `VideoMedia` at the specified index(`media_index`) in the `playlist`.
### `next()`[​](https://flet.dev/docs/controls/video/#next "Direct link to next")
Jumps to the next `VideoMedia` in the `playlist`.
### `pause()`[​](https://flet.dev/docs/controls/video/#pause "Direct link to pause")
Pauses the video player.
### `play()`[​](https://flet.dev/docs/controls/video/#play "Direct link to play")
Starts playing the video.
### `play_or_pause()`[​](https://flet.dev/docs/controls/video/#play_or_pause "Direct link to play_or_pause")
Cycles between play and pause states of the video player. (Plays if paused, pauses if playing)
### `playlist_add(media)`[​](https://flet.dev/docs/controls/video/#playlist_addmedia "Direct link to playlist_addmedia")
Appends/Adds the given `media` (of type `VideoMedia`) to the `playlist`.
### `playlist_remove(media_index)`[​](https://flet.dev/docs/controls/video/#playlist_removemedia_index "Direct link to playlist_removemedia_index")
Removes the `VideoMedia` at the specified index(`media_index`) from the `playlist`.
### `previous()`[​](https://flet.dev/docs/controls/video/#previous "Direct link to previous")
Jumps to the previous `VideoMedia` in the `playlist`.
### `seek(position_milliseconds)`[​](https://flet.dev/docs/controls/video/#seekposition_milliseconds "Direct link to seekposition_milliseconds")
Seeks the currently playing `VideoMedia` in the `playlist` by the specified amount of milliseconds.
### `stop()`[​](https://flet.dev/docs/controls/video/#stop "Direct link to stop")
Stops recording session and release internal recorder resource. It returns a string which is the location of the recorded file. On web, it returns the blob which could be opened using [`page.lauch_url()`](https://flet.dev/docs/controls/page#launch_urlurl). On other platforms, it returns the path to the file which is the `output_path` parameter passed to `start_recording()` method.
## Events[​](https://flet.dev/docs/controls/video/#events "Direct link to Events")
### `on_enter_fullscreen`[​](https://flet.dev/docs/controls/video/#on_enter_fullscreen "Direct link to on_enter_fullscreen")
Fires when the video enters fullscreen
### `on_error`[​](https://flet.dev/docs/controls/video/#on_error "Direct link to on_error")
Fires when an error occurs.
### `on_completed`[​](https://flet.dev/docs/controls/video/#on_completed "Direct link to on_completed")
Fires when a video completes.
### `on_track_changed`[​](https://flet.dev/docs/controls/video/#on_track_changed "Direct link to on_track_changed")
Fires when a video track changes, returns an Int of track currently playing.
### `on_exit_fullscreen`[​](https://flet.dev/docs/controls/video/#on_exit_fullscreen "Direct link to on_exit_fullscreen")
Fires when the video exits fullscreen
### `on_loaded`[​](https://flet.dev/docs/controls/video/#on_loaded "Direct link to on_loaded")
Fires when the video player is initialized and ready for playback.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/video.md)
[PreviousTransparentPointer](https://flet.dev/docs/controls/transparentpointer)[NextWindowDragArea](https://flet.dev/docs/controls/windowdragarea)
  * [Examples](https://flet.dev/docs/controls/video/#examples)
    * [Basic Example](https://flet.dev/docs/controls/video/#basic-example)
  * [Properties](https://flet.dev/docs/controls/video/#properties)
    * [`alignment`](https://flet.dev/docs/controls/video/#alignment)
    * [`aspect_ratio`](https://flet.dev/docs/controls/video/#aspect_ratio)
    * [`autoplay`](https://flet.dev/docs/controls/video/#autoplay)
    * [`fit`](https://flet.dev/docs/controls/video/#fit)
    * [`filter_quality`](https://flet.dev/docs/controls/video/#filter_quality)
    * [`fill_color`](https://flet.dev/docs/controls/video/#fill_color)
    * [`muted`](https://flet.dev/docs/controls/video/#muted)
    * [`resume_upon_entering_foreground_mode`](https://flet.dev/docs/controls/video/#resume_upon_entering_foreground_mode)
    * [`show_controls`](https://flet.dev/docs/controls/video/#show_controls)
    * [`shuffle_playlist`](https://flet.dev/docs/controls/video/#shuffle_playlist)
    * [`subtitle_configuration`](https://flet.dev/docs/controls/video/#subtitle_configuration)
    * [`title`](https://flet.dev/docs/controls/video/#title)
    * [`volume`](https://flet.dev/docs/controls/video/#volume)
    * [`pause_upon_entering_background_mode`](https://flet.dev/docs/controls/video/#pause_upon_entering_background_mode)
    * [`pitch`](https://flet.dev/docs/controls/video/#pitch)
    * [`playback_rate`](https://flet.dev/docs/controls/video/#playback_rate)
    * [`playlist`](https://flet.dev/docs/controls/video/#playlist)
    * [`playlist_mode`](https://flet.dev/docs/controls/video/#playlist_mode)
    * [`wakelock`](https://flet.dev/docs/controls/video/#wakelock)
  * [Methods](https://flet.dev/docs/controls/video/#methods)
    * [`get_current_position()`](https://flet.dev/docs/controls/video/#get_current_position)
    * [`get_duration()`](https://flet.dev/docs/controls/video/#get_duration)
    * [`is_completed()`](https://flet.dev/docs/controls/video/#is_completed)
    * [`is_playing()`](https://flet.dev/docs/controls/video/#is_playing)
    * [`jump_to(media_index)`](https://flet.dev/docs/controls/video/#jump_tomedia_index)
    * [`next()`](https://flet.dev/docs/controls/video/#next)
    * [`pause()`](https://flet.dev/docs/controls/video/#pause)
    * [`play()`](https://flet.dev/docs/controls/video/#play)
    * [`play_or_pause()`](https://flet.dev/docs/controls/video/#play_or_pause)
    * [`playlist_add(media)`](https://flet.dev/docs/controls/video/#playlist_addmedia)
    * [`playlist_remove(media_index)`](https://flet.dev/docs/controls/video/#playlist_removemedia_index)
    * [`previous()`](https://flet.dev/docs/controls/video/#previous)
    * [`seek(position_milliseconds)`](https://flet.dev/docs/controls/video/#seekposition_milliseconds)
    * [`stop()`](https://flet.dev/docs/controls/video/#stop)
  * [Events](https://flet.dev/docs/controls/video/#events)
    * [`on_enter_fullscreen`](https://flet.dev/docs/controls/video/#on_enter_fullscreen)
    * [`on_error`](https://flet.dev/docs/controls/video/#on_error)
    * [`on_completed`](https://flet.dev/docs/controls/video/#on_completed)
    * [`on_track_changed`](https://flet.dev/docs/controls/video/#on_track_changed)
    * [`on_exit_fullscreen`](https://flet.dev/docs/controls/video/#on_exit_fullscreen)
    * [`on_loaded`](https://flet.dev/docs/controls/video/#on_loaded)


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
