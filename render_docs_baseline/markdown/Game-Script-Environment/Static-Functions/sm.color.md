# sm.color

**Associated type:** [Color](../Userdata/Color.md)

A <strong>color</strong> is represented using a red, green, blue and alpha component. Colors are prominently used for blocks and parts that are colored by the <em>Paint Tool</em>.

To create one, use [sm.color.new](#new). It is possible to use hex `0xRRGGBBAA` or strings `"RRGGBBAA"`.

> **Note:**
> R, G, B, A values range between 0.0&ndash;1.0.

## Functions

### lerp {#lerp}

``` { .lua .api-signature }
sm.color.lerp( color1, color2, t )
```

Linearly interpolates between two colors

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `color1` | [Color](../Userdata/Color.md) | The first color. |
| `color2` | [Color](../Userdata/Color.md) | The second color. |
| `t` | number | Interpolation amount between the two inputs. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | Interpolated color. |

<a id="new"></a>
### new(Color) {#new-color}

``` { .lua .api-signature }
sm.color.new( color )
```

Creates a new color object from another color object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `color` | [Color](../Userdata/Color.md) | The color to copy. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The created color. |

### new(number, number, number, number?) {#new-number-number-number-number-optional}

``` { .lua .api-signature }
sm.color.new( r, g, b, a? )
```

Creates a new color object from R, G, B, A.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `r` | number | The red value. |
| `g` | number | The green value. |
| `b` | number | The blue value. |
| `a` *(optional)* | number | The alpha value. Defaults to 1.0. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The created color. |

### new(string) {#new-string}

``` { .lua .api-signature }
sm.color.new( hexStr )
```

Creates a new color object from a hex string `"RRGGBBAA"`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `hexStr` | string | The hex string. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The created color. |

### new(integer) {#new-integer}

``` { .lua .api-signature }
sm.color.new( hexInt )
```

Creates a new color object from a hex value `0xRRGGBBAA`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `hexInt` | integer | The hex value. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The created color. |
