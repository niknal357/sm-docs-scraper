# Unit

**Associated namespace:** [sm.unit](../Static-Functions/sm.unit.md)

**Usage:** Server Only

**Serializable:** Yes

A userdata object representing a <strong>unit</strong> in the game.

**Values:**

- <a id="character"></a>`character` [ **[Character](Character.md)** ] <br>
    - `Get`: (Server-Only) Returns the character associated with a unit.

- <a id="eyeheight"></a>`eyeHeight` [ **number** ] <br>
    - `Set`: (Server-Only) Sets the eye height for a unit

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: (Server-Only) Returns the id of a unit.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a unit.
    - `Set`: (Server-Only) Sets (server) public data on a unit.

- <a id="visionfrustum"></a>`visionFrustum` [ **table** ] <br>
    - `Set`: (Server-Only) Sets the vision frustum for a unit

        ```lua
        * self.unit.visionFrustum = {
        *	 { 3.0, math.rad( 80.0 ),  math.rad( 80.0 ) },
        *	 { 20.0, math.rad( 40.0 ), math.rad( 35.0 ) },
        *	 { 40.0, math.rad( 20.0 ), math.rad( 20.0 ) }
        * }
        ```

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Unit == Unit` | boolean | Checks if two instances of [Unit](Unit.md) refer to the same Unit. |

## Server + Client

### getContainer {#getcontainer}

``` { .lua .api-signature }
unit:getContainer( index? )
```

Returns the container stored in the given index inside the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `index` *(optional)* | integer | The index of the container (default: 0). |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The container. |

## Server-only

### addContainer {#addcontainer}

``` { .lua .api-signature }
unit:addContainer( index, size, stackSize? )
```

Creates and stores a container in the given index inside the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `index` | integer | The index of the container [0-15]. |
| `size` | integer | The number of slots in the container. |
| `stackSize` *(optional)* | integer | The stack size. Defaults to maximum possible stack size(65535). |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The created container. |

### createState {#createstate}

``` { .lua .api-signature }
unit:createState( stateName )
```

Creates a Ai State from a name (See [AiState](AiState.md))

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `stateName` | string | Name of predefined ai state. |

**Returns:**

| Type | Description |
| --- | --- |
| [AiState](AiState.md)					The ai state. |  |

### destroy {#destroy}

``` { .lua .api-signature }
unit:destroy(  )
```

Destroy a unit

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

### getCharacter {#getcharacter}

``` { .lua .api-signature }
unit:getCharacter(  )
```

Returns the character associated with a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The associated character. |

### getCurrentFacingDirection {#getcurrentfacingdirection}

``` { .lua .api-signature }
unit:getCurrentFacingDirection(  )
```

Gets the current facing direction of a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The units facing direction. |

### getCurrentMovementDirection {#getcurrentmovementdirection}

``` { .lua .api-signature }
unit:getCurrentMovementDirection(  )
```

Gets the current movement direction of a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The units movement direction. |

### getId {#getid}

``` { .lua .api-signature }
unit:getId(  )
```

Returns the id of a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The unit's id. |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
unit:getPublicData(  )
```

Returns (server) public data from a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### removeContainer {#removecontainer}

``` { .lua .api-signature }
unit:removeContainer( index )
```

Removes the container stored in the given index inside the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `index` | integer | The index of the container. |

### sendCharacterEvent {#sendcharacterevent}

``` { .lua .api-signature }
unit:sendCharacterEvent( event )
```

Sends a event to the associated character of the unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `event` | string | The event name. |

### setFacingDirection {#setfacingdirection}

``` { .lua .api-signature }
unit:setFacingDirection( direction )
```

Sets the facing direction for a unit

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `direction` | [Vec3](Vec3.md) | The desired facing direction. |

### setHearingData {#sethearingdata}

``` { .lua .api-signature }
unit:setHearingData( noiseScale )
```

Notifies a unit that it heard a sound

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `noiseScale` | number | The noise amount. |

### setMovementDirection {#setmovementdirection}

``` { .lua .api-signature }
unit:setMovementDirection( direction )
```

Sets the movement direction for a unit

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `direction` | [Vec3](Vec3.md) | The desired movement direction. |

### setMovementType {#setmovementtype}

``` { .lua .api-signature }
unit:setMovementType( moveTypeName )
```

Sets the movment type for a unit

moveType can be "stand", "walk", "sprint" or "crouch"

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `moveTypeName` | string | The movement type to set |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
unit:setPublicData( data )
```

Sets (server) public data on a unit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `data` | table | The public data. |

### setWantsCrouch {#setwantscrouch}

``` { .lua .api-signature }
unit:setWantsCrouch( wantCrouch )
```

Set a unit to crouch

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `wantCrouch` | boolean | True if the unit should crouch |

### setWantsJump {#setwantsjump}

``` { .lua .api-signature }
unit:setWantsJump( wantJump )
```

Set a unit to jump

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `wantJump` | boolean | True if the unit should jump |

### setWhiskerData {#setwhiskerdata}

``` { .lua .api-signature }
unit:setWhiskerData( whiskerCount, maxAngle, startLength, endLength )
```

Sets the whisker data for obstacle avoidance

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](Unit.md) | The unit. |
| `whiskerCount` | integer | The whiskerCount. |
| `maxAngle` | number | The maxAngle. |
| `startLength` | number | The startLength. |
| `endLength` | number | The endLength. |
