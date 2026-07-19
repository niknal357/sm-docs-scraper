# sm.quat

**Associated type:** [Quat](../Userdata/Quat.md)

A <strong>quaternion</strong> is used to represent rotation as a <a target="_blank" href="https://en.wikipedia.org/wiki/Quaternion">generalization of complex numbers</a>.

To create one, use [sm.quat.new](#new).

> **Warning:**
> It is uncommon to modify individual X, Y, Z, W components directly. To create a new quaternion, consider using [sm.vec3.getRotation](sm.vec3.md#getrotation).

## Functions

### angleAxis {#angleaxis}

``` { .lua .api-signature }
sm.quat.angleAxis( angle, axis )
```

Creates a new quaternion from angle and axis.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `angle` | number | The rotation angle in radians. |
| `axis` | [Vec3](../Userdata/Vec3.md) | The axis vector to rotate around. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The quaternion for rotating angle radians around axis. |

### fromEuler {#fromeuler}

``` { .lua .api-signature }
sm.quat.fromEuler( euler )
```

Create a new quaternion from an euler angle vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `euler` | [Vec3](../Userdata/Vec3.md) | The euler angle vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The quaternion. |

### identity {#identity}

``` { .lua .api-signature }
sm.quat.identity(  )
```

Creates a new identity quaternion.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The created quaternion. |

### lookRotation {#lookrotation}

``` { .lua .api-signature }
sm.quat.lookRotation( at, up )
```

Create a new quaternion from direction vectors. DEPRECATED

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `at` | [Vec3](../Userdata/Vec3.md) | The forward vector. |
| `up` | [Vec3](../Userdata/Vec3.md) | The up vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The quaternion. |

<a id="new"></a>
### new(Quat) {#new-quat}

``` { .lua .api-signature }
sm.quat.new( quaternion )
```

Creates a new quaternion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion` | [Quat](../Userdata/Quat.md) | The original quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The created quaternion. |

### new(number, number, number, number) {#new-number-number-number-number}

``` { .lua .api-signature }
sm.quat.new( x, y, z, w )
```

Creates a new quaternion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `z` | number | The Z value. |
| `w` | number | The W value. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The created quaternion. |

### rotNegX90 {#rotnegx90}

``` { .lua .api-signature }
sm.quat.rotNegX90(  )
```

Returns the rotation constant for rotating -90 degrees around the X-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotNegY90 {#rotnegy90}

``` { .lua .api-signature }
sm.quat.rotNegY90(  )
```

Returns the rotation constant for rotating -90 degrees around the Y-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotNegZ90 {#rotnegz90}

``` { .lua .api-signature }
sm.quat.rotNegZ90(  )
```

Returns the rotation constant for rotating -90 degrees around the Z-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotX180 {#rotx180}

``` { .lua .api-signature }
sm.quat.rotX180(  )
```

Returns the rotation constant for rotating 180 degrees around the X-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotX90 {#rotx90}

``` { .lua .api-signature }
sm.quat.rotX90(  )
```

Returns the rotation constant for rotating 90 degrees around the X-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotY180 {#roty180}

``` { .lua .api-signature }
sm.quat.rotY180(  )
```

Returns the rotation constant for rotating 180 degrees around the Y-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotY90 {#roty90}

``` { .lua .api-signature }
sm.quat.rotY90(  )
```

Returns the rotation constant for rotating 90 degrees around the Y-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotZ180 {#rotz180}

``` { .lua .api-signature }
sm.quat.rotZ180(  )
```

Returns the rotation constant for rotating 180 degrees around the Z-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### rotZ90 {#rotz90}

``` { .lua .api-signature }
sm.quat.rotZ90(  )
```

Returns the rotation constant for rotating 90 degrees around the Z-axis.

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The rotation quaternion. |

### slerp {#slerp}

``` { .lua .api-signature }
sm.quat.slerp( quaternion1, quaternion2, t )
```

Performs a spherical linear interpolation between two quaternion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `quaternion1` | [Quat](../Userdata/Quat.md) | The first quaternion. |
| `quaternion2` | [Quat](../Userdata/Quat.md) | The second quaternion. |
| `t` | number | Interpolation amount between the two inputs. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The interpolated quaternion. |
