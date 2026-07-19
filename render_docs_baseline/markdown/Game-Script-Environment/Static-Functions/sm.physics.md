# sm.physics

Contains functions regarding the physics engine.

## Constants

### filter {#filter}

Collision filter types

| Value |
| --- |
| dynamicBody |
| staticBody |
| character |
| areaTrigger |
| joints |
| terrainSurface |
| terrainAsset |
| harvestable |
| areaTrigger |
| static |
| default |
| all |
| allTerrain |

**Returns:**

| Type | Description |
| --- | --- |
| table | The physics types list. |

### types {#types}

Physics types are used to define an object's characteristics is in the physics world. Upon a raycast or collision detection, these types are used to find out what object was intersected.

| Value | Description |
| --- | --- |
| "invalid" | No object. |
| "terrainSurface" | The ground. |
| "terrainAsset" | Trees and boulders. |
| "lift" | A [Lift](../Userdata/Lift.md). |
| "body" | A [Body](../Userdata/Body.md). |
| "character" | A [Character](../Userdata/Character.md). |
| "joint" | A [Joint](../Userdata/Joint.md). |
| "harvestable" | A [Harvestable](../Userdata/Harvestable.md). |
| "vision" | A collision area used by sensors. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The physics types list. |

## Server + Client

<a id="applyimpulse"></a>
### applyImpulse(Shape, Vec3, boolean?, Vec3?) {#applyimpulse-shape-vec3-boolean-optional-vec3-optional}

``` { .lua .api-signature }
sm.physics.applyImpulse( target, impulse, worldSpace?, offset? )
```

Applies an impulse to a [Shape](../Userdata/Shape.md), changing its velocity immediately. The impulse is applied to the shape's centerpoint with an optional offset.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `target` | [Shape](../Userdata/Shape.md) | The object on which the impulse is exerted on. |
| `impulse` | [Vec3](../Userdata/Vec3.md) | The direction and strength of the impulse. |
| `worldSpace` *(optional)* | boolean | Whether the impulse is applied in world space coordinates. (Defaults to local rotation) |
| `offset` *(optional)* | [Vec3](../Userdata/Vec3.md) | The offset from the center point. (Defaults to no offset) |

### applyImpulse(Body, Vec3, boolean?, Vec3?) {#applyimpulse-body-vec3-boolean-optional-vec3-optional}

``` { .lua .api-signature }
sm.physics.applyImpulse( target, impulse, worldSpace?, offset? )
```

Applies an impulse to a [Body](../Userdata/Body.md), changing its velocity immediately. The impulse is applied to the body's center of mass with an optional offset.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `target` | [Body](../Userdata/Body.md) | The object on which the impulse is exerted on. |
| `impulse` | [Vec3](../Userdata/Vec3.md) | The direction and strength of the impulse. |
| `worldSpace` *(optional)* | boolean | Whether the impulse is applied in world space coordinates. (Defaults to local rotation) |
| `offset` *(optional)* | [Vec3](../Userdata/Vec3.md) | The offset from the center point. (Defaults to no offset) |

### applyImpulse(Character, Vec3) {#applyimpulse-character-vec3}

``` { .lua .api-signature }
sm.physics.applyImpulse( target, impulse )
```

Applies an impulse to a [Character](../Userdata/Character.md), changing its velocity immediately. The impulse is applied to the character's centerpoint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `target` | [Character](../Userdata/Character.md) | The character on which the impulse is exerted on. |
| `impulse` | [Vec3](../Userdata/Vec3.md) | The direction and strength of the impulse. |

### applyTorque {#applytorque}

``` { .lua .api-signature }
sm.physics.applyTorque( target, torque, worldSpace? )
```

Applies a torque impulse to a [Body](../Userdata/Body.md), changing its angular velocity immediately. The torque is applied along the body's center of mass, making it rotate.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `target` | [Body](../Userdata/Body.md) | The object on which the torque is exerted on. |
| `torque` | [Vec3](../Userdata/Vec3.md) | The direction and strength of the torque. |
| `worldSpace` *(optional)* | boolean | Whether the torque is applied in world space coordinates. (Defaults to local rotation) |

### capsuleContactCount {#capsulecontactcount}

``` { .lua .api-signature }
sm.physics.capsuleContactCount( from, to, radius, mask? )
```

Returns the number of collision objects that are found inside a given capsule.

The capsule is formed by connecting two spheres.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [Vec3](../Userdata/Vec3.md) | The world position of the first sphere. |
| `to` | [Vec3](../Userdata/Vec3.md) | The world position of the second sphere. |
| `radius` | number | The radius of the spheres. |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of objects. |

### capsuleHasContact {#capsulehascontact}

``` { .lua .api-signature }
sm.physics.capsuleHasContact( from, to, radius, mask? )
```

Returns true if any collision object is found inside a given capsule.

Faster than capsuleContactCount when only checking for existence.

The capsule is formed by connecting two spheres.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `from` | [Vec3](../Userdata/Vec3.md) | The world position of the first sphere. |
| `to` | [Vec3](../Userdata/Vec3.md) | The world position of the second sphere. |
| `radius` | number | The radius of the spheres. |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if any contact was found. |

### capsulecast {#capsulecast}

``` { .lua .api-signature }
sm.physics.capsulecast(
    start,
    end,
    radius,
    height,
    ignore?,
    mask?,
    world?,
    ignoreUuids?
)
```

Performs a capsule <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">ray cast</a> (Z-axis aligned) between two positions.

The returned [RaycastResult](../Userdata/RaycastResult.md) contains information about any object intersected by the ray.

If the ray cast is called from within a shape (e.g. a Sensor), a [Body](../Userdata/Body.md) may be provided which the ray will not intersect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `end` | [Vec3](../Userdata/Vec3.md) | The end position. |
| `radius` | number | The radius of the capsule. |
| `height` | number | The height of the cylindrical part of the capsule. |
| `ignore` *(optional)* | [Body](../Userdata/Body.md)\|[Shape](../Userdata/Shape.md)\|[Harvestable](../Userdata/Harvestable.md)\|[Character](../Userdata/Character.md)\|[AreaTrigger](../Userdata/AreaTrigger.md) | An object to be ignored. (Optional) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter) (Optional) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to perform the cast in. (Optional) |
| `ignoreUuids` *(optional)* | table | A table of uuids {[Uuid](../Userdata/Uuid.md), ...} of [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or [Character](../Userdata/Character.md) type to be ignored. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,	[RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; The raycast result data. |

### distanceRaycast {#distanceraycast}

``` { .lua .api-signature }
sm.physics.distanceRaycast( start, direction )
```

Performs a distance <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">ray cast</a> from a position with a given direction.

> **Note:**
> [sm.physics.distanceRaycast](#distanceraycast) is generally cheaper to use than [sm.physics.raycast](#raycast) as it performs collision checks in a simplified world. If the raycast is only used for checking collision, it is advised to use this method instead.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The ray's direction and length. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean, number | 2 values: whether raycast was successful; the fraction (0&ndash;1) of the distance reached until collision divided by the ray's length. |

### getBoxContacts {#getboxcontacts}

``` { .lua .api-signature }
sm.physics.getBoxContacts( pos, rotation, halfExtents, world, mask? )
```

Returns a table of the game objects that are found inside the given box

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `pos` | [Vec3](../Userdata/Vec3.md) | The world position of the box center. |
| `rotation` | [Quat](../Userdata/Quat.md) | The rotation of the box. |
| `halfExtents` | [Vec3](../Userdata/Vec3.md) | The half extents of the box. |
| `world` | [World](../Userdata/World.md) | The world to search in. (optional) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.static](#filter) and [sm.physics.filter.dynamicBody](#filter) and [sm.physics.filter.character](#filter) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table with tables of objects found inside the box. { bodies={[Body](../Userdata/Body.md), ..}, characters={[Character](../Userdata/Character.md), ..}, harvestables={[Harvestable](../Userdata/Harvestable.md), ..}, lifts={[Lift](../Userdata/Lift.md), ..} } |

### getGroundMaterial {#getgroundmaterial}

``` { .lua .api-signature }
sm.physics.getGroundMaterial( worldPosition )
```

Returns the material at the given position in the terrain.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | The world position to check the material at. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The material name. |

### getMaterialId {#getmaterialid}

``` { .lua .api-signature }
sm.physics.getMaterialId( materialName )
```

Returns the material id from name

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `materialName` | string | Material name. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The id of the material. |

### getShapeContactsInBox {#getshapecontactsinbox}

``` { .lua .api-signature }
sm.physics.getShapeContactsInBox( position, rotation, halfExtents, world )
```

Returns a table of all shapes colliding with a given box.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The center position of the box. |
| `rotation` | [Quat](../Userdata/Quat.md) | The rotation of the box. |
| `halfExtents` | [Vec3](../Userdata/Vec3.md) | The halved size of the box. |
| `world` | [World](../Userdata/World.md) | The world to search in. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of found shapes. {{shape=[Shape](../Userdata/Shape.md), contactWorldPosition=[Vec3](../Userdata/Vec3.md) }, ..} |

### getShapeContactsInSphere {#getshapecontactsinsphere}

``` { .lua .api-signature }
sm.physics.getShapeContactsInSphere( center, radius, world )
```

Returns a table of all shapes colliding with a given sphere.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `center` | [Vec3](../Userdata/Vec3.md) | The center position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `world` | [World](../Userdata/World.md) | The world to search in. (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of found shapes. {{shape=[Shape](../Userdata/Shape.md), contactWorldPosition=[Vec3](../Userdata/Vec3.md) }, ..} |

### getSphereContacts {#getspherecontacts}

``` { .lua .api-signature }
sm.physics.getSphereContacts( pos, radius, world?, mask? )
```

Returns a table of the game objects that are found inside the given sphere

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `pos` | [Vec3](../Userdata/Vec3.md) | The world position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to search in. Defaults to current world (Optional) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.static](#filter) and [sm.physics.filter.dynamicBody](#filter) and [sm.physics.filter.character](#filter) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table with tables of objects found inside the sphere. { bodies={[Body](../Userdata/Body.md), ..}, characters={[Character](../Userdata/Character.md), ..}, harvestables={[Harvestable](../Userdata/Harvestable.md), ..}, lifts={[Lift](../Userdata/Lift.md), ..} } |

### isPointInLiquid {#ispointinliquid}

``` { .lua .api-signature }
sm.physics.isPointInLiquid( position, world? )
```

Returns whether a point is in a liquid or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position to check. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to check in. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the point is inside liquid or not |

### isSphereHittingLiquid {#isspherehittingliquid}

``` { .lua .api-signature }
sm.physics.isSphereHittingLiquid( position, world?, radius )
```

Returns whether a sphere is hitting a liquid or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position to check. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to check in. |
| `radius` | number | The radius of the sphere. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the sphere is hitting a liquid or not |

### multicast {#multicast}

``` { .lua .api-signature }
sm.physics.multicast( casts, world? )
```

Performs multiple sphere and/or raycasts given a table of parameters.

Type can be "sphere" or "ray". Radius is ignored for rays.

ignoreUuids option is a table of uuids {[Uuid](../Userdata/Uuid.md), ...} of [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or [Character](../Userdata/Character.md) type to be ignored.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `casts` | table | Table of casts. { type=string, startPoint=[Vec3](../Userdata/Vec3.md), endPoint=[Vec3](../Userdata/Vec3.md), radius=number, mask=[sm.physics.filter](#filter), ignoreUuids=table } |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to perform the cast in. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Array of pairs of boolean and [RaycastResult](../Userdata/RaycastResult.md). {{boolean,  [RaycastResult](../Userdata/RaycastResult.md)}, ..} |

### raycast {#raycast}

``` { .lua .api-signature }
sm.physics.raycast( start, end, body?, mask?, world?, ignoreUuids? )
```

Performs a <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">ray cast</a> between two positions.

The returned [RaycastResult](../Userdata/RaycastResult.md) contains information about any object intersected by the ray.

If the ray cast is called from within a shape (e.g. a Sensor), a [Body](../Userdata/Body.md) may be provided which the ray will not intersect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `end` | [Vec3](../Userdata/Vec3.md) | The end position. |
| `body` *(optional)* | [Body](../Userdata/Body.md) | The body to be ignored. (Optional) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter) (Optional) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to perform the raycast in. (Optional) |
| `ignoreUuids` *(optional)* | table | A table of uuids {[Uuid](../Userdata/Uuid.md), ...} of [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or [Character](../Userdata/Character.md) type to be ignored. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,	[RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; The raycast result data. |

### raycastTarget {#raycasttarget}

``` { .lua .api-signature }
sm.physics.raycastTarget( start, end, body, world?, ignoreUuids? )
```

Performs a <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">ray cast</a> between two positions to find a specific target.

a [Body](../Userdata/Body.md) must be provided as a target.

The returned [RaycastResult](../Userdata/RaycastResult.md) contains information about any object intersected by the ray.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `end` | [Vec3](../Userdata/Vec3.md) | The end position. |
| `body` | [Body](../Userdata/Body.md) | The body to be exclusively checked. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to perform the raycast in. (Optional) |
| `ignoreUuids` *(optional)* | table | A table of uuids {[Uuid](../Userdata/Uuid.md), ...} of [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or [Character](../Userdata/Character.md) type to be ignored. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,	[RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; The raycast result data. |

### sphereContactCount {#spherecontactcount}

``` { .lua .api-signature }
sm.physics.sphereContactCount(
    worldPosition,
    radius,
    includeTerrain?,
    countWater?,
    mask?
)
```

Returns the number of collision objects that are found inside the given sphere

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | The world position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `includeTerrain` *(optional)* | boolean | True if terrain should be included in the test (Defaults to false) |
| `countWater` *(optional)* | boolean | True if water should be included (Defaults to false) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter). Using this will override "includeTerrain" and "countWater". (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of objects. |

### sphereHasContact {#spherehascontact}

``` { .lua .api-signature }
sm.physics.sphereHasContact(
    worldPosition,
    radius,
    includeTerrain?,
    countWater?,
    mask?
)
```

Returns true if any collision object is found inside the given sphere.

Faster than sphereContactCount when only checking for existence.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | The world position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `includeTerrain` *(optional)* | boolean | True if terrain should be included in the test (Defaults to false) |
| `countWater` *(optional)* | boolean | True if water should be included (Defaults to false) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter). Using this will override "includeTerrain" and "countWater". (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if any contact was found. |

### spherecast {#spherecast}

``` { .lua .api-signature }
sm.physics.spherecast(
    start,
    end,
    radius,
    ignore?,
    mask?,
    world?,
    ignoreUuids?
)
```

Performs a spherical <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">ray cast</a> between two positions.

The returned [RaycastResult](../Userdata/RaycastResult.md) contains information about any object intersected by the ray.

If the ray cast is called from within a shape (e.g. a Sensor), a [Body](../Userdata/Body.md) may be provided which the ray will not intersect.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `start` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `end` | [Vec3](../Userdata/Vec3.md) | The end position. |
| `radius` | number | The radius of the sphere. |
| `ignore` *(optional)* | [Body](../Userdata/Body.md)\|[Shape](../Userdata/Shape.md)\|[Harvestable](../Userdata/Harvestable.md)\|[Character](../Userdata/Character.md)\|[AreaTrigger](../Userdata/AreaTrigger.md) | An object to be ignored. (Optional) |
| `mask` *(optional)* | integer | The collision mask. Defaults to [sm.physics.filter.default](#filter) (Optional) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to perform the cast in. (Optional) |
| `ignoreUuids` *(optional)* | table | A table of uuids {[Uuid](../Userdata/Uuid.md), ...} of [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or [Character](../Userdata/Character.md) type to be ignored. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean,	[RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; The raycast result data. |

## Server-only

### explode {#explode}

``` { .lua .api-signature }
sm.physics.explode(
    position,
    level,
    destructionRadius,
    impulseRadius,
    magnitude,
    effectName?,
    ignoreShape?,
    parameters?,
    world?,
    damage?,
    source?,
    type?
)
```

Creates an explosion at given position. The explosion creates a shockwave that is capable of destroying blocks and pushing characters and creations away.

Shapes that are within the explosion's destruction radius may receive the event [server_onExplosionHit](../Classes/ShapeClass.md#server_onexplosion).

> **Note:**
> The <strong>destruction level</strong> is the damage effect on blocks and parts, determining how likely it is that they are destroyed. This is related to the `qualityLevel` found in parts json-files.
> Any quality level equal to or less than the destruction level may be destroyed. The effect fades one level every half travelled of the remaining destruction radius.
> A quality level of 0 means a block or part is indestructible.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The center point of the explosion. |
| `level` | integer | The destruction level affecting nearby objects. |
| `destructionRadius` | number | The destruction radius. Objects inside this sphere may be destroyed. |
| `impulseRadius` | number | The impulse radius. Objects inside this sphere are affected by an [impulse](#applyimpulse). |
| `magnitude` | number | The impulse strength of the explosion. The strength diminishes with distance. |
| `effectName` *(optional)* | string | The name of the effect to be played upon explosion. (Optional) |
| `ignoreShape` *(optional)* | [Shape](../Userdata/Shape.md) | The shape to be ignored. (Optional) |
| `parameters` *(optional)* | table | The table containing the parameters for the effect. (Optional) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world to cause the explosion in. (Optional) |
| `damage` *(optional)* | integer | The damage of the explosion. Defaults to 2 * destruction level (Optional) |
| `source` *(optional)* | userdata | The source of the explosion. Defaults to none (Optional) |
| `type` *(optional)* | [Uuid](../Userdata/Uuid.md) | The explosionType. Defaults to nil uuid (Optional) |

### getGravity {#getgravity}

``` { .lua .api-signature }
sm.physics.getGravity(  )
```

Returns the gravitational acceleration affecting [shapes](../Userdata/Shape.md) and [bodies](../Userdata/Body.md).

**Returns:**

| Type | Description |
| --- | --- |
| number | The gravitational value. |

### setGravity {#setgravity}

``` { .lua .api-signature }
sm.physics.setGravity( gravity )
```

Sets the gravitational acceleration affecting [shapes](../Userdata/Shape.md) and [bodies](../Userdata/Body.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gravity` | number | The gravitational value. |
