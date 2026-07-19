# sm.debugDraw

The <strong>Debug Draw</strong> api can be used for drawing geometric primitives for debug purposes.

## Functions

### addAabb {#addaabb}

``` { .lua .api-signature }
sm.debugDraw.addAabb( name, min, max, color? )
```

Adds a named aabb debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug transform name. |
| `min` | [Vec3](../Userdata/Vec3.md) | The box minimum extent. |
| `max` | [Vec3](../Userdata/Vec3.md) | The box maximum extent. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |

### addArrow {#addarrow}

``` { .lua .api-signature }
sm.debugDraw.addArrow( name, from, to?, color? )
```

Adds a named arrow debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug arrow name. |
| `from` | [Vec3](../Userdata/Vec3.md) | The from position. |
| `to` *(optional)* | [Vec3](../Userdata/Vec3.md) | The to position. Defaults to the from position plus one along the z axis. (World up vector) |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |

### addBox {#addbox}

``` { .lua .api-signature }
sm.debugDraw.addBox( name, min, max, position, rotation?, color? )
```

Adds a named box debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug transform name. |
| `min` | [Vec3](../Userdata/Vec3.md) | The box minimum extent. |
| `max` | [Vec3](../Userdata/Vec3.md) | The box maximum extent. |
| `position` | [Vec3](../Userdata/Vec3.md) | The box position. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The box rotation. Defaults to identity. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |

### addSphere {#addsphere}

``` { .lua .api-signature }
sm.debugDraw.addSphere( name, center, radius?, color? )
```

Adds a named sphere debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug sphere name. |
| `center` | [Vec3](../Userdata/Vec3.md) | The sphere center. |
| `radius` *(optional)* | number | The sphere radius. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |

### addText {#addtext}

``` { .lua .api-signature }
sm.debugDraw.addText( name, text, position, fade?, scale?, color? )
```

Adds text in world debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The text name. |
| `text` | string | The text content. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position of the text. |
| `fade` *(optional)* | boolean | If the text should fade. Defaults to false. |
| `scale` *(optional)* | number | The scale of the text. Defaults to 30. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |

### addTransform {#addtransform}

``` { .lua .api-signature }
sm.debugDraw.addTransform( name, origin, rotation, scale? )
```

Adds a named transform debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug transform name. |
| `origin` | [Vec3](../Userdata/Vec3.md) | The transform origin. |
| `rotation` | [Quat](../Userdata/Quat.md) | The transform rotation. |
| `scale` *(optional)* | number | The transform scale. Defaults to 1.0. |

### clear {#clear}

``` { .lua .api-signature }
sm.debugDraw.clear( name? )
```

Removes all debug draws beginning with a given name.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` *(optional)* | string | The name to match (Defaults to "", matching all debug draws). |

### drawArrowTopDown {#drawarrowtopdown}

``` { .lua .api-signature }
sm.debugDraw.drawArrowTopDown( from, to?, color? )
```

Draws an arrow.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [Vec3](../Userdata/Vec3.md) | The starting position of the arrow. |
| `to` *(optional)* | [Vec3](../Userdata/Vec3.md) | The ending position of the arrow. Defaults to the starting position plus one unit along the z-axis (world up vector). |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the arrow. Defaults to white. |

### drawBoxTopDown {#drawboxtopdown}

``` { .lua .api-signature }
sm.debugDraw.drawBoxTopDown( min, max, position, rotation?, color?, duration? )
```

Draws a box.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum extent of the box. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum extent of the box. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position of the box. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation of the box. Defaults to identity. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the box. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### drawCircleTopDown {#drawcircletopdown}

``` { .lua .api-signature }
sm.debugDraw.drawCircleTopDown( center, radius?, color? )
```

Draws a circle.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the circle. |
| `radius` *(optional)* | number | The radius of the circle. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the circle. Defaults to white. |

### drawRectTopDown {#drawrecttopdown}

``` { .lua .api-signature }
sm.debugDraw.drawRectTopDown( min, max, color? )
```

Draws a rectangle.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum extent of the rectangle. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum extent of the rectangle. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the rectangle. Defaults to white. |

### drawSphereTopDown {#drawspheretopdown}

``` { .lua .api-signature }
sm.debugDraw.drawSphereTopDown( center, radius?, color? )
```

Draws a sphere.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the sphere. |
| `radius` *(optional)* | number | The radius of the sphere. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the sphere. Defaults to white. |

### flashAabb {#flashaabb}

``` { .lua .api-signature }
sm.debugDraw.flashAabb( min, max, color?, duration? )
```

Flashes an axis-aligned bounding box for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum world extent of the box. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum world extent of the box. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the box. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashArrow {#flasharrow}

``` { .lua .api-signature }
sm.debugDraw.flashArrow( from, to?, color?, duration? )
```

Flashes an arrow for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [Vec3](../Userdata/Vec3.md) | The starting position of the arrow. |
| `to` *(optional)* | [Vec3](../Userdata/Vec3.md) | The ending position of the arrow. Defaults to the starting position plus one unit along the z-axis (world up vector). |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the arrow. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashArrowTopDown {#flasharrowtopdown}

``` { .lua .api-signature }
sm.debugDraw.flashArrowTopDown( from, to?, color?, duration? )
```

Flashes an arrow for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [Vec3](../Userdata/Vec3.md) | The starting position of the arrow. |
| `to` *(optional)* | [Vec3](../Userdata/Vec3.md) | The ending position of the arrow. Defaults to the starting position plus one unit along the z-axis (world up vector). |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the arrow. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashBox {#flashbox}

``` { .lua .api-signature }
sm.debugDraw.flashBox( min, max, position, rotation?, color?, duration? )
```

Flashes a box for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum extent of the box. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum extent of the box. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position of the box. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation of the box. Defaults to identity. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the box. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashBoxTopDown {#flashboxtopdown}

``` { .lua .api-signature }
sm.debugDraw.flashBoxTopDown( min, max, position, rotation?, color?, duration? )
```

Flashes a box for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum extent of the box. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum extent of the box. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position of the box. |
| `rotation` *(optional)* | [Quat](../Userdata/Quat.md) | The rotation of the box. Defaults to identity. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the box. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashCircleTopDown {#flashcircletopdown}

``` { .lua .api-signature }
sm.debugDraw.flashCircleTopDown( center, radius?, color?, duration? )
```

Flashes a circle for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the circle. |
| `radius` *(optional)* | number | The radius of the circle. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the circle. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashRectTopDown {#flashrecttopdown}

``` { .lua .api-signature }
sm.debugDraw.flashRectTopDown( min, max, color?, duration? )
```

Flashes a rectangle for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | [Vec3](../Userdata/Vec3.md) | The minimum extent of the rectangle. |
| `max` | [Vec3](../Userdata/Vec3.md) | The maximum extent of the rectangle. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the rectangle. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashSphere {#flashsphere}

``` { .lua .api-signature }
sm.debugDraw.flashSphere( center, radius?, color?, duration? )
```

Flashes a sphere for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the sphere. |
| `radius` *(optional)* | number | The radius of the sphere. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the sphere. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashSphereTopDown {#flashspheretopdown}

``` { .lua .api-signature }
sm.debugDraw.flashSphereTopDown( center, radius?, color?, duration? )
```

Flashes a sphere for a specified duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the sphere. |
| `radius` *(optional)* | number | The radius of the sphere. Defaults to 0.125. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color of the sphere. Defaults to white. |
| `duration` *(optional)* | number | The duration of the flash animation in seconds. Defaults to 0.5 seconds. |

### flashText {#flashtext}

``` { .lua .api-signature }
sm.debugDraw.flashText( text, position, fade?, scale?, color?, time? )
```

Draws text in world debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `text` | string | The text content. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position of the text. |
| `fade` *(optional)* | boolean | If the text should fade. Defaults to false. |
| `scale` *(optional)* | number | The scale of the text. Defaults to 30. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. Defaults to white. |
| `time` *(optional)* | number | Time to show text. Defaults to 0.5. |

### removeArrow {#removearrow}

``` { .lua .api-signature }
sm.debugDraw.removeArrow( name )
```

Removes a named arrow debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug arrow name. |

### removeBox {#removebox}

``` { .lua .api-signature }
sm.debugDraw.removeBox( name )
```

Removes a named box debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug box name. |

### removeSphere {#removesphere}

``` { .lua .api-signature }
sm.debugDraw.removeSphere( name )
```

Removes a named sphere debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug sphere name. |

### removeText {#removetext}

``` { .lua .api-signature }
sm.debugDraw.removeText( name )
```

Remove text in world debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The text name. |

### removeTransform {#removetransform}

``` { .lua .api-signature }
sm.debugDraw.removeTransform( name )
```

Removes a named transform debug draw.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The debug transform name. |
