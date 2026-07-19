# sm.localPlayer

<strong>Local player</strong> represents the current character being controlled on the client's computer. This library can only be used on the client.

For more information about other players in the world, see [sm.player](sm.player.md).

## Client-only

### addRenderable {#addrenderable}

``` { .lua .api-signature }
sm.localPlayer.addRenderable( renderable )
```

Adds a renderable (file containing model data) to be used for the local player in first person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `renderable` | string | The renderable path. |

### getActiveItem {#getactiveitem}

``` { .lua .api-signature }
sm.localPlayer.getActiveItem(  )
```

Returns the item currently held by the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The player's held item uuid. |

### getAimSensitivity {#getaimsensitivity}

``` { .lua .api-signature }
sm.localPlayer.getAimSensitivity(  )
```

Return the player aim sensitivity

**Returns:**

| Type | Description |
| --- | --- |
| number | The aim sensitivity |

### getCarry {#getcarry}

``` { .lua .api-signature }
sm.localPlayer.getCarry(  )
```

Returns the carrying container of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Container](../Userdata/Container.md) | The player's carry. |

### getCarryColor {#getcarrycolor}

``` { .lua .api-signature }
sm.localPlayer.getCarryColor(  )
```

Returns the color of the shape the local player is carrying.

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) | The color of the shape the local player is carrying. |

### getConstructionPlacement {#getconstructionplacement}

``` { .lua .api-signature }
sm.localPlayer.getConstructionPlacement(  )
```

Gets the world position and rotation of the local player's shape placement if it is not colliding. Otherwise nil is returned.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md), [Quat](../Userdata/Quat.md) | World position and rotation. |

### getDirection {#getdirection}

``` { .lua .api-signature }
sm.localPlayer.getDirection(  )
```

Returns the direction the local player is aiming.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The direction of the player's aim. |

### getFpAnimationInfo {#getfpanimationinfo}

``` { .lua .api-signature }
sm.localPlayer.getFpAnimationInfo( name )
```

Returns general information for a first person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table containing name, duration and looping. |

### getFpBonePos {#getfpbonepos}

``` { .lua .api-signature }
sm.localPlayer.getFpBonePos( jointName )
```

Returns the world position for a bone in the first person view animation skeleton.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `jointName` | string | The joint name. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The joint position. |

### getGarmentName {#getgarmentname}

``` { .lua .api-signature }
sm.localPlayer.getGarmentName( uuid )
```

Gets the title of the garment with the given uuid in the current language.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The garment. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The title of the garment |

### getGarmentUpperCaseTitle {#getgarmentuppercasetitle}

``` { .lua .api-signature }
sm.localPlayer.getGarmentUpperCaseTitle( uuid )
```

Gets the UPPER CASE title of the garment with the given uuid in the current language.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The garment. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The title of the garment |

### getHotbar {#gethotbar}

``` { .lua .api-signature }
sm.localPlayer.getHotbar(  )
```

Returns the hotbar container of the player.

**Returns:**

| Type | Description |
| --- | --- |
| [Container](../Userdata/Container.md) | The player's hotbar. |

### getId {#getid}

``` { .lua .api-signature }
sm.localPlayer.getId(  )
```

Returns the unique player id of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| integer | The player's id. |

### getInventory {#getinventory}

``` { .lua .api-signature }
sm.localPlayer.getInventory(  )
```

Returns the inventory container of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Container](../Userdata/Container.md) | The player's inventory. |

### getLatestRaycast {#getlatestraycast}

``` { .lua .api-signature }
sm.localPlayer.getLatestRaycast(  )
```

Returns the latest interaction raycast result of the local player. This is the raycast that is constantly performed to detect interactable objects up to a range of 7.5.

**Returns:**

| Type | Description |
| --- | --- |
| bool, [RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; Raycast result data. |

### getMouseDelta {#getmousedelta}

``` { .lua .api-signature }
sm.localPlayer.getMouseDelta(  )
```

Returns delta positions of mouse

**Returns:**

| Type | Description |
| --- | --- |
| number,number | Delta X; Delta Y |

### getOwnedLift {#getownedlift}

``` { .lua .api-signature }
sm.localPlayer.getOwnedLift(  )
```

Returns the [Lift](../Userdata/Lift.md) of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Lift](../Userdata/Lift.md) | The player's lift. |

### getPlayer {#getplayer}

``` { .lua .api-signature }
sm.localPlayer.getPlayer(  )
```

Returns the player object of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Player](../Userdata/Player.md) | The player object. |

### getPosition {#getposition}

``` { .lua .api-signature }
sm.localPlayer.getPosition(  )
```

> **Deprecated:**
> Use [Character.worldPosition](../Userdata/Character.md#worldposition) or [Character.getWorldPosition](../Userdata/Character.md#getworldposition)
>

Returns the world position of the local player.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The player's world position. |

### getRaycast {#getraycast}

``` { .lua .api-signature }
sm.localPlayer.getRaycast( range, origin?, direction? )
```

Performs a <a target="_blank" href="https://en.wikipedia.org/wiki/Ray_casting">raycast</a> relative to the local player's perspective.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `range` | number | The maximum range. |
| `origin` *(optional)* | [Vec3](../Userdata/Vec3.md) | The start position. (Defaults to [sm.localPlayer.getRaycastStart](#getraycaststart)) |
| `direction` *(optional)* | [Vec3](../Userdata/Vec3.md) | The direction. (Defaults to [sm.localPlayer.getDirection](#getdirection)) |

**Returns:**

| Type | Description |
| --- | --- |
| bool, [RaycastResult](../Userdata/RaycastResult.md) | True if raycast was successful; Raycast result data. |

### getRaycastStart {#getraycaststart}

``` { .lua .api-signature }
sm.localPlayer.getRaycastStart(  )
```

Returns the start position of the local player's raycast. The position depends on the [camera](sm.camera.md)'s position, and whether it's in first- of third-person.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The start position of the raycast. |

### getRight {#getright}

``` { .lua .api-signature }
sm.localPlayer.getRight(  )
```

Returns the right-vector perpendicular to the local player's aim.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The right-vector of the player's aim. |

### getSelectedHotbarSlot {#getselectedhotbarslot}

``` { .lua .api-signature }
sm.localPlayer.getSelectedHotbarSlot(  )
```

Returns the local player's selected slot.

**Returns:**

| Type | Description |
| --- | --- |
| integer | The player's selected slot. |

### getUp {#getup}

``` { .lua .api-signature }
sm.localPlayer.getUp(  )
```

Returns the up-vector perpendicular to the local player's aim.

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](../Userdata/Vec3.md) | The up-vector of the player's aim. |

### getWantsSprint {#getwantssprint}

``` { .lua .api-signature }
sm.localPlayer.getWantsSprint(  )
```

Checks if local player wants to sprint (pressing the sprint key).

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is holding the sprint key. |

### getWorld {#getworld}

``` { .lua .api-signature }
sm.localPlayer.getWorld(  )
```

Gets the world the local player's character is in, if any, otherwise nil.

**Returns:**

| Type | Description |
| --- | --- |
| [World](../Userdata/World.md) | The world the local player is in, if any. |

### grantQuestItem {#grantquestitem}

``` { .lua .api-signature }
sm.localPlayer.grantQuestItem( uid )
```

**Visibility:** Hidden

Unlocks a cosmetic with the given uuid for the player. Requires survival mode, non modified core files and no active mods to function.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uid` | [Uuid](../Userdata/Uuid.md) | The uuid of the unlocked cosmetic. |

### isGarmentUnlocked {#isgarmentunlocked}

``` { .lua .api-signature }
sm.localPlayer.isGarmentUnlocked( uuid )
```

Check if the garment has been granted to the local player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The garment. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the garment is unlocked. |

### isInFirstPersonView {#isinfirstpersonview}

``` { .lua .api-signature }
sm.localPlayer.isInFirstPersonView(  )
```

Returns whether the player is in first person view where the viewpoint is rendered from the player's perspective. Otherwise, the player is in third person view where the camera is behind the player.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether the player is in first person view. |

### removeRenderable {#removerenderable}

``` { .lua .api-signature }
sm.localPlayer.removeRenderable( renderable )
```

Removes a renderable (file containing model data) that was used for the local player in first person view.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `renderable` | string | The renderable path. |

### secondaryInteractBusy {#secondaryinteractbusy}

``` { .lua .api-signature }
sm.localPlayer.secondaryInteractBusy(  )
```

Returns if the currently equipped tool consumes the secondary interaction, such as aiming with the spudgun.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the tool consumes the secondary interaction. |

### setBlockSprinting {#setblocksprinting}

``` { .lua .api-signature }
sm.localPlayer.setBlockSprinting( blockSprinting )
```

Stops the local player from sprinting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blockSprinting` | boolean | Sets whether sprinting is blocked. |

### setDirection {#setdirection}

``` { .lua .api-signature }
sm.localPlayer.setDirection( direction )
```

Sets the direction of where the player is viewing or aiming. Intended to be used when the controls have been locked. (See [sm.localPlayer.setLockedControls](#setlockedcontrols))

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `direction` | [Vec3](../Userdata/Vec3.md) | The world direction. |

### setLockedControls {#setlockedcontrols}

``` { .lua .api-signature }
sm.localPlayer.setLockedControls( locked )
```

Sets whether the player's in-game controls are locked.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `locked` | boolean | The lock state. |

### updateFpAnimation {#updatefpanimation}

``` { .lua .api-signature }
sm.localPlayer.updateFpAnimation( name, time, weight?, looping? )
```

Updates a first person view animation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `time` | number | The time. |
| `weight` *(optional)* | number | The weight. (Defaults to -1.0) |
| `looping` *(optional)* | boolean | The looping. (Defaults to false) |
