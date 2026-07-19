# sm.projectile

Information about projectiles are located in `/Data/Projectiles/ProjectileSets/projectiles.json`.

## Server + Client

<a id="getprojectilemass"></a>
### getProjectileMass(string) {#getprojectilemass-string}

``` { .lua .api-signature }
sm.projectile.getProjectileMass( name )
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Returns the mass of a projectile.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The mass. |

### getProjectileMass(Uuid) {#getprojectilemass-uuid}

``` { .lua .api-signature }
sm.projectile.getProjectileMass( uuid )
```

Returns the mass of a projectile.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The mass. |

### getProjectileRadius {#getprojectileradius}

``` { .lua .api-signature }
sm.projectile.getProjectileRadius( uuid )
```

Returns the radius of a projectile.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The radius. |

<a id="harvestableprojectileattack"></a>
### harvestableProjectileAttack(string, integer, Vec3, Vec3, Harvestable, integer?) {#harvestableprojectileattack-string-integer-vec3-vec3-harvestable-integer-optional}

``` { .lua .api-signature }
sm.projectile.harvestableProjectileAttack(
    name,
    damage,
    position,
    velocity,
    source,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Harvestable](../Userdata/Harvestable.md) | The [Harvestable](../Userdata/Harvestable.md) that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### harvestableProjectileAttack(Uuid, integer, Vec3, Vec3, Harvestable, integer?, number?, integer?) {#harvestableprojectileattack-uuid-integer-vec3-vec3-harvestable-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.harvestableProjectileAttack(
    uuid,
    damage,
    position,
    velocity,
    source,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Harvestable](../Userdata/Harvestable.md) | The [Harvestable](../Userdata/Harvestable.md) that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

<a id="projectileattack"></a>
### projectileAttack(string, integer, Vec3, Vec3, Player, Vec3?, Vec3?, integer?) {#projectileattack-string-integer-vec3-vec3-player-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.projectileAttack(
    name,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### projectileAttack(string, integer, Vec3, Vec3, Unit, Vec3?, Vec3?, integer?) {#projectileattack-string-integer-vec3-vec3-unit-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.projectileAttack(
    name,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Unit](../Userdata/Unit.md) | The Unit that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### projectileAttack(Uuid, integer, Vec3, Vec3, Player, Vec3?, Vec3?, integer?, number?, integer?) {#projectileattack-uuid-integer-vec3-vec3-player-vec3-optional-vec3-optional-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.projectileAttack(
    uuid,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

### projectileAttack(Uuid, integer, Vec3, Vec3, Unit, Vec3?, Vec3?, integer?, number?, integer?) {#projectileattack-uuid-integer-vec3-vec3-unit-vec3-optional-vec3-optional-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.projectileAttack(
    uuid,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Unit](../Userdata/Unit.md) | The Unit that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

<a id="shapeprojectileattack"></a>
### shapeProjectileAttack(string, integer, Vec3, Vec3, Shape, integer?) {#shapeprojectileattack-string-integer-vec3-vec3-shape-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeProjectileAttack(
    name,
    damage,
    position,
    velocity,
    source,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in the shape's local space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Shape](../Userdata/Shape.md) | The shape that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### shapeProjectileAttack(Uuid, integer, Vec3, Vec3, Shape, integer?, number?, integer?) {#shapeprojectileattack-uuid-integer-vec3-vec3-shape-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeProjectileAttack(
    uuid,
    damage,
    position,
    velocity,
    source,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in the shape's local space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Shape](../Userdata/Shape.md) | The shape that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

### solveBallisticArc {#solveballisticarc}

``` { .lua .api-signature }
sm.projectile.solveBallisticArc( firePos, targetPos, velocity, gravity )
```

Calculate the ballistic arc of a projectile. There are two potential solutions to the problem. 

One with a low fire angle and one with a high fire angle. Solutions can be nil if no solution is found.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `firePos` | [Vec3](../Userdata/Vec3.md) | The position the projectile is fired from. |
| `targetPos` | [Vec3](../Userdata/Vec3.md) | The position the projectile should hit. |
| `velocity` | number | The fire velocity of the projectile. |
| `gravity` | number | The gravity ( positive down ). |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md), [Vec3](../Userdata/Vec3.md) | The low angle solution; The high angle solution. |

## Server-only

<a id="customprojectileattack"></a>
### customProjectileAttack(table, string, integer, Vec3, Vec3, Player, Vec3?, Vec3?, integer?) {#customprojectileattack-table-string-integer-vec3-vec3-player-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.customProjectileAttack(
    userdata,
    name,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### customProjectileAttack(table, string, integer, Vec3, Vec3, Unit, Vec3?, Vec3?, integer?) {#customprojectileattack-table-string-integer-vec3-vec3-unit-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.customProjectileAttack(
    userdata,
    name,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Unit](../Userdata/Unit.md) | The Unit that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### customProjectileAttack(table, Uuid, integer, Vec3, Vec3, World, Vec3?, Vec3?, integer?, number?, integer?) {#customprojectileattack-table-uuid-integer-vec3-vec3-world-vec3-optional-vec3-optional-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.customProjectileAttack(
    userdata,
    uuid,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [World](../Userdata/World.md) | The world that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

### customProjectileAttack(table, Uuid, integer, Vec3, Vec3, Player, Vec3?, Vec3?, integer?, number?, integer?) {#customprojectileattack-table-uuid-integer-vec3-vec3-player-vec3-optional-vec3-optional-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.customProjectileAttack(
    userdata,
    uuid,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

### customProjectileAttack(table, Uuid, integer, Vec3, Vec3, Unit, Vec3?, Vec3?, integer?, number?, integer?) {#customprojectileattack-table-uuid-integer-vec3-vec3-unit-vec3-optional-vec3-optional-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.customProjectileAttack(
    userdata,
    uuid,
    damage,
    position,
    velocity,
    source,
    fakePosThird?,
    fakePosFirst?,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Unit](../Userdata/Unit.md) | The Unit that is the source of the projectile. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

<a id="harvestablecustomprojectileattack"></a>
### harvestableCustomProjectileAttack(table, string, integer, Vec3, Vec3, Harvestable, integer?) {#harvestablecustomprojectileattack-table-string-integer-vec3-vec3-harvestable-integer-optional}

``` { .lua .api-signature }
sm.projectile.harvestableCustomProjectileAttack(
    userdata,
    name,
    damage,
    position,
    velocity,
    source,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Harvestable](../Userdata/Harvestable.md) | The harvestable that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### harvestableCustomProjectileAttack(table, Uuid, integer, Vec3, Vec3, Harvestable, integer?, number?, integer?) {#harvestablecustomprojectileattack-table-uuid-integer-vec3-vec3-harvestable-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.harvestableCustomProjectileAttack(
    userdata,
    uuid,
    damage,
    position,
    velocity,
    source,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in world space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Harvestable](../Userdata/Harvestable.md) | The harvestable that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

<a id="shapecustomprojectileattack"></a>
### shapeCustomProjectileAttack(table, string, integer, Vec3, Vec3, Shape, integer?) {#shapecustomprojectileattack-table-string-integer-vec3-vec3-shape-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeCustomProjectileAttack(
    userdata,
    name,
    damage,
    position,
    velocity,
    source,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `name` | string | The projectile's name. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in the shape's local space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Shape](../Userdata/Shape.md) | The shape that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### shapeCustomProjectileAttack(table, Uuid, integer, Vec3, Vec3, Shape, integer?, number?, integer?) {#shapecustomprojectileattack-table-uuid-integer-vec3-vec3-shape-integer-optional-number-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeCustomProjectileAttack(
    userdata,
    uuid,
    damage,
    position,
    velocity,
    source,
    delay?,
    acceleration?,
    lifetime?
)
```

Perform a customized projectile attack

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `userdata` | table | The custom user data |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `damage` | integer | The damage the projectile will inflict. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position in the shape's local space. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `source` | [Shape](../Userdata/Shape.md) | The shape that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `acceleration` *(optional)* | number | The acceleration of the projectile. (Defaults to 0) |
| `lifetime` *(optional)* | integer | The max lifetime of the projectile in ticks. (Defaults to 400) |

<a id="shapefire"></a>
### shapeFire(Shape, string, Vec3, Vec3, integer?) {#shapefire-shape-string-vec3-vec3-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeFire( shape, name, position, velocity, delay? )
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Creates and fires a projectile from a [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The shape. |
| `name` | string | The projectile's name. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### shapeFire(Shape, Uuid, Vec3, Vec3, integer?, integer?) {#shapefire-shape-uuid-vec3-vec3-integer-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.shapeFire(
    shape,
    uuid,
    position,
    velocity,
    delay?,
    projectileAmount?
)
```

Creates and fires a projectile from a [Shape](../Userdata/Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](../Userdata/Shape.md) | The shape. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |
| `projectileAmount` *(optional)* | integer | The amount of shots that will be fired. Uses projectile amount from json if not set (Optional, range of 0-255) |

## Client-only

<a id="playerfire"></a>
### playerFire(string, Vec3, Vec3, Vec3?, Vec3?, integer?) {#playerfire-string-vec3-vec3-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.playerFire(
    name,
    position,
    velocity,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

> **Deprecated:**
> Name is deprecated, use uuid instead
>

Creates and fires a projectile from a player.

The projectile is normally fired from the player's position, but due to the weapon being held off-center it may require a fake position for where the projectile appears to be fired from.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The projectile's name. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

### playerFire(Uuid, Vec3, Vec3, Vec3?, Vec3?, integer?) {#playerfire-uuid-vec3-vec3-vec3-optional-vec3-optional-integer-optional}

``` { .lua .api-signature }
sm.projectile.playerFire(
    uuid,
    position,
    velocity,
    fakePosThird?,
    fakePosFirst?,
    delay?
)
```

Creates and fires a projectile from a player.

The projectile is normally fired from the player's position, but due to the weapon being held off-center it may require a fake position for where the projectile appears to be fired from.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The projectile's uuid. |
| `position` | [Vec3](../Userdata/Vec3.md) | The start position. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The direction and velocity. |
| `fakePosThird` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in third-person. (Defaults to position) |
| `fakePosFirst` *(optional)* | [Vec3](../Userdata/Vec3.md) | The visual start position in first-person. (Defaults to position) |
| `delay` *(optional)* | integer | The number of ticks before firing. (Defaults to 0) |

<a id="removeprojectileswithsource"></a>
### removeProjectilesWithSource(World, integer?) {#removeprojectileswithsource-world-integer-optional}

``` { .lua .api-signature }
sm.projectile.removeProjectilesWithSource( source, delay? )
```

Removes projectiles created by a given source. The source world must exist.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `source` | [World](../Userdata/World.md) | The world that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before destroying the projectile. (Defaults to 0) |

### removeProjectilesWithSource(Player, integer?) {#removeprojectileswithsource-player-integer-optional}

``` { .lua .api-signature }
sm.projectile.removeProjectilesWithSource( source, delay? )
```

Removes projectiles created by a given source. The source player must exist.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `source` | [Player](../Userdata/Player.md) | The player that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before destroying the projectile. (Defaults to 0) |

### removeProjectilesWithSource(Character, integer?, World?) {#removeprojectileswithsource-character-integer-optional-world-optional}

``` { .lua .api-signature }
sm.projectile.removeProjectilesWithSource( source, delay?, world? )
```

Removes projectiles created by a given character source. Can remove projectiles from a source that doesn't exist, in this case a world to remove from is required.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `source` | [Character](../Userdata/Character.md) | The Character that is the source of the projectile. |
| `delay` *(optional)* | integer | The number of ticks before destroying the projectile. (Defaults to 0) |
| `world` *(optional)* | [World](../Userdata/World.md) | The world the projectiles should be removed from. (Defaults to same world as source.) |
