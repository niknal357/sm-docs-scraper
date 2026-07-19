# sm.scriptableObject

**Associated type:** [ScriptableObject](../Userdata/ScriptableObject.md)

ScriptableObject creation

## Server-only

### createScriptableObject {#createscriptableobject}

``` { .lua .api-signature }
sm.scriptableObject.createScriptableObject( uuid, params?, world? )
```

Create a new Scriptable Object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | ScriptableObject uuid. |
| `params` *(optional)* | any | self.params on scriptable object. |
| `world` *(optional)* | [World](../Userdata/World.md) | The world this script belongs to, for world dependent api calls. Defaults to [sm.world.ids.noWorld](sm.world.md#ids) |

**Returns:**

| Type | Description |
| --- | --- |
| [ScriptableObject](../Userdata/ScriptableObject.md) | The scriptable object. |
