# ToolClass

**Script template:** [View starter script](ToolClass-Template.md)

A script class that is instanced for every active [Tool](../Userdata/Tool.md) in the game.

A tool something that a [Player](../Userdata/Player.md) can equip by selecting it in the hotbar. For instance the Sledgehammer.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `data` | any | Data from the "data" json element. |
| `tool` | [Tool](../Userdata/Tool.md) | The [Tool](../Userdata/Tool.md) game object belonging to this class instance. |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |

## Constants

### equipWhileSeated {#equipwhileseated}

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
ToolClass:server_onCreate(  )
ToolClass:client_onCreate(  )
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
ToolClass:server_onDestroy(  )
ToolClass:client_onDestroy(  )
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
ToolClass:server_onRefresh(  )
ToolClass:client_onRefresh(  )
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
ToolClass:server_onFixedUpdate( timeStep )
ToolClass:client_onFixedUpdate( timeStep )
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
ToolClass:server_onReceiveUpdate(  )
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
ToolClass:client_onUpdate( deltaTime )
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
ToolClass:client_onClientDataUpdate( data, channel )
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
ToolClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |

<a id="client_onequip"></a>
### onEquip {#onequip}

``` { .lua .api-signature }
ToolClass:client_onEquip( animate )
```

Called when a [Player](../Userdata/Player.md) equips the [Tool](../Userdata/Tool.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `animate` | boolean | A boolean indicating whether the event should be animated or not. |

<a id="client_onunequip"></a>
### onUnequip {#onunequip}

``` { .lua .api-signature }
ToolClass:client_onUnequip( animate )
```

Called when a [Player](../Userdata/Player.md) unequips the [Tool](../Userdata/Tool.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `animate` | boolean | A boolean indicating whether the event should be animated or not. |

<a id="client_onequippedupdate"></a>
### onEquippedUpdate {#onequippedupdate}

``` { .lua .api-signature }
ToolClass:client_onEquippedUpdate( primaryState, secondaryState )
```

Called every frame for the currently equipped [Tool](../Userdata/Tool.md).

> **Note:**
> Swinging the sledgehammer is a typical example where you want to block other primary input.
> Force building is an example where the primary input action is not blocked.
> Not blocking secondary input allows shape removal while the tool is equipped.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `primaryState` | integer | The interact state of the primary (left) mouse button. (See [sm.tool.interactState](../Static-Functions/sm.tool.md#interactstate)) |
| `secondaryState` | integer | The interact state of the secondary (right) mouse button. (See [sm.tool.interactState](../Static-Functions/sm.tool.md#interactstate)) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean, boolean | The first boolean indicates if other primary input actions should be blocked. The second if secondary input actions should be blocked. (Defaults to false, false) |

<a id="client_ontoggle"></a>
### onToggle {#ontoggle}

``` { .lua .api-signature }
ToolClass:client_onToggle(  )
```

Called when the [Player](../Userdata/Player.md) presses a toggle key with the [Tool](../Userdata/Tool.md) equipped (default 'Q' and 'Shift' + 'Q).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean that indicates if other toggle actions should be blocked (rotating shapes). (Defaults to false) |

<a id="client_onreload"></a>
### onReload {#onreload}

``` { .lua .api-signature }
ToolClass:client_onReload(  )
```

Called when the [Player](../Userdata/Player.md) presses the 'Reload' key with the [Tool](../Userdata/Tool.md) equipped (default 'R').

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean that indicates if other reload actions should be blocked ([PlayerClass.client_onReload](PlayerClass.md#client_onreload)). (Defaults to false) |

<a id="client_canequip"></a>
### canEquip {#canequip}

``` { .lua .api-signature }
ToolClass:client_canEquip(  )
```

This event is called to check whether the [Tool](../Userdata/Tool.md) can be equipped.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | A boolean that indicates if the [Tool](../Userdata/Tool.md) can be equipped. (Defaults to true) |
