# Interactable

**Associated namespace:** [sm.interactable](../Static-Functions/sm.interactable.md)

**Usage:** Server And Client

**Serializable:** Yes

Represents an interactable object in the game

**Values:**

- <a id="active"></a>`active` [ **boolean** ] <br>
    - `Get`: Returns the logic output signal of an interactable. Signal is a boolean, <strong>on</strong> or <strong>off</strong>.
    - `Set`: (Server-Only) Sets the logic output signal of an interactable. Signal is a boolean, <strong>on</strong> or <strong>off</strong>.

- <a id="body"></a>`body` [ **[Body](Body.md)** ] <br>
    - `Get`: Returns the [Body](Body.md) an interactable's [Shape](Shape.md) is part of.

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns (client) public data from a interactable.
    - `Set`: (Client-Only) Sets (client) public data on a interactable.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of an interactable.

- <a id="power"></a>`power` [ **number** ] <br>
    - `Get`: Returns the power output signal of an interactable. Signal is a number between -1 to 1, where 1 is forward and -1 backward.
    - `Set`: (Server-Only) Sets the power output signal of an interactable. Signal is a number between -1 to 1, where 1 is forward and -1 backward.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a interactable.
    - `Set`: (Server-Only) Sets (server) public data on a interactable.

- <a id="shape"></a>`shape` [ **[Shape](Shape.md)** ] <br>
    - `Get`: Returns the [Shape](Shape.md) of an interactable.

- <a id="type"></a>`type` [ **string** ] <br>
    - `Get`: Returns the interactable type of an interactable.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Interactable == Interactable` | boolean | Checks if two instances of [Interactable](Interactable.md) refer to the same Interactable. |

## Server + Client

### getBearings {#getbearings}

``` { .lua .api-signature }
interactable:getBearings(  )
```

Returns a table of [bearings](Joint.md) that an interactable is connected to.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of the connected [bearings](Joint.md) {[Joint](Joint.md), ..}. |

### getBody {#getbody}

``` { .lua .api-signature }
interactable:getBody(  )
```

Returns the [Body](Body.md) an interactable's [Shape](Shape.md) is part of.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Body](Body.md) | The body an interactable's shape is part of. |

### getChildren {#getchildren}

``` { .lua .api-signature }
interactable:getChildren( flags )
```

Returns a table of child [interactables](Interactable.md) that an interactable is connected to. The children listen to the interactable's output.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `flags` | integer | Connection type flags filter. (defaults to all types except for sm.interactable.connectionType.bearing and sm.interactable.connectionType.steering (for backwards compability)) |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of the connected child [interactables](Interactable.md) {[Interactable](Interactable.md), ..}. |

### getColorHighlight {#getcolorhighlight}

``` { .lua .api-signature }
interactable:getColorHighlight(  )
```

Returns the connection-point highlight color of an interactable. The point is shown when using the <em>Connect Tool</em>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The connection-point highlight color. |

### getColorNormal {#getcolornormal}

``` { .lua .api-signature }
interactable:getColorNormal(  )
```

Returns the connection-point color of an interactable. The point is shown when using the <em>Connect Tool</em>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The connection-point color. |

### getConnectionInputType {#getconnectioninputtype}

``` { .lua .api-signature }
interactable:getConnectionInputType(  )
```

Returns the input connection type.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | connection type The input connection type. |

### getConnectionOutputType {#getconnectionoutputtype}

``` { .lua .api-signature }
interactable:getConnectionOutputType(  )
```

Returns the output connection type.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | connection type The output connection type. |

### getContainer {#getcontainer}

``` { .lua .api-signature }
interactable:getContainer( index? )
```

Returns the container stored in the given index inside the controller

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` *(optional)* | integer | The index of the container (default: 0). |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The container. |

### getId {#getid}

``` { .lua .api-signature }
interactable:getId(  )
```

Returns the id of an interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The interactable's id. |

### getJointCustomData {#getjointcustomdata}

``` { .lua .api-signature }
interactable:getJointCustomData( joint )
```

Returns custom joint script data.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable, needs to be of script type. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data. |

### getJoints {#getjoints}

``` { .lua .api-signature }
interactable:getJoints(  )
```

Returns a table of all [joints](Joint.md) that an interactable is connected to. Joints include <strong>bearings</strong> and <strong>pistons</strong>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of the connected [joints](Joint.md) {[Joint](Joint.md), ..}. |

### getLocalBonePosition {#getlocalboneposition}

``` { .lua .api-signature }
interactable:getLocalBonePosition( name )
```

Return the position of the bone

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The bone name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The position. |

### getMaxChildCount {#getmaxchildcount}

``` { .lua .api-signature }
interactable:getMaxChildCount(  )
```

Returns the maximum number of allowed child connections of an interactable &ndash; the number of outgoing connections.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The max child connection count. |

### getMaxParentCount {#getmaxparentcount}

``` { .lua .api-signature }
interactable:getMaxParentCount(  )
```

Returns the maximum number of allowed parent connections of an interactable &ndash; the number of incoming connections.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The max parent connection count. |

### getParents {#getparents}

``` { .lua .api-signature }
interactable:getParents( flags )
```

Returns a table of parent [interactables](Interactable.md) that are connected to an interactable. The parents act as the interactable's input.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `flags` | integer | Connection type flags filter. (default to all types) |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of the connected parent [interactables](Interactable.md) {[Interactable](Interactable.md), ..}. |

### getPistons {#getpistons}

``` { .lua .api-signature }
interactable:getPistons(  )
```

Returns a table of [pistons](Joint.md) that an interactable is connected to.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of the connected [pistons](Joint.md) {[Joint](Joint.md), ..}. |

### getPower {#getpower}

``` { .lua .api-signature }
interactable:getPower(  )
```

Returns the power output signal of an interactable. Signal is a number between -1 to 1, where 1 is forward and -1 backward.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The power output signal. |

### getSeatCharacter {#getseatcharacter}

``` { .lua .api-signature }
interactable:getSeatCharacter(  )
```

Returns the [Character](Character.md) that is seated in the [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The character. |

### getSeatInteractables {#getseatinteractables}

``` { .lua .api-signature }
interactable:getSeatInteractables(  )
```

Retrieves the list of [Interactable](Interactable.md) connected to the seat.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The list of connected [interactables](Interactable.md) {[Interactable](Interactable.md), ..}. |

### getShape {#getshape}

``` { .lua .api-signature }
interactable:getShape(  )
```

Returns the [Shape](Shape.md) of an interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The shape which hosts the interactable. |

### getSingleParent {#getsingleparent}

``` { .lua .api-signature }
interactable:getSingleParent(  )
```

Returns the parent [Interactable](Interactable.md) that is connected to an interactable. The parent act as the interactable's input.

> **Warning:**
> This method is <strong>not</strong> allowed for an interactable that allows more than one parent connection.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Interactable](Interactable.md) | The connected parent interactable. |

### getSteeringAngle {#getsteeringangle}

``` { .lua .api-signature }
interactable:getSteeringAngle(  )
```

Returns the steering angle of an steering interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The steering angle |

### getSteeringJointLeftAngleLimit {#getsteeringjointleftanglelimit}

``` { .lua .api-signature }
interactable:getSteeringJointLeftAngleLimit( joint )
```

Returns the left angle limit of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The left angle limit. |

### getSteeringJointLeftAngleSpeed {#getsteeringjointleftanglespeed}

``` { .lua .api-signature }
interactable:getSteeringJointLeftAngleSpeed( joint )
```

Returns the left angle speed of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The left angle speed. |

### getSteeringJointRightAngleLimit {#getsteeringjointrightanglelimit}

``` { .lua .api-signature }
interactable:getSteeringJointRightAngleLimit( joint )
```

Returns the right angle limit of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The right angle limit. |

### getSteeringJointRightAngleSpeed {#getsteeringjointrightanglespeed}

``` { .lua .api-signature }
interactable:getSteeringJointRightAngleSpeed( joint )
```

Returns the right angle speed of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The right angle speed. |

### getSteeringJointSettings {#getsteeringjointsettings}

``` { .lua .api-signature }
interactable:getSteeringJointSettings( joint )
```

Returns the settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| number,number,number,number,boolean | The left angle speed; right angle speed; left angle limit; right angle limit; true if the joint is unlocked. |

### getSteeringJointUnlocked {#getsteeringjointunlocked}

``` { .lua .api-signature }
interactable:getSteeringJointUnlocked( joint )
```

Returns the unlocked state of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the joint is unlocked |

### getSteeringPower {#getsteeringpower}

``` { .lua .api-signature }
interactable:getSteeringPower(  )
```

Returns the [Character](Character.md) that is locking the controller.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The character. |

### getSteeringSprint {#getsteeringsprint}

``` { .lua .api-signature }
interactable:getSteeringSprint(  )
```

Returns the sprint value of an steering interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The sprint value |

### getType {#gettype}

``` { .lua .api-signature }
interactable:getType(  )
```

Returns the interactable type of an interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The interactable's type. ([sm.interactable.types](../Static-Functions/sm.interactable.md#types)) |

### getWorldBonePosition {#getworldboneposition}

``` { .lua .api-signature }
interactable:getWorldBonePosition( name )
```

Return the position of the bone

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The bone name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The position. |

### hasChanged {#haschanged}

``` { .lua .api-signature }
interactable:hasChanged( tick )
```

Returns true if the interactable had updates since the given tick.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `tick` | integer | The tick. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the interactable has been updated. |

### hasOutputType {#hasoutputtype}

``` { .lua .api-signature }
interactable:hasOutputType( flags )
```

Returns true if the [Interactable](Interactable.md) has the output type.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `flags` | integer | The output type. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Has the output type. |

### hasSeat {#hasseat}

``` { .lua .api-signature }
interactable:hasSeat(  )
```

Returns true if [Interactable](Interactable.md) has a seat component.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The result. |

### hasSteering {#hassteering}

``` { .lua .api-signature }
interactable:hasSteering(  )
```

Returns true if [Interactable](Interactable.md) has a steering component.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The result. |

### isActive {#isactive}

``` { .lua .api-signature }
interactable:isActive(  )
```

Returns the logic output signal of an interactable. Signal is a boolean, <strong>on</strong> or <strong>off</strong>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The logic output signal. |

### pressSeatInteractable {#pressseatinteractable}

``` { .lua .api-signature }
interactable:pressSeatInteractable( index )
```

Triggers a press interaction on a [Interactable](Interactable.md) connected to the seat.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index of the interactable to press. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if successful. |

### releaseSeatInteractable {#releaseseatinteractable}

``` { .lua .api-signature }
interactable:releaseSeatInteractable( index )
```

Triggers a release interaction on a [Interactable](Interactable.md) connected to the seat.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index of the interactable to release. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if successful. |

### setGyroForce {#setgyroforce}

``` { .lua .api-signature }
interactable:setGyroForce( force )
```

Sets a max motor force on the turret seat

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `force` | number | The maximum motor force. |

### setGyroMaxSpeed {#setgyromaxspeed}

``` { .lua .api-signature }
interactable:setGyroMaxSpeed( speedModifier )
```

Sets a target speed multiplier on the turret seat

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `speedModifier` | number | The speed modifier. |

### setParams {#setparams}

``` { .lua .api-signature }
interactable:setParams( data )
```

Sets param data for a script interactable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable, needs to be of script type. |
| `data` | any | The param data. |

### setSeatCharacter {#setseatcharacter}

``` { .lua .api-signature }
interactable:setSeatCharacter( character )
```

Requests to seat a [Character](Character.md) in the [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `character` | [Character](Character.md) | The character. |

### setSteeringFlag {#setsteeringflag}

``` { .lua .api-signature }
interactable:setSteeringFlag( steeringFlags )
```

Set the steering flag for a steering interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `steeringFlags` | integer | The steering flags. |

### unsetSteeringFlag {#unsetsteeringflag}

``` { .lua .api-signature }
interactable:unsetSteeringFlag( steeringFlags )
```

Unset the steering flag for a steering interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `steeringFlags` | integer | The steering flags. |

## Server-only

### addContainer {#addcontainer}

``` { .lua .api-signature }
interactable:addContainer( index, size, stackSize? )
```

Creates and stores a container in the given index inside the controller

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index of the container [0-15]. |
| `size` | integer | The number of slots in the container. |
| `stackSize` *(optional)* | integer | The stack size. Defaults to maximum possible stack size(65535). |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The created container. |

### bindDamageDestruction {#binddamagedestruction}

``` { .lua .api-signature }
interactable:bindDamageDestruction( callback )
```

Binds a callback to be called if the interactable is destroyed through a source of damage.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `callback` | string | The name of the lua function to bind. |

### clearLightOverrideColor {#clearlightoverridecolor}

``` { .lua .api-signature }
interactable:clearLightOverrideColor(  )
```

Clear the override color of a light controller.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

### connect {#connect}

``` { .lua .api-signature }
interactable:connect( child )
```

Connects two interactables. Similar to using the Connect Tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `parent` | [Interactable](Interactable.md) | The sender of a connection. |
| `child` | [Interactable](Interactable.md) | The receiver of a connection. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the connection attempt was successful. |

### connectToJoint {#connecttojoint}

``` { .lua .api-signature }
interactable:connectToJoint( child )
```

Connects interactable with joint.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `parent` | [Interactable](Interactable.md) | The sender of a connection. |
| `child` | [Joint](Joint.md) | The receiver of a connection. |

### disconnect {#disconnect}

``` { .lua .api-signature }
interactable:disconnect( child )
```

Disconnects two interactables. Similar to using the Connect Tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `parent` | [Interactable](Interactable.md) | The sender of a connection. |
| `child` | [Interactable](Interactable.md) | The receiver of a connection. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the disconnect attempt was successful. |

### getCarryData {#getcarrydata}

``` { .lua .api-signature }
interactable:getCarryData(  )
```

Get carry data for a script interactable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable, needs to be of script type. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
interactable:getPublicData(  )
```

Returns (server) public data from a interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### removeContainer {#removecontainer}

``` { .lua .api-signature }
interactable:removeContainer( index )
```

Removes the container stored in the given index inside the controller

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index of the container. |

### setActive {#setactive}

``` { .lua .api-signature }
interactable:setActive( signal )
```

Sets the logic output signal of an interactable. Signal is a boolean, <strong>on</strong> or <strong>off</strong>.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `signal` | boolean | The logic output signal. |

### setCarryData {#setcarrydata}

``` { .lua .api-signature }
interactable:setCarryData( data )
```

Set carry data for a script interactable

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable, needs to be of script type. |
| `data` | any | The carry data. |

### setJointCustomData {#setjointcustomdata}

``` { .lua .api-signature }
interactable:setJointCustomData( joint, data )
```

Sets custom joint script data.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable, needs to be of script type. |
| `joint` | [Joint](Joint.md) | The joint. |
| `data` | any | The data. |

### setLightOverrideColor {#setlightoverridecolor}

``` { .lua .api-signature }
interactable:setLightOverrideColor( color )
```

Set the override color of a light controller, ignoring the color of the shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `color` | [Color](Color.md) | The color to override with. |

### setPower {#setpower}

``` { .lua .api-signature }
interactable:setPower( signal )
```

Sets the power output signal of an interactable. Signal is a number between -1 to 1, where 1 is forward and -1 backward.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `signal` | number | The power output signal. |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
interactable:setPublicData( data )
```

Sets (server) public data on a interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `data` | table | The public data. |

## Client-only

### getAnimDuration {#getanimduration}

``` { .lua .api-signature }
interactable:getAnimDuration( name )
```

Returns animation duration in seconds.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The name of the animation. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The animation duration. |

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
interactable:getClientPublicData(  )
```

Returns (client) public data from a interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### getGlowMultiplier {#getglowmultiplier}

``` { .lua .api-signature }
interactable:getGlowMultiplier(  )
```

Gets the glow multiplier.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The glow multiplier (0.0 - 1.0). |

### getPoseWeight {#getposeweight}

``` { .lua .api-signature }
interactable:getPoseWeight( index )
```

Returns the pose weight of the pose in the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The pose weight. |

### getUvFrameIndex {#getuvframeindex}

``` { .lua .api-signature }
interactable:getUvFrameIndex(  )
```

Returns the index of the current UV animation frame

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The uv frame. |

### hasAnim {#hasanim}

``` { .lua .api-signature }
interactable:hasAnim( name )
```

Checks if an animation exists.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The name of the animation. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if exists, false otherwise. |

### isAnimLooping {#isanimlooping}

``` { .lua .api-signature }
interactable:isAnimLooping( name )
```

Returns if the animation isLooping or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The name of the animation. |

**Returns:**

| Type | Description |
| --- | --- |
| bool | Is the animation looping. |

### setAnimEnabled {#setanimenabled}

``` { .lua .api-signature }
interactable:setAnimEnabled( name, enabled )
```

Sets whether the animation with the given name should be applied to the mesh. True enables the animation and false disables it.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The name of the animation. |
| `enabled` | boolean | The boolean enable state. |

### setAnimProgress {#setanimprogress}

``` { .lua .api-signature }
interactable:setAnimProgress( name, progress )
```

Sets the progress on the animation with the given name.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | The name of the animation. |
| `progress` | number | The animation's progress between 0 and 1. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
interactable:setClientPublicData( data )
```

Sets (client) public data on a interactable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `data` | table | The public data. |

### setGlowMultiplier {#setglowmultiplier}

``` { .lua .api-signature }
interactable:setGlowMultiplier( value )
```

Sets a value to multiply the glow from asg texture with.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `value` | number | The glow multiplier (0.0 - 1.0). |

### setGyroDirection {#setgyrodirection}

``` { .lua .api-signature }
interactable:setGyroDirection( direction )
```

Set the direction of the gyro

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `direction` | [Vec3](Vec3.md) | The gyro direction. |

### setPoseWeight {#setposeweight}

``` { .lua .api-signature }
interactable:setPoseWeight( index, value )
```

Set the pose weight of the pose in the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index. |
| `value` | number | The pose weight. |

### setSteeringJointLeftAngleLimit {#setsteeringjointleftanglelimit}

``` { .lua .api-signature }
interactable:setSteeringJointLeftAngleLimit( joint, value )
```

Sets the left angle limit settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `value` | number | The left angle limit. |

### setSteeringJointLeftAngleSpeed {#setsteeringjointleftanglespeed}

``` { .lua .api-signature }
interactable:setSteeringJointLeftAngleSpeed( joint, value )
```

Sets the left angle speed settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `value` | number | The left angle speed. |

### setSteeringJointRightAngleLimit {#setsteeringjointrightanglelimit}

``` { .lua .api-signature }
interactable:setSteeringJointRightAngleLimit( joint, value )
```

Sets the right angle limit settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `value` | number | The right angle limit. |

### setSteeringJointRightAngleSpeed {#setsteeringjointrightanglespeed}

``` { .lua .api-signature }
interactable:setSteeringJointRightAngleSpeed( joint, value )
```

Sets the right angle speed settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `value` | number | The right angle speed. |

### setSteeringJointSettings {#setsteeringjointsettings}

``` { .lua .api-signature }
interactable:setSteeringJointSettings(
    joint,
    leftAngleSpeed,
    rightAngleSpeed,
    leftAngleLimit,
    rightAngleLimit,
    unlocked
)
```

Sets the settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `leftAngleSpeed` | number | The left angle speed. |
| `rightAngleSpeed` | number | The right angle speed. |
| `leftAngleLimit` | number | The left angle limit. |
| `rightAngleLimit` | number | The right angle limit. |
| `unlocked` | boolean | Whether the joint is unlocked. |

### setSteeringJointUnlocked {#setsteeringjointunlocked}

``` { .lua .api-signature }
interactable:setSteeringJointUnlocked( joint, value )
```

Sets unlocked settings of a [Joint](Joint.md) connected to a steering [Interactable](Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `joint` | [Joint](Joint.md) | The joint. |
| `value` | boolean | true if joint is unlocked |

### setSubMeshVisible {#setsubmeshvisible}

``` { .lua .api-signature }
interactable:setSubMeshVisible( name, visible )
```

Set the visibility of a submesh

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `name` | string | Name of the submesh. |
| `visible` | boolean | True if the submesh should be visible. |

### setUvFrameIndex {#setuvframeindex}

``` { .lua .api-signature }
interactable:setUvFrameIndex( index )
```

Sets the UV animation frame with the given index.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](Interactable.md) | The interactable. |
| `index` | integer | The index. |
