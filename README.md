# tkNotification
Windows10-like ToastNotification written in tkinter


A class that simulates Windows 10\'s Toast Notification


### Parameters

title: string -> Title of the notification. If you don't want a title just pass an empty string

message: string -> Body of the notification

icon_path: string -> Path to the icon to be displayed. .ico files are not recommended. The image will be resized to a
smaller image of 1:1 ratio

buttons: list -> List of tuples containing 2 elements
* [0] element is text to be displayed on button
* [1] element is function to be called on click

timeout: int -> seconds before the notification vanishes

### Example

```python

def ok():
    print('ok')


def cancel():
    print('cancel')


def close():
    print('close')

notification = Notification('Battery', 'Battery has been sufficiently charged.',
                 'path to icon', [
                     ('OK', ok), ('Cancel', cancel), ('Close', close)])
notification.notify()

```

### Screenshot

![screenshot]()

### Issues

- Does not play a sound

