# sm.builderGuide

**Associated type:** [BuilderGuide](../Userdata/BuilderGuide.md)

Builder Guide

## Functions

### createBuilderGuide {#createbuilderguide}

``` { .lua .api-signature }
sm.builderGuide.createBuilderGuide(
    path,
    shape,
    ignoreBlockUuid?,
    recordErrors?,
    allowExtraBlocks?
)
```

Create a [BuilderGuide](../Userdata/BuilderGuide.md), comparing the creation from the root [Shape](../Userdata/Shape.md) to the blueprint given by the path.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | A file path to the builder guide blueprint. |
| `shape` | [Shape](../Userdata/Shape.md) | Root [Shape](../Userdata/Shape.md) for comparing the creation from. |
| `ignoreBlockUuid` *(optional)* | boolean | Should block uuid be ignored for stage completion. (Defaults to false) |
| `recordErrors` *(optional)* | boolean | Should errors be recorded. Needed for getErrorInfo (Defaults to false) |
| `allowExtraBlocks` *(optional)* | boolean | Should extra blocks be ignored for stage completion. (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| [BuilderGuide](../Userdata/BuilderGuide.md) | The created guide. |
