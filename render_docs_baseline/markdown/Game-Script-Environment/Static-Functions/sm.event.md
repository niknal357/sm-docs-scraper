# sm.event

Events for communicating between scripts by running callbacks.

## Constants

### types {#types}

Event types

| Value | Description |
| --- | --- |
| validate | Will make sure script instance exists, and that the callback is declared on the receiving end, before queuing the event. This is the default type. |
| blind | Will blindly queue the event without making any validation checks. Can be useful for sending events to script we know will come alive the next tick. |
| instant | Same as blind event, but sent immediately. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The event types list. |

## Functions

### sendToCharacter {#sendtocharacter}

``` { .lua .api-signature }
sm.event.sendToCharacter( character, callback, args?, eventType?, pauseSave? )
```

Sends an event to a specified [Character](../Userdata/Character.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The character. |
| `callback` | string | The function name in a character script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result					Returns true if the event was successfully processed. |

### sendToGame {#sendtogame}

``` { .lua .api-signature }
sm.event.sendToGame( callback, args?, eventType?, pauseSave? )
```

Sends an event to the game script.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `callback` | string | The function name in the game script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result			Returns true if the event was successfully processed. |

### sendToHarvestable {#sendtoharvestable}

``` { .lua .api-signature }
sm.event.sendToHarvestable(
    harvestable,
    callback,
    args?,
    eventType?,
    pauseSave?
)
```

Sends an event to a specified [Harvestable](../Userdata/Harvestable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `harvestable` | [Harvestable](../Userdata/Harvestable.md) | The harvestable. |
| `callback` | string | The function name in a harvestable script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result				Returns true if the event was successfully processed. |

### sendToInteractable {#sendtointeractable}

``` { .lua .api-signature }
sm.event.sendToInteractable(
    interactable,
    callback,
    args?,
    eventType?,
    pauseSave?
)
```

Sends an event to a specified [Interactable](../Userdata/Interactable.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The interactable. |
| `callback` | string | The function name in an interactable script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result				Returns true if the event was successfully processed. |

### sendToPlayer {#sendtoplayer}

``` { .lua .api-signature }
sm.event.sendToPlayer( player, callback, args?, eventType?, pauseSave? )
```

Sends an event to a specified [Player](../Userdata/Player.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](../Userdata/Player.md) | The player. |
| `callback` | string | The function name in a player script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result				Returns true if the event was successfully processed. |

### sendToScriptableObject {#sendtoscriptableobject}

``` { .lua .api-signature }
sm.event.sendToScriptableObject(
    scriptableObject,
    callback,
    args?,
    eventType?,
    pauseSave?
)
```

Sends an event to a specified [ScriptableObject](../Userdata/ScriptableObject.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](../Userdata/ScriptableObject.md) | The scriptableObject. |
| `callback` | string | The function name in a scriptableObject script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result				Returns true if the event was successfully processed. |

### sendToTool {#sendtotool}

``` { .lua .api-signature }
sm.event.sendToTool( tool, callback, args?, eventType?, pauseSave? )
```

Sends an event to a specified [Tool](../Userdata/Tool.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tool` | [Tool](../Userdata/Tool.md) | The tool. |
| `callback` | string | The function name in a tool script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result				Returns true if the event was successfully queued. |

### sendToUnit {#sendtounit}

``` { .lua .api-signature }
sm.event.sendToUnit( unit, callback, args?, eventType?, pauseSave? )
```

Sends an event to a specified [Unit](../Userdata/Unit.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `unit` | [Unit](../Userdata/Unit.md) | The unit. |
| `callback` | string | The function name in a unit script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result			Returns true if the event was successfully processed. |

### sendToWorld {#sendtoworld}

``` { .lua .api-signature }
sm.event.sendToWorld( world, callback, args?, eventType?, pauseSave? )
```

Sends an event to a specified [World](../Userdata/World.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world. |
| `callback` | string | The function name in a world script. |
| `args` *(optional)* | any | Optional arguments to be sent to the callback. |
| `eventType` *(optional)* | integer | The type of event. Defaults to [sm.event.types.validate](#types). |
| `pauseSave` *(optional)* | boolean | Optional, defaults to true. If true, pauses saving for 1 tick for delayed event types (server only). |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | result			Returns true if the event was successfully processed. |
