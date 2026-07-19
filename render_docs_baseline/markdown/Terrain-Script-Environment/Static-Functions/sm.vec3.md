# sm.vec3

**Associated type:** [Vec3](../Userdata/Vec3.md)

A <strong>vector</strong> is used to represent position and direction in 3D space, using X, Y and Z coordinates.

To create one, use [sm.vec3.new](#new).

## Functions

### bezier2 {#bezier2}

``` { .lua .api-signature }
sm.vec3.bezier2( c0, c1, c2, t )
```

Quadratic Bezier interpolation. Three dimensional bezier curve.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `c0` | [Vec3](../Userdata/Vec3.md) | The start point. |
| `c1` | [Vec3](../Userdata/Vec3.md) | The control point. |
| `c2` | [Vec3](../Userdata/Vec3.md) | The end point. |
| `t` | number | The interpolation step. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The interpolated value between two values. |

### bezier3 {#bezier3}

``` { .lua .api-signature }
sm.vec3.bezier3( c0, c1, c2, c3, t )
```

Cubic Bezier interpolation. Three dimensional bezier curve.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `c0` | number | The start point. |
| `c1` | number | The first control point. |
| `c2` | number | The second control point. |
| `c3` | number | The end point. |
| `t` | number | The interpolation step. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The interpolated value between two values. |

### closestAxis {#closestaxis}

``` { .lua .api-signature }
sm.vec3.closestAxis( vector )
```

Finds the closest axis-aligned vector from the given vector

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](../Userdata/Vec3.md) | The vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The axis-aligned vector. |

### fuzzyEquals {#fuzzyequals}

``` { .lua .api-signature }
sm.vec3.fuzzyEquals( v1, v2 )
```

Compare vectors with threshold FLT_EPSILON.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](../Userdata/Vec3.md) | The first vector. |
| `v2` | [Vec3](../Userdata/Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean		The result of the comparison. |  |

### getDistance {#getdistance}

``` { .lua .api-signature }
sm.vec3.getDistance( vector, vector )
```

Get the distance between 2 vectors

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](../Userdata/Vec3.md) | Vector A |
| `vector` | [Vec3](../Userdata/Vec3.md) | Vector B |

**Returns:**

| Type | Description |
| --- | --- |
| number | distance	The distance between the vectors |

### getDistanceSquared {#getdistancesquared}

``` { .lua .api-signature }
sm.vec3.getDistanceSquared( vector, vector )
```

Get the distance between 2 vectors

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](../Userdata/Vec3.md) | Vector A |
| `vector` | [Vec3](../Userdata/Vec3.md) | Vector B |

**Returns:**

| Type | Description |
| --- | --- |
| number | distance	The squared distance between the vectors |

### getRotation {#getrotation}

``` { .lua .api-signature }
sm.vec3.getRotation( v1, v2 )
```

Returns a [quaternion](../Userdata/Quat.md) representing the rotation from one vector to another.

The quaternion can then be multiplied with any vector to rotate it in the same fashion.

```lua
v1 = sm.vec3.new(1,0,0)
v2 = sm.vec3.new(0,1,0)

trans = sm.vec3.getRotation(v1, v2)
-- `trans` now rotates a vector 90 degrees

print(trans * v2)
-- {<Vec3>, x = -1, y = 0, z = 0}
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](../Userdata/Vec3.md) | The first vector. |
| `v2` | [Vec3](../Userdata/Vec3.md) | The second vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](../Userdata/Quat.md) | The transformation. |

### lerp {#lerp}

``` { .lua .api-signature }
sm.vec3.lerp( v1, v2, t )
```

Performs a <a target="_blank" href="https://en.wikipedia.org/wiki/Linear_interpolation">linear interpolation</a> between two vectors.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `v1` | [Vec3](../Userdata/Vec3.md) | The first vector. |
| `v2` | [Vec3](../Userdata/Vec3.md) | The second vector. |
| `t` | number | Interpolation amount between the two inputs. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | Interpolated vector. |

<a id="new"></a>
### new(Vec3) {#new-vec3}

``` { .lua .api-signature }
sm.vec3.new( vector )
```

Creates a new vector from an existing one.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vector` | [Vec3](../Userdata/Vec3.md) | The original vector. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The created vector. |

### new(number, number, number) {#new-number-number-number}

``` { .lua .api-signature }
sm.vec3.new( x, y, z )
```

Creates a new vector.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `z` | number | The Z value. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The created vector. |

### one {#one}

``` { .lua .api-signature }
sm.vec3.one(  )
```

Creates a new vector with 1 in x, y, x.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The one vector. |

### zero {#zero}

``` { .lua .api-signature }
sm.vec3.zero(  )
```

Creates a new vector with 0 in x, y, x.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The zero vector. |
