[Skip to main content](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/encrypting-sensitive-data/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/encrypting-sensitive-data/)
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
  * Encrypting sensitive data


On this page
# Encrypting sensitive data
Sensitive data such as tokens, keys, credit card numbers and other "secrets" must be stored at rest (database, files, [client storage](https://flet.dev/docs/cookbook/client-storage)) in encrypted form to avoid data breaches.
Flet includes utility methods to encrypt and decrypt sensitive text data using symmetric algorithm (where the same key is used for encryption and decryption). They use [Fernet](https://github.com/fernet/spec/blob/master/Spec.md) implementation from [cryptography](https://pypi.org/project/cryptography/) package, which is AES 128 with some additional hardening, plus PBKDF2 to derive encryption key from a user passphrase.
## Secret key[​](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#secret-key "Direct link to Secret key")
Encryption secret key (aka password, or passphrase) is an arbitrary password-like string configured by a user and used for encrypting and decrypting data. Crypto algorithm uses secret key to "derive" encryption key (32 bytes).
danger
Do not embed any secrets into the source code to avoid accidental exposure to the public!
You can provide a secret to your app via environment variable:
```
import ossecret_key = os.getenv("MY_APP_SECRET_KEY")
```

Before running the app set the secret in a command line:
```
$ export MY_APP_SECRET_KEY="<secret>"
```

note
While passing secrets via environment variables is a common practice amongst developers and service providers it does not fully prevent secrets leaking in some environments. Other mechanisms can be used to inject secrets to your application such as mounting secret files or vault services.
## Encrypting data[​](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#encrypting-data "Direct link to Encrypting data")
Use `encrypt()` method to encrypt a string:
```
import osfrom flet.security import encrypt, decryptsecret_key = os.getenv("MY_APP_SECRET_KEY")plain_text ="This is a secret message!"encrypted_data = encrypt(plain_text, secret_key)
```

`encrypted_data` is a URL-safe base64-encoded string.
`encrypt` accepts strings only, so any objects must be serialized to JSON, XML or other text-based format before encryption.
## Decrypting data[​](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#decrypting-data "Direct link to Decrypting data")
Use `decrypt()` method to decrypt the data:
```
import osfrom flet.security import encrypt, decryptsecret_key = os.getenv("MY_APP_SECRET_KEY")encrypted_data ="601llp2zpPp4QjBWe2cOwGdBQUFBQUJqTTFJbmgyWU5jblVp..."plain_text = decrypt(encrypted_data, secret_key)print(plain_text)
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/encrypting-sensitive-data.md)
[PreviousSession storage](https://flet.dev/docs/cookbook/session-storage)[NextPubSub](https://flet.dev/docs/cookbook/pub-sub)
  * [Secret key](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#secret-key)
  * [Encrypting data](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#encrypting-data)
  * [Decrypting data](https://flet.dev/docs/cookbook/encrypting-sensitive-data/#decrypting-data)


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
