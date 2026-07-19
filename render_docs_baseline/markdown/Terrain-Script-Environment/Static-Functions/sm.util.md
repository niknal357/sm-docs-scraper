# sm.util

Offers various math-related functions.

## Constants

### easingFunctionIds {#easingfunctionids}

Easing function ids can be passed to the easing function instead of the easing function's name.

The easings are:

- <strong>linear</strong>
- <strong>easeInQuad</strong>
- <strong>easeOutQuad</strong>
- <strong>easeInOutQuad</strong>
- <strong>easeInCubic</strong>
- <strong>easeOutCubic</strong>
- <strong>easeInOutCubic</strong>
- <strong>easeInQuart</strong>
- <strong>easeOutQuart</strong>
- <strong>easeInOutQuart</strong>
- <strong>easeInQuint</strong>
- <strong>easeOutQuint</strong>
- <strong>easeInOutQuint</strong>
- <strong>easeInSine</strong>
- <strong>easeOutSine</strong>
- <strong>easeInOutSine</strong>
- <strong>easeInCirc</strong>
- <strong>easeOutCirc</strong>
- <strong>easeInOutCirc</strong>
- <strong>easeInExpo</strong>
- <strong>easeOutExpo</strong>
- <strong>easeInOutExpo</strong>
- <strong>easeInElastic</strong>
- <strong>easeOutElastic</strong>
- <strong>easeInOutElastic</strong>
- <strong>easeInBack</strong>
- <strong>easeOutBack</strong>
- <strong>easeInOutBack</strong>
- <strong>easeInBounce</strong>
- <strong>easeOutBounce</strong>
- <strong>easeInOutBounce</strong>

**Returns:**

| Type | Description |
| --- | --- |
| table | The area trigger type list. |

## Functions

### axesToQuat {#axestoquat}

``` { .lua .api-signature }
sm.util.axesToQuat( xAxis, yAxis )
```

Constructs a quaternion from a X and Z axis

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `xAxis` | [Vec3](../Userdata/Vec3.md) | The X axis. |
| `yAxis` | [Vec3](../Userdata/Vec3.md) | The Z axis. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | rotation		The quaternion. |

### bezier2 {#bezier2}

``` { .lua .api-signature }
sm.util.bezier2( c0, c1, c2, t )
```

Quadratic Bezier interpolation. One dimensional bezier curve.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `c0` | number | The start value. |
| `c1` | number | The control point. |
| `c2` | number | The end value. |
| `t` | number | The interpolation step. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The interpolated value between two values. |

### bezier3 {#bezier3}

``` { .lua .api-signature }
sm.util.bezier3( c0, c1, c2, c3, t )
```

Cubic Bezier interpolation. One dimensional bezier curve.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `c0` | number | The start value. |
| `c1` | number | The first control point. |
| `c2` | number | The second control point. |
| `c3` | number | The end value. |
| `t` | number | The interpolation step. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The interpolated value between two values. |

### clamp {#clamp}

``` { .lua .api-signature }
sm.util.clamp( value, min, max )
```

Restricts a value to a given range.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `value` | number | The value. |
| `min` | number | The lower limit. |
| `max` | number | The upper limit. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The clamped value. |

### clampUtf8String {#clamputf8string}

``` { .lua .api-signature }
sm.util.clampUtf8String( string, maxLength )
```

Clamps a UTF-8 string to a maximum number of characters without splitting multi-byte sequences.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `string` | string | The input string. |
| `maxLength` | integer | The maximum number of UTF-8 characters. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The clamped string. |

<a id="easing"></a>
### easing(integer, number) {#easing-integer-number}

``` { .lua .api-signature }
sm.util.easing( easingFunctionId, p )
```

Applies an easing function to a given input.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `easingFunctionId` | integer | The easing function to use. (See [sm.util.easingFunctionIds](#easingfunctionids)) |
| `p` | number | The easing function input. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The output. |

### easing(string, number) {#easing-string-number}

``` { .lua .api-signature }
sm.util.easing( easing, p )
```

Applies an easing function to a given input.

Easing function names:

| Value |
| --- |
| <em>linear</em> |
| <em>easeInQuad</em> |
| <em>easeOutQuad</em> |
| <em>easeInOutQuad</em> |
| <em>easeInCubic</em> |
| <em>easeOutCubic</em> |
| <em>easeInOutCubic</em> |
| <em>easeInQuart</em> |
| <em>easeOutQuart</em> |
| <em>easeInOutQuart</em> |
| <em>easeInQuint</em> |
| <em>easeOutQuint</em> |
| <em>easeInOutQuint</em> |
| <em>easeInSine</em> |
| <em>easeOutSine</em> |
| <em>easeInOutSine</em> |
| <em>easeInCirc</em> |
| <em>easeOutCirc</em> |
| <em>easeInOutCirc</em> |
| <em>easeInExpo</em> |
| <em>easeOutExpo</em> |
| <em>easeInOutExpo</em> |
| <em>easeInElastic</em> |
| <em>easeOutElastic</em> |
| <em>easeInOutElastic</em> |
| <em>easeInBack</em> |
| <em>easeOutBack</em> |
| <em>easeInOutBack</em> |
| <em>easeInBounce</em> |
| <em>easeOutBounce</em> |
| <em>easeInOutBounce</em> |

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `easing` | string | The easing function name. |
| `p` | number | The easing function input. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The output. |

### geometricMedian {#geometricmedian}

``` { .lua .api-signature }
sm.util.geometricMedian( points, initialGuess?, iterations? )
```

Numerically approximates the geometric median from a table of points.

If no initial guess is made, the mean position of all the points will be used as a guess.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `points` | table | The table of points. { [Vec3](../Userdata/Vec3.md), ... }. |
| `initialGuess` *(optional)* | [Vec3](../Userdata/Vec3.md) | A guessed position to start searching from. (Optional) |
| `iterations` *(optional)* | integer | The number of iterations. (Defaults to 1) |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The estimated geometric median. |

### hash {#hash}

``` { .lua .api-signature }
sm.util.hash( ... )
```

Create a hash from arguments.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `...` | any | The arguments to be hashed. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The hash. |

### lerp {#lerp}

``` { .lua .api-signature }
sm.util.lerp( a, b, t )
```

Linear interpolation between two values. This is known as a lerp.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `a` | number | The first value. |
| `b` | number | The second value. |
| `t` | number | The interpolation step. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The interpolated value between two values. |

### positiveModulo {#positivemodulo}

``` { .lua .api-signature }
sm.util.positiveModulo( x, n )
```

Returns the positive remainder after division of x by n.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The number. |
| `n` | integer | The modulo value. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The value. |

### smootherstep {#smootherstep}

``` { .lua .api-signature }
sm.util.smootherstep( edge0, edge1, x )
```

An improved version of the [smoothstep](#smoothstep) function which has zero 1st and 2nd order derivatives at `x = edge0` and `x = edge1`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `edge0` | number | The value of the lower edge of the Hermite function. |
| `edge1` | number | The value of the upper edge of the Hermite function. |
| `x` | number | The source value for interpolation. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The value. |

### smoothstep {#smoothstep}

``` { .lua .api-signature }
sm.util.smoothstep( edge0, edge1, x )
```

Performs smooth Hermite interpolation between 0 and 1 when `edge0 < x < edge1`. This is useful in cases where a threshold function with a smooth transition is desired.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `edge0` | number | The value of the lower edge of the Hermite function. |
| `edge1` | number | The value of the upper edge of the Hermite function. |
| `x` | number | The source value for interpolation. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The value. |

### utf8StringLength {#utf8stringlength}

``` { .lua .api-signature }
sm.util.utf8StringLength( string )
```

Returns the number of UTF-8 characters in a string.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `string` | string | The input string. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of UTF-8 characters. |
