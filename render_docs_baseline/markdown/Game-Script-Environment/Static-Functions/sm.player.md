# sm.player

**Associated type:** [Player](../Userdata/Player.md)

A <strong>player</strong> is a user playing the game. Every player controls a [Character](../Userdata/Character.md) in the world.

## Functions

### getAllPlayers {#getallplayers}

``` { .lua .api-signature }
sm.player.getAllPlayers( getInactive? )
```

Returns a table of all [players](../Userdata/Player.md) that are currently in the game.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `getInactive` *(optional)* | boolean | Include getting inactive players. Defaults to false. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table of all players in the game. {[Player](../Userdata/Player.md), ..} |

### getHostPlayer {#gethostplayer}

``` { .lua .api-signature }
sm.player.getHostPlayer(  )
```

Returns the player of the game host.

**Returns:**

| Type | Description |
| --- | --- |
| [Player](../Userdata/Player.md) | The host player. |
