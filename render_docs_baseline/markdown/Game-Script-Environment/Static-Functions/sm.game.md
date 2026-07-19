# sm.game

Used to check the state of the game.

## Server + Client

### bindChatCommand {#bindchatcommand}

``` { .lua .api-signature }
sm.game.bindChatCommand( command, params, callback, help )
```

Binds a chat command to a callback function. The callback function receives an array of parameters. The first parameter is the command itself.

Example:

```lua
sm.game.bindChatCommand( "/enable_client_toilet",
						 { { "bool", "enabled", false } },
						 "onChatCommand",
						 "Enables or disables client toilet." )
```

```lua
function MyGameScript.onChatCommand( self, params )
	if params[1] == "/enable_client_toilet" then
		self.settings.enable_client_toilet = params[2]
	end
end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `command` | string | The command. |
| `params` | table | An array of parameters the callback function expects in the form of { { type, name (, optional, autocomplete ) }, ... }. The first is the <strong>type</strong> name of the parameter as a string. Valid types are "bool", "int", "number" and "string". The second is the <strong>name</strong> in the help text. Defaults to automatic naming ("p1", "p2", "p3", ...). The third is a bool value where true means that this parameter is <strong>optional</strong> (Optional, defaults to false). The fourth is a list of values that can be auto-completed to by pressing tab (Optional). |
| `callback` | string | The name of the Lua function to bind. |
| `help` | string | Help text. |

### exitToMenu {#exittomenu}

``` { .lua .api-signature }
sm.game.exitToMenu(  )
```

Only for testing!

### exitToMenuWithEndCredits {#exittomenuwithendcredits}

``` { .lua .api-signature }
sm.game.exitToMenuWithEndCredits(  )
```

Exits to the main menu and requests the end-game credits sequence to play once there.

### getCurrentTick {#getcurrenttick}

``` { .lua .api-signature }
sm.game.getCurrentTick(  )
```

Return the current game tick.

**Returns:**

| Type | Description |
| --- | --- |
| integer | The tick. |

### getDifficulty {#getdifficulty}

``` { .lua .api-signature }
sm.game.getDifficulty(  )
```

Return the index of the current difficulty setting.

**Returns:**

| Type | Description |
| --- | --- |
| integer | index	The difficulty index. |

### getEnableAggro {#getenableaggro}

``` { .lua .api-signature }
sm.game.getEnableAggro(  )
```

Returns true if aggro is enabled and false if aggro is disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getEnableAmmoConsumption {#getenableammoconsumption}

``` { .lua .api-signature }
sm.game.getEnableAmmoConsumption(  )
```

Returns true if ammo consumption is enabled and false if ammo consumption is disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getEnableFuelConsumption {#getenablefuelconsumption}

``` { .lua .api-signature }
sm.game.getEnableFuelConsumption(  )
```

Returns true if fuel consumption is enabled and false if fuel consumption is disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getEnableRestrictions {#getenablerestrictions}

``` { .lua .api-signature }
sm.game.getEnableRestrictions(  )
```

Returns true if restrictions are enabled and false if restrictions are disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getEnableUpgrade {#getenableupgrade}

``` { .lua .api-signature }
sm.game.getEnableUpgrade(  )
```

Returns true if upgrading is enabled and false if upgrading is disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getLimitedInventory {#getlimitedinventory}

``` { .lua .api-signature }
sm.game.getLimitedInventory(  )
```

Return limited inventory state. If true the items are limited, if false the items are unlimited.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Is limited. |

### getRecipesEnabled {#getrecipesenabled}

``` { .lua .api-signature }
sm.game.getRecipesEnabled(  )
```

Returns true if recipes is enabled and false if recipes are is disabled.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The enable state. |

### getServerTick {#getservertick}

``` { .lua .api-signature }
sm.game.getServerTick(  )
```

Return estimated game tick on the server.

**Returns:**

| Type | Description |
| --- | --- |
| integer | The tick. |

### getSettingBoolean {#getsettingboolean}

``` { .lua .api-signature }
sm.game.getSettingBoolean( name )
```

Get the boolean value of a named setting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the setting |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | value	The value of the setting. |

### getSettingString {#getsettingstring}

``` { .lua .api-signature }
sm.game.getSettingString( name )
```

Get the string value of a named setting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the setting |

**Returns:**

| Type | Description |
| --- | --- |
| string | value	The value of the setting. |

### getSettingValue {#getsettingvalue}

``` { .lua .api-signature }
sm.game.getSettingValue( name )
```

Get the number value of a named setting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the setting |

**Returns:**

| Type | Description |
| --- | --- |
| number | value	The value of the setting. |

### getTimeOfDay {#gettimeofday}

``` { .lua .api-signature }
sm.game.getTimeOfDay(  )
```

Return the fraction value of how far the current day has progressed.

**Returns:**

| Type | Description |
| --- | --- |
| number | The fraction of the day cycle. |

## Server-only

### banPlayer {#banplayer}

``` { .lua .api-signature }
sm.game.banPlayer( player )
```

Ban a player from the server.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](../Userdata/Player.md) | The player to be banned. |

### kickPlayer {#kickplayer}

``` { .lua .api-signature }
sm.game.kickPlayer( player )
```

Kick a player from the server.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](../Userdata/Player.md) | The player to be kicked. |

### pauseSaving {#pausesaving}

``` { .lua .api-signature }
sm.game.pauseSaving( waitName, ticks )
```

Pauses saving for the specified number of ticks. Server only.

If already paused, extends to the longer of current remaining and the requested ticks.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `waitName` | string | The name identifying this pause request. |
| `ticks` | integer | The number of ticks to pause saving for. |

### resumeSaving {#resumesaving}

``` { .lua .api-signature }
sm.game.resumeSaving( waitName )
```

Resumes saving by removing a named pause request. Server only.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `waitName` | string | The name identifying the pause request to remove. |

### setEnableAggro {#setenableaggro}

``` { .lua .api-signature }
sm.game.setEnableAggro( enableAggro )
```

Enables and disables aggro. If true, player's will be detected as targets.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableAggro` | boolean | The enable state. |

### setEnableAmmoConsumption {#setenableammoconsumption}

``` { .lua .api-signature }
sm.game.setEnableAmmoConsumption( enableAmmoConsumption )
```

Enables and disables ammo consumption. If true, ammo will be required to shoot spudguns.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableAmmoConsumption` | boolean | The enable state. |

### setEnableFuelConsumption {#setenablefuelconsumption}

``` { .lua .api-signature }
sm.game.setEnableFuelConsumption( enableFuelConsumption )
```

Enables and disables fuel consumption. If true, fuel will be consumed from engines.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableFuelConsumption` | boolean | The enable state. |

### setEnableRecipes {#setenablerecipes}

``` { .lua .api-signature }
sm.game.setEnableRecipes( enableRecipes )
```

Enables and disables recipes. If true, player's will need to unlock recipes before they become available for crafting.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableRecipes` | boolean | The enable state. |

### setEnableRestrictions {#setenablerestrictions}

``` { .lua .api-signature }
sm.game.setEnableRestrictions( enableRestrictions )
```

Enables and disables the use of restrictions. If true restrictions will be applied, if false the restrictions will default to unrestricted.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableRestrictions` | boolean | Restrictions enable state. |

### setEnableUpgrade {#setenableupgrade}

``` { .lua .api-signature }
sm.game.setEnableUpgrade( enableUpgrade )
```

Enables and disables upgrade. If true, the [Interactable](../Userdata/Interactable.md) can be upgraded with component kits.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `enableUpgrade` | boolean | The enable state. |

### setLimitedInventory {#setlimitedinventory}

``` { .lua .api-signature }
sm.game.setLimitedInventory( isLimited )
```

Sets limited inventory. If true the items are limited, if false the items are unlimited.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `isLimited` | boolean | Is limited. |

## Client-only

### loadWatchedTutorials {#loadwatchedtutorials}

``` { .lua .api-signature }
sm.game.loadWatchedTutorials(  )
```

Loads the users watched tutorials and returns it as a table.

**Returns:**

| Type | Description |
| --- | --- |
| table | Users watched tutorials table. |

### saveWatchedTutorials {#savewatchedtutorials}

``` { .lua .api-signature }
sm.game.saveWatchedTutorials( watchedTutorials )
```

Saves the user's watched tutorials.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `watchedTutorials` | table | The table of watched tutorials. |

### setTimeOfDay {#settimeofday}

``` { .lua .api-signature }
sm.game.setTimeOfDay( time )
```

Sets the fraction value of how far the current day has progressed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `time` | number | The fraction of the day cycle. |
