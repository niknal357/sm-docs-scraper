# Color

**Associated namespace:** [sm.color](../Static-Functions/sm.color.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>color</strong>.

**Values:**

- <a id="a"></a>`a` [ **number** ] <br>
    - `Get`: Returns the alpha value of a color.
    - `Set`: Sets the alpha value of a color.

- <a id="b"></a>`b` [ **number** ] <br>
    - `Get`: Returns the blue value of a color.
    - `Set`: Sets the blue value of a color.

- <a id="g"></a>`g` [ **number** ] <br>
    - `Get`: Returns the green value of a color.
    - `Set`: Sets the green value of a color.

- <a id="r"></a>`r` [ **number** ] <br>
    - `Get`: Returns the red value of a color.
    - `Set`: Sets the red value of a color.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__add"></a>`Color + Color` | [Color](Color.md) | Returns the sum of two colors, adding each component. |
| <a id="__div"></a>`Color / Color` | [Color](Color.md) | Returns the quotient of two colors, dividing each component. |
| `Color / number` | [Color](Color.md) | Returns the quotient of a color and a scalar. |
| <a id="__eq"></a>`Color == Color` | boolean | Checks if two colors are equal. |
| <a id="__mul"></a>`Color * Color` | [Color](Color.md) | Returns the product of two colors, multiplying each component. |
| `Color * number` | [Color](Color.md) | Returns the product of a color and a scalar. |
| <a id="__sub"></a>`Color - Color` | [Color](Color.md) | Returns the difference of two colors, subtracting each component. |
| <a id="__tostring"></a>`tostring(Color)` | string | Returns the color as a string. |

## Functions

### getGuiColorStr {#getguicolorstr}

``` { .lua .api-signature }
color:getGuiColorStr(  )
```

Get the json gui color representation of the color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `color` | [Color](Color.md) | The color object. |

**Returns:**

| Type | Description |
| --- | --- |
| string | Json gui color string. |

### getHexStr {#gethexstr}

``` { .lua .api-signature }
color:getHexStr(  )
```

Get the hex representation of the color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `color` | [Color](Color.md) | The color object. |

**Returns:**

| Type | Description |
| --- | --- |
| string | Hex string. |

### getUintRgba {#getuintrgba}

``` { .lua .api-signature }
color:getUintRgba(  )
```

Get the uint rgba representation of the color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `color` | [Color](Color.md) | The color object. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | color value. |
