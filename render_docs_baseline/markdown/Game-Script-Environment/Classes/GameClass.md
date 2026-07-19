# GameClass

**Script template:** [View starter script](GameClass-Template.md)

A script class that defines the game mode. Only one instance of this class is made.

This is the first script that will be run.

The game script is responsible for creating and managing [worlds](../Userdata/World.md).

Can receive events sent with [sm.event.sendToGame](../Static-Functions/sm.event.md#sendtogame).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |
| `data` | any | Game start data. |

## Constants

### defaultInventorySize {#defaultinventorysize}

Sets default player inventory size. (Defaults to 40)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### enableAggro {#enableaggro}

Enables or disables enemy aggression. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableAmmoConsumption {#enableammoconsumption}

Enables or disables ammo consumption. (Defaults to false)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableFuelConsumption {#enablefuelconsumption}

Enables or disables fuel consumption. (Defaults to false)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableLimitedInventory {#enablelimitedinventory}

Enables or disables limited inventory. (Defaults to false)

When limited in inventory is on, items have a limited amount. When off, the player has access to all items. (Except for items with json value "hidden": true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableRecipes {#enablerecipes}

Enables or disables recipes being locked and needing to be learned to build items. (Defaults to true)

### enableRestrictions {#enablerestrictions}

Enables or disables build restrictions. (Defaults to false)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableUpgrade {#enableupgrade}

Enables or disables interactable part upgrade. (Defaults to false)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
GameClass:server_onCreate(  )
GameClass:client_onCreate(  )
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
GameClass:server_onDestroy(  )
GameClass:client_onDestroy(  )
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
GameClass:server_onRefresh(  )
GameClass:client_onRefresh(  )
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
GameClass:server_onFixedUpdate( timeStep )
GameClass:client_onFixedUpdate( timeStep )
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
GameClass:server_onReceiveUpdate(  )
```

Called occasionally to indicate that some time has passed.

For performance reasons; it recommended to use this instead of [server_onFixedUpdate](#server_onfixedupdate) for updates that do not need to happen frequently.

Use [sm.game.getCurrentTick](../Static-Functions/sm.game.md#getcurrenttick) to calculate the time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onplayerjoined"></a>
### onPlayerJoined {#onplayerjoined}

``` { .lua .api-signature }
GameClass:server_onPlayerJoined( player, newPlayer )
```

Called when a [Player](../Userdata/Player.md) joins the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `player` | [Player](../Userdata/Player.md) | The joining player. |
| `newPlayer` | boolean | True if the player has not been in this game before. |

<a id="server_onplayerleft"></a>
### onPlayerLeft {#onplayerleft}

``` { .lua .api-signature }
GameClass:server_onPlayerLeft( player )
```

Called when a [Player](../Userdata/Player.md) leaves the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `player` | [Player](../Userdata/Player.md) | The leaving player. |

<a id="server_onreset"></a>
### onReset {#onreset}

``` { .lua .api-signature }
GameClass:server_onReset(  )
```

Challenge Mode only!

Called when the user wants to reset the challenge level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onrestart"></a>
### onRestart {#onrestart}

``` { .lua .api-signature }
GameClass:server_onRestart(  )
```

Challenge Mode only!

Called when the user wants to restart the challenge level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onsavelevel"></a>
### onSaveLevel {#onsavelevel}

``` { .lua .api-signature }
GameClass:server_onSaveLevel(  )
```

Challenge Builder only!

Called when the user wants to save the challenge level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_ontestlevel"></a>
### onTestLevel {#ontestlevel}

``` { .lua .api-signature }
GameClass:server_onTestLevel(  )
```

Challenge Builder only!

Called when the user wants to save and test the challenge level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onstoptest"></a>
### onStopTest {#onstoptest}

``` { .lua .api-signature }
GameClass:server_onStopTest(  )
```

Challenge Builder only!

Called when the user wants to stop testing the challenge level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onunload"></a>
### onUnload {#onunload}

``` { .lua .api-signature }
GameClass:server_onUnload(  )
```

Called when a game session ends.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
GameClass:client_onUpdate( deltaTime )
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
GameClass:client_onClientDataUpdate( data, channel )
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
GameClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |

<a id="client_onloadingscreenlifted"></a>
### onLoadingScreenLifted {#onloadingscreenlifted}

``` { .lua .api-signature }
GameClass:client_onLoadingScreenLifted(  )
```

Called when the loading screen is lifted when entering a game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="client_onlanguagechange"></a>
### onLanguageChange {#onlanguagechange}

``` { .lua .api-signature }
GameClass:client_onLanguageChange( language )
```

Called when the user changes language in the in-game menus.

Possible language values:

"Brazilian", "Chinese", "English", "French", "German", "Italian", "Japanese", "Korean", "Polish", "Russian", "Spanish"

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `language` | string | The new language. |

<a id="client_onunstuck"></a>
### onUnstuck {#onunstuck}

``` { .lua .api-signature }
GameClass:client_onUnstuck(  )
```

Called when the user presses unstuck in the in-game main menu.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
