# PlayerClass

**Script template:** [View starter script](PlayerClass-Template.md)

A script class that is instanced for every active [Player](../Userdata/Player.md) in the game.

A player represent a user controlling a [Character](../Userdata/Character.md).

The player script handles actions made by the user.

Can receive events sent with [sm.event.sendToPlayer](../Static-Functions/sm.event.md#sendtoplayer).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](../Userdata/Player.md) | The [Player](../Userdata/Player.md) game object belonging to this class instance. |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
PlayerClass:server_onCreate(  )
PlayerClass:client_onCreate(  )
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
PlayerClass:server_onDestroy(  )
PlayerClass:client_onDestroy(  )
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
PlayerClass:server_onRefresh(  )
PlayerClass:client_onRefresh(  )
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
PlayerClass:server_onFixedUpdate( timeStep )
PlayerClass:client_onFixedUpdate( timeStep )
```

Called every game tick &ndash; 40 ticks a second. If the frame rate is lower than 40 fps, this event may be called twice.

During a fixed update, physics and logic between interactables are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `timeStep` | number | The time period of a tick. (Is always 0.025, a 1/40th of a second.) |

## Server-only

<a id="server_onreceiveupdate"></a>
### onReceiveUpdate {#onreceiveupdate}

``` { .lua .api-signature }
PlayerClass:server_onReceiveUpdate(  )
```

Called occasionally to indicate that some time has passed.

For performance reasons; it recommended to use this instead of [server_onFixedUpdate](#server_onfixedupdate) for updates that do not need to happen frequently.

Use [sm.game.getCurrentTick](../Static-Functions/sm.game.md#getcurrenttick) to calculate the time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onprojectile"></a>
### onProjectile {#onprojectile}

``` { .lua .api-signature }
PlayerClass:server_onProjectile(
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

Called when the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md). |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. |
| `damage` | integer | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |
| `mass` | number | The mass of the projectile. |

<a id="server_onexplosion"></a>
### onExplosion {#onexplosion}

``` { .lua .api-signature }
PlayerClass:server_onExplosion( center, destructionLevel, damage )
```

Called when the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is hit by an explosion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `center` | [Vec3](../Userdata/Vec3.md) | The center of the explosion. |
| `destructionLevel` | integer | The level of destruction done by this explosion. Corresponds to the 'durability' rating of a [Shape](../Userdata/Shape.md). |
| `damage` | integer | The damage value of the explosion. |

<a id="server_onmelee"></a>
### onMelee {#onmelee}

``` { .lua .api-signature }
PlayerClass:server_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is hit by a melee hit.

> **Note:**
> If the attacker is destroyed before the projectile hits, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md) or nil if unknown. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="server_oncollision"></a>
### onCollision {#oncollision}

``` { .lua .api-signature }
PlayerClass:server_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
```

Called when the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) collides with another object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `other` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `selfPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) had at the point of collision. |
| `otherPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal between the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) and the other other object. |

<a id="server_oncollisioncrush"></a>
### onCollisionCrush {#oncollisioncrush}

``` { .lua .api-signature }
PlayerClass:server_onCollisionCrush(  )
```

Called when the [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is crushed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onshaperemoved"></a>
### onShapeRemoved {#onshaperemoved}

``` { .lua .api-signature }
PlayerClass:server_onShapeRemoved( items )
```

Called when the [Player](../Userdata/Player.md) removed a [Shape](../Userdata/Shape.md) from the [World](../Userdata/World.md).

Will receive a table of tables listing the items removed by this action.

Element format: 

| Type | Name | Description |
| --- | --- | --- |
| [Uuid](../Userdata/Uuid.md) | uuid | The item uuid. |
| integer | amount | The amount of items with this uuid. |
| string | type | Type of shape removed. Can be "part", "block" or "joint". |

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `items` | table | A table listing the removed items. {{uuid=[Uuid](../Userdata/Uuid.md), amount=integer, type=string}, ..} |

<a id="server_oninventorychanges"></a>
### onInventoryChanges {#oninventorychanges}

``` { .lua .api-signature }
PlayerClass:server_onInventoryChanges( inventory, changes )
```

Called when the [Player](../Userdata/Player.md) has changes in the inventory [Container](../Userdata/Container.md).

Will receive a table listing the changes.

Element format: 

| Type | Name | Description |
| --- | --- | --- |
| [Uuid](../Userdata/Uuid.md) | uuid | The item uuid |
| integer | difference | The change in amount. Positive numbers mean item gain, negative item loss. |
| [Tool](../Userdata/Tool.md) | tool | (Optional) If the item is a [Tool](../Userdata/Tool.md), this is the tool. Otherwise nil. |

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `inventory` | [Container](../Userdata/Container.md) | The player's inventory [Container](../Userdata/Container.md). |
| `changes` | table | A table listing the changes. {{uuid=[Uuid](../Userdata/Uuid.md), difference=integer, tool=[Tool](../Userdata/Tool.md)}, ..} |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
PlayerClass:client_onUpdate( deltaTime )
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
PlayerClass:client_onClientDataUpdate( data, channel )
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
PlayerClass:client_onLocalPlayerChangedWorld( world )
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
PlayerClass:client_onInteract( character, state )
```

Called when the player presses or releases the 'Use' key (default 'E').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md)'. Same as self.player.character. |
| `state` | boolean | The interaction state. (true if pressed, false if released) |

<a id="client_oncancel"></a>
### onCancel {#oncancel}

``` { .lua .api-signature }
PlayerClass:client_onCancel(  )
```

Called when the player presses the 'Cancel' key (default 'Esc').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="client_onskipdialog"></a>
### onSkipDialog {#onskipdialog}

``` { .lua .api-signature }
PlayerClass:client_onSkipDialog(  )
```

Called when the player presses the 'Cancel' key (default 'Esc') if a dialogue is active and no other gui has focus.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="client_onreload"></a>
### onReload {#onreload}

``` { .lua .api-signature }
PlayerClass:client_onReload(  )
```

Called when the player presses the 'Reload' key (default 'R').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
