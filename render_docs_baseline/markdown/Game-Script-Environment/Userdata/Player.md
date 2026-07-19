# Player

**Associated namespace:** [sm.player](../Static-Functions/sm.player.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>player</strong> in the game.

**Values:**

- <a id="character"></a>`character` [ **[Character](Character.md)** ] <br>
    - `Get`: Returns the character the player is controlling.

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns client public data from a player.
    - `Set`: (Client-Only) Sets client public data on a player.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a player.

- <a id="name"></a>`name` [ **string** ] <br>
    - `Get`: Returns the name of a player.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a player.
    - `Set`: (Server-Only) Sets (server) public data on a player.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Player == Player` | boolean | Checks if two instances of [Player](Player.md) refer to the same Player. |

## Server + Client

### getCarry {#getcarry}

``` { .lua .api-signature }
player:getCarry(  )
```

Returns the carry container of the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The player's carry. |

### getCharacter {#getcharacter}

``` { .lua .api-signature }
player:getCharacter(  )
```

Returns the character the player is controlling.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The player's character. |

### getCurrentToolUuid {#getcurrenttooluuid}

``` { .lua .api-signature }
player:getCurrentToolUuid( player )
```

Returns the uuid of the tool the player is currently holding.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Uuid](Uuid.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| [Tool](Tool.md) | The player's held tool uuid. |

### getHotbar {#gethotbar}

``` { .lua .api-signature }
player:getHotbar(  )
```

Returns the hotbar container of the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The player's hotbar. |

### getId {#getid}

``` { .lua .api-signature }
player:getId(  )
```

Returns the id of a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The player's id. |

### getInventory {#getinventory}

``` { .lua .api-signature }
player:getInventory(  )
```

Returns the inventory container of the player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| [Container](Container.md) | The player's inventory. |

### getName {#getname}

``` { .lua .api-signature }
player:getName(  )
```

Returns the name of a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The player's name. |

### isActive {#isactive}

``` { .lua .api-signature }
player:isActive(  )
```

Returns true if the player is currently in the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if active. |

### isFemale {#isfemale}

``` { .lua .api-signature }
player:isFemale(  )
```

Check if the player is female

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if female |

### isMale {#ismale}

``` { .lua .api-signature }
player:isMale(  )
```

Check if the player is male

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if male |

## Server-only

### getCarryColor {#getcarrycolor}

``` { .lua .api-signature }
player:getCarryColor(  )
```

Returns the color of the shape the player is carrying.

**Returns:**

| Type | Description |
| --- | --- |
| [Color](Color.md) | The color of the shape the player is carrying. |

### getCarryData {#getcarrydata}

``` { .lua .api-signature }
player:getCarryData(  )
```

Get the carry data on a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The carry data. |

### getCustomizationUuid {#getcustomizationuuid}

``` { .lua .api-signature }
player:getCustomizationUuid( categoryIndex )
```

Get uuid of customization from index

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |
| `categoryIndex` | integer | The index of the customization category to get the uuid for. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](Uuid.md) | uuid |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
player:getPublicData(  )
```

Returns (server) public data from a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### placeLift {#placelift}

``` { .lua .api-signature }
player:placeLift( creation, position, level, rotation )
```

Place down a lift game object

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player to own the lift. |
| `creation` | table | The bodies to place on the lift. {[Body](Body.md), ..} |
| `position` | [Vec3](Vec3.md) | The lift position. |
| `level` | integer | The lift level. |
| `rotation` | integer | The rotation of the creation on the lift. |

### removeLift {#removelift}

``` { .lua .api-signature }
player:removeLift(  )
```

Remove the player's lift, if the lift exists.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player that owns the lift. |

### sendCharacterEvent {#sendcharacterevent}

``` { .lua .api-signature }
player:sendCharacterEvent( event )
```

Sends an event to a given player

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player to send to |
| `event` | string | The event to send |

### setCarryData {#setcarrydata}

``` { .lua .api-signature }
player:setCarryData( data )
```

Set the carry data on a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |
| `data` | table | The carry data. |

### setCharacter {#setcharacter}

``` { .lua .api-signature }
player:setCharacter( character )
```

Sets the character the player is controlling.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |
| `character` | [Character](Character.md) | The character. |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
player:setPublicData( data )
```

Sets (server) public data on a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |
| `data` | table | The public data. |

## Client-only

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
player:getClientPublicData(  )
```

Returns client public data from a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The client public data. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
player:setClientPublicData( data )
```

Sets client public data on a player.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](Player.md) | The player. |
| `data` | table | The client public data. |
