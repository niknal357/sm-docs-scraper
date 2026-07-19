# sm.render

Render settings

## Server + Client

### getDefaultCameraLight {#getdefaultcameralight}

``` { .lua .api-signature }
sm.render.getDefaultCameraLight(  )
```

Gets a table of the default camera light render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default camera light render settings. |

### getDefaultFog {#getdefaultfog}

``` { .lua .api-signature }
sm.render.getDefaultFog(  )
```

Gets a table of the default fog render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default fog render settings. |

### getDefaultGI {#getdefaultgi}

``` { .lua .api-signature }
sm.render.getDefaultGI(  )
```

Gets a table of the default GI render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default GI render settings. |

### getDefaultHorizonLight {#getdefaulthorizonlight}

``` { .lua .api-signature }
sm.render.getDefaultHorizonLight(  )
```

Gets a table of the default horizon light render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default horizon light render settings. |

### getDefaultReflectionColor {#getdefaultreflectioncolor}

``` { .lua .api-signature }
sm.render.getDefaultReflectionColor(  )
```

Gets a table of the default reflection color render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default reflection color render settings. |

### getDefaultVolumetricFog {#getdefaultvolumetricfog}

``` { .lua .api-signature }
sm.render.getDefaultVolumetricFog(  )
```

Gets a table of the default Volumetric fog render settings.

**Returns:**

| Type | Description |
| --- | --- |
| table | The default Volumetric fog render settings. |

### getDefaultVoxelLODBoost {#getdefaultvoxellodboost}

``` { .lua .api-signature }
sm.render.getDefaultVoxelLODBoost(  )
```

Gets the default voxel LOD boost render setting.

**Returns:**

| Type | Description |
| --- | --- |
| number | The default voxel LOD boost render setting. |

### getScreenCoordinatesFromWorldPosition {#getscreencoordinatesfromworldposition}

``` { .lua .api-signature }
sm.render.getScreenCoordinatesFromWorldPosition( pos, width, height )
```

Return the screen coordinates that align with the given world position.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `pos` | [Vec3](../Userdata/Vec3.md) | World position to align |
| `width` | integer | Screen width |
| `height` | integer | Screen height |

**Returns:**

| Type | Description |
| --- | --- |
| number, number | The x and y screen coordinates. |

### resetCameraLight {#resetcameralight}

``` { .lua .api-signature }
sm.render.resetCameraLight(  )
```

Resets the camera light override settings.

## Client-only

### getDrawDistance {#getdrawdistance}

``` { .lua .api-signature }
sm.render.getDrawDistance(  )
```

Gets the draw distance.

**Returns:**

| Type | Description |
| --- | --- |
| number | The draw distance. |

### getOutdoorLighting {#getoutdoorlighting}

``` { .lua .api-signature }
sm.render.getOutdoorLighting(  )
```

Gets the lighting cycle fraction.

**Returns:**

| Type | Description |
| --- | --- |
| number | The fraction of the day cycle lighting. |

### isOutdoor {#isoutdoor}

``` { .lua .api-signature }
sm.render.isOutdoor(  )
```

Checks if client is outdoor

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if local client is outdoor. |

### resetAllReflectionColor {#resetallreflectioncolor}

``` { .lua .api-signature }
sm.render.resetAllReflectionColor(  )
```

Resets all the reflection color settings.

### resetFog {#resetfog}

``` { .lua .api-signature }
sm.render.resetFog(  )
```

Resets the fog override settings.

### resetGI {#resetgi}

``` { .lua .api-signature }
sm.render.resetGI(  )
```

Resets the global illumination override settings.

### resetHorizonLight {#resethorizonlight}

``` { .lua .api-signature }
sm.render.resetHorizonLight(  )
```

Resets the Horizon light settings.

### resetLUT {#resetlut}

``` { .lua .api-signature }
sm.render.resetLUT(  )
```

Resets the LUT override settings.

### resetVolumetricFog {#resetvolumetricfog}

``` { .lua .api-signature }
sm.render.resetVolumetricFog(  )
```

Resets the Volumetric fog override settings.

### resetVoxelLODBoost {#resetvoxellodboost}

``` { .lua .api-signature }
sm.render.resetVoxelLODBoost(  )
```

Resets the voxel terrain LOD boost override setting.

### setCameraLight {#setcameralight}

``` { .lua .api-signature }
sm.render.setCameraLight(
    intensity,
    range,
    color,
    farIntensity?,
    farRange?,
    farColor?
)
```

Sets the camera light override settings.

Optionally sets far camera light settings (used for camera pullback lerp).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `intensity` | number | The light intensity. |
| `range` | number | Light range. |
| `color` | [Color](../Userdata/Color.md) | Light color. |
| `farIntensity` *(optional)* | number | Far light intensity. (Optional) |
| `farRange` *(optional)* | number | Far light range. (Optional) |
| `farColor` *(optional)* | [Color](../Userdata/Color.md) | Far light color. (Optional) |

### setCinematic {#setcinematic}

``` { .lua .api-signature }
sm.render.setCinematic( cinematic )
```

Sets if a cinematic is playing

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `cinematic` | boolean | If true, sets to cinematic |

### setCloudSettings {#setcloudsettings}

``` { .lua .api-signature }
sm.render.setCloudSettings(
    coverage,
    height,
    radius,
    tallnessScale,
    directionalLightMod,
    scroll,
    scrollRotation
)
```

Sets the cloud settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `coverage` | number | The fraction of the cloud coverage. |
| `height` | number | The cloud height. |
| `radius` | number | The atmosphere radius. |
| `tallnessScale` | number | The tallness scale(0.1 - 4.0). |
| `directionalLightMod` | number | Directional light mod (0.0 - 1.0). |
| `scroll` | [Vec3](../Userdata/Vec3.md) | Cloud scroll. |
| `scrollRotation` | [Vec3](../Userdata/Vec3.md) | Cloud scroll rotation. |

### setFog {#setfog}

``` { .lua .api-signature }
sm.render.setFog(
    startDistance,
    endDistance,
    falloffFactor,
    startColor,
    endColor,
    verticalOpacity,
    verticalFadeDistance,
    verticalFalloff,
    verticalStart,
    verticalEnd,
    verticalStartColor,
    verticalEndColor,
    fadeDistance
)
```

Sets the fog override settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `startDistance` | number | Fog start distance. |
| `endDistance` | number | Fog end distance. |
| `falloffFactor` | number | Fog falloff. |
| `startColor` | [Color](../Userdata/Color.md) | Fog start color. |
| `endColor` | [Color](../Userdata/Color.md) | Fog end color. |
| `verticalOpacity` | number | Vertical fog opacity. (Optional) |
| `verticalFadeDistance` | number | Vertical fog fade distance.  (Optional) |
| `verticalFalloff` | number | Vertical fog falloff.  (Optional) |
| `verticalStart` | number | Vertical fog start distance.  (Optional) |
| `verticalEnd` | number | Vertical fog end distance.  (Optional) |
| `verticalStartColor` | [Color](../Userdata/Color.md) | Vertical fog start color.  (Optional) |
| `verticalEndColor` | [Color](../Userdata/Color.md) | Vertical fog end color.  (Optional) |
| `fadeDistance` | number | Fog fade distance. (Optional) |

### setGI {#setgi}

``` { .lua .api-signature }
sm.render.setGI( weight )
```

Sets the global illumination override settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `weight` | number | GI weight. |

### setHorizonLight {#sethorizonlight}

``` { .lua .api-signature }
sm.render.setHorizonLight(
    topColor,
    horizonColor,
    bottomColor,
    direction,
    start,
    end,
    falloff
)
```

Sets the Horizon light settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `topColor` | [Color](../Userdata/Color.md) | Color of the top of the horizon light. |
| `horizonColor` | [Color](../Userdata/Color.md) | Color of the horizon of the horizon light. |
| `bottomColor` | [Color](../Userdata/Color.md) | Color of the bottom of the horizon light. |
| `direction` | [Vec3](../Userdata/Vec3.md) | Direction of the horizon light. |
| `start` | number | Start distance for the horizon light. (Optional) |
| `end` | number | End distance for the horizon light. (Optional) |
| `falloff` | number | Falloff factor for the horizon light. (Optional) |

### setLUT {#setlut}

``` { .lua .api-signature }
sm.render.setLUT( LUT-A, LUT-B?, blend? )
```

Sets the LUT override settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `LUT-A` | string | Name of LUT A. |
| `LUT-B` *(optional)* | string | Name of LUT B. |
| `blend` *(optional)* | number | blend between 0.0 and 1.0 for LUT A and B. (Defaults to 0.0) |

### setOutdoorLighting {#setoutdoorlighting}

``` { .lua .api-signature }
sm.render.setOutdoorLighting( value )
```

Sets the lighting cycle fraction.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `value` | number | The fraction of the day cycle lighting. |

### setReflectionLevelColor {#setreflectionlevelcolor}

``` { .lua .api-signature }
sm.render.setReflectionLevelColor( settingsLevel, min, max, mul )
```

Sets the reflection color correction settings for one reflection level.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `settingsLevel` | string | Off/Low/Medium/High. |
| `min` | number | Color min. |
| `max` | number | Color max. |
| `mul` | number | Color mul. |

### setVolumetricFog {#setvolumetricfog}

``` { .lua .api-signature }
sm.render.setVolumetricFog( min, max, loopSpeed, scrollSpeed, scale, intensity )
```

Sets the Volumetric fog override settings.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `min` | number | Fog min. |
| `max` | number | Fog max. |
| `loopSpeed` | number | Fog loop speed. |
| `scrollSpeed` | [Vec3](../Userdata/Vec3.md) | Fog scroll speed. |
| `scale` | [Vec3](../Userdata/Vec3.md) | Fog scale. |
| `intensity` | number | Fog intensity. |

### setVoxelLODBoost {#setvoxellodboost}

``` { .lua .api-signature }
sm.render.setVoxelLODBoost( boost )
```

Sets the voxel terrain LOD boost override setting.

The value is capped by the current draw distance quality.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `boost` | number | Voxel terrain LOD boost. |
