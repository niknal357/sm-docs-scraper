# Shape

**Associated namespace:** [sm.shape](../Static-Functions/sm.shape.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>shape</strong> in the game.

**Values:**

- <a id="at"></a>`at` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the direction of a shape's front side.

        The direction is affected by the shape's rotation in the world.

- <a id="body"></a>`body` [ **[Body](Body.md)** ] <br>
    - `Get`: Returns the [Body](Body.md) a shape is part of.

- <a id="buildable"></a>`buildable` [ **boolean** ] <br>
    - `Get`: Check if a shape is buildable

- <a id="buoyancy"></a>`buoyancy` [ **number** ] <br>
    - `Get`: Returns the buoyancy multiplier of a shape.

- <a id="color"></a>`color` [ **[Color](Color.md)** ] <br>
    - `Get`: Returns the color of a shape.
    - `Set`: (Server-Only) Sets the color of a shape. This is similar to coloring with the <em>Paint Tool</em>.

- <a id="connectable"></a>`connectable` [ **boolean** ] <br>
    - `Get`: Check if a shape is connectable

- <a id="convertabletodynamic"></a>`convertableToDynamic` [ **boolean** ] <br>
    - `Get`: Check if a shape is convertible to dynamic form

- <a id="destructable"></a>`destructable` [ **boolean** ] <br>
    - `Get`: Check if a shape is destructable.

- <a id="erasable"></a>`erasable` [ **boolean** ] <br>
    - `Get`: Check if a shape is erasable.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a shape.

- <a id="interactable"></a>`interactable` [ **[Interactable](Interactable.md)** ] <br>
    - `Get`: Returns the [Interactable](Interactable.md) of a shape, if one exists. Otherwise the function will return nil.

- <a id="isblock"></a>`isBlock` [ **boolean** ] <br>
    - `Get`: Return true if a shape is a basicmaterial

- <a id="iswedge"></a>`isWedge` [ **boolean** ] <br>
    - `Get`: Return true if a shape is a wedge

- <a id="liftable"></a>`liftable` [ **boolean** ] <br>
    - `Get`: Check if a shape is liftable

- <a id="localposition"></a>`localPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local grid position of a shape.

- <a id="localrotation"></a>`localRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the local rotation of a shape.

- <a id="mass"></a>`mass` [ **number** ] <br>
    - `Get`: Returns the mass of a shape.

- <a id="material"></a>`material` [ **string** ] <br>
    - `Get`: Returns the material of a shape.

- <a id="materialid"></a>`materialId` [ **integer** ] <br>
    - `Get`: Returns the material id of a shape.

- <a id="paintable"></a>`paintable` [ **boolean** ] <br>
    - `Get`: Check if a shape is paintable

- <a id="right"></a>`right` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the direction of a shape's right side.

        The direction is affected by the shape's rotation in the world.

- <a id="shapeuuid"></a>`shapeUuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the uuid unique to a shape/block type.

- <a id="stackedamount"></a>`stackedAmount` [ **integer** ] <br>
    - `Get`: Return the amount that is stacked in the shape
    - `Set`: (Server-Only) Set the amount that is stacked in the shape

- <a id="stackeditem"></a>`stackedItem` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Return the item [Uuid](Uuid.md) that is stacked in the shape
    - `Set`: (Server-Only) Set the item [Uuid](Uuid.md) that is stacked in the shape

- <a id="up"></a>`up` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the direction of a shape's top side.

        The direction is affected by the shape's rotation in the world.

- <a id="usable"></a>`usable` [ **boolean** ] <br>
    - `Get`: Check if a shape is interactable

- <a id="uuid"></a>`uuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the uuid unique to a shape/block type.

- <a id="velocity"></a>`velocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the linear velocity of a shape.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of a shape.

- <a id="worldrotation"></a>`worldRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the world rotation of a shape.

- <a id="xaxis"></a>`xAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local x-axis vector of a shape.

- <a id="yaxis"></a>`yAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local y-axis vector of a shape.

- <a id="zaxis"></a>`zAxis` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the local z-axis vector of a shape.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Shape == Shape` | boolean | Checks if two instances of [Shape](Shape.md) refer to the same Shape. |

## Server + Client

### getAt {#getat}

``` { .lua .api-signature }
shape:getAt(  )
```

Returns the direction of a shape's front side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's at-axis. |

### getBody {#getbody}

``` { .lua .api-signature }
shape:getBody(  )
```

Returns the [Body](Body.md) a shape is part of.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Body](Body.md) | The body which the shape is part of. |

### getBoundingBox {#getboundingbox}

``` { .lua .api-signature }
shape:getBoundingBox(  )
```

Returns the bounding box of a shape &ndash; the dimensions that a shape occupies when building.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The size of the shape's bounding box. |

### getBuoyancy {#getbuoyancy}

``` { .lua .api-signature }
shape:getBuoyancy(  )
```

Returns the buoyancy multiplier of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The buoyancy multiplier. |

### getBurning {#getburning}

``` { .lua .api-signature }
shape:getBurning(  )
```

Check if a shape is burning.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the shape is burning. |

### getClosestBlockLocalPosition {#getclosestblocklocalposition}

``` { .lua .api-signature }
shape:getClosestBlockLocalPosition( position )
```

Transform a world position to the closest block's local position in a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The block shape. |
| `position` | [Vec3](Vec3.md) | The world position. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The closest position. |

### getColor {#getcolor}

``` { .lua .api-signature }
shape:getColor(  )
```

Returns the color of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The shape's color. |

### getCompromised {#getcompromised}

``` { .lua .api-signature }
shape:getCompromised(  )
```

Check if a shape is compromised.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the shape is compromised. |

### getId {#getid}

``` { .lua .api-signature }
shape:getId(  )
```

Returns the id of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The shape's id. |

### getInteractable {#getinteractable}

``` { .lua .api-signature }
shape:getInteractable(  )
```

Returns the [Interactable](Interactable.md) of a shape, if one exists. Otherwise the function will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Interactable](Interactable.md) | The interactable belonging to the shape. |

### getInterpolatedAt {#getinterpolatedat}

``` { .lua .api-signature }
shape:getInterpolatedAt(  )
```

Returns the interpolated direction of a shape's front side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's interpolated at-axis. |

### getInterpolatedRight {#getinterpolatedright}

``` { .lua .api-signature }
shape:getInterpolatedRight(  )
```

Returns the interpolated direction of a shape's right side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's interpolated right-axis. |

### getInterpolatedUp {#getinterpolatedup}

``` { .lua .api-signature }
shape:getInterpolatedUp(  )
```

Returns the interpolated direction of a shape's top side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's interpolated up-axis. |

### getInterpolatedWorldPosition {#getinterpolatedworldposition}

``` { .lua .api-signature }
shape:getInterpolatedWorldPosition(  )
```

Returns the interpolated world position of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's interpolated world position. |

### getIsHarvest {#getisharvest}

``` { .lua .api-signature }
shape:getIsHarvest(  )
```

Return whether the shape belongs to a harvest shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the shape is harvestable. |

### getIsStackable {#getisstackable}

``` { .lua .api-signature }
shape:getIsStackable(  )
```

Return whether the shape belongs to a stackable shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the shape is stackable. |

### getJoints {#getjoints}

``` { .lua .api-signature }
shape:getJoints( onlyChildJoints? )
```

Returns a table of all [joints](Joint.md) that are attached to the shape.

Will return all attached joints when onlyChildJoints is set to false.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `onlyChildJoints` *(optional)* | boolean | Filters what joints to return. Defaults to true (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of joints attached to the shape. {[Joint](Joint.md), ..} |

### getLocalAabb {#getlocalaabb}

``` { .lua .api-signature }
shape:getLocalAabb(  )
```

Get the local aabb of the shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | Returns the aabb min and max. |

### getLocalPosition {#getlocalposition}

``` { .lua .api-signature }
shape:getLocalPosition(  )
```

Returns the local grid position of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's local position. |

### getLocalRotation {#getlocalrotation}

``` { .lua .api-signature }
shape:getLocalRotation(  )
```

Returns the local rotation of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The shape's local rotation. |

### getMass {#getmass}

``` { .lua .api-signature }
shape:getMass(  )
```

Returns the mass of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The shape's mass. |

### getMaterial {#getmaterial}

``` { .lua .api-signature }
shape:getMaterial(  )
```

Returns the material of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The shape's material. |

### getMaterialId {#getmaterialid}

``` { .lua .api-signature }
shape:getMaterialId(  )
```

Returns the material id of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The shape's material id. |

### getMultiShapeJoints {#getmultishapejoints}

``` { .lua .api-signature }
shape:getMultiShapeJoints(  )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | A shape that is a multishape |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of joints contained in the multishape (returns nil if shape wasn't a multishape) |

### getMultiShapeShapes {#getmultishapeshapes}

``` { .lua .api-signature }
shape:getMultiShapeShapes(  )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | A shape that is a multishape |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of shapes contained in the multishape (returns nil if shape wasn't a multishape) |

### getPipeOffsets {#getpipeoffsets}

``` { .lua .api-signature }
shape:getPipeOffsets( direction? )
```

Returns a table offsets for the pipe connections of the shape. Can specify direction using sm.pipeGraph.direction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `direction` *(optional)* | integer | The direction to fetch in. Defaults to [sm.pipeGraph.direction.any](../Static-Functions/sm.pipeGraph.md#direction) (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | table of local offset positions. {[Vec3](Vec3.md), ..} |

### getRight {#getright}

``` { .lua .api-signature }
shape:getRight(  )
```

Returns the direction of a shape's right side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's right-axis. |

### getShapeOutputContainerIndex {#getshapeoutputcontainerindex}

``` { .lua .api-signature }
shape:getShapeOutputContainerIndex(  )
```

Returns the shapes output container index listed in the shapeset for pipe graph affecting shapes.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) |  |

### getShapeUuid {#getshapeuuid}

``` { .lua .api-signature }
shape:getShapeUuid(  )
```

Returns the uuid unique to a shape/block type.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | The shape's uuid. |

### getSticky {#getsticky}

``` { .lua .api-signature }
shape:getSticky(  )
```

Returns the sticky directions of the shape for positive xyz and negative xyz.

A value of 1 means that the direction is sticky and a value of 0 means that the direction is not sticky.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| {[Vec3](Vec3.md),[Vec3](Vec3.md)} | The negative xyz sticky and the positive xyz sticky. |

### getUp {#getup}

``` { .lua .api-signature }
shape:getUp(  )
```

Returns the direction of a shape's top side.

The direction is affected by the shape's rotation in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's up-axis. |

### getVelocity {#getvelocity}

``` { .lua .api-signature }
shape:getVelocity(  )
```

Returns the linear velocity of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's linear velocity. |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
shape:getWorldPosition(  )
```

Returns the world position of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's world position. |

### getWorldRotation {#getworldrotation}

``` { .lua .api-signature }
shape:getWorldRotation(  )
```

Returns the world rotation of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The shape's world rotation. |

### getXAxis {#getxaxis}

``` { .lua .api-signature }
shape:getXAxis(  )
```

Returns the local x-axis vector of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's x-axis. |

### getYAxis {#getyaxis}

``` { .lua .api-signature }
shape:getYAxis(  )
```

Returns the local y-axis vector of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's y-axis. |

### getZAxis {#getzaxis}

``` { .lua .api-signature }
shape:getZAxis(  )
```

Returns the local z-axis vector of a shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The shape's z-axis. |

### isPipe {#ispipe}

``` { .lua .api-signature }
shape:isPipe(  )
```

Returns whether the shape is a pipe or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the shape was a pipe or not. |

### setCollisionSoundEnabled {#setcollisionsoundenabled}

``` { .lua .api-signature }
shape:setCollisionSoundEnabled( enabled )
```

Sets if the shape should generate sound on collisions.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `enabled` | boolean | Whether the sound should be enabled or not. |

### setPhysicsMaterial {#setphysicsmaterial}

``` { .lua .api-signature }
shape:setPhysicsMaterial( material )
```

Sets the physics material of the shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `material` | integer | The new physics material for the shape. |

### shapeExists {#shapeexists}

``` { .lua .api-signature }
shape:shapeExists(  )
```

> **Deprecated:**
> use [sm.exists](../Static-Functions/sm.md#exists)
>

Return true if a shape exists.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the shape exists. |

### transformDirection {#transformdirection}

``` { .lua .api-signature }
shape:transformDirection( vector )
```

Transform a world direction to the local shape transform.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `vector` | [Vec3](Vec3.md) | The untransformed direction. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The transformed direction. |

### transformLocalDirection {#transformlocaldirection}

``` { .lua .api-signature }
shape:transformLocalDirection( vector )
```

Transform a local direction to world space.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `vector` | [Vec3](Vec3.md) | The local direction. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The world direction. |

### transformLocalPoint {#transformlocalpoint}

``` { .lua .api-signature }
shape:transformLocalPoint( vector )
```

Transform a local point to world space.

```lua
local worldPos = self.shape:transformLocalPoint( localPos )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `vector` | [Vec3](Vec3.md) | The local point. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The world point. |

### transformPoint {#transformpoint}

``` { .lua .api-signature }
shape:transformPoint( vector )
```

Transform a world point to the local shape transform.

```lua
local localPos = self.shape:transformPoint( worldPos )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `vector` | [Vec3](Vec3.md) | The world point. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The local point. |

### transformRotation {#transformrotation}

``` { .lua .api-signature }
shape:transformRotation( quat )
```

Transform a world rotation to the local shape transform.

```lua
local worldUp = sm.vec3.new( 0, 0, 1 )
local worldRot = sm.vec3.getRotation( worldUp, worldDir )
local localRot = self.shape:transformRotation( worldRot )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `quat` | [Quat](Quat.md) | The untransformed quaternion. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The transformed quaternion. |

## Server-only

### createJoint {#createjoint}

``` { .lua .api-signature }
shape:createJoint( uuid, position, direction )
```

Create a new joint

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The host shape. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the joint. |
| `position` | [Vec3](Vec3.md) | The joint's grid position. |
| `direction` | [Vec3](Vec3.md) | The joint's normal direction. |

**Returns:**

| Type | Description |
| --- | --- |
| [Joint](Joint.md)					The created joint. |  |

### destroyBlock {#destroyblock}

``` { .lua .api-signature }
shape:destroyBlock(
    position,
    size?,
    attackLevel?,
    destructionType?,
    destructionPosition?,
    destructionNormal?
)
```

Destroy a block.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The block shape. |
| `position` | [Vec3](Vec3.md) | The local position of the removal box corner. |
| `size` *(optional)* | [Vec3](Vec3.md) | The size of the removal box. Defaults to 1x1x1 (Optional) |
| `attackLevel` *(optional)* | integer | Determines which quality level of block the attack can destroy. Setting it to 0 (default) will destroy any block. |
| `destructionType` *(optional)* | integer | The type of destruction (Optional). (See[sm.shape.destructionType). (Defaults to sm.shape.destructionType.none) |
| `destructionPosition` *(optional)* | [Vec3](Vec3.md) | The position of the destruction would hit the block (Optional) |
| `destructionNormal` *(optional)* | [Vec3](Vec3.md) | The normal direction of where the destruction would hit the block (Optional) |

### destroyPart {#destroypart}

``` { .lua .api-signature }
shape:destroyPart(
    attackLevel,
    destructionType?,
    destructionPosition?,
    destructionNormal?
)
```

> **Deprecated:**
> use [Shape.destroyShape](#destroyshape)
>

Destroy a part

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The part. |
| `attackLevel` | integer | Determines which quality level of parts the attack can destroy. Setting it to 0 (default) will destroy any part. |
| `destructionType` *(optional)* | integer | The type of destruction (Optional). (See[sm.shape.destructionType). (Defaults to sm.shape.destructionType.none) |
| `destructionPosition` *(optional)* | [Vec3](Vec3.md) | The position of the destruction would hit the part (Optional) |
| `destructionNormal` *(optional)* | [Vec3](Vec3.md) | The normal direction of where the destruction would hit the part (Optional) |

### destroyShape {#destroyshape}

``` { .lua .api-signature }
shape:destroyShape(
    attackLevel,
    destructionType?,
    destructionPosition?,
    destructionNormal?
)
```

Destroy a shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `attackLevel` | integer | Determines which quality level of shape the attack can destroy. Setting it to 0 (default) will destroy any shape. |
| `destructionType` *(optional)* | integer | The type of destruction (Optional). (See[sm.shape.destructionType). (Defaults to sm.shape.destructionType.none) |
| `destructionPosition` *(optional)* | [Vec3](Vec3.md) | The position of the destruction would hit the shape (Optional) |
| `destructionNormal` *(optional)* | [Vec3](Vec3.md) | The normal direction of where the destruction would hit the shape (Optional) |

### getNeighbours {#getneighbours}

``` { .lua .api-signature }
shape:getNeighbours(  )
```

Returns a table of shapes which are neighbours to the shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| table | table of shapes. {[Shape](Shape.md), ..} |

### getPipedNeighbours {#getpipedneighbours}

``` { .lua .api-signature }
shape:getPipedNeighbours(  )
```

Returns a table of shapes which are neighbours connected with pipes to the shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |

**Returns:**

| Type | Description |
| --- | --- |
| table | table of shapes. {[Shape](Shape.md), ..} |

### removeColor {#removecolor}

``` { .lua .api-signature }
shape:removeColor(  )
```

Restores the color of a shape to its base color. This is similar to coloring with the <em>Paint Tool</em>

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape |

### replaceShape {#replaceshape}

``` { .lua .api-signature }
shape:replaceShape( uuid )
```

Creates a new [Shape](Shape.md) from [Uuid](Uuid.md) to replace the given [Shape](Shape.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `uuid` | [Uuid](Uuid.md) | The uuid of the new shape. |

### setBurning {#setburning}

``` { .lua .api-signature }
shape:setBurning( state )
```

Set the state that determines if a shape is burning.

True to set burning and false to set not burning.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `state` | boolean | The state. |

### setColor {#setcolor}

``` { .lua .api-signature }
shape:setColor( color )
```

Sets the color of a shape. This is similar to coloring with the <em>Paint Tool</em>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `color` | [Color](Color.md) | The color. |

### setCompromised {#setcompromised}

``` { .lua .api-signature }
shape:setCompromised( state )
```

Set the state that determines if a shape is compromised.

True to set compromised and false to set not compromised.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `state` | boolean | The state. |

## Client-only

### applyShakeImpulse {#applyshakeimpulse}

``` { .lua .api-signature }
shape:applyShakeImpulse( shake )
```

Applies a shake impulse to the shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Shape](Shape.md) | The shape. |
| `shake` | number | The shake impulse value. |
