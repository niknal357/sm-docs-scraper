# Body

**Associated namespace:** [sm.body](../Static-Functions/sm.body.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>body</strong> in the game.

**Values:**

- <a id="angularvelocity"></a>`angularVelocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the angular velocity of a body.

- <a id="buildable"></a>`buildable` [ **boolean** ] <br>
    - `Get`: Check if a body is buildable
    - `Set`: (Server-Only) Controls whether a body is buildable

- <a id="centerofmassposition"></a>`centerOfMassPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the center of mass world position of a body.

- <a id="connectable"></a>`connectable` [ **boolean** ] <br>
    - `Get`: Check if a body is connectable
    - `Set`: (Server-Only) Controls whether a body is connectable

- <a id="convertabletodynamic"></a>`convertableToDynamic` [ **boolean** ] <br>
    - `Get`: Check if a body is convertible to dynamic form
    - `Set`: (Server-Only) Controls whether a body is convertible to dynamic form

- <a id="destructable"></a>`destructable` [ **boolean** ] <br>
    - `Get`: Check if a body is destructable.
    - `Set`: (Server-Only) Controls whether a body is destructable

- <a id="erasable"></a>`erasable` [ **boolean** ] <br>
    - `Get`: Check if a body is erasable.
    - `Set`: (Server-Only) Controls whether a body is erasable

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a body.

- <a id="liftable"></a>`liftable` [ **boolean** ] <br>
    - `Get`: Check if a body is liftable
    - `Set`: (Server-Only) Controls whether a body is liftable

- <a id="mass"></a>`mass` [ **number** ] <br>
    - `Get`: Returns the mass of a body.

- <a id="paintable"></a>`paintable` [ **boolean** ] <br>
    - `Get`: Check if a body is paintable
    - `Set`: (Server-Only) Controls whether a body is non paintable

- <a id="usable"></a>`usable` [ **boolean** ] <br>
    - `Get`: Check if a body is interactable
    - `Set`: (Server-Only) Controls whether a body is interactable

- <a id="velocity"></a>`velocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the linear velocity of a body.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of a body.

- <a id="worldrotation"></a>`worldRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the world rotation of a body.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Body == Body` | boolean | Checks if two instances of [Body](Body.md) refer to the same Body. |

## Server + Client

### getAngularVelocity {#getangularvelocity}

``` { .lua .api-signature }
body:getAngularVelocity(  )
```

Returns the angular velocity of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The body's angular velocity. |

### getCenterOfMassPosition {#getcenterofmassposition}

``` { .lua .api-signature }
body:getCenterOfMassPosition(  )
```

Returns the center of mass world position of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The body's center of mass world position. |

### getCreationBodies {#getcreationbodies}

``` { .lua .api-signature }
body:getCreationBodies(  )
```

Returns a table of all bodies in a creation.

A creation includes all bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | An array table of all bodies in a creation. {[Body](Body.md), ...} |

### getCreationId {#getcreationid}

``` { .lua .api-signature }
body:getCreationId(  )
```

Returns the local id of the creation

> **Note:**
> Server and client ids will not match

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The creation's local id |

### getCreationJoints {#getcreationjoints}

``` { .lua .api-signature }
body:getCreationJoints(  )
```

Returns a table of all [joints](Joint.md) that are part of a creation.

A creation includes all bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of joints in a creation. {[Joint](Joint.md), ...} |

### getCreationShapes {#getcreationshapes}

``` { .lua .api-signature }
body:getCreationShapes(  )
```

Returns a table of all [shapes](Shape.md) that are part of a creation.

A creation includes all bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of shapes in a creation. {[Shape](Shape.md), ...} |

### getId {#getid}

``` { .lua .api-signature }
body:getId(  )
```

Returns the id of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The body's id. |

### getInteractables {#getinteractables}

``` { .lua .api-signature }
body:getInteractables(  )
```

Returns a table of all [interactables](Interactable.md) that are part of a body.

This will <strong>not</strong> return interactables in neighbouring bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of interactables in a body. {[Interactable](Interactable.md), ...} |

### getJoints {#getjoints}

``` { .lua .api-signature }
body:getJoints(  )
```

Returns a table of all [joints](Joint.md) that are part of a body.

This will <strong>not</strong> return joints in neighbouring bodies.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of joints in a body. {[Joint](Joint.md), ...} |

### getLocalAabb {#getlocalaabb}

``` { .lua .api-signature }
body:getLocalAabb(  )
```

Get the local aabb of the body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | Returns the aabb min and max. |

### getMass {#getmass}

``` { .lua .api-signature }
body:getMass(  )
```

Returns the mass of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The body's mass. |

### getShape {#getshape}

``` { .lua .api-signature }
body:getShape( index )
```

Returns a shape that is part of a body by index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `index` | integer | The index of the shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The shape at the specified index, or nil if the index is out of range. |

### getShapeCount {#getshapecount}

``` { .lua .api-signature }
body:getShapeCount(  )
```

Returns the number of shapes in a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of shapes in the body. |

### getShapes {#getshapes}

``` { .lua .api-signature }
body:getShapes(  )
```

Returns a table of all [shapes](Shape.md) that are part of a body.

This will <strong>not</strong> return shapes in neighbouring bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of shapes in a body. {[Shape](Shape.md), ...} |

### getShapesByUuid {#getshapesbyuuid}

``` { .lua .api-signature }
body:getShapesByUuid( uuid )
```

Returns a table of all [shapes](Shape.md) that are part of a body and have a specified uuid.

This will <strong>not</strong> return shapes in neighbouring bodies connected by [joints](Joint.md), etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `uuid` | [Uuid](Uuid.md) | The uuid to look for. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of shapes in a body. {[Shape](Shape.md), ...} |

### getVelocity {#getvelocity}

``` { .lua .api-signature }
body:getVelocity(  )
```

Returns the linear velocity of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The body's linear velocity. |

### getWorld {#getworld}

``` { .lua .api-signature }
body:getWorld(  )
```

Returns the world a body exists in.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The world the body exists in. |

### getWorldAabb {#getworldaabb}

``` { .lua .api-signature }
body:getWorldAabb(  )
```

Get the world aabb of the body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | Returns the aabb min and max. |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
body:getWorldPosition(  )
```

Returns the world position of a body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The body's world position. |

### hasChanged {#haschanged}

``` { .lua .api-signature }
body:hasChanged( tick )
```

Returns true if the given tick is lower than the tick the body was last changed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `tick` | integer | The tick. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the body has been changed. |

### isBuildable {#isbuildable}

``` { .lua .api-signature }
body:isBuildable(  )
```

Check if a body is buildable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is buildable. |

### isConnectable {#isconnectable}

``` { .lua .api-signature }
body:isConnectable(  )
```

Check if a body is connectable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is connectable. |

### isConvertibleToDynamic {#isconvertibletodynamic}

``` { .lua .api-signature }
body:isConvertibleToDynamic(  )
```

Check if a body is convertible to dynamic form

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body can be converted to dynamic. |

### isDestructable {#isdestructable}

``` { .lua .api-signature }
body:isDestructable(  )
```

Check if a body is destructable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is destructable. |

### isDynamic {#isdynamic}

``` { .lua .api-signature }
body:isDynamic(  )
```

Check if a body is dynamic

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is dynamic. |

### isErasable {#iserasable}

``` { .lua .api-signature }
body:isErasable(  )
```

Check if a body is erasable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is erasable. |

### isGhost {#isghost}

``` { .lua .api-signature }
body:isGhost(  )
```

Check if the body is a ghost body.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the body is a ghost body. |

### isLiftable {#isliftable}

``` { .lua .api-signature }
body:isLiftable(  )
```

Check if a body is liftable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is liftable. |

### isOnLift {#isonlift}

``` { .lua .api-signature }
body:isOnLift(  )
```

Check if a body is on a lift

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is on a lift |

### isOnVirtualLift {#isonvirtuallift}

``` { .lua .api-signature }
body:isOnVirtualLift(  )
```

Check if a body is on a virtual lift

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is on a lift |

### isPaintable {#ispaintable}

``` { .lua .api-signature }
body:isPaintable(  )
```

Check if a body is paintable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is paintable. |

### isStatic {#isstatic}

``` { .lua .api-signature }
body:isStatic(  )
```

Check if a body is static

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is static. |

### isUsable {#isusable}

``` { .lua .api-signature }
body:isUsable(  )
```

Check if a body is interactable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the body is interactable. |

### transformLocalPoint {#transformlocalpoint}

``` { .lua .api-signature }
body:transformLocalPoint( point )
```

Transforms a point from local space to world space.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `point` | [Vec3](Vec3.md) | The point in local space. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The point in world space. |

### transformPoint {#transformpoint}

``` { .lua .api-signature }
body:transformPoint( point )
```

Transforms a point from local space to world space.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `point` | [Vec3](Vec3.md) | The point in local space. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The point in world space. |

### transformWorldPoint {#transformworldpoint}

``` { .lua .api-signature }
body:transformWorldPoint( point )
```

Transforms a point from world space to local space.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `point` | [Vec3](Vec3.md) | The point in world space. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The point in local space. |

## Server-only

### createBlock {#createblock}

``` { .lua .api-signature }
body:createBlock( uuid, size, position, forceAccept? )
```

Create a block on body

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The parent body. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the shape. |
| `size` | [Vec3](Vec3.md) | The shape's size. |
| `position` | [Vec3](Vec3.md) | The shape's local position. |
| `forceAccept` *(optional)* | boolean | Set true to force the body to accept the shape. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The created block |

### createPart {#createpart}

``` { .lua .api-signature }
body:createPart( uuid, position, z-axis, x-axis, forceAccept? )
```

Create a part on body

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The parent body. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the shape. |
| `position` | [Vec3](Vec3.md) | The shape's local position. |
| `z-axis` | [Vec3](Vec3.md) | The shape's local z direction. |
| `x-axis` | [Vec3](Vec3.md) | The shape's local x direction. |
| `forceAccept` *(optional)* | boolean | Set true to force the body to accept the shape. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The created part |

### createWedge {#createwedge}

``` { .lua .api-signature }
body:createWedge( uuid, size, position, z-axis, x-axis, forceAccept? )
```

Creates a wedge attached to a body. The wedge is oriented with one 

cathetus along the Y-axis and the other along the Z-axis, forming a right angle. The wedge's 

rotation is controlled by z-axis and x-axis parameters, similar to standard part rotation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The parent body. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the shape. |
| `size` | [Vec3](Vec3.md) | The shape's size. |
| `position` | [Vec3](Vec3.md) | The shape's local position. |
| `z-axis` | [Vec3](Vec3.md) | The shape's local z direction. |
| `x-axis` | [Vec3](Vec3.md) | The shape's local x direction. |
| `forceAccept` *(optional)* | boolean | Set true to force the body to accept the shape. (Defaults to true) |

### destroyCreation {#destroycreation}

``` { .lua .api-signature }
body:destroyCreation(  )
```

Destroys the entire creation connected to this body

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

### getAllSeatedCharacter {#getallseatedcharacter}

``` { .lua .api-signature }
body:getAllSeatedCharacter(  )
```

Returns a table with all characters seated in this body

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of all seated characters. {[Character](Character.md), ...} |

### setBuildable {#setbuildable}

``` { .lua .api-signature }
body:setBuildable( value )
```

Controls whether a body is buildable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is buildable. |

### setConnectable {#setconnectable}

``` { .lua .api-signature }
body:setConnectable( value )
```

Controls whether a body is connectable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is connectable. |

### setConvertibleToDynamic {#setconvertibletodynamic}

``` { .lua .api-signature }
body:setConvertibleToDynamic( value )
```

Controls whether a body is convertible to dynamic form

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is convertible to dynamic form. |

### setDestructable {#setdestructable}

``` { .lua .api-signature }
body:setDestructable( value )
```

Controls whether a body is destructable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is destructable. |

### setErasable {#seterasable}

``` { .lua .api-signature }
body:setErasable( value )
```

Controls whether a body is erasable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is erasable. |

### setLiftable {#setliftable}

``` { .lua .api-signature }
body:setLiftable( value )
```

Controls whether a body is liftable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is liftable. |

### setPaintable {#setpaintable}

``` { .lua .api-signature }
body:setPaintable( value )
```

Controls whether a body is non paintable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is paintable. |

### setUsable {#setusable}

``` { .lua .api-signature }
body:setUsable( value )
```

Controls whether a body is interactable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](Body.md) | The body. |
| `value` | boolean | Whether the body is interactable. |
