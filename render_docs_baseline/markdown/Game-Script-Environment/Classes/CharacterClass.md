# CharacterClass

**Script template:** [View starter script](CharacterClass-Template.md)

A script class that is instanced for every [Character](../Userdata/Character.md) in the game.

A [Character](../Userdata/Character.md) is a temporary vessel controlled by a [Player](../Userdata/Player.md) or [Unit](../Userdata/Unit.md).

Can receive events sent with [sm.event.sendToCharacter](../Static-Functions/sm.event.md#sendtocharacter).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) game object belonging to this class instance. |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `data` | any | Data from the "data" json element. |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
CharacterClass:server_onCreate(  )
CharacterClass:client_onCreate(  )
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
CharacterClass:server_onDestroy(  )
CharacterClass:client_onDestroy(  )
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
CharacterClass:server_onRefresh(  )
CharacterClass:client_onRefresh(  )
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
CharacterClass:server_onFixedUpdate( timeStep )
CharacterClass:client_onFixedUpdate( timeStep )
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
CharacterClass:server_onReceiveUpdate(  )
```

Called occasionally to indicate that some time has passed.

For performance reasons; it recommended to use this instead of [server_onFixedUpdate](#server_onfixedupdate) for updates that do not need to happen frequently.

Use [sm.game.getCurrentTick](../Static-Functions/sm.game.md#getcurrenttick) to calculate the time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
CharacterClass:client_onUpdate( deltaTime )
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
CharacterClass:client_onClientDataUpdate( data, channel )
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
CharacterClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |

<a id="client_onprojectile"></a>
### onProjectile {#onprojectile}

``` { .lua .api-signature }
CharacterClass:client_onProjectile(
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

Called when the [Character](../Userdata/Character.md) is hit by a projectile.

> **Note:**
> If the shooter is destroyed before the hit lands, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit the [Character](../Userdata/Character.md). |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter, can be a [Player](../Userdata/Player.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. Projectiles shot by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | number | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |
| `mass` | number | The mass of the projectile. |

<a id="client_onmelee"></a>
### onMelee {#onmelee}

``` { .lua .api-signature }
CharacterClass:client_onMelee(
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
```

Called when the [Character](../Userdata/Character.md) is hit by a melee hit.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the [Character](../Userdata/Character.md) was hit. |
| `attacker` | [Player](../Userdata/Player.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md) or nil if unknown. Attacks made by a [Unit](../Userdata/Unit.md) will be nil on the client. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="client_oncollision"></a>
### onCollision {#oncollision}

``` { .lua .api-signature }
CharacterClass:client_onCollision(
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
```

Called when the [Character](../Userdata/Character.md) collides with another object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `other` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `selfPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the [Character](../Userdata/Character.md) had at the point of collision. |
| `otherPointVelocity` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal between the [Character](../Userdata/Character.md) and the other other object. |

<a id="client_ongraphicsloaded"></a>
### onGraphicsLoaded {#ongraphicsloaded}

``` { .lua .api-signature }
CharacterClass:client_onGraphicsLoaded(  )
```

Called when graphics are loaded for the [Character](../Userdata/Character.md).

After this; graphics related functions can be called, like accessing animations.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="client_ongraphicsunloaded"></a>
### onGraphicsUnloaded {#ongraphicsunloaded}

``` { .lua .api-signature }
CharacterClass:client_onGraphicsUnloaded(  )
```

Called when graphics are unloaded for the [Character](../Userdata/Character.md).

After this; graphics related functions no longer has an effect or will fail.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="client_oninteract"></a>
### onInteract {#oninteract}

``` { .lua .api-signature }
CharacterClass:client_onInteract( character, state )
```

Called when a [Player](../Userdata/Player.md) is interacting with the [Character](../Userdata/Character.md) by pressing the 'Use' key (default 'E').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is interacting with this [Character](../Userdata/Character.md). |
| `state` | boolean | The interaction state. Always true. The [CharacterClass](CharacterClass.md) only receives the key down event. |

<a id="client_caninteract"></a>
### canInteract {#caninteract}

``` { .lua .api-signature }
CharacterClass:client_canInteract( character )
```

Called to check whether the [Character](../Userdata/Character.md) can be interacted with at this moment.

> **Note:**
> This callback is also responsible for updating interaction text shown to the player using [sm.gui.setInteractionText](../Static-Functions/sm.gui.md#setinteractiontext).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `character` | [Character](../Userdata/Character.md) | The [Character](../Userdata/Character.md) of the [Player](../Userdata/Player.md) that is looking at this [Character](../Userdata/Character.md). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean indicating whether the characer can be interacted with or not. (Defaults to true if [client_onInteract](#client_oninteract) is implemented, otherwise false) |

<a id="client_onevent"></a>
### onEvent {#onevent}

``` { .lua .api-signature }
CharacterClass:client_onEvent( event )
```

Called when the [Character](../Userdata/Character.md) receives an event from [Player.sendCharacterEvent](../Userdata/Player.md#sendcharacterevent) or [Unit.sendCharacterEvent](../Userdata/Unit.md#sendcharacterevent).

This is usually for triggering animations on the character.

For more extensive events, see [sm.event.sendToCharacter](../Static-Functions/sm.event.md#sendtocharacter).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `event` | string | The event name. |
