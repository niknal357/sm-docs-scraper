# Character

**Associated namespace:** [sm.character](../Static-Functions/sm.character.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>character</strong> in the game.

**Values:**

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns client public data from a character.
    - `Set`: (Client-Only) Sets client public data on a character.

- <a id="color"></a>`color` [ **[Color](Color.md)** ] <br>
    - `Get`: Returns the base color of a character.
    - `Set`: (Server-Only) Sets the character color.

- <a id="direction"></a>`direction` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the direction of where a character is viewing or aiming.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a character.

- <a id="mass"></a>`mass` [ **number** ] <br>
    - `Get`: Returns the mass of a character.

- <a id="movementspeedfraction"></a>`movementSpeedFraction` [ **number** ] <br>
    - `Get`: Gets the current fraction multiplier applied on the character's movement speed.
    - `Set`: Sets a fraction multiplier to the character's movement speed.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a character.
    - `Set`: (Server-Only) Sets (server) public data on a character.

- <a id="smoothdirection"></a>`smoothDirection` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the smooth direction of where a character is viewing or aiming.

- <a id="velocity"></a>`velocity` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the velocity of a character.

- <a id="world"></a>`world` [ **[World](World.md)** ] <br>
    - `Get`: Returns the world a character exists in.

- <a id="worldposition"></a>`worldPosition` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of a character.
    - `Set`: (Server-Only) Sets the world position of a character.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Character == Character` | boolean | Checks if two instances of [Character](Character.md) refer to the same Character. |

## Server + Client

### applyTumblingImpulse {#applytumblingimpulse}

``` { .lua .api-signature }
character:applyTumblingImpulse( impulse, offset? )
```

Applies impulse to the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `impulse` | [Vec3](Vec3.md) | The impulse. |
| `offset` *(optional)* | [Vec3](Vec3.md) | The offset from the center point. (Defaults to no offset) |

### bindAnimationCallback {#bindanimationcallback}

``` { .lua .api-signature }
character:bindAnimationCallback( animationName, triggerTime, callback )
```

Binds a character's animation to a callback function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `animationName` | string | The name of the animation. |
| `triggerTime` | number | The required time that will have elapsed in the animation when the callback is triggered. |
| `callback` | string | The name of the Lua function to bind. |

### getActiveAnimations {#getactiveanimations}

``` { .lua .api-signature }
character:getActiveAnimations(  )
```

Returns the set of active animations.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The set of active animations { { name = string, weight = number }, ...} |

### getCanSwim {#getcanswim}

``` { .lua .api-signature }
character:getCanSwim(  )
```

Returns whether the character will float or sink in liquid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the character will float, false if the character will sink. |

### getCharacterType {#getcharactertype}

``` { .lua .api-signature }
character:getCharacterType(  )
```

Returns the uuid of the character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | The character type. |

### getColor {#getcolor}

``` { .lua .api-signature }
character:getColor(  )
```

Returns the base color of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The character color. |

### getCurrentMovementNoiseRadius {#getcurrentmovementnoiseradius}

``` { .lua .api-signature }
character:getCurrentMovementNoiseRadius(  )
```

Returns the radius around the character where it can be heard.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The noise radius of the character. |

### getCurrentMovementSpeed {#getcurrentmovementspeed}

``` { .lua .api-signature }
character:getCurrentMovementSpeed(  )
```

Returns the current movement speed of the character depending on state and multiplier.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The current movement speed. |

### getDirection {#getdirection}

``` { .lua .api-signature }
character:getDirection(  )
```

Returns the direction of where a character is viewing or aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The character's view direction. |

### getHeight {#getheight}

``` { .lua .api-signature }
character:getHeight(  )
```

Returns the height of a character

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The character's height. |

### getId {#getid}

``` { .lua .api-signature }
character:getId(  )
```

Returns the id of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The character's id. |

### getJumpSpeedFraction {#getjumpspeedfraction}

``` { .lua .api-signature }
character:getJumpSpeedFraction(  )
```

Gets the current fraction multiplier applied on the character's jump speed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The jump speed fraction. |

### getLockingHarvestable {#getlockingharvestable}

``` { .lua .api-signature }
character:getLockingHarvestable(  )
```

Get the [Harvestable](Harvestable.md) that the [Character](Character.md) is locked to.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](Harvestable.md) | The harvestable. |

### getLockingInteractable {#getlockinginteractable}

``` { .lua .api-signature }
character:getLockingInteractable(  )
```

Get the [Interactable](Interactable.md) that the [Character](Character.md) is locked to.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Interactable](Interactable.md) | The interactable. |

### getMass {#getmass}

``` { .lua .api-signature }
character:getMass(  )
```

Returns the mass of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The character's mass. |

### getMoveSpeed {#getmovespeed}

``` { .lua .api-signature }
character:getMoveSpeed(  )
```

Returns the move speed of a character

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The character's move speed. |

### getMovementSpeedFraction {#getmovementspeedfraction}

``` { .lua .api-signature }
character:getMovementSpeedFraction(  )
```

Gets the current fraction multiplier applied on the character's movement speed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The movement speed fraction. |

### getPlayer {#getplayer}

``` { .lua .api-signature }
character:getPlayer(  )
```

Returns the player controlling the character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Player](Player.md) | The player controlling the character. |

### getRadius {#getradius}

``` { .lua .api-signature }
character:getRadius(  )
```

Returns the radius of a character

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The character's radius. |

### getSmoothViewDirection {#getsmoothviewdirection}

``` { .lua .api-signature }
character:getSmoothViewDirection(  )
```

Returns the smooth direction of where a character is viewing or aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The character's smooth view direction. |

### getSprintSpeed {#getsprintspeed}

``` { .lua .api-signature }
character:getSprintSpeed(  )
```

Returns the sprint speed of a character

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The character's sprint speed. |

### getSurfaceNormal {#getsurfacenormal}

``` { .lua .api-signature }
character:getSurfaceNormal(  )
```

Returns the normal of the character's contact with a surface. Defaults to a zero vector when no contact is found.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The surface normal. |

### getTpBonePos {#gettpbonepos}

``` { .lua .api-signature }
character:getTpBonePos( jointName )
```

Returns the world position for a bone in the third person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint position. |

### getTpBoneRot {#gettpbonerot}

``` { .lua .api-signature }
character:getTpBoneRot( jointName )
```

Returns the world rotation for a bone in the third person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The joint rotation. |

### getTumblingAngularVelocity {#gettumblingangularvelocity}

``` { .lua .api-signature }
character:getTumblingAngularVelocity(  )
```

Returns the angular velocity of the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The tumbling shape's angular velocity. |

### getTumblingExtent {#gettumblingextent}

``` { .lua .api-signature }
character:getTumblingExtent(  )
```

Returns the extent of the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The tumbling shape's extent. |

### getTumblingLinearVelocity {#gettumblinglinearvelocity}

``` { .lua .api-signature }
character:getTumblingLinearVelocity(  )
```

Returns the linear velocity of the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The tumbling shape's linear velocity. |

### getTumblingWorldPosition {#gettumblingworldposition}

``` { .lua .api-signature }
character:getTumblingWorldPosition(  )
```

Returns the world position of the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The tumbling shape's world position. |

### getTumblingWorldRotation {#gettumblingworldrotation}

``` { .lua .api-signature }
character:getTumblingWorldRotation(  )
```

Returns the world rotation of the characters tumbling shape.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The tumbling shape's world rotation. |

### getUnit {#getunit}

``` { .lua .api-signature }
character:getUnit(  )
```

Returns the unit controlling the character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Unit](Unit.md) | The unit controlling the character. |

### getVelocity {#getvelocity}

``` { .lua .api-signature }
character:getVelocity(  )
```

Returns the velocity of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The character's velocity. |

### getWorld {#getworld}

``` { .lua .api-signature }
character:getWorld(  )
```

Returns the world a character exists in.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The world the character exists in. |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
character:getWorldPosition(  )
```

Returns the world position of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The character's world position. |

### isAiming {#isaiming}

``` { .lua .api-signature }
character:isAiming(  )
```

Returns whether a character is currently aiming with a weapon.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is aiming. |

### isClimbing {#isclimbing}

``` { .lua .api-signature }
character:isClimbing(  )
```

Get the character climbing state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The climbing state. |

### isCrouching {#iscrouching}

``` { .lua .api-signature }
character:isCrouching(  )
```

Returns whether a character is currently crouching.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is crouching. |

### isDefaultColor {#isdefaultcolor}

``` { .lua .api-signature }
character:isDefaultColor(  )
```

Returns true if the current character color is its default color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the color is the base color. |

### isDiving {#isdiving}

``` { .lua .api-signature }
character:isDiving(  )
```

Get the character diving state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The diving state. |

### isDowned {#isdowned}

``` { .lua .api-signature }
character:isDowned(  )
```

Get the character downed state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The downed state. |

### isFlying {#isflying}

``` { .lua .api-signature }
character:isFlying(  )
```

Get the character flying state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The flying state. |

### isHovering {#ishovering}

``` { .lua .api-signature }
character:isHovering(  )
```

Get the character hovering state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The hovering state. |

### isLadderClimbing {#isladderclimbing}

``` { .lua .api-signature }
character:isLadderClimbing(  )
```

Get whether the character is climbing a ladder.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The ladder climbing state. |

### isMoving {#ismoving}

``` { .lua .api-signature }
character:isMoving(  )
```

Returns whether a character is currently moving.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is moving. |

### isOnGround {#isonground}

``` { .lua .api-signature }
character:isOnGround(  )
```

Returns whether the character is currently standing on the ground.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is on the ground. |

### isPlayer {#isplayer}

``` { .lua .api-signature }
character:isPlayer(  )
```

Returns whether a character is owned by a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is owned by a player. |

### isSeated {#isseated}

``` { .lua .api-signature }
character:isSeated(  )
```

Returns whether the character is currently seated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is seated. |

### isSprinting {#issprinting}

``` { .lua .api-signature }
character:isSprinting(  )
```

Returns whether a character is currently sprinting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is sprinting. |

### isSwimming {#isswimming}

``` { .lua .api-signature }
character:isSwimming(  )
```

Get the character swimming state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The swimming state. |

### isTumbling {#istumbling}

``` { .lua .api-signature }
character:isTumbling(  )
```

Get the character tumbling state.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The tumbling state. |

### removeAnimationCallbacks {#removeanimationcallbacks}

``` { .lua .api-signature }
character:removeAnimationCallbacks(  )
```

Removes all of a character's animation callbacks.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

### setJumpSpeedFraction {#setjumpspeedfraction}

``` { .lua .api-signature }
character:setJumpSpeedFraction( fraction )
```

Sets a fraction multiplier to the character's jump speed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `fraction` | number | The jump speed fraction. |

### setLockingHarvestable {#setlockingharvestable}

``` { .lua .api-signature }
character:setLockingHarvestable( harvestable )
```

Set the [Harvestable](Harvestable.md) that the [Character](Character.md) is locked to. Set [Harvestable](Harvestable.md) to nil to unlock.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `harvestable` | [Harvestable](Harvestable.md) | The harvestable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the character was successfully locked or unlocked. |

### setLockingInteractable {#setlockinginteractable}

``` { .lua .api-signature }
character:setLockingInteractable( interactable )
```

Set the [Interactable](Interactable.md) that the [Character](Character.md) is locked to. Set [Interactable](Interactable.md) to nil to unlock.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `interactable` | [Interactable](Interactable.md) | The interactable. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the character was successfully locked or unlocked. |

### setMovementEffects {#setmovementeffects}

``` { .lua .api-signature }
character:setMovementEffects( filepath )
```

Sets the movement effect set filepath.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `filepath` | string | The effect set filepath. |

### setMovementSpeedFraction {#setmovementspeedfraction}

``` { .lua .api-signature }
character:setMovementSpeedFraction( fraction )
```

Sets a fraction multiplier to the character's movement speed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `fraction` | number | The movement speed fraction. |

## Server-only

### getImmovable {#getimmovable}

``` { .lua .api-signature }
character:getImmovable(  )
```

Returns whether a non-player character is immovable,

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The immovable state of the character. |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
character:getPublicData(  )
```

Returns (server) public data from a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### setClimbing {#setclimbing}

``` { .lua .api-signature }
character:setClimbing( state )
```

Sets whether the character is climbing.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The climbing state. |

### setColor {#setcolor}

``` { .lua .api-signature }
character:setColor( color )
```

Sets the character color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `color` | [Color](Color.md) | The character color. |

### setDiving {#setdiving}

``` { .lua .api-signature }
character:setDiving( state )
```

Sets whether the character is diving.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The diving state. |

### setDowned {#setdowned}

``` { .lua .api-signature }
character:setDowned( state )
```

Sets whether the character is downed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The downed state. |

### setFlying {#setflying}

``` { .lua .api-signature }
character:setFlying( state )
```

Sets whether the character is flying.

Will not activate flight for player characters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The flying state. |

### setHovering {#sethovering}

``` { .lua .api-signature }
character:setHovering( state )
```

Sets whether the character is hovering.

Will not activate hover for player characters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The hovering state. |

### setImmovable {#setimmovable}

``` { .lua .api-signature }
character:setImmovable( enable )
```

Sets the immovable state on a non-player character. This prevents the character from updating its physics.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `enable` | boolean | Set immovable state. |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
character:setPublicData( data )
```

Sets (server) public data on a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `data` | table | The public data. |

### setSwimming {#setswimming}

``` { .lua .api-signature }
character:setSwimming( state )
```

Sets whether the character is swimming.

> **Note:**
> By default the swimming state is controlled by the client as part of the player movement. This value is treated like an override that is synchronized from the server. Buoyancy calculations in the character controller require that the character touches a liquid volume.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The swimming state. |

### setTumbling {#settumbling}

``` { .lua .api-signature }
character:setTumbling( state )
```

Sets whether the character is tumbling.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `state` | boolean | The tumbling state. |

### setWorldPosition {#setworldposition}

``` { .lua .api-signature }
character:setWorldPosition( position )
```

Sets the world position of a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `position` | [Vec3](Vec3.md) | The character's new world position. |

## Client-only

### addRenderable {#addrenderable}

``` { .lua .api-signature }
character:addRenderable( renderable )
```

Adds a renderable (file containing model data) to be used for the character in third person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `renderable` | string | The renderable path. |

### getAnimationInfo {#getanimationinfo}

``` { .lua .api-signature }
character:getAnimationInfo( name )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The animation info { name = string, duration = number, looping = boolean }. |

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
character:getClientPublicData(  )
```

Returns client public data from a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The client public data. |

### getGlowMultiplier {#getglowmultiplier}

``` { .lua .api-signature }
character:getGlowMultiplier(  )
```

Gets the glow multiplier.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The glow multiplier (0.0 - 1.0). |

### hasActiveOverrideAnimation {#hasactiveoverrideanimation}

``` { .lua .api-signature }
character:hasActiveOverrideAnimation(  )
```

Returns whether or not the character has an active animation override on its third person animations.

A third person animation override could be the crowbar animation when picking something up or the hammer when placing something.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Character](Character.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| bool | Has active animation override. |

### hasGraphics {#hasgraphics}

``` { .lua .api-signature }
character:hasGraphics(  )
```

Checks if a character has graphics.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character has graphics. |

### isVisible {#isvisible}

``` { .lua .api-signature }
character:isVisible(  )
```

Returns whether a character is visible.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the character is visible. |

### overrideRenderableList {#overriderenderablelist}

``` { .lua .api-signature }
character:overrideRenderableList( renderables )
```

Overrides a non player character's third person renderable list with a new list of renderables. Will trigger a rebuild of the character's graphics.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `renderables` | table | An array of renderable file paths to override with. |

### removeRenderable {#removerenderable}

``` { .lua .api-signature }
character:removeRenderable( renderable )
```

Removes a renderable (file containing model data) that was used for the character in third person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `renderable` | string | The renderable path. |

### setAllowTumbleAnimations {#setallowtumbleanimations}

``` { .lua .api-signature }
character:setAllowTumbleAnimations( allow )
```

Enables or disables event animations.

When set to false no animations can play while tumble is active, and when set to true the animations will play while tumbling.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `allow` | boolean | The state. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
character:setClientPublicData( data )
```

Sets client public data on a character.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `data` | table | The client public data. |

### setGlowMultiplier {#setglowmultiplier}

``` { .lua .api-signature }
character:setGlowMultiplier( value )
```

Sets a value to multiply the glow from asg texture with.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `value` | number | The glow multiplier (0.0 - 1.0). |

### setMovementWeights {#setmovementweights}

``` { .lua .api-signature }
character:setMovementWeights( lower, upper )
```

Sets the weights for movement animations on a character's upper and lower body.

For a value of 0 no movement animations will play, and for a value of 1 the movement animations will fully play unless otherwise overridden.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `lower` | number | The lower weight. |
| `upper` | number | The upper weight. |

### setNameTag {#setnametag}

``` { .lua .api-signature }
character:setNameTag(
    name,
    color?,
    requiresLoS?,
    renderDistance?,
    fadeDistance?
)
```

Sets the name tag display value for the character

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `name` | string | The new name tag text value. |
| `color` *(optional)* | [Color](Color.md) | The color of the name. (defaults to white) |
| `requiresLoS` *(optional)* | boolean | Whether broken line of sight will hide the name tag. (Defaults to false) |
| `renderDistance` *(optional)* | number | Max distance the name tag will render in. (Defaults to 10000) |
| `fadeDistance` *(optional)* | number | Distance where fade out will start. (Defaults to 9500) |

### setUpDirection {#setupdirection}

``` { .lua .api-signature }
character:setUpDirection( up )
```

Sets the upward direction of the character's graphics.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `up` | [Vec3](Vec3.md) | The direction. |

### setVisible {#setvisible}

``` { .lua .api-signature }
character:setVisible( visible )
```

Sets the visibility.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `visible` | boolean | Whether the character should be visible. |

### updateAnimation {#updateanimation}

``` { .lua .api-signature }
character:updateAnimation( name, time, weight?, additive? )
```

Updates a character animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](Character.md) | The character. |
| `name` | string | The animation name. |
| `time` | number | The time. |
| `weight` *(optional)* | number | The weight. Defaults to -1.0. (Optional) |
| `additive` *(optional)* | boolean | Whether the animation will be added to the default animation. Defaults to false. (Optional) |
