# sm.debris

<strong>Debris</strong> are visual objects that have no impact on any other object.

## Client-only

### createBlackHole {#createblackhole}

``` { .lua .api-signature }
sm.debris.createBlackHole(
    position,
    radius?,
    force?,
    position2?,
    wanderForce?,
    dissolveRadius?,
    timeToLive?,
    channel?
)
```

Add a black hole that attracts nearby debris towards its position.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The position of the black hole. |
| `radius` *(optional)* | number | The radius of effect. (Defaults to 10) |
| `force` *(optional)* | number | The attraction force. (Defaults to 100) |
| `position2` *(optional)* | [Vec3](../Userdata/Vec3.md) | An optional secondary position, making the black hole a capsule shape instead of a sphere. |
| `wanderForce` *(optional)* | number | A force applied along direction from position to position2. (Defaults to 0) |
| `dissolveRadius` *(optional)* | number | The radius within which debris will start to dissolve. (Defaults to 0) |
| `timeToLive` *(optional)* | number | The time the black hole will be simulated before disappearing. (Defaults to one tick) |
| `channel` *(optional)* | number | The channel this black hole affects. Debris only reacts to black holes matching its channel. 0 means no debris is affected. (Defaults to 1) |

### createDebris {#createdebris}

``` { .lua .api-signature }
sm.debris.createDebris(
    uuid,
    position,
    rotation,
    velocity?,
    angularVelocity?,
    color?,
    timeToLive?,
    gravity?,
    friction?,
    linearDamping?,
    angularDamping?,
    time?
)
```

Create visual debris of a [shape](../Userdata/Shape.md) from its [uuid](../Userdata/Uuid.md), that collides with world objects but does not have an impact on them.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the shape. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position. |
| `rotation` | [Quat](../Userdata/Quat.md) | The rotation. |
| `velocity` *(optional)* | [Vec3](../Userdata/Vec3.md) | The linear velocity. (Defaults to zero) |
| `angularVelocity` *(optional)* | [Vec3](../Userdata/Vec3.md) | The angular velocity in radians per second around the axes (x,y,z). (Defaults to zero) |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color. (Defaults to the shape's default color) |
| `timeToLive` *(optional)* | number | Time to live. (Defaults to 10) |
| `gravity` *(optional)* | number | Gravity vector. (Defaults to { 0,0,-10 }) |
| `friction` *(optional)* | number | Amount of friction. (Defaults to 1) |
| `linearDamping` *(optional)* | number | Amount of linear damping. (Defaults to 0.3) |
| `angularDamping` *(optional)* | number | Amount of angular damping. (Defaults to 0.3) |
| `time` *(optional)* | number | The time the debris will be simulated before disappearing. (Defaults to 10 seconds) |
