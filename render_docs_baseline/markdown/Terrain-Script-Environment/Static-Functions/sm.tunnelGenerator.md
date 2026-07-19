# sm.tunnelGenerator

Use to generate cell data for producing tunnels through voxels.

## Functions

### generate {#generate}

``` { .lua .api-signature }
sm.tunnelGenerator.generate(
    seed,
    min,
    max,
    pathingSettings,
    tunnelRequests,
    gridSize
)
```

Returns an array table of pathing results. Each element consisting of a table {positions={[Vec3](../Userdata/Vec3.md),...}} of position arrays.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `seed` | integer | Simplex noise seed. |
| `min` | [Vec3](../Userdata/Vec3.md) | Grid min x (inclusive). |
| `max` | [Vec3](../Userdata/Vec3.md) | Grid max x (non inclusive). |
| `pathingSettings` | table | An table of available pathing settings to be used by tunnel requests. {costNoiseFrequency=number,costNoiseIntensity=number,costZPenalty=number} |
| `tunnelRequests` | table | An array table of tunnel requests. {{posA=[Vec3](../Userdata/Vec3.md), posB=[Vec3](../Userdata/Vec3.md)(, dirA=[Vec3](../Userdata/Vec3.md))(, dirB=[Vec3](../Userdata/Vec3.md)), pathingSettings=string},...} |
| `gridSize` | number | Size of each grid cell in world units. (Used for debug draw only.) |

**Returns:**

| Type | Description |
| --- | --- |
| table | An array table with one tunnel result per request. {{positions={[Vec3](../Userdata/Vec3.md),...}}, ...} |
