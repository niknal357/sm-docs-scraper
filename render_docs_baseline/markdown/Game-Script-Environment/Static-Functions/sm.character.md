# sm.character

**Associated type:** [Character](../Userdata/Character.md)

A <strong>character</strong> is the physical body of a living entity in the world. Both <strong>players</strong> and <strong>units</strong> may control a character.

## Server-only

### createCharacter {#createcharacter}

``` { .lua .api-signature }
sm.character.createCharacter( player, world, position, yaw?, pitch?, visible? )
```

Creates a new character in a world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `player` | [Player](../Userdata/Player.md) | The player controlling the character. |
| `world` | [World](../Userdata/World.md) | The world the character is created in. |
| `position` | [Vec3](../Userdata/Vec3.md) | The world position of the character. |
| `yaw` *(optional)* | number | The initial yaw of the character (Optional). |
| `pitch` *(optional)* | number | The initial pitch of the character (Optional). |
| `visible` *(optional)* | boolean | Whether the character is visible on spawn. Defaults to true. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](../Userdata/Character.md) | The created character. |

## Client-only

### preloadRenderables {#preloadrenderables}

``` { .lua .api-signature }
sm.character.preloadRenderables( renderables )
```

Pre-loads renderable data to be used by the character. This eliminates excessive loading during run time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `renderables` | table | The table of renderables { name = string, ... }. |
