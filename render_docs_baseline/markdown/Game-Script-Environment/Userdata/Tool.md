# Tool

**Associated namespace:** [sm.tool](../Static-Functions/sm.tool.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>tool</strong> in the game.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a tool.

- <a id="uuid"></a>`uuid` [ **[Uuid](Uuid.md)** ] <br>
    - `Get`: Returns the tool type uuid.

## Server + Client

### getId {#getid}

``` { .lua .api-signature }
tool:getId(  )
```

Returns the id of a tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The tool's id. |

### getOwner {#getowner}

``` { .lua .api-signature }
tool:getOwner(  )
```

Returns the player that owns the tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Player](Player.md) | The tool's owner. |

### getUuid {#getuuid}

``` { .lua .api-signature }
tool:getUuid(  )
```

Returns the tool type uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | The tool's uuid. |

### setInteractionTextSuppressed {#setinteractiontextsuppressed}

``` { .lua .api-signature }
tool:setInteractionTextSuppressed(  )
```

> **Deprecated:**
> Deprecated function. Kept for compability with old scripts.
>

Does nothing.

## Client-only

### getAnimationInfo {#getanimationinfo}

``` { .lua .api-signature }
tool:getAnimationInfo( name )
```

Returns general information for a third person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table containing "name", "duration" and "looping". |

### getCameraWeights {#getcameraweights}

``` { .lua .api-signature }
tool:getCameraWeights(  )
```

Get the current weights for the tool's local camera settings.

**Returns:**

| Type | Description |
| --- | --- |
| {number, number} | The third-person weight and the first-person weight |

### getDirection {#getdirection}

``` { .lua .api-signature }
tool:getDirection(  )
```

Returns the direction of where the player is viewing or aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The player's view direction. |

### getFpAnimationInfo {#getfpanimationinfo}

``` { .lua .api-signature }
tool:getFpAnimationInfo( name )
```

Returns general information for a first person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table containing "name", "duration" and "looping". |

### getFpBoneDir {#getfpbonedir}

``` { .lua .api-signature }
tool:getFpBoneDir( jointName, convertToWorldSpace? )
```

Returns the local or world direction for a bone in the first person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |
| `convertToWorldSpace` *(optional)* | boolean | Whether to convert the position to world space. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint direction. |

### getFpBonePos {#getfpbonepos}

``` { .lua .api-signature }
tool:getFpBonePos( jointName, convertToWorldSpace? )
```

Returns the local or world position for a bone in the first person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |
| `convertToWorldSpace` *(optional)* | boolean | Whether to convert the position to world space. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint position. |

### getFpBoneRot {#getfpbonerot}

``` { .lua .api-signature }
tool:getFpBoneRot( jointName, convertToWorldSpace? )
```

Returns the local or world rotation for a bone in the first person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |
| `convertToWorldSpace` *(optional)* | boolean | Whether to convert the position to world space. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The joint rotation. |

### getMovementSpeedFraction {#getmovementspeedfraction}

``` { .lua .api-signature }
tool:getMovementSpeedFraction(  )
```

Returns the fraction of the player's movement speed in proportion to its maximum. This is affected by sprinting, crouching, blocking, aiming, etc.

| Value | Description |
| --- | --- |
| sprinting | 1.0 |
| walking | 0.5 |
| crouching | 0.375 |
| aiming | 0.3125 |

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The player's movement speed fraction. |

### getMovementVelocity {#getmovementvelocity}

``` { .lua .api-signature }
tool:getMovementVelocity(  )
```

Returns the movement velocity of the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The player's velocity. |

### getPosition {#getposition}

``` { .lua .api-signature }
tool:getPosition(  )
```

Returns the world position of the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The player's world position. |

### getRelativeMoveDirection {#getrelativemovedirection}

``` { .lua .api-signature }
tool:getRelativeMoveDirection(  )
```

Returns the relative movement direction of the player. This is the direction the player wants to move based on movement input.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The player's relative movement direction. |

### getSmoothDirection {#getsmoothdirection}

``` { .lua .api-signature }
tool:getSmoothDirection(  )
```

Returns the smooth direction of where the player is viewing or aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The player's smooth view direction. |

### getTpBoneDir {#gettpbonedir}

``` { .lua .api-signature }
tool:getTpBoneDir( jointName )
```

Returns the world direction for a bone in the third person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint direction. |

### getTpBonePos {#gettpbonepos}

``` { .lua .api-signature }
tool:getTpBonePos( jointName )
```

Returns the world position for a bone in the third person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The joint position. |

### getTpBoneRot {#gettpbonerot}

``` { .lua .api-signature }
tool:getTpBoneRot( jointName )
```

Returns the world rotations for a bone in the third person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The joint rotation. |

### isCrouching {#iscrouching}

``` { .lua .api-signature }
tool:isCrouching(  )
```

Returns whether the player is currently crouching.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is crouching. |

### isEquipped {#isequipped}

``` { .lua .api-signature }
tool:isEquipped(  )
```

Returns whether the tool is equipped or not.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | whether the tool is equipped or not. |

### isInFirstPersonView {#isinfirstpersonview}

``` { .lua .api-signature }
tool:isInFirstPersonView(  )
```

Returns whether the player is in first person view where the viewpoint is rendered from the player's perspective. Otherwise, the player is in third person view where the camera is behind the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is in first person view. |

### isLocal {#islocal}

``` { .lua .api-signature }
tool:isLocal(  )
```

Returns whether the player holding the tool is the as [sm.localPlayer](../Static-Functions/sm.localPlayer.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is the local player. |

### isOnGround {#isonground}

``` { .lua .api-signature }
tool:isOnGround(  )
```

Returns whether the player is currently standing on the ground.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is on the ground. |

### isSprinting {#issprinting}

``` { .lua .api-signature }
tool:isSprinting(  )
```

Returns whether the player is currently sprinting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is sprinting. |

### setBlockSprint {#setblocksprint}

``` { .lua .api-signature }
tool:setBlockSprint( block )
```

Sets whether the player is unable to sprint. Sprinting is normally blocked when the player is attacking, blocking, aiming, etc.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `block` | boolean | Whether the player's sprinting is blocked. |

### setCrossHairAlpha {#setcrosshairalpha}

``` { .lua .api-signature }
tool:setCrossHairAlpha( alpha )
```

Sets the opacity of the crosshair. An alpha value of 0 makes the crosshair transparent.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `alpha` | number | The alpha value for the crosshair. |

### setCrossHairColor {#setcrosshaircolor}

``` { .lua .api-signature }
tool:setCrossHairColor( color )
```

Sets the color of the crosshair. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `color` | [Color](Color.md) | The color. |

### setCrossHairType {#setcrosshairtype}

``` { .lua .api-signature }
tool:setCrossHairType( type )
```

Sets the type of the crosshair. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `type` | number | The type value for the crosshair. |

### setDispersionFraction {#setdispersionfraction}

``` { .lua .api-signature }
tool:setDispersionFraction( dispersion, dispersionSecondary? )
```

Sets the tool's dispersion fraction. This represents the accuracy of the tool, and affects the size of the player's crosshair.

A dispersion value of 0 is perfect accuracy, whereas 1 is the worst.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `dispersion` | number | The dispersion fraction. |
| `dispersionSecondary` *(optional)* | number | The secondary dispersion fraction for circles. (Optional) |

### setFpColor {#setfpcolor}

``` { .lua .api-signature }
tool:setFpColor( color )
```

Sets the color to be used for the tool in first person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `color` | [Color](Color.md) | The color. |

### setFpRenderables {#setfprenderables}

``` { .lua .api-signature }
tool:setFpRenderables( renderables )
```

Sets the renderables (files containing model data) to be used for the character in first person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `renderables` | table | The table of renderables names {string, ..} |

### setMovementAnimation {#setmovementanimation}

``` { .lua .api-signature }
tool:setMovementAnimation( name, animation )
```

Sets the current third person view movement animation to be used by the tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The name. |
| `animation` | string | The animation. |

### setMovementSlowDown {#setmovementslowdown}

``` { .lua .api-signature }
tool:setMovementSlowDown( slowDown )
```

Sets whether the player is slowed down. This is similar to crouching and normally occurs when the player is aiming.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `slowDown` | boolean | Whether the player movement is slowed down. |

### setTpColor {#settpcolor}

``` { .lua .api-signature }
tool:setTpColor( color )
```

Sets the color to be used for the tool in third person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `color` | [Color](Color.md) | The color. |

### setTpRenderables {#settprenderables}

``` { .lua .api-signature }
tool:setTpRenderables( renderables )
```

Sets the renderables (files containing model data) to be used for the character in third person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `renderables` | table | The table of renderables names. {string, ..} |

### updateAnimation {#updateanimation}

``` { .lua .api-signature }
tool:updateAnimation( name, time, weight? )
```

Updates a third person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The animation name. |
| `time` | number | The time. |
| `weight` *(optional)* | number | The weight. (Defaults to -1.0) |

### updateCamera {#updatecamera}

``` { .lua .api-signature }
tool:updateCamera( distance, fov, offset, weight )
```

Updates the third person view camera for the tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `distance` | number | The distance. |
| `fov` | number | The fov. |
| `offset` | [Vec3](Vec3.md) | The offset. |
| `weight` | number | The weight. |

### updateFpAnimation {#updatefpanimation}

``` { .lua .api-signature }
tool:updateFpAnimation( name, time, weight?, looping? )
```

Updates a first person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The name. |
| `time` | number | The time. |
| `weight` *(optional)* | number | The weight. (Defaults to -1.0) |
| `looping` *(optional)* | boolean | The looping. (Defaults to false) |

### updateFpCamera {#updatefpcamera}

``` { .lua .api-signature }
tool:updateFpCamera( fov, offset, weight, bobbing )
```

Updates the first person view camera for the tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `fov` | number | The fov. |
| `offset` | [Vec3](Vec3.md) | The offset. |
| `weight` | number | The weight. |
| `bobbing` | number | The bobbing. |

### updateJoint {#updatejoint}

``` { .lua .api-signature }
tool:updateJoint( name, rotation, weight? )
```

Sets the rotation and weight for a bone in the animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `name` | string | The name. |
| `rotation` | [Vec3](Vec3.md) | The rotation. |
| `weight` *(optional)* | number | The weight. (Defaults to -1.0) |

### updateMovementAnimation {#updatemovementanimation}

``` { .lua .api-signature }
tool:updateMovementAnimation( time, weight? )
```

Updates the currently set third person view movement animation for the tool.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](Tool.md) | The tool. |
| `time` | number | The time. |
| `weight` *(optional)* | number | The weight. (Defaults to -1.0) |
