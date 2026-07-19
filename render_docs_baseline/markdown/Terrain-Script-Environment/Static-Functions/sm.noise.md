# sm.noise

Contains methods related to random number and noise generation.

Most noise related functions are used for terrain generation.

## Functions

### floatNoise2d {#floatnoise2d}

``` { .lua .api-signature }
sm.noise.floatNoise2d( x, y, seed )
```

A number noise 2d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `seed` | integer | The seed. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |

### gunSpread {#gunspread}

``` { .lua .api-signature }
sm.noise.gunSpread( direction, spreadAngle )
```

Returns a directional vector with a random spread given by a [normal distribution](#randomnormaldistribution).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction. |
| `spreadAngle` | number | The spread angle in degrees. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The spread direction. |

### intNoise2d {#intnoise2d}

``` { .lua .api-signature }
sm.noise.intNoise2d( x, y, seed )
```

An integer noise 2d function. Generates positive numbers only.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `seed` | integer | The seed. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The noise value. |

### octaveNoise2d {#octavenoise2d}

``` { .lua .api-signature }
sm.noise.octaveNoise2d( x, y, octaves, seed )
```

An octave noise 2d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `octaves` | integer | The octaves. |
| `seed` | integer | The seed. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |

### perlinNoise2d {#perlinnoise2d}

``` { .lua .api-signature }
sm.noise.perlinNoise2d( x, y, seed )
```

A perlin noise 2d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `seed` | integer | The seed. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |

### randomNormalDistribution {#randomnormaldistribution}

``` { .lua .api-signature }
sm.noise.randomNormalDistribution( mean, deviation )
```

Returns a random number according to the <a target="_blank" href="https://en.wikipedia.org/wiki/Normal_distribution">normal random number distribution</a>.

Values near the <strong>mean</strong> are the most likely.

Standard <strong>deviation</strong> affects the dispersion of generated values from the mean.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `mean` | number | The mean. |
| `deviation` | number | The deviation. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The random number. |

### randomRange {#randomrange}

``` { .lua .api-signature }
sm.noise.randomRange( a, b )
```

Returns a random number N such that `a <= N <= b`.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `a` | number | The lower bound. |
| `b` | number | The upper bound. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The random value. |

### simplexNoise1d {#simplexnoise1d}

``` { .lua .api-signature }
sm.noise.simplexNoise1d( x, xm? )
```

A simplex noise 1d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `xm` *(optional)* | number | X value multiplier. (Default 1) |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |

### simplexNoise2d {#simplexnoise2d}

``` { .lua .api-signature }
sm.noise.simplexNoise2d( x, y, xm?, ym? )
```

A simplex noise 2d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `xm` *(optional)* | number | X value multiplier. (Default 1) |
| `ym` *(optional)* | number | Y value multiplier. (Default xm) |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |

### simplexNoise3d {#simplexnoise3d}

``` { .lua .api-signature }
sm.noise.simplexNoise3d( x, y, z, xm?, ym?, zm? )
```

A simplex noise 3d function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | number | The X value. |
| `y` | number | The Y value. |
| `z` | number | The Z value. |
| `xm` *(optional)* | number | X value multiplier. (Default 1) |
| `ym` *(optional)* | number | Y value multiplier. (Default xm) |
| `zm` *(optional)* | number | Z value multiplier. (Default xm) |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise value. |
