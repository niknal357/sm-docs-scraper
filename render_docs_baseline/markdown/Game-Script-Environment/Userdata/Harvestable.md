# Harvestable

**Associated namespace:** [sm.harvestable](../Static-Functions/sm.harvestable.md)

**Usage:** Server And Client

**Serializable:** Yes

Represents a harvestable object in the game.

**Values:**

- <a id="angularvelocity"></a>`angularVelocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the angular velocity of the harvestable.

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns client public data from a harvestable.
    - `Set`: (Client-Only) Sets client public data on a harvestable.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a harvestable.

- <a id="initialhash"></a>`initialHash` [ **number** ] <br>
    - `Get`: Gets the initial hash of a kinematic. The initial hash identifies the kinematic by its initial world position, uuid and world id.

        This can be used to match kinematics spawned from the same entity in a tile even though each loaded kinematic is technically a different object.

- <a id="initialposition"></a>`initialPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the initial world coordinates of a kinematic.

- <a id="initialrotation"></a>`initialRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the initial quaternion rotation of a harvestable.

- <a id="mass"></a>`mass` [ **number** ] <br>
    - `Get`: Returns the mass of a harvestable. The mass scales with the harvestable's scale.

- <a id="material"></a>`material` [ **string** ] <br>
    - `Get`: Returns the material name of a harvestable.

- <a id="materialid"></a>`materialId` [ **integer** ] <br>
    - `Get`: Returns the material id of a harvestable.

- <a id="name"></a>`name` [ **string** ] <br>
    - `Get`: Returns the name of a harvestable.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a harvestable.
    - `Set`: (Server-Only) Sets (server) public data on a harvestable.

- <a id="type"></a>`type` [ **string** ] <br>
    - `Get`: Returns the type of a harvestable.

- <a id="uuid"></a>`uuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the [Uuid](Uuid.md) of the harvestable.

- <a id="velocity"></a>`velocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the velocity of the harvestable.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world coordinates of a harvestable.

- <a id="worldrotation"></a>`worldRotation` [ **[Quat](Quat.md)** ] <br>
    - `Get`: Returns the quaternion rotation of a harvestable.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Harvestable == Harvestable` | boolean | Checks if two instances of [Harvestable](Harvestable.md) refer to the same Harvestable. |

## Server + Client

### getAabb {#getaabb}

``` { .lua .api-signature }
harvestable:getAabb(  )
```

Returns the axis aligned world space bounds of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | The min and max bounds. |

### getAngularVelocity {#getangularvelocity}

``` { .lua .api-signature }
harvestable:getAngularVelocity(  )
```

Returns the angular velocity of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The angular velocity. |

### getColor {#getcolor}

``` { .lua .api-signature }
harvestable:getColor(  )
```

Returns the color of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The color. |

### getData {#getdata}

``` { .lua .api-signature }
harvestable:getData(  )
```

Get the script data from a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | data			The script data. |

### getId {#getid}

``` { .lua .api-signature }
harvestable:getId(  )
```

Returns the id of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The harvestable id. |

### getInitialHash {#getinitialhash}

``` { .lua .api-signature }
harvestable:getInitialHash(  )
```

Gets the initial hash of a kinematic. The initial hash identifies the kinematic by its initial world position, uuid and world id.

This can be used to match kinematics spawned from the same entity in a tile even though each loaded kinematic is technically a different object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The kinematic to get the initial hash from. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The initial hash. Returns 0 if the harvestable is not kinematic. |

### getLocalAabb {#getlocalaabb}

``` { .lua .api-signature }
harvestable:getLocalAabb(  )
```

Returns the axis aligned local space bounds of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md),[Vec3](Vec3.md) | The min and max bounds. |

### getMass {#getmass}

``` { .lua .api-signature }
harvestable:getMass(  )
```

Returns the mass of a harvestable. The mass scales with the harvestable's scale.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The mass. |

### getMaterial {#getmaterial}

``` { .lua .api-signature }
harvestable:getMaterial(  )
```

Returns the material name of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The name of the material. |

### getMaterialId {#getmaterialid}

``` { .lua .api-signature }
harvestable:getMaterialId(  )
```

Returns the material id of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The id of the material. |

### getName {#getname}

``` { .lua .api-signature }
harvestable:getName(  )
```

Returns the name of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The harvestable name. |

### getPosition {#getposition}

``` { .lua .api-signature }
harvestable:getPosition(  )
```

Returns the world coordinates of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The position. |

### getRotation {#getrotation}

``` { .lua .api-signature }
harvestable:getRotation(  )
```

Returns the quaternion rotation of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The rotation. |

### getScale {#getscale}

``` { .lua .api-signature }
harvestable:getScale(  )
```

Returns the scale of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The scale. |

### getSeatCharacter {#getseatcharacter}

``` { .lua .api-signature }
harvestable:getSeatCharacter(  )
```

Returns the [Character](Character.md) that is seated in the kinematic.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `kinematic` | [Harvestable](Harvestable.md) | The kinematic. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The character. |

### getType {#gettype}

``` { .lua .api-signature }
harvestable:getType(  )
```

Returns the type of a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The harvestable's type. |

### getUuid {#getuuid}

``` { .lua .api-signature }
harvestable:getUuid(  )
```

Returns the [Uuid](Uuid.md) of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | The uuid. |

### getVelocity {#getvelocity}

``` { .lua .api-signature }
harvestable:getVelocity(  )
```

Returns the velocity of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The velocity. |

### getWorld {#getworld}

``` { .lua .api-signature }
harvestable:getWorld(  )
```

Returns the world a harvestable exists in.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The world the harvestable exists in. |

### hasSeat {#hasseat}

``` { .lua .api-signature }
harvestable:hasSeat(  )
```

Returns true if kinematic has a seat component.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `kinematic` | [Harvestable](Harvestable.md) | The kinematic. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The result. |

### isCellKinematic {#iscellkinematic}

``` { .lua .api-signature }
harvestable:isCellKinematic(  )
```

Check if a kinematic comes from a cell or is created from a script.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable to check. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if it is a kinematic from a cell, false if it is not. Nil if it is not a kinematic. |

### isKinematic {#iskinematic}

``` { .lua .api-signature }
harvestable:isKinematic(  )
```

Check if a harvestable is kinematic

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the harvestable is kinematic. |

### setPosition {#setposition}

``` { .lua .api-signature }
harvestable:setPosition( position )
```

Set the world coordinates of a harvestable. Can only be used on kinematic harvestables.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `position` | [Vec3](Vec3.md) | The position. |

### setRotation {#setrotation}

``` { .lua .api-signature }
harvestable:setRotation( rotation )
```

Set the quaternion rotation of a harvestable. Can only be used on kinematic harvestables.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `rotation` | [Quat](Quat.md) | The rotation. |

### setSeatCharacter {#setseatcharacter}

``` { .lua .api-signature }
harvestable:setSeatCharacter( character )
```

Requests to seat a [Character](Character.md) in the kinematic.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `kinematic` | [Harvestable](Harvestable.md) | The kinematic. |
| `character` | [Character](Character.md) | The character. |

### transformDirection {#transformdirection}

``` { .lua .api-signature }
harvestable:transformDirection( direction )
```

Transforms a direction in the world into a local direction of the harvestable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `direction` | [Vec3](Vec3.md) | The world direction. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The local direction. |

### transformLocalPoint {#transformlocalpoint}

``` { .lua .api-signature }
harvestable:transformLocalPoint( vector )
```

Transform a local point to world space.

```lua
local worldPos = self.harvestable:transformLocalPoint( localPos )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvetable` | [Harvestable](Harvestable.md) | The harvestable. |
| `vector` | [Vec3](Vec3.md) | The local point. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The world point. |

### transformPoint {#transformpoint}

``` { .lua .api-signature }
harvestable:transformPoint( vector )
```

Transform a world point to the local harvestable transform.

```lua
local localPos = self.harvestable:transformPoint( worldPos )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `vector` | [Vec3](Vec3.md) | The world point. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The local point. |

## Server-only

### destroy {#destroy}

``` { .lua .api-signature }
harvestable:destroy(  )
```

Destroys a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
harvestable:getPublicData(  )
```

Returns (server) public data from a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### setParams {#setparams}

``` { .lua .api-signature }
harvestable:setParams( data )
```

Sets param data for a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `data` | any | The param data. |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
harvestable:setPublicData( data )
```

Sets (server) public data on a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `data` | table | The public data. |

## Client-only

### applyShakeImpulse {#applyshakeimpulse}

``` { .lua .api-signature }
harvestable:applyShakeImpulse( shake )
```

Applies a shake impulse to the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `shake` | number | The shake impulse value. |

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
harvestable:getClientPublicData(  )
```

Returns client public data from a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The client public data. |

### getPoseWeight {#getposeweight}

``` { .lua .api-signature }
harvestable:getPoseWeight( index )
```

Returns the pose weight of the pose in the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `index` | integer | The index. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The pose weight. |

### getUvFrameIndex {#getuvframeindex}

``` { .lua .api-signature }
harvestable:getUvFrameIndex(  )
```

Returns the index of the current UV animation frame

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The uv frame. |

### setAllSubMeshVisible {#setallsubmeshvisible}

``` { .lua .api-signature }
harvestable:setAllSubMeshVisible( visible )
```

Set the visibility of all submeshes

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `visible` | boolean | True if the submeshes should be visible. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
harvestable:setClientPublicData( data )
```

Sets client public data on a harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `data` | table | The client public data. |

### setColor {#setcolor}

``` { .lua .api-signature }
harvestable:setColor( color )
```

Sets the color of the harvestable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `color` | [Color](Color.md) | The color. |

### setPoseWeight {#setposeweight}

``` { .lua .api-signature }
harvestable:setPoseWeight( index, value )
```

Set the pose weight of the pose in the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `index` | integer | The index. |
| `value` | number | The pose weight. |

### setSubMeshVisible {#setsubmeshvisible}

``` { .lua .api-signature }
harvestable:setSubMeshVisible( name, visible )
```

Set the visibility of a submesh

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `name` | string | Name of the submesh. |
| `visible` | boolean | True if the submesh should be visible. |

### setUvFrameIndex {#setuvframeindex}

``` { .lua .api-signature }
harvestable:setUvFrameIndex( index )
```

Sets the UV animation frame with the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |
| `index` | integer | The index. |
