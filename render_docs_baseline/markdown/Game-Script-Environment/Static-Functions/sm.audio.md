# sm.audio

The <strong>audio</strong> manager is used to play sound effects in the game.

> **Note:**
> This manager does only produce sound for the local client. This is useful for small sound effects such as for GUI.
> For more information about sound and particle effects that affect all players, see [sm.effect](sm.effect.md).

## Constants

### soundList {#soundlist}

> **Deprecated:**
> Audio is deprecated, use Effect instead
>

A table with all the names of available sounds in the game.

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of sound names. {string, ...}  |

## Client-only

### getGlobalParameter {#getglobalparameter}

``` { .lua .api-signature }
sm.audio.getGlobalParameter( name )
```

Gets a named global parameter value from FMOD.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The parameter value. |

### play {#play}

``` { .lua .api-signature }
sm.audio.play( sound, position? )
```

Plays a sound.

If position is specified, the sound will play at the given coordinates in the world. Otherwise, the sound will play normally.

For a list of available sounds to play, see [sm.audio.soundList](#soundlist).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `sound` | string | The sound to play. |
| `position` *(optional)* | [Vec3](../Userdata/Vec3.md) | The world position of the sound. (Optional) |

### setGlobalParameter {#setglobalparameter}

``` { .lua .api-signature }
sm.audio.setGlobalParameter( name, value )
```

Sets a named global parameter value in FMOD.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name. |
| `value` | number | The parameter value. |
