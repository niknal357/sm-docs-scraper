# JsonGui

**Associated namespace:** [sm.jsonGui](../Static-Functions/sm.jsonGui.md)

**Usage:** Client Only

**Serializable:** No

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a gui.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`JsonGui == JsonGui` | boolean | Checks if two instances of [JsonGui](JsonGui.md) refer to the same JsonGui. |

## Functions

### clearOnCloseCallback {#clearonclosecallback}

``` { .lua .api-signature }
jsonGui:clearOnCloseCallback(  )
```

Clears the close callback so it will not be called when the gui is closed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |

### close {#close}

``` { .lua .api-signature }
jsonGui:close(  )
```

Close a JsonGui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |

### getWidget {#getwidget}

``` { .lua .api-signature }
jsonGui:getWidget( widgetName )
```

Returns a JsonWidget. Nil if no widget was found with the name

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |
| `widgetName` | string | The name of the widget. |

**Returns:**

| Type | Description |
| --- | --- |
| [JsonWidget](JsonWidget.md) | widget			The found widget in the JsonGui. |

### getWidgetAbsolutePosition {#getwidgetabsoluteposition}

``` { .lua .api-signature }
jsonGui:getWidgetAbsolutePosition( widgetName )
```

Get the absolute position of a named widget in 720 coords

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |
| `widgetName` | string | The name of the widget. |

**Returns:**

| Type | Description |
| --- | --- |
| number, number | Left, Top |

### isActive {#isactive}

``` { .lua .api-signature }
jsonGui:isActive(  )
```

Check if a JsonGui is active

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Is the gui active? |

### isHidden {#ishidden}

``` { .lua .api-signature }
jsonGui:isHidden(  )
```

Gets the visibility of the gui.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | hidden			True if the gui is hidden. |

### render {#render}

``` { .lua .api-signature }
jsonGui:render( DOM, forceProperties? )
```

Renders the DOM

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |
| `DOM` | table | A table representing the gui elements to show |
| `forceProperties` *(optional)* | boolean | Force update widget properties (optional). (Defaults to false) |

### setHidden {#sethidden}

``` { .lua .api-signature }
jsonGui:setHidden( hidden )
```

Sets desired visibility of the gui.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [JsonGui](JsonGui.md) | The gui. |
| `hidden` | boolean | True if the gui should be hidden. |
