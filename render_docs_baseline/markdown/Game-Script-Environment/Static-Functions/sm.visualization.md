# sm.visualization

**Associated type:** [BlueprintVisualization](../Userdata/BlueprintVisualization.md)

<strong>Visualization</strong> is used for visualizing game objects.

## Client-only

<a id="createblueprint"></a>
### createBlueprint(string) {#createblueprint-string}

``` { .lua .api-signature }
sm.visualization.createBlueprint( path )
```

Create a [BlueprintVisualization](../Userdata/BlueprintVisualization.md) from a blueprint file path.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | A file path to the blueprint to be visualized |

**Returns:**

| Type | Description |
| --- | --- |
| [BlueprintVisualization](../Userdata/BlueprintVisualization.md) | The blueprint visualization |

### createBlueprint(table) {#createblueprint-table}

``` { .lua .api-signature }
sm.visualization.createBlueprint( blueprintTable )
```

Create a [BlueprintVisualization](../Userdata/BlueprintVisualization.md) from a blueprint table.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `blueprintTable` | table | Table with blueprint information to be visualized |

**Returns:**

| Type | Description |
| --- | --- |
| [BlueprintVisualization](../Userdata/BlueprintVisualization.md) | The blueprint visualization |

### createBuilderGuide {#createbuilderguide}

``` { .lua .api-signature }
sm.visualization.createBuilderGuide(
    path,
    shape,
    ignoreBlockUuid?,
    completeEffectName?,
    completeEffectAtBaseName?
)
```

Create a builder guide [BlueprintVisualization](../Userdata/BlueprintVisualization.md), comparing the creation from the root [Shape](../Userdata/Shape.md) to the blueprint give by path.

The builder guide blueprint contains stage indices based on shape color, stage color order is the same as the color order in the PaintTool color picker.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | A file path to the builder guide blueprint |
| `shape` | [Shape](../Userdata/Shape.md) | Root [Shape](../Userdata/Shape.md) for comparing the creation from |
| `ignoreBlockUuid` *(optional)* | boolean | Should block uuid be evaluated for stage completion (Defaults to false) |
| `completeEffectName` *(optional)* | string | The name of the effect that should be played at the placed block once the builder guide stage is completed (Defaults to "") |
| `completeEffectAtBaseName` *(optional)* | string | The name of the effect that should be played at the base once the builder guide stage is completed (Defaults to "") |

**Returns:**

| Type | Description |
| --- | --- |
| [BlueprintVisualization](../Userdata/BlueprintVisualization.md) | The builder guide blueprint visualization |

### drawLine {#drawline}

``` { .lua .api-signature }
sm.visualization.drawLine( startingPoint, endPoint, color? )
```

Adds a builderguide connection guide line between two points.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `startingPoint` | [Vec3](../Userdata/Vec3.md) | The starting point for the line. |
| `endPoint` | [Vec3](../Userdata/Vec3.md) | The end point for the line. |
| `color` *(optional)* | [Color](../Userdata/Color.md) | The color for the line. Defaults to yellow. (Optional) |

### getShapePlacementVisualization {#getshapeplacementvisualization}

``` { .lua .api-signature }
sm.visualization.getShapePlacementVisualization(  )
```

Returns a table containing the current state of the shape placement visualization.

**Returns:**

| Type | Description |
| --- | --- |
| table | Table containing { worldPosition = [Vec3](../Userdata/Vec3.md), worldRotation = [Quat](../Userdata/Quat.md), shapeUuid = [Uuid](../Userdata/Uuid.md), isLegal = boolean }. |

<a id="setblockvisualization"></a>
### setBlockVisualization(Vec3, boolean?, Shape) {#setblockvisualization-vec3-boolean-optional-shape}

``` { .lua .api-signature }
sm.visualization.setBlockVisualization( position, illegal?, shape )
```

Visualizes a block on a shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The local space position |
| `illegal` *(optional)* | boolean | Whether the visualization should render as illegal (Defaults to false) |
| `shape` | [Shape](../Userdata/Shape.md) | Shape to visualize on |

### setBlockVisualization(Vec3, boolean?, Joint) {#setblockvisualization-vec3-boolean-optional-joint}

``` { .lua .api-signature }
sm.visualization.setBlockVisualization( position, illegal?, joint )
```

Visualizes a block on a joint

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The local space position |
| `illegal` *(optional)* | boolean | Whether the visualization should render as illegal (Defaults to false) |
| `joint` | [Joint](../Userdata/Joint.md) | joint to visualize on |

### setBlockVisualization(Vec3, boolean?) {#setblockvisualization-vec3-boolean-optional}

``` { .lua .api-signature }
sm.visualization.setBlockVisualization( position, illegal? )
```

Visualizes a block in world space

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | The world space position |
| `illegal` *(optional)* | boolean | Whether the visualization should render as illegal (Defaults to false) |

### setCreationBodies {#setcreationbodies}

``` { .lua .api-signature }
sm.visualization.setCreationBodies( bodies )
```

Sets an array of bodies to visualize.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `bodies` | table | Array of bodies to visualize {[Body](../Userdata/Body.md), ..}. |

### setCreationFreePlacement {#setcreationfreeplacement}

``` { .lua .api-signature }
sm.visualization.setCreationFreePlacement( valid )
```

Controls the transform of the creation visualization. If true the visualization will render using setFreePlacementPosition/setFreePlacementRotation functions.

If false the visualization will render on top of the creation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `valid` | boolean | Should the creation visualization be free placement |

### setCreationFreePlacementPosition {#setcreationfreeplacementposition}

``` { .lua .api-signature }
sm.visualization.setCreationFreePlacementPosition( position )
```

Set the world position of the creation visualization. Only works if setFreePlacement is true.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | World position of the creation visualization |

### setCreationFreePlacementRotation {#setcreationfreeplacementrotation}

``` { .lua .api-signature }
sm.visualization.setCreationFreePlacementRotation( index )
```

Set the rotation index of the creation visualization. Only works if setFreePlacement is true.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `index` | integer | Index to rotate the creation visualization with |

### setCreationValid {#setcreationvalid}

``` { .lua .api-signature }
sm.visualization.setCreationValid( valid, lift? )
```

Controls the rendering of the creation visualization. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `valid` | boolean | Should the visualization should render be valid |
| `lift` *(optional)* | boolean | Should the visualization should render be lift or place (Defaults to false) |

### setCreationVisible {#setcreationvisible}

``` { .lua .api-signature }
sm.visualization.setCreationVisible( visible )
```

Controls the visibility of the creation visualization

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `visible` | boolean | Should the creation visualization be visible |

### setLiftLevel {#setliftlevel}

``` { .lua .api-signature }
sm.visualization.setLiftLevel( level )
```

Set the lift level of the lift visualization.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `level` | integer | The level of the lift |

### setLiftPosition {#setliftposition}

``` { .lua .api-signature }
sm.visualization.setLiftPosition( position )
```

Set the world position of the lift visualization.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `position` | [Vec3](../Userdata/Vec3.md) | World position of the lift visualization |

### setLiftValid {#setliftvalid}

``` { .lua .api-signature }
sm.visualization.setLiftValid( valid )
```

Controls the rendering of the lift visualization. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `valid` | boolean | Whether the visualization should render as valid |

### setLiftVisible {#setliftvisible}

``` { .lua .api-signature }
sm.visualization.setLiftVisible( visible )
```

Controls the visibility of the lift visualization

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `visible` | boolean | Whether the lift visualization is visible |
