# sm.challenge

The <strong>Challenge</strong> api contains functions related to the Challenge game mode.

## Server-only

### getCompletionTime {#getcompletiontime}

``` { .lua .api-signature }
sm.challenge.getCompletionTime( level )
```

Retrieve challenge completion time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `level` | [Uuid](../Userdata/Uuid.md) | The level's uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The completion time. |

### getSaveData {#getsavedata}

``` { .lua .api-signature }
sm.challenge.getSaveData( level )
```

Retrieve challenge level save data.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `level` | [Uuid](../Userdata/Uuid.md) | The level's uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The save data. |

### hasStarted {#hasstarted}

``` { .lua .api-signature }
sm.challenge.hasStarted(  )
```

Check if a challenge has started

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the challenge has started. |

### levelCompleted {#levelcompleted}

``` { .lua .api-signature }
sm.challenge.levelCompleted( level, time, save )
```

Completes a challenge level and saves progression.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `level` | [Uuid](../Userdata/Uuid.md) | The level's uuid. |
| `time` | number | The completion time. |
| `save` | table | A table containing save data. |

### resolveContentPath {#resolvecontentpath}

``` { .lua .api-signature }
sm.challenge.resolveContentPath( path )
```

Resolves a path containing $CONTENT_DATA to path that can be accessed in the main scripting environment.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The path containing $CONTENT_DATA. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The resolved path. |

### start {#start}

``` { .lua .api-signature }
sm.challenge.start(  )
```

Starts challenge.

### stop {#stop}

``` { .lua .api-signature }
sm.challenge.stop(  )
```

Stops challenge.

### takePicture {#takepicture}

``` { .lua .api-signature }
sm.challenge.takePicture( width, height, rotation )
```

Takes a picture of the challenge level with a custom resolution.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `width` | integer | Preview width. |
| `height` | integer | Preview height. |
| `rotation` | integer | Rotation step. |

### takePicturesForMenu {#takepicturesformenu}

``` { .lua .api-signature }
sm.challenge.takePicturesForMenu( rotation )
```

Takes pictures of the challenge level to use as icon and preview.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `rotation` | integer | Rotation step. |

## Client-only

### isMasterMechanicTrial {#ismastermechanictrial}

``` { .lua .api-signature }
sm.challenge.isMasterMechanicTrial(  )
```

Returns true if the current content is the master mechanic trial pack.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | The content pack status. |
