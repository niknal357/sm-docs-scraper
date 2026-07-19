# Quat

**Associated namespace:** [sm.quat](../Static-Functions/sm.quat.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>quaternion</strong>.

**Values:**

- <a id="w"></a>`w` [ **number** ] <br>
    - `Get`: Returns the W value of a quaternion.
    - `Set`: Sets the W value of a quaternion.

- <a id="x"></a>`x` [ **number** ] <br>
    - `Get`: Returns the X value of a quaternion.
    - `Set`: Sets the X value of a quaternion.

- <a id="y"></a>`y` [ **number** ] <br>
    - `Get`: Returns the Y value of a quaternion.
    - `Set`: Sets the Y value of a quaternion.

- <a id="z"></a>`z` [ **number** ] <br>
    - `Get`: Returns the Z value of a quaternion.
    - `Set`: Sets the Z value of a quaternion.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Quat == Quat` | boolean | Checks if two quaternions are equal. |
| <a id="__mul"></a>`Quat * Quat` | [Quat](Quat.md) | Returns the <a target="_blank" href="https://en.wikipedia.org/wiki/Quaternion#Hamilton_product">Hamilton product</a> of two quaternions. |
| `Quat * Vec3` | [Vec3](Vec3.md) | Returns the rotation by a quaternion on a vector. |

## Functions

### getAt {#getat}

``` { .lua .api-signature }
quat:getAt(  )
```

Returns the quaternions at vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The at vector.	 |

### getRight {#getright}

``` { .lua .api-signature }
quat:getRight(  )
```

Returns the quaternions right vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The right vector. |

### getUp {#getup}

``` { .lua .api-signature }
quat:getUp(  )
```

Returns the quaternions up vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The up vector. |

### inverse {#inverse}

``` { .lua .api-signature }
quat:inverse(  )
```

Inverts the quaternion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The inverted quaternion. |

### normalize {#normalize}

``` { .lua .api-signature }
quat:normalize(  )
```

Normalizes a quaternion, ie. converts to a unit quaternion of length 1.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The normalized quaternion. |

### round90 {#round90}

``` { .lua .api-signature }
quat:round90(  )
```

Rounds the quaternion rotation into 90 degree steps

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The rounded quaternion. |

### safeNormalize {#safenormalize}

``` { .lua .api-signature }
quat:safeNormalize( fallback )
```

Normalizes a quaternion with safety, ie. converts to a unit quaternion of length 1.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](Quat.md) | The quaternion. |
| `fallback` | [Quat](Quat.md) | The fallback quaternion |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The normalized quaternion. |
