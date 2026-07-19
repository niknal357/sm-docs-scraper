# sm.jsonGui

**Associated type:** [JsonGui](../Userdata/JsonGui.md)

## Server + Client

### createGui {#creategui}

``` { .lua .api-signature }
sm.jsonGui.createGui( settings? )
```

Creates a new gui.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `settings` *(optional)* | table | Table with bool settings for: isHud, isInteractive, needsCursor, hidesHotbar, isOverlapped, backgroundAlpha, handleKeySetup, name, layer |

**Returns:**

| Type | Description |
| --- | --- |
| [JsonGui](../Userdata/JsonGui.md) | gui		The gui |

## Client-only

### getViewSize {#getviewsize}

``` { .lua .api-signature }
sm.jsonGui.getViewSize(  )
```

Returns the size of the window in 720 coords.

**Returns:**

| Type | Description |
| --- | --- |
| integer,integer | The view size as width and height. |
