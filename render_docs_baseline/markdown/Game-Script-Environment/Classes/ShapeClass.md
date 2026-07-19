# ShapeClass

**Script template:** [View starter script](ShapeClass-Template.md)

A script class that is instanced for every "scripted" [Interactable](../Userdata/Interactable.md) [Shape](../Userdata/Shape.md) in the game.

An interactable part is a [Shape](../Userdata/Shape.md) that is usually built by the player and can be interacted with. For instance a button or an engine.

Can receive events sent with [sm.event.sendToInteractable](../Static-Functions/sm.event.md#sendtointeractable).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The [Interactable](../Userdata/Interactable.md) game object belonging to this class instance. (The same as shape.interactable) |
| `shape` | [Shape](../Userdata/Shape.md) | The [Shape](../Userdata/Shape.md) game object that the [Interactable](../Userdata/Interactable.md) is attached to. (The same as interactable.shape) |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |
| `data` | any | Data from the "data" json element. |
| `params` | any | Parameter set with [Interactable.setParams](../Userdata/Interactable.md#setparams) when created from a script. |

## Constants

### colorHighlight {#colorhighlight}

Sets the connection-point highlight color. The connection-point is shown when using the <em>Connect Tool</em> and selecting the interactable. (Defaults to white)

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) |  |

### colorNormal {#colornormal}

Sets the connection-point normal color. The connection-point is shown when using the <em>Connect Tool</em>. (Defaults to gray)

**Returns:**

| Type | Description |
| --- | --- |
| [Color](../Userdata/Color.md) |  |

### connectIcon {#connecticon}

Sets the connection-point texture name that maps to texture specified in connectIcons.json. The connection-point is shown when using the <em>Connect Tool</em> and selecting the interactable. (Defaults to empty)

**Returns:**

| Type | Description |
| --- | --- |
| string |  |

### connectIconScale {#connecticonscale}

Sets the connection-point visualization scale. The connection-point is shown when using the <em>Connect Tool</em> and selecting the interactable. (Defaults to 0.75)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### connectionInput {#connectioninput}

Sets the connection input type flags. (See [sm.interactable.connectionType](../Static-Functions/sm.interactable.md#connectiontype)) (Defaults to 0, no input)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### connectionOutput {#connectionoutput}

Sets the connection output type flags. (See [sm.interactable.connectionType](../Static-Functions/sm.interactable.md#connectiontype)) (Defaults to 0, no output)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### maxChildCount {#maxchildcount}

Sets the maximum number of allowed child connections &ndash; the number of output connections. (Defaults to 0, no allowed child connections)

> **Note:**
> Implement [client_getAvailableChildConnectionCount](#client_getavailablechildconnectioncount) to control specific types.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### maxParentCount {#maxparentcount}

Sets the maximum number of allowed parent connections &ndash; the number of input connections. (Defaults to 0, no allowed parent connections)

> **Note:**
> Implement [client_getAvailableParentConnectionCount](#client_getavailableparentconnectioncount) to control specific types.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### poseWeightCount {#poseweightcount}

Sets the number of animation poses the shape's model is able to use.

Value can be are integers 0-3. (Defaults to 0, no poses)

A value greater that 0 indicates that the renderable's "mesh" is set up blend into "pose0", "pose1", "pose2".

This is, for instance, used to move the lever on the engine.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
ShapeClass:server_onCreate(  )
ShapeClass:client_onCreate(  )
```

Called when the scripted object is created. This occurs when a new object is built, spawned, or loaded from the save file.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_ondestroy"></a>
<a id="client_ondestroy"></a>
### onDestroy {#ondestroy}

``` { .lua .api-signature }
ShapeClass:server_onDestroy(  )
ShapeClass:client_onDestroy(  )
```

Called when the scripted object is destroyed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onrefresh"></a>
<a id="client_onrefresh"></a>
### onRefresh {#onrefresh}

``` { .lua .api-signature }
ShapeClass:server_onRefresh(  )
ShapeClass:client_onRefresh(  )
```

Called if the Lua script attached to the object is modified while the game is running.

> **Note:**
> This event requires Scrap Mechanic to be running with the '-dev' flag. This will allow scripts to automatically refresh upon changes.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onfixedupdate"></a>
<a id="client_onfixedupdate"></a>
### onFixedUpdate {#onfixedupdate}

``` { .lua .api-signature }
ShapeClass:server_onFixedUpdate( timeStep )
ShapeClass:client_onFixedUpdate( timeStep )
```

Called every game tick &ndash; 40 ticks a second. If the frame rate is lower than 40 fps, this event may be called twice.

During a fixed update, physics and logic between interactables are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `timeStep` | number | The time period of a tick. (Is always 0.025, a 1/40th of a second.) |

<a id="server_onprojectile"></a>
<a id="client_onprojectile"></a>
### onProjectile {#onprojectile}

#### Server

``` { .lua .api-signature }
ShapeClass:server_onProjectile(
    position,
    airTime,
    velocity,
    projectileName,
    shooter,
    damage,
    customData,
    normal,
    uuid,
    mass
)
```

Called when the [Shape](../Userdata/Shape.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Shape](../Userdata/Shape.md). |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. |
| `damage` | integer | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |
| `mass` | number | The mass of the projectile. |

#### Client

``` { .lua .api-signature }
ShapeClass:client_onProjectile(
    position,
    airTime,
    velocity,
    projectileName,
    shooter,
    damage,
    customData,
    normal,
    uuid,
    mass
)
```

Called when the [Shape](../Userdata/Shape.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Shape](../Userdata/Shape.md). |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter, can be a [Player](../Userdata/Player.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. Projectiles shot by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | number | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |
| `mass` | number | The mass of the projectile. |

<a id="server_onmelee"></a>
<a id="client_onmelee"></a>
### onMelee {#onmelee}

#### Server

``` { .lua .api-signature }
ShapeClass:server_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Shape](../Userdata/Shape.md) is hit by a melee attack.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Shape](../Userdata/Shape.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md) or nil if unknown. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

#### Client

``` { .lua .api-signature }
ShapeClass:client_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Shape](../Userdata/Shape.md) is hit by a melee attack.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Shape](../Userdata/Shape.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md) or nil if unknown. Attacks made by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="server_oncollision"></a>
<a id="client_oncollision"></a>
### onCollision {#oncollision}

``` { .lua .api-signature }
ShapeClass:server_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
ShapeClass:client_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
```

Called when the [Shape](../Userdata/Shape.md) collides with another object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `other` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `selfPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the [Shape](../Userdata/Shape.md) had at the point of collision. |
| `otherPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal between the [Shape](../Userdata/Shape.md) and the other other object. |

<a id="server_canerase"></a>
<a id="client_canerase"></a>
### canErase {#canerase}

``` { .lua .api-signature }
ShapeClass:server_canErase(  )
ShapeClass:client_canErase(  )
```

Called to check whether the [Shape](../Userdata/Shape.md) can be erased at this moment.

> **Note:**
> Can be used to override restrictions. (See [Shape.erasable](../Userdata/Shape.md#erasable))

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the [Shape](../Userdata/Shape.md) can be erased or not. (Defaults to true) |

## Server-only

<a id="server_onreceiveupdate"></a>
### onReceiveUpdate {#onreceiveupdate}

``` { .lua .api-signature }
ShapeClass:server_onReceiveUpdate(  )
```

Called occasionally to indicate that some time has passed.

For performance reasons; it recommended to use this instead of [server_onFixedUpdate](#server_onfixedupdate) for updates that do not need to happen frequently.

Use [sm.game.getCurrentTick](../Static-Functions/sm.game.md#getcurrenttick) to calculate the time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onunload"></a>
### onUnload {#onunload}

``` { .lua .api-signature }
ShapeClass:server_onUnload(  )
```

Called when the [Interactable](../Userdata/Interactable.md) is unloaded from the game because no [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is close enough to it. Also called when exiting the game.

> **Note:**
> The creation, consisting of one or more [bodies](../Userdata/Body.md), consisting of one or more [shapes](../Userdata/Shape.md) joined together with [joints](../Userdata/Joint.md) are always unloaded at the same time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onsledgehammer"></a>
### onSledgehammer {#onsledgehammer}

``` { .lua .api-signature }
ShapeClass:server_onSledgehammer(  )
```

> **Deprecated:**
> Use [server_onMelee](#server_onmelee) instead.
>

<a id="server_onexplosion"></a>
### onExplosion {#onexplosion}

``` { .lua .api-signature }
ShapeClass:server_onExplosion( center, destructionLevel, damage )
```

Called when the [Shape](../Userdata/Shape.md) is hit by an explosion.

For more information about explosions, see [sm.physics.explode](../Static-Functions/sm.physics.md#explode).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `center` | [Vec3](../Userdata/Vec3.md) | The center of the explosion. |
| `destructionLevel` | integer | The level of destruction done by this explosion. Corresponds to the 'durability' rating of a [Shape](../Userdata/Shape.md). |
| `damage` | integer | The damage value of the explosion. |

<a id="server_onworldchanged"></a>
### onWorldChanged {#onworldchanged}

``` { .lua .api-signature }
ShapeClass:server_onWorldChanged(  )
```

Called when a shape changes world

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
ShapeClass:client_onUpdate( deltaTime )
```

Called every frame.

During a frame update, graphics, animations and effects are updated.

> **Warning:**
> Because of how frequent this event is called, the game's frame rate is greatly affected by the amount of code executed here.
> For any non-graphics related code, consider using [client_onFixedUpdate](#client_onfixedupdate) instead.
> If the event is not in use, consider removing it from the script. (Event callbacks that are not implemented will not be called.)

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `deltaTime` | number | Delta time since the last frame. |

<a id="client_onclientdataupdate"></a>
### onClientDataUpdate {#onclientdataupdate}

``` { .lua .api-signature }
ShapeClass:client_onClientDataUpdate( data, channel )
```

Called when the client receives new client data updates from the server set with [Network.setClientData](../Userdata/Network.md#setclientdata).

Data set in this way is persistent and the latest data will automatically be sent to new clients.

The data will arrive after [client_onCreate](#client_oncreate) during the same tick.

Channel 1 will be received before channel 2 if both are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `data` | any | Any lua object set with [Network.setClientData](../Userdata/Network.md#setclientdata) |
| `channel` | integer | Client data channel, 1 or 2. (default: 1) |

<a id="client_onlocalplayerchangedworld"></a>
### onLocalPlayerChangedWorld {#onlocalplayerchangedworld}

``` { .lua .api-signature }
ShapeClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |

<a id="client_oninteract"></a>
### onInteract {#oninteract}

``` { .lua .api-signature }
ShapeClass:client_onInteract( character, state )
```

Called when a [Player](../Userdata/Player.md) is interacting with the [Interactable](../Userdata/Interactable.md) by pressing the 'Use' key (default 'E') or pressing '0&ndash;9' if the [Interactable](../Userdata/Interactable.md) is connected to a seat. (See: [Interactable.pressSeatInteractable](../Userdata/Interactable.md#pressseatinteractable))

> **Note:**
> If this method is defined, the player will see the interaction text "E Use" when looking at the [Shape](../Userdata/Shape.md).

```lua
-- Example of interaction
function MySwitch.client_onInteract( self, character, state ) 
	if state == true then
		self.network:sendToServer( 'sv_n_toggle' )
	end
end

function MySwitch.sv_n_toggle( self ) 
	-- Toggle on and off
	self.interactable.active = not self.interactable.active
end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is interacting with the [Interactable](../Userdata/Interactable.md). |
| `state` | boolean | The interaction state. (true if pressed, false if released) |

<a id="client_ontinker"></a>
### onTinker {#ontinker}

``` { .lua .api-signature }
ShapeClass:client_onTinker( character, state )
```

Called when a [Player](../Userdata/Player.md) is tinkering with the [Interactable](../Userdata/Interactable.md) by pressing the 'Tinker' key (default 'U').

> **Note:**
> Tinkering usually means opening the upgrade menu for seats.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is tinkering with the [Interactable](../Userdata/Interactable.md). |
| `state` | boolean | The interaction state. (true if pressed, false if released) |

<a id="client_oninteractthroughjoint"></a>
### onInteractThroughJoint {#oninteractthroughjoint}

``` { .lua .api-signature }
ShapeClass:client_onInteractThroughJoint( character, state, joint )
```

Called when a [Player](../Userdata/Player.md) is interacting with the [Interactable](../Userdata/Interactable.md) through a connected [Joint](../Userdata/Joint.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is interacting with the [Interactable](../Userdata/Interactable.md). |
| `state` | boolean | The interaction state. Always true. [client_onInteractThroughJoint](#client_oninteractthroughjoint) only receives the key down event. |
| `joint` | [Joint](../Userdata/Joint.md) | The [Joint](../Userdata/Joint.md) that the [Player](../Userdata/Player.md) interacted through. |

<a id="client_onaction"></a>
### onAction {#onaction}

``` { .lua .api-signature }
ShapeClass:client_onAction( action, state )
```

Called when the interactable receives input from a [Player](../Userdata/Player.md) with the [Character](../Userdata/Character.md) locked to the [Interactable](../Userdata/Interactable.md).

When a [Character](../Userdata/Character.md) is seated in an [Interactable](../Userdata/Interactable.md) [Shape](../Userdata/Shape.md) with a "seat" component, the [Character](../Userdata/Character.md) is also considered locked to the [Interactable](../Userdata/Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `action` | integer | The action as an integer value. More details in [sm.interactable.actions](../Static-Functions/sm.interactable.md#actions). |
| `state` | boolean | True on begin action, false on end action. |

<a id="client_caninteract"></a>
### canInteract {#caninteract}

``` { .lua .api-signature }
ShapeClass:client_canInteract( character )
```

Called to check whether the [Interactable](../Userdata/Interactable.md) can be interacted with at this moment.

> **Note:**
> This callback can also be used to change the interaction text shown to the player using [sm.gui.setInteractionText](../Static-Functions/sm.gui.md#setinteractiontext). (Defaults to "E Use")

> **Note:**
> Can be used to override restrictions. (See [Shape.usable](../Userdata/Shape.md#usable))

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is looking at the [Shape](../Userdata/Shape.md). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the interactable can be interacted with or not. (Defaults to true if [client_onInteract](#client_oninteract) is implemented, otherwise false) |

<a id="client_caninteractthroughjoint"></a>
### canInteractThroughJoint {#caninteractthroughjoint}

``` { .lua .api-signature }
ShapeClass:client_canInteractThroughJoint( character, joint )
```

Called to check whether the [Interactable](../Userdata/Interactable.md) can be interacted with through a child [Joint](../Userdata/Joint.md) at this moment.

> **Note:**
> This callback can also be used to change the interaction text shown to the player using [sm.gui.setInteractionText](../Static-Functions/sm.gui.md#setinteractiontext). (Defaults to "E Use")

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is looking at the [Joint](../Userdata/Joint.md). |
| `joint` | [Joint](../Userdata/Joint.md) | The [Joint](../Userdata/Joint.md). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the interactable can be interacted with or not. (Defaults to true if [client_onInteractThroughJoint](#client_oninteractthroughjoint) is implemented, otherwise false) |

<a id="client_cantinker"></a>
### canTinker {#cantinker}

``` { .lua .api-signature }
ShapeClass:client_canTinker( character )
```

Called to check whether the [Interactable](../Userdata/Interactable.md) can be tinkered with at this moment.

> **Note:**
> Tinkering usually means opening the upgrade menu for seats.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is looking at the [Shape](../Userdata/Shape.md). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the interactable can be tinkered with or not. (Defaults to true if [client_onTinker](#client_ontinker) is implemented, otherwise false) |

<a id="client_getavailableparentconnectioncount"></a>
### getAvailableParentConnectionCount {#getavailableparentconnectioncount}

``` { .lua .api-signature }
ShapeClass:client_getAvailableParentConnectionCount( flags )
```

Called to check how many more parent (input) connections with the given type [flag](../Static-Functions/sm.interactable.md#connectiontype) the [Interactable](../Userdata/Interactable.md) will accept. Return 1 or more to allow a connection of this type.

```lua
-- Example of implementation where logic and power shares the same slot but electricity counts as separate
MyIteractable.maxParentCount = 2
MyIteractable.connectionInput = sm.interactable.connectionType.logic + sm.interactable.connectionType.power + sm.interactable.connectionType.electricity

function MyIteractable.client_getAvailableParentConnectionCount( self, flags )
	if bit.band( flags, bit.bor( sm.interactable.connectionType.logic, sm.interactable.connectionType.power ) ) ~= 0 then
		return 1 - self:getParents( bit.bor( sm.interactable.connectionType.logic, sm.interactable.connectionType.power ) )
	end
	if bit.band( flags, sm.interactable.connectionType.electricity ) ~= 0 then
		return 1 - self:getParents( sm.interactable.connectionType.electricity )
	end
	return 0
end
```

> **Note:**
> [maxParentCount](#maxparentcount) must be 1 or more for this callback to be called.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `flags` | integer | Connection type flags. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of available connections. |

<a id="client_getavailablechildconnectioncount"></a>
### getAvailableChildConnectionCount {#getavailablechildconnectioncount}

``` { .lua .api-signature }
ShapeClass:client_getAvailableChildConnectionCount( flags )
```

Called to check how many more child (output) connections with the given type [flag](../Static-Functions/sm.interactable.md#connectiontype) the [Interactable](../Userdata/Interactable.md) will accept. Return 1 or more to allow a connection of this type.

```lua
-- Example of implementation that accepts 10 logic connections and 1 power connection
MyInteractable.maxChildCount = 11
MyInteractable.connectionOutput = sm.interactable.connectionType.logic + sm.interactable.connectionType.power

function MyIteractable.client_getAvailableChildConnectionCount( self, flags )
	if bit.band( flags, sm.interactable.connectionType.logic ) ~= 0 then
		return 10 - self:getParents( sm.interactable.connectionType.logic )
	end
	if bit.band( flags, sm.interactable.connectionType.power ) ~= 0 then
		return 1 - self:getParents( sm.interactable.connectionType.power )
	end
	return 0
end
```

> **Note:**
> [maxChildCount](#maxchildcount) must be 1 or more for this callback to be called.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `flags` | integer | Connection type flags. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of available connections. |

<a id="client_cancarry"></a>
### canCarry {#cancarry}

``` { .lua .api-signature }
ShapeClass:client_canCarry(  )
```

Called to check if the shape must be carried instead of put in the inventory.

> **Note:**
> Shapes with the "carryItem" attribute are always carried.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the interacable must be carried or not. (Defaults to false) |

<a id="client_onchildjointremoved"></a>
### onChildJointRemoved {#onchildjointremoved}

``` { .lua .api-signature }
ShapeClass:client_onChildJointRemoved( joint )
```

Called when a child [Joint](../Userdata/Joint.md) is removed from the [Interactable](../Userdata/Interactable.md)'s connection list.

This can happen when a player explicitly disconnects the [Joint](../Userdata/Joint.md) or when the [Joint](../Userdata/Joint.md) is destroyed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `joint` | [Joint](../Userdata/Joint.md) | The [Joint](../Userdata/Joint.md) that was removed. |
