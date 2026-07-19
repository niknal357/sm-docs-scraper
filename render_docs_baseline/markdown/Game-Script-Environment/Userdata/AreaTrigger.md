# AreaTrigger

**Associated namespace:** [sm.areaTrigger](../Static-Functions/sm.areaTrigger.md)

**Usage:** Server And Client

**Serializable:** No

A userdata object representing an <strong>area trigger</strong> in the game.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of an area trigger.

- <a id="world"></a>`world` [ **[World](World.md)** ] <br>
    - `Get`: Returns the world id of the area trigger. Keep in mind that area triggers can move between worlds, so world id might change!

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`AreaTrigger == AreaTrigger` | boolean | Checks if two instances of [AreaTrigger](AreaTrigger.md) refer to the same AreaTrigger. |

## Server + Client

### bindOnDestroy {#bindondestroy}

``` { .lua .api-signature }
areaTrigger:bindOnDestroy( callback, object? )
```

Bind the lua function to be called when the area trigger is destroyed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnEnter {#bindonenter}

``` { .lua .api-signature }
areaTrigger:bindOnEnter( callback, object? )
```

Binds an area trigger's onEnter event to a custom callback. The onEnter event is triggered when an object enters the trigger area.

The callback receives:

- <strong>self</strong> (<em>table</em>) &ndash; The class instance.
- <strong>trigger</strong> (<em>[AreaTrigger](AreaTrigger.md)</em>) &ndash; The area trigger instance.
- <strong>results</strong> (<em>table</em>) &ndash; A table of [characters](Character.md) and/or [bodies](Body.md) and/or [harvestables](Harvestable.md) and/or [lifts](Lift.md) and/or [areaTriggers](AreaTrigger.md).

```lua
function MyClass.onEnter( self, trigger, results ) ...
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnExit {#bindonexit}

``` { .lua .api-signature }
areaTrigger:bindOnExit( callback, object? )
```

Binds an area trigger's onExit event to a custom callback. The onExit event is triggered when an object leaves the trigger area.

The callback receives:

- <strong>self</strong> (<em>table</em>) &ndash; The class instance.
- <strong>trigger</strong> (<em>[AreaTrigger](AreaTrigger.md)</em>) &ndash; The area trigger instance.
- <strong>results</strong> (<em>table</em>) &ndash; A table of [characters](Character.md) and/or [bodies](Body.md) and/or [harvestables](Harvestable.md) and/or [lifts](Lift.md) and/or [areaTriggers](AreaTrigger.md).

```lua
function MyClass.onExit( self, trigger, results ) ...
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnHostDestroy {#bindonhostdestroy}

``` { .lua .api-signature }
areaTrigger:bindOnHostDestroy( callback, object? )
```

Bind the lua function to be used when an area trigger is destroyed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. ( optional ) |

### bindOnHostUnload {#bindonhostunload}

``` { .lua .api-signature }
areaTrigger:bindOnHostUnload( callback, object? )
```

Bind the lua function to be used when an interactable area trigger's host object is unloaded.

Note: Only the game host can know if a host object is unloaded, to a connected client it will look like the host object was destroyed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. ( optional ) |

### bindOnProjectile {#bindonprojectile}

``` { .lua .api-signature }
areaTrigger:bindOnProjectile( callback, object? )
```

Binds an area trigger's onProjectile event to a custom callback. The onProjectile event is triggered if a projectile collides with the trigger area

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnStay {#bindonstay}

``` { .lua .api-signature }
areaTrigger:bindOnStay( callback, object? )
```

Binds an area trigger's onStay event to a custom callback. The onStay event is triggered every tick as long as an object is staying inside of the trigger area.

The callback receives:

- <strong>self</strong> (<em>table</em>) &ndash; The class instance.
- <strong>trigger</strong> (<em>[AreaTrigger](AreaTrigger.md)</em>) &ndash; The area trigger instance.
- <strong>results</strong> (<em>table</em>) &ndash; A table of [characters](Character.md) and/or [bodies](Body.md) and/or [harvestables](Harvestable.md) and/or [lifts](Lift.md) and/or [areaTriggers](AreaTrigger.md).

```lua
function MyClass.onStay( self, trigger, results ) ...
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### destroy {#destroy}

``` { .lua .api-signature }
areaTrigger:destroy(  )
```

Destroys an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger to be destroyed. |

### getCharacters {#getcharacters}

``` { .lua .api-signature }
areaTrigger:getCharacters(  )
```

Gets the trigger collisions for characters inside the area trigger

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of character trigger collisions. |

### getContents {#getcontents}

``` { .lua .api-signature }
areaTrigger:getContents(  )
```

Gets the contents of the area trigger.

Returns a table of [characters](Character.md) and/or [bodies](Body.md) and/or [harvestables](Harvestable.md) and/or [lifts](Lift.md) and/or [areaTriggers](AreaTrigger.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table with the content. |

### getHarvestables {#getharvestables}

``` { .lua .api-signature }
areaTrigger:getHarvestables(  )
```

Gets the trigger collisions for harvestables inside the area trigger

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of harvestable trigger collisions. |

### getHostInteractable {#gethostinteractable}

``` { .lua .api-signature }
areaTrigger:getHostInteractable(  )
```

Returns the attached host [interactable](../Static-Functions/sm.interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Interactable](Interactable.md) | The area trigger's host interactable. |

### getId {#getid}

``` { .lua .api-signature }
areaTrigger:getId(  )
```

Returns the id of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The area trigger's id. |

### getShapes {#getshapes}

``` { .lua .api-signature }
areaTrigger:getShapes(  )
```

Gets the trigger collisions for shapes inside the area trigger

Will only return one [Shape](Shape.md) for each [Body](Body.md) that is colliding with the [AreaTrigger](AreaTrigger.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table of shape trigger collisions. |

### getSize {#getsize}

``` { .lua .api-signature }
areaTrigger:getSize(  )
```

Returns the size of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The area trigger's size. |

### getUserData {#getuserdata}

``` { .lua .api-signature }
areaTrigger:getUserData(  )
```

Returns the user data set on the area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The user data set on this trigger |

### getWorld {#getworld}

``` { .lua .api-signature }
areaTrigger:getWorld(  )
```

Returns the world id of the area trigger. Keep in mind that area triggers can move between worlds, so world id might change!

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger user. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | The _current_ world id of the area trigger. |

### getWorldMax {#getworldmax}

``` { .lua .api-signature }
areaTrigger:getWorldMax(  )
```

Returns the world max corner position of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The area trigger's max corner position. |

### getWorldMin {#getworldmin}

``` { .lua .api-signature }
areaTrigger:getWorldMin(  )
```

Returns the world min corner position of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The area trigger's min corner position. |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
areaTrigger:getWorldPosition(  )
```

Returns the world position of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md) | The area trigger's world position. |

### getWorldRotation {#getworldrotation}

``` { .lua .api-signature }
areaTrigger:getWorldRotation(  )
```

Returns the world rotation of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| [Quat](Quat.md) | The area trigger's world rotation. |

### hasVoxelTerrainContact {#hasvoxelterraincontact}

``` { .lua .api-signature }
areaTrigger:hasVoxelTerrainContact(  )
```

Returns true if the [AreaTrigger](AreaTrigger.md) is in contact with destructable terrain.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Destructable terrain contact. |

### setCharacterDetection {#setcharacterdetection}

``` { .lua .api-signature }
areaTrigger:setCharacterDetection( detectCharacters )
```

When set to true the area trigger can calculate which characters are inside of the trigger and get the collision information.

with a call to [AreaTrigger](AreaTrigger.md): getCharacters

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `detectCharacters` | boolean | Character detection on or off. |

### setDestroyOnErase {#setdestroyonerase}

``` { .lua .api-signature }
areaTrigger:setDestroyOnErase( destroyOnErase )
```

Sets whether the areatrigger should be destroyed immediately upon being erased or simply invoke the bound OnErase callback. True by default.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `destroyOnErase` | boolean | Destroy on erase. |

### setEraseTime {#seterasetime}

``` { .lua .api-signature }
areaTrigger:setEraseTime( eraseTime )
```

Sets the time it takes to erase this trigger if it is erasable.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `eraseTime` | number | The time it takes to erase this area trigger. |

### setHarvestableDetection {#setharvestabledetection}

``` { .lua .api-signature }
areaTrigger:setHarvestableDetection( detectHarvestables )
```

When set to true the area trigger can calculate which harvestables are inside of the trigger and get the collision information.

with a call to [AreaTrigger](AreaTrigger.md): getHarvestables

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `detectHarvestables` | boolean | Harvestable detection on or off. |

### setIncludeShapesInContent {#setincludeshapesincontent}

``` { .lua .api-signature }
areaTrigger:setIncludeShapesInContent( includeShapesInContent )
```

When set to true the area trigger will include individual shapes in its content list.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `includeShapesInContent` | boolean | Include shapes in content on or off. |

### setShapeDetection {#setshapedetection}

``` { .lua .api-signature }
areaTrigger:setShapeDetection( detectShapes )
```

Shape detection is off by default. When set to true the area trigger can calculate which shapes are inside of the trigger

with a call to [AreaTrigger](AreaTrigger.md): getShapes

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `detectShapes` | boolean | Shape detection on or off. |

### setSize {#setsize}

``` { .lua .api-signature }
areaTrigger:setSize( size )
```

Sets the new size of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `size` | [Vec3](Vec3.md) | The area trigger's new size. |

### setVoxelDestructible {#setvoxeldestructible}

``` { .lua .api-signature }
areaTrigger:setVoxelDestructible( destructible )
```

Sets whether VoxelTerrain can destroy this area trigger by voxel addition.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `destructible` | boolean | The state to set |

### setWaterType {#setwatertype}

``` { .lua .api-signature }
areaTrigger:setWaterType( waterType )
```

Sets the liquid type of the area trigger. (See [sm.areaTrigger.liquidType](../Static-Functions/sm.areaTrigger.md#liquidtype))

Only has an effect on area triggers with the 'water' proxy type; setting it on any other proxy type has no effect.

Currently only 'lava' has special behavior: it occasionally destroys submerged shapes. Lava behavior requires

shapes to be included in the content list via [AreaTrigger](AreaTrigger.md): setIncludeShapesInContent.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `waterType` | integer | The liquid type. (See [sm.areaTrigger.liquidType](../Static-Functions/sm.areaTrigger.md#liquidtype)) |

### setWorldPosition {#setworldposition}

``` { .lua .api-signature }
areaTrigger:setWorldPosition( position )
```

Sets the new world position of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `position` | [Vec3](Vec3.md) | The area trigger's new world position. |

### setWorldRotation {#setworldrotation}

``` { .lua .api-signature }
areaTrigger:setWorldRotation( rotation )
```

Sets the new world rotation of an area trigger.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `rotation` | [Quat](Quat.md) | The area trigger's new world rotation. |

## Server-only

### bindOnMelee {#bindonmelee}

``` { .lua .api-signature }
areaTrigger:bindOnMelee( callback, object? )
```

Bind the lua function to be used when the area trigger is hit by a melee attack.

Requires that areaTriggerProxyType has been set to [sm.areaTrigger.areaTriggerProxyType.melee](../Static-Functions/sm.areaTrigger.md#areatriggerproxytype)

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

## Client-only

### bindCanErase {#bindcanerase}

``` { .lua .api-signature }
areaTrigger:bindCanErase( callback, object? )
```

Bind a callback that checks if the area trigger can be erased.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindCanInteract {#bindcaninteract}

``` { .lua .api-signature }
areaTrigger:bindCanInteract( callback, object? )
```

Bind the lua function to be used when checking for player interaction with the area trigger

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnErase {#bindonerase}

``` { .lua .api-signature }
areaTrigger:bindOnErase( callback, object? )
```

Bind the lua function to be used when an interactable area trigger is erased.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### bindOnInteract {#bindoninteract}

``` { .lua .api-signature }
areaTrigger:bindOnInteract( callback, object? )
```

Bind the lua function to be used when a player interacts with an area trigger

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `areaTrigger` | [AreaTrigger](AreaTrigger.md) | The area trigger instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |
