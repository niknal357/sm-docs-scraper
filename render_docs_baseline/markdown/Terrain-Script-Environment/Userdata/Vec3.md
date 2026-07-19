# Vec3

**Associated namespace:** [sm.vec3](../Static-Functions/sm.vec3.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a 3D <strong>vector</strong>.

**Values:**

- <a id="x"></a>`x` [ **number** ] <br>
    - `Get`: Returns the X value of a vector.
    - `Set`: Sets the X value of a vector.

- <a id="y"></a>`y` [ **number** ] <br>
    - `Get`: Returns the Y value of a vector.
    - `Set`: Sets the Y value of a vector.

- <a id="z"></a>`z` [ **number** ] <br>
    - `Get`: Returns the Z value of a vector.
    - `Set`: Sets the Z value of a vector.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__add"></a>`Vec3 + Vec3` | [Vec3](Vec3.md) | Returns the sum of two vectors. |
| `Vec3 + number` | [Vec3](Vec3.md) | Returns the per element sum of a vector and a scalar. |
| <a id="__div"></a>`Vec3 / Vec3` | [Vec3](Vec3.md) | Returns the quotient of two vectors, dividing element by element. |
| `Vec3 / number` | [Vec3](Vec3.md) | Returns the quotient of a vector and a scalar. |
| <a id="__eq"></a>`Vec3 == Vec3` | boolean | Checks if two vectors are equal. |
| <a id="__lt"></a>`Vec3 < Vec3` | boolean | Returns whether the first vector is "less than" the second. |
| <a id="__mul"></a>`Vec3 * Vec3` | [Vec3](Vec3.md) | Returns the product of two vectors, multiplying element by element. |
| `Vec3 * number` | [Vec3](Vec3.md) | Returns the product of a vector and a scalar. |
| <a id="__sub"></a>`Vec3 - Vec3` | [Vec3](Vec3.md) | Returns the difference of two vectors. |
| `Vec3 - number` | [Vec3](Vec3.md) | Returns the per element difference of a vector and a scalar. |
| <a id="__tostring"></a>`tostring(Vec3)` | string | String representation of vector. |
| <a id="__unm"></a>`-Vec3` | [Vec3](Vec3.md) | Returns the negated vector. |

## Functions

### abs {#abs}

``` { .lua .api-signature }
vec3:abs(  )
```

Returns a vector of only positive values by taking the absolute value of each component in the input vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The absolute value vector. |

### ceil {#ceil}

``` { .lua .api-signature }
vec3:ceil(  )
```

Ceil each component of the vector

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The ceiled vector. |

### cross {#cross}

``` { .lua .api-signature }
vec3:cross( v2 )
```

Returns the <a target="_blank" href="https://en.wikipedia.org/wiki/Cross_product">cross product</a> of two vectors.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](Vec3.md) | The first vector. |
| `v2` | [Vec3](Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The cross product. |

### dot {#dot}

``` { .lua .api-signature }
vec3:dot( v2 )
```

Returns the <a target="_blank" href="https://en.wikipedia.org/wiki/Dot_product">dot product</a> of a vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](Vec3.md) | The first vector. |
| `v2` | [Vec3](Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The dot product. |

### floor {#floor}

``` { .lua .api-signature }
vec3:floor(  )
```

Floor each component of the vector

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The floored vector. |

### length {#length}

``` { .lua .api-signature }
vec3:length(  )
```

Returns the length of the vector.

If you want the squared length, using [length2](#length2) is faster than squaring the result of this function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The length of the vector. |

### length2 {#length2}

``` { .lua .api-signature }
vec3:length2(  )
```

Returns the squared length of the vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The squared length of the vector. |

### max {#max}

``` { .lua .api-signature }
vec3:max( v2 )
```

Returns the maximum value between two vectors components.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](Vec3.md) | The first vector. |
| `v2` | [Vec3](Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | Component wise maximum value vector. |

### min {#min}

``` { .lua .api-signature }
vec3:min( v2 )
```

Returns the minimum value between two vectors components.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](Vec3.md) | The first vector. |
| `v2` | [Vec3](Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | Component wise minimum value vector. |

### normalize {#normalize}

``` { .lua .api-signature }
vec3:normalize(  )
```

Normalizes a vector, ie. converts to a unit vector of length 1.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The normalized vector. |

### rotate {#rotate}

``` { .lua .api-signature }
vec3:rotate( angle, normal )
```

Rotate a vector around an axis.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |
| `angle` | number | The angle. |
| `normal` | [Vec3](Vec3.md) | The axis to be rotated around. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The rotated vector. |

### rotateX {#rotatex}

``` { .lua .api-signature }
vec3:rotateX( angle )
```

Rotate a vector around the X axis.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |
| `angle` | number | The angle. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The rotated vector. |

### rotateY {#rotatey}

``` { .lua .api-signature }
vec3:rotateY( angle )
```

Rotate a vector around the Y axis.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |
| `angle` | number | The angle. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The rotated vector. |

### rotateZ {#rotatez}

``` { .lua .api-signature }
vec3:rotateZ( angle )
```

Rotate a vector around the Z axis.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |
| `angle` | number | The angle. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The rotated vector. |

### safeNormalize {#safenormalize}

``` { .lua .api-signature }
vec3:safeNormalize( fallback )
```

Normalizes a vector with safety, ie. converts to a unit vector of length 1.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](Vec3.md) | The vector. |
| `fallback` | [Vec3](Vec3.md) | The fallback vector |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The normalized vector. |
