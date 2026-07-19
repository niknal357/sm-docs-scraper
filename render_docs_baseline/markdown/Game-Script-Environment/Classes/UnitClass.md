# UnitClass

**Script template:** [View starter script](UnitClass-Template.md)

A script class that is instanced for every [Unit](../Userdata/Unit.md) in the game.

A unit represents an AI controlling a [Character](../Userdata/Character.md).

The unit script only runs on the server side.

Can receive events sent with [sm.event.sendToUnit](../Static-Functions/sm.event.md#sendtounit).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The [Unit](../Userdata/Unit.md) game object belonging to this class instance. |
| `storage` | [Storage](../Userdata/Storage.md) | A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |
| `data` | any | Data from the "data" json element. |
| `params` | any | Parameter sent to [sm.unit.createUnit](../Static-Functions/sm.unit.md#createunit). |

## Constants

### isSaveObject {#issaveobject}

Enables or disables saving of this unit. (Defaults to true)

If enabled, the [Unit](../Userdata/Unit.md) will be recreated when loading a game. Otherwise, the [Unit](../Userdata/Unit.md) is considered a temporary object.

> **Note:**
> If disabled, self.storage can not be used.

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
UnitClass:server_onCreate(  )
UnitClass:client_onCreate(  )
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
UnitClass:server_onDestroy(  )
UnitClass:client_onDestroy(  )
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
UnitClass:server_onRefresh(  )
UnitClass:client_onRefresh(  )
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
UnitClass:server_onFixedUpdate( timeStep )
UnitClass:client_onFixedUpdate( timeStep )
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
UnitClass:server_onReceiveUpdate(  )
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
UnitClass:server_onProjectile(
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

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md). |
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
UnitClass:server_onExplosion( center, destructionLevel, damage )
```

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) is hit by an explosion.

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
UnitClass:server_onMelee( position, attacker, damage, power, direction, normal )
```

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) is hit by a melee hit.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md) or nil if unknown. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="server_oncollision"></a>
### onCollision {#oncollision}

``` { .lua .api-signature }
UnitClass:server_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
```

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) collides with another object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `other` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `selfPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) had at the point of collision. |
| `otherPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal between the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) and the other other object. |

<a id="server_oncollisioncrush"></a>
### onCollisionCrush {#oncollisioncrush}

``` { .lua .api-signature }
UnitClass:server_onCollisionCrush(  )
```

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) is crushed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onunitupdate"></a>
### onUnitUpdate {#onunitupdate}

``` { .lua .api-signature }
UnitClass:server_onUnitUpdate( deltaTime )
```

Called occasionally for units based on how many units are active.

It is recommended to do heavier AI decisions here instead of in [server_onFixedUpdate](#server_onfixedupdate).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `deltaTime` | number | The time, in seconds, since [server_onUnitUpdate](#server_onunitupdate) was last called for this [Unit](../Userdata/Unit.md). |

<a id="server_oncharacterchangedcolor"></a>
### onCharacterChangedColor {#oncharacterchangedcolor}

``` { .lua .api-signature }
UnitClass:server_onCharacterChangedColor( color )
```

Called when the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md) color is set. Either by painting or set using [Character.setColor](../Userdata/Character.md#setcolor) or [Character.color](../Userdata/Character.md#color).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `color` | [Color](../Userdata/Color.md) | The new [Color](../Userdata/Color.md) of the [Unit](../Userdata/Unit.md)'s [Character](../Userdata/Character.md). |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
UnitClass:client_onUpdate( deltaTime )
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
UnitClass:client_onClientDataUpdate( data, channel )
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
UnitClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |
