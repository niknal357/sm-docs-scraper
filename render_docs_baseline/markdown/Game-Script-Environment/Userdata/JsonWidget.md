# JsonWidget

**Usage:** Client Only

**Serializable:** No

**Values:**

- <a id="name"></a>`name` [ **string** ] <br>
    - `Get`: (Client-Only) Get the name of the jsonWidget.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`JsonWidget == JsonWidget` | boolean | Checks if two instances of [JsonWidget](JsonWidget.md) refer to the same JsonWidget. |

## Client-only

### getEffect {#geteffect}

``` { .lua .api-signature }
jsonWidget:getEffect( name )
```

Gets an effect from a widget.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `name` | string | The name of the effect on the json widget to get. |

**Returns:**

| Type | Description |
| --- | --- |
| [Effect](Effect.md) | The effect. |

### getUserString {#getuserstring}

``` { .lua .api-signature }
jsonWidget:getUserString( key )
```

Gets a string associated with the given key from a json widget.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `key` | string | The key connected to the value. |

**Returns:**

| Type | Description |
| --- | --- |
| string		value			The value associated with the key. |  |

### isEffectDone {#iseffectdone}

``` { .lua .api-signature }
jsonWidget:isEffectDone( name )
```

Returns if a named effect is done or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `name` | string | The name of the effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the effect is done, false otherwise. |

### isEffectPlaying {#iseffectplaying}

``` { .lua .api-signature }
jsonWidget:isEffectPlaying( name )
```

Returns if a named effect is playing or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `name` | string | The name of the effect. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the effect is playing, false otherwise. |

### setPosition {#setposition}

``` { .lua .api-signature }
jsonWidget:setPosition( x, y )
```

Sets the position of the widget. This will not change the json data position.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `x` | integer | The x position. |
| `y` | integer | The y position. |

<a id="setpreview"></a>
### setPreview(uuid) {#setpreview-uuid}

``` { .lua .api-signature }
jsonWidget:setPreview( uuid )
```

Sets the item preview uuid for a json widget. Passing nil clears the preview.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `uuid` | uuid | The item uuid. |

### setPreview(string) {#setpreview-string}

``` { .lua .api-signature }
jsonWidget:setPreview( string )
```

Sets the blueprint preview path for a json widget. Passing nil clears the preview.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `string` | string | The blueprint path. |

### setPreview() {#setpreview-no-arguments}

``` { .lua .api-signature }
jsonWidget:setPreview(  )
```

### setUserString {#setuserstring}

``` { .lua .api-signature }
jsonWidget:setUserString( key, value )
```

Sets a custom string on a json widget that can be fetched using the key.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `key` | string | The key connected to the value. |
| `value` | string | The value being written onto the widget. |

### setVisible {#setvisible}

``` { .lua .api-signature }
jsonWidget:setVisible( stopImmediate )
```

Sets the visibility of a widget.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `stopImmediate` | boolean | The widgets new visibility state. |

### startEffect {#starteffect}

``` { .lua .api-signature }
jsonWidget:startEffect( name )
```

Starts the effect applied to the widget.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `name` | string | The name of the effect on the json widget to start. |

### stopEffect {#stopeffect}

``` { .lua .api-signature }
jsonWidget:stopEffect( name, stopImmediate? )
```

Stops the effect applied to the widget.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jsonWidget` | [JsonWidget](JsonWidget.md) | The JsonWidget. |
| `name` | string | The name of the effect to stop. |
| `stopImmediate` *(optional)* | boolean | If the effect should stop immediately. (Optional) (Defaults to false) |
