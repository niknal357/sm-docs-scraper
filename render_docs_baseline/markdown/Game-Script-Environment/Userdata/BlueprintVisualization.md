# BlueprintVisualization

**Associated namespace:** [sm.visualization](../Static-Functions/sm.visualization.md)

**Usage:** Client Only

**Serializable:** No

A userdata object representing a <strong>blueprint visualziation</strong>.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`BlueprintVisualization == BlueprintVisualization` | boolean | Checks if two instances of [BlueprintVisualization](BlueprintVisualization.md) refer to the same BlueprintVisualization. |

## Client-only

### destroy {#destroy}

``` { .lua .api-signature }
blueprintVisualization:destroy(  )
```

Destroy a [BlueprintVisualization](BlueprintVisualization.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | The blueprint visualization to be destroyed |

### setPosition {#setposition}

``` { .lua .api-signature }
blueprintVisualization:setPosition( position )
```

Set the world position of a [BlueprintVisualization](BlueprintVisualization.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | A blueprint visualization |
| `position` | [Vec3](Vec3.md) | World position |

### setRotation {#setrotation}

``` { .lua .api-signature }
blueprintVisualization:setRotation( rotation )
```

Set the rotation of a [BlueprintVisualization](BlueprintVisualization.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | A blueprint visualization |
| `rotation` | [Quat](Quat.md) | Rotation |

### setScale {#setscale}

``` { .lua .api-signature }
blueprintVisualization:setScale( scale )
```

Set the scale of a [BlueprintVisualization](BlueprintVisualization.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | A blueprint visualization |
| `scale` | [Vec3](Vec3.md) | Scale |

### setVisualizationColor {#setvisualizationcolor}

``` { .lua .api-signature }
blueprintVisualization:setVisualizationColor( visualizationColor )
```

Controls the rendering of the [BlueprintVisualization](BlueprintVisualization.md).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | A blueprint visualization |
| `visualizationColor` | string | Visualization color name to render the blueprint in. |

### updateBuilderGuide {#updatebuilderguide}

``` { .lua .api-signature }
blueprintVisualization:updateBuilderGuide(  )
```

Update the state of a builder guide [BlueprintVisualization](BlueprintVisualization.md). Should be called whenever the root [Shape](Shape.md) of the builder guide has changed.

But should not be called every frame or tick for performance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintVisualization` | [BlueprintVisualization](BlueprintVisualization.md) | A blueprint visualization created with [sm.visualization.createBuilderGuide](../Static-Functions/sm.visualization.md#createbuilderguide) |
