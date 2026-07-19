# HarvestableClass

**Script template:** [View starter script](HarvestableClass-Template.md)

A script class that is instanced for every [Harvestable](../Userdata/Harvestable.md) in the game.

A tree or a plant that can be harvested is a typical case of a harvestable.

Can receive events sent with [sm.event.sendToHarvestable](../Static-Functions/sm.event.md#sendtoharvestable).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The [Harvestable](../Userdata/Harvestable.md) game object belonging to this class instance. |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |
| `data` | any | Data from the "data" json element. |
| `params` | any | Parameter sent to [sm.harvestable.create](../Static-Functions/sm.harvestable.md#create) or set in the terrain generation script. |
| `tags` | any | The tags set on the harvestable from the editor. |

## Constants

### poseWeightCount {#poseweightcount}

Sets the number of animation poses the harvestable's model is able to use.

Value can be are integers 0-3. (Defaults to 0, no poses)

A value greater that 0 indicates that the renderable's "mesh" is set up blend into "pose0", "pose1", "pose2".

This is, for instance, used for growing plants.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
HarvestableClass:server_onCreate(  )
HarvestableClass:client_onCreate(  )
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
HarvestableClass:server_onDestroy(  )
HarvestableClass:client_onDestroy(  )
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
HarvestableClass:server_onRefresh(  )
HarvestableClass:client_onRefresh(  )
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
HarvestableClass:server_onFixedUpdate( timeStep )
HarvestableClass:client_onFixedUpdate( timeStep )
```

Called every game tick &ndash; 40 ticks a second. If the frame rate is lower than 40 fps, this event may be called twice.

During a fixed update, physics and logic between interactables are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `timeStep` | number | The time period of a tick. (Is always 0.025, a 1/40th of a second.) |

<a id="server_oncollision"></a>
<a id="client_oncollision"></a>
### onCollision {#oncollision}

``` { .lua .api-signature }
HarvestableClass:server_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
HarvestableClass:client_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
```

Called when the [Harvestable](../Userdata/Harvestable.md) collides with another object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `other` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md) | The other object. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `selfPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that the [Harvestable](../Userdata/Harvestable.md) had at the point of collision. |
| `otherPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal between the [Harvestable](../Userdata/Harvestable.md) and the other other object. |

<a id="server_onprojectile"></a>
<a id="client_onprojectile"></a>
### onProjectile {#onprojectile}

#### Server

``` { .lua .api-signature }
HarvestableClass:server_onProjectile(
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

Called when the [Harvestable](../Userdata/Harvestable.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Harvestable](../Userdata/Harvestable.md). |
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
HarvestableClass:client_onProjectile(
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

Called when the [Harvestable](../Userdata/Harvestable.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Harvestable](../Userdata/Harvestable.md). |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter, can be a [Player](../Userdata/Player.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. Projectiles shot by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | integer | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |
| `mass` | number | The mass of the projectile. |

<a id="server_onmelee"></a>
<a id="client_onmelee"></a>
### onMelee {#onmelee}

#### Server

``` { .lua .api-signature }
HarvestableClass:server_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Harvestable](../Userdata/Harvestable.md) is hit by a melee attack.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Harvestable](../Userdata/Harvestable.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md) or nil if unknown. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

#### Client

``` { .lua .api-signature }
HarvestableClass:client_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Harvestable](../Userdata/Harvestable.md) is hit by a melee attack.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Harvestable](../Userdata/Harvestable.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md) or nil if unknown. Attacks made by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="server_canerase"></a>
<a id="client_canerase"></a>
### canErase {#canerase}

``` { .lua .api-signature }
HarvestableClass:server_canErase(  )
HarvestableClass:client_canErase(  )
```

Called to check whether the [Harvestable](../Userdata/Harvestable.md) can be erased at this moment.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the [Harvestable](../Userdata/Harvestable.md) can be removed or not. (Defaults to "removable" json value which defaults to false) |

## Server-only

<a id="server_onreceiveupdate"></a>
### onReceiveUpdate {#onreceiveupdate}

``` { .lua .api-signature }
HarvestableClass:server_onReceiveUpdate(  )
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
HarvestableClass:server_onUnload(  )
```

Called when the [Harvestable](../Userdata/Harvestable.md) is unloaded from the game because no [Player](../Userdata/Player.md)'s [Character](../Userdata/Character.md) is close enough to it. Also called when exiting the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onexplosion"></a>
### onExplosion {#onexplosion}

``` { .lua .api-signature }
HarvestableClass:server_onExplosion( center, destructionLevel, damage )
```

Called when the [Harvestable](../Userdata/Harvestable.md) is hit by an explosion.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `center` | [Vec3](../Userdata/Vec3.md) | The center of the explosion. |
| `destructionLevel` | integer | The level of destruction done by this explosion. Corresponds to the "durability" rating of a [Shape](../Userdata/Shape.md). |
| `damage` | integer | The damage value of the explosion. |

<a id="server_onremoved"></a>
### onRemoved {#onremoved}

``` { .lua .api-signature }
HarvestableClass:server_onRemoved( player )
```

Called when a [Player](../Userdata/Player.md) wants to remove the [Harvestable](../Userdata/Harvestable.md).

> **Note:**
> The [HarvestableClass](HarvestableClass.md) is responsible for doing the remove using [Harvestable.destroy](../Userdata/Harvestable.md#destroy).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `player` | [Player](../Userdata/Player.md) | The [Player](../Userdata/Player.md) that wants to remove the [Harvestable](../Userdata/Harvestable.md). |

<a id="server_onignite"></a>
### onIgnite {#onignite}

``` { .lua .api-signature }
HarvestableClass:server_onIgnite(  )
```

Called when the [Harvestable](../Userdata/Harvestable.md) is ignited by a nearby fire.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onfloating"></a>
### onFloating {#onfloating}

``` { .lua .api-signature }
HarvestableClass:server_onFloating(  )
```

Called when the [Harvestable](../Userdata/Harvestable.md) is floating.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
HarvestableClass:client_onUpdate( deltaTime )
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
HarvestableClass:client_onClientDataUpdate( data, channel )
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
HarvestableClass:client_onLocalPlayerChangedWorld( world )
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
HarvestableClass:client_onInteract( character, state )
```

Called when a [Player](../Userdata/Player.md) is interacting with the [Harvestable](../Userdata/Harvestable.md) by pressing the 'Use' key (default 'E').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is interacting with the [Harvestable](../Userdata/Harvestable.md). |
| `state` | boolean | The interaction state. Always true. The [HarvestableClass](HarvestableClass.md) only receives the key down event. |

<a id="client_caninteract"></a>
### canInteract {#caninteract}

``` { .lua .api-signature }
HarvestableClass:client_canInteract( character )
```

Called to check whether the [Harvestable](../Userdata/Harvestable.md) can be interacted with at this moment.

> **Note:**
> This callback is also responsible for updating interaction text shown to the player using [sm.gui.setInteractionText](../Static-Functions/sm.gui.md#setinteractiontext).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is looking at the [Harvestable](../Userdata/Harvestable.md). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the harvestable can be interacted with or not. (Defaults to true if [client_onInteract](#client_oninteract) is implemented, otherwise false) |

<a id="client_onaction"></a>
### onAction {#onaction}

``` { .lua .api-signature }
HarvestableClass:client_onAction( action, state )
```

Called when the harvestable receives input from a player with the [Character](../Userdata/Character.md) locked to the [Harvestable](../Userdata/Harvestable.md).

When a [Character](../Userdata/Character.md) is seated in a [Harvestable](../Userdata/Harvestable.md) with a "seat" component, the [Character](../Userdata/Character.md) is also considered locked to the [Harvestable](../Userdata/Harvestable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `action` | integer | The action as an integer value. More details in [sm.interactable.actions](../Static-Functions/sm.interactable.md#actions). |
| `state` | boolean | True on begin action, false on end action. |
