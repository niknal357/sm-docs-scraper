# GuiInterface

**Usage:** Client Only

**Serializable:** No

A userdata object representing a <strong>GUI interface</strong>.

A <strong>gui interface</strong> is an adapter between a script and a GUI.

Can only be used on the client.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`GuiInterface == GuiInterface` | boolean | Checks if two instances of [GuiInterface](GuiInterface.md) refer to the same GuiInterface. |

## Client-only

### addGridItem {#addgriditem}

``` { .lua .api-signature }
guiInterface:addGridItem( gridName, item )
```

Adds an item to a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `item` | table | The item |

### addGridItemsFromFile {#addgriditemsfromfile}

``` { .lua .api-signature }
guiInterface:addGridItemsFromFile( gridName, jsonPath, additionalData? )
```

Adds items to a grid from json

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `jsonPath` | string | Json file path |
| `additionalData` *(optional)* | table | Additional data to the json (Optional) |

### addListItem {#addlistitem}

``` { .lua .api-signature }
guiInterface:addListItem( listName, itemName, data )
```

Appends an item to a list

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `listName` | string | The name of the list |
| `itemName` | string | The name of the item |
| `data` | table | Table of data to store |

### addToPickupDisplay {#addtopickupdisplay}

``` { .lua .api-signature }
guiInterface:addToPickupDisplay( uuid, amount )
```

Adds an item to the item pickup display

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The players survival hud interface |
| `uuid` | [Uuid](Uuid.md) | The item uuid |
| `amount` | number | Quantity of items picked up |

### clearGrid {#cleargrid}

``` { .lua .api-signature }
guiInterface:clearGrid( gridName )
```

Clears a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid to clear |

### clearList {#clearlist}

``` { .lua .api-signature }
guiInterface:clearList( listName )
```

Clears a list

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `listName` | string | The name of the list |

### clearOnCloseCallback {#clearonclosecallback}

``` { .lua .api-signature }
guiInterface:clearOnCloseCallback(  )
```

Clears the close callback so it will not be called when the gui is closed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |

### close {#close}

``` { .lua .api-signature }
guiInterface:close(  )
```

Close a gui interface

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface to close |

### compassAddIcon {#compassaddicon}

``` { .lua .api-signature }
guiInterface:compassAddIcon( iconName, image?, showDistance?, width?, height? )
```

Add an icon to the compass.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `compassHud` | [GuiInterface](GuiInterface.md) | The compass hud GUI. |
| `iconName` | string | Name of the new compass icon. |
| `image` *(optional)* | string | The name or path of the image. (Optional) |
| `showDistance` *(optional)* | string | If the icon should display distance. (Optional) |
| `width` *(optional)* | string | The width of the icon, defaults to 22. (Optional) |
| `height` *(optional)* | string | The height of the icon, defaults to 22. (Optional) |

### compassPingMarker {#compasspingmarker}

``` { .lua .api-signature }
guiInterface:compassPingMarker(  )
```

### compassRemoveIcon {#compassremoveicon}

``` { .lua .api-signature }
guiInterface:compassRemoveIcon( iconName )
```

Remove an icon from the compass.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `compassHud` | [GuiInterface](GuiInterface.md) | The compass hud GUI. |
| `iconName` | string | Name of a compass icon. |

<a id="compassseticonhost"></a>
### compassSetIconHost(Character, string?) {#compassseticonhost-character-string-optional}

``` { .lua .api-signature }
guiInterface:compassSetIconHost( host, joint? )
```

Sets a [Character](Character.md) as host for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `host` | [Character](Character.md) | The host of the icon |
| `joint` *(optional)* | string | The joint/bone name (Optional) |

### compassSetIconHost(string, Shape, string?) {#compassseticonhost-string-shape-string-optional}

``` { .lua .api-signature }
guiInterface:compassSetIconHost( iconName, host, joint? )
```

Sets a [Shape](Shape.md) as host for a compass icon

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `compassHud` | [GuiInterface](GuiInterface.md) | The compass hud GUI. |
| `iconName` | string | Name of a compass icon. |
| `host` | [Shape](Shape.md) | The host of the icon |
| `joint` *(optional)* | string | The host joint/bone name (Optional) |

### compassSetIconStacking {#compassseticonstacking}

``` { .lua .api-signature }
guiInterface:compassSetIconStacking( iconName, stacking )
```

Sets whether the icon should be stacked on top of other icons.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `compassHud` | [GuiInterface](GuiInterface.md) | The compass hud GUI. |
| `iconName` | string | Name of a compass icon. |
| `stacking` | boolean | The stacking setting. |

### compassSetIconWorldPosition {#compassseticonworldposition}

``` { .lua .api-signature }
guiInterface:compassSetIconWorldPosition( iconName, worldPosition, world? )
```

Sets the world position for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `compassHud` | [GuiInterface](GuiInterface.md) | The compass hud GUI. |
| `iconName` | string | Name of a compass icon. |
| `worldPosition` | [Vec3](Vec3.md) | The position to set. |
| `world` *(optional)* | [World](World.md) | The world, defaults to same as the script |

### createDropDown {#createdropdown}

``` { .lua .api-signature }
guiInterface:createDropDown( widgetName, functionName, options )
```

Creates a dropdown at the specified widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `functionName` | string | The name of the function |
| `options` | table | The options in the dropdown menu |

### createGridFromJson {#creategridfromjson}

``` { .lua .api-signature }
guiInterface:createGridFromJson( gridName, index )
```

Creats a grid from a table/json

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `index` | table | Grid data table { type=string, layout=string, itemWidth=integer, itemHeight=integer, itemCount=integer } |

### createHorizontalSlider {#createhorizontalslider}

``` { .lua .api-signature }
guiInterface:createHorizontalSlider(
    widgetName,
    range,
    value,
    functionName,
    numbered?,
    inverted?
)
```

Creates a slider at the specified widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `range` | number | The range of the slider |
| `value` | number | The start value on the slider |
| `functionName` | string | Slider change callback function name |
| `numbered` *(optional)* | boolean | Enable numbered steps (Defaults to false) |
| `inverted` *(optional)* | boolean | Invert slider direction (Defaults to false) |

### createVerticalSlider {#createverticalslider}

``` { .lua .api-signature }
guiInterface:createVerticalSlider( widgetName, range, value, functionName )
```

Creates a slider at the specified widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `range` | number | The range of the slider |
| `value` | number | The start value on the slider |
| `functionName` | string | Slider change callback function name |

### destroy {#destroy}

``` { .lua .api-signature }
guiInterface:destroy(  )
```

Destroy a gui interface

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The interface to destroy |

### getWorldPosition {#getworldposition}

``` { .lua .api-signature }
guiInterface:getWorldPosition(  )
```

Gets the current world position of a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |

**Returns:**

| Type | Description |
| --- | --- |
| [Vec3](Vec3.md)								The in world position of the gui |  |

### isActive {#isactive}

``` { .lua .api-signature }
guiInterface:isActive(  )
```

Checks if a gui interface is active

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if gui is active |

### open {#open}

``` { .lua .api-signature }
guiInterface:open(  )
```

Open a gui interface

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface to open |

### playEffect {#playeffect}

``` { .lua .api-signature }
guiInterface:playEffect( widgetName, effectName, restart?, useHistory? )
```

Plays an effect at a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `effectName` | string | The name of the effect |
| `restart` *(optional)* | boolean | If the effect should restart if its already playing (Defaults to true) |
| `useHistory` *(optional)* | boolean | If the effect should use call history (Defaults to false) |

### playGridEffect {#playgrideffect}

``` { .lua .api-signature }
guiInterface:playGridEffect( gridName, index, effectName, restart? )
```

Plays an effect at widget inside a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `index` | integer | The index in the grid |
| `effectName` | string | The name of the effect |
| `restart` *(optional)* | boolean | If the effect should restart if its already palying (Defaults to true) |

### removeFromPickupDisplay {#removefrompickupdisplay}

``` { .lua .api-signature }
guiInterface:removeFromPickupDisplay( uuid, amount )
```

Removes an item from the item pickup display

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The players survival hud interface |
| `uuid` | [Uuid](Uuid.md) | The item uuid |
| `amount` | number | Quantity of items to remove |

### setButtonCallback {#setbuttoncallback}

``` { .lua .api-signature }
guiInterface:setButtonCallback( buttonName, callback )
```

Sets a button callback to be called when the button is pressed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `buttonName` | string | The button name |
| `callback` | string | Function to be called when button is pressed |

### setButtonEnabled {#setbuttonenabled}

``` { .lua .api-signature }
guiInterface:setButtonEnabled( widgetName, enabled )
```

Sets the enabled state of a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `enabled` | boolean | True if the widget should be enabled |

### setButtonState {#setbuttonstate}

``` { .lua .api-signature }
guiInterface:setButtonState( buttonName, state )
```

Sets the button state

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `buttonName` | string | The name of the button |
| `state` | boolean | The state of the button |

### setColor {#setcolor}

``` { .lua .api-signature }
guiInterface:setColor( widgetName, Color )
```

Sets the color of a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `Color` | [Color](Color.md) | The color |

### setContainer {#setcontainer}

``` { .lua .api-signature }
guiInterface:setContainer( gridName, container )
```

Sets a container to a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `container` | [Container](Container.md) | The container |

### setContainers {#setcontainers}

``` { .lua .api-signature }
guiInterface:setContainers( gridName, containers )
```

Sets multiple containers to a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `containers` | table | Table of containers. {[Container](Container.md), ..} |

### setData {#setdata}

``` { .lua .api-signature }
guiInterface:setData( widgetName, data )
```

Sets data to a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `data` | table | The data |

### setDressbotUnlockCallback {#setdressbotunlockcallback}

``` { .lua .api-signature }
guiInterface:setDressbotUnlockCallback( function )
```

Sets the Lua callback for when the DressbotGui unlocks something. The callback will receive the uuid of the unlocked customization item.

/

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The DressbotGui interface. |
| `function` | string | The name function. |

### setFadeRange {#setfaderange}

``` { .lua .api-signature }
guiInterface:setFadeRange( range )
```

Sets the fade range for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `range` | number | The fade range |

### setFocus {#setfocus}

``` { .lua .api-signature }
guiInterface:setFocus( widgetName )
```

Sets a widget to receive key focus

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget that needs focus |

### setGridButtonCallback {#setgridbuttoncallback}

``` { .lua .api-signature }
guiInterface:setGridButtonCallback( buttonName, callback )
```

Sets a callback to be called when a button inside a grid is pressed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `buttonName` | string | The button name |
| `callback` | string | Function to be called when button is pressed |

### setGridItem {#setgriditem}

``` { .lua .api-signature }
guiInterface:setGridItem( gridName, index, item )
```

Sets an item in a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `index` | integer | The item index |
| `item` | table | The item |

### setGridItemChangedCallback {#setgriditemchangedcallback}

``` { .lua .api-signature }
guiInterface:setGridItemChangedCallback( gridName, callback )
```

Sets a callback to be called when a grid item is changed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The grid name |
| `callback` | string | Function to be called when button is pressed |

### setGridItemClickedCallback {#setgriditemclickedcallback}

``` { .lua .api-signature }
guiInterface:setGridItemClickedCallback( gridName, callback )
```

Sets a callback to be called when a grid item is changed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The grid name |
| `callback` | string | Function to be called when button is pressed |

### setGridMouseFocusCallback {#setgridmousefocuscallback}

``` { .lua .api-signature }
guiInterface:setGridMouseFocusCallback( buttonName, callback )
```

Sets a callback to be called when a grid widget gets mouse focus

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `buttonName` | string | The button name |
| `callback` | string | Function to be called when button is pressed |

### setGridSize {#setgridsize}

``` { .lua .api-signature }
guiInterface:setGridSize( gridName, index )
```

Sets the size of a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `index` | integer | The size |

<a id="sethost"></a>
### setHost(Character, string?) {#sethost-character-string-optional}

``` { .lua .api-signature }
guiInterface:setHost( character, joint? )
```

Sets a [Character](Character.md) as host for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `character` | [Character](Character.md) | The character to host the gui |
| `joint` *(optional)* | string | The joint (Optional) |

### setHost(Shape, string?) {#sethost-shape-string-optional}

``` { .lua .api-signature }
guiInterface:setHost( shape, joint? )
```

Sets a [Shape](Shape.md) as host for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `shape` | [Shape](Shape.md) | The shape to host the gui |
| `joint` *(optional)* | string | The joint (Optional) |

### setIconImage {#seticonimage}

``` { .lua .api-signature }
guiInterface:setIconImage( itembox, uuid )
```

Sets the icon image to a shape from an uuid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `itembox` | string | The name of the itembox |
| `uuid` | [Uuid](Uuid.md) | The item uuid |

### setImage {#setimage}

``` { .lua .api-signature }
guiInterface:setImage( imagebox, image )
```

Sets the image of an imagebox

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `imagebox` | string | The name of the imagebox widget |
| `image` | string | The name or path of the image |

### setItemIcon {#setitemicon}

``` { .lua .api-signature }
guiInterface:setItemIcon( imagebox, itemResource, itemGroup, itemName )
```

Sets the resource, group and item name on an imagebox widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `imagebox` | string | The name of the imagebox |
| `itemResource` | string | The item resource  |
| `itemGroup` | string | The item group |
| `itemName` | string | The item name |

### setListSelectionCallback {#setlistselectioncallback}

``` { .lua .api-signature }
guiInterface:setListSelectionCallback( listName, callback )
```

Sets a callback to be called when a list selection is changed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `listName` | string | The list name |
| `callback` | string | Function to be called when list is selected |

### setMaxRenderDistance {#setmaxrenderdistance}

``` { .lua .api-signature }
guiInterface:setMaxRenderDistance( distance )
```

Sets the maximum render distance for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `distance` | number | The max render distance |

### setMeshPreview {#setmeshpreview}

``` { .lua .api-signature }
guiInterface:setMeshPreview( widgetName, uuid )
```

Sets a mesh preview to display an item from uuid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `uuid` | [Uuid](Uuid.md) | The item uuid to display |

### setOnCloseCallback {#setonclosecallback}

``` { .lua .api-signature }
guiInterface:setOnCloseCallback( callback )
```

Sets a callback to be called when the gui is closed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `callback` | string | Function to be called when gui is closed |

### setOnOpenCallback {#setonopencallback}

``` { .lua .api-signature }
guiInterface:setOnOpenCallback( callback )
```

Sets a callback to be called when the gui is opened

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `callback` | string | Function to be called when gui is opened |

### setOpenCloseEffect {#setopencloseeffect}

``` { .lua .api-signature }
guiInterface:setOpenCloseEffect( openEffectName, closEffectName )
```

Overwrites default gui effects with specified open and close effects

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `openEffectName` | string | The name of the open effect |
| `closEffectName` | string | The name of the close effect |

### setRequireLineOfSight {#setrequirelineofsight}

``` { .lua .api-signature }
guiInterface:setRequireLineOfSight( required )
```

Sets if a world gui requires line of sight to be shown

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `required` | boolean | True if gui requires line of sight to render |

### setSelectedDropDownItem {#setselecteddropdownitem}

``` { .lua .api-signature }
guiInterface:setSelectedDropDownItem(  )
```

### setSelectedListItem {#setselectedlistitem}

``` { .lua .api-signature }
guiInterface:setSelectedListItem( listName, itemName )
```

Selects an item in a list

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `listName` | string | The name of the list |
| `itemName` | string | The name of the item |

### setSliderCallback {#setslidercallback}

``` { .lua .api-signature }
guiInterface:setSliderCallback( sliderName, callback )
```

Sets a callback to be called when the slider is moved

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `sliderName` | string | The button name |
| `callback` | string | Function to be called when slider is moved |

### setSliderData {#setsliderdata}

``` { .lua .api-signature }
guiInterface:setSliderData( sliderName, range, position )
```

Sets the position and range of a slider

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `sliderName` | string | The name of the slider |
| `range` | unsigned | The slider range |
| `position` | unsigned | The slider position |

### setSliderPosition {#setsliderposition}

``` { .lua .api-signature }
guiInterface:setSliderPosition( sliderName, position )
```

Sets the position of a slider

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `sliderName` | string | The name of the slider |
| `position` | integer | The slider position |

### setSliderRange {#setsliderrange}

``` { .lua .api-signature }
guiInterface:setSliderRange( sliderName, range )
```

Sets the slider range of a slider.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `sliderName` | string | The name of the slider |
| `range` | integer | The slider range |

### setSliderRangeLimit {#setsliderrangelimit}

``` { .lua .api-signature }
guiInterface:setSliderRangeLimit( sliderName, limit )
```

Sets the range limit of a slider

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `sliderName` | string | The name of the slider |
| `limit` | integer | The slider range limit |

### setText {#settext}

``` { .lua .api-signature }
guiInterface:setText( textbox, text )
```

Sets the text caption of a textbox widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `textbox` | string | The name of the textbox widget |
| `text` | string | The text |

### setTextAcceptedCallback {#settextacceptedcallback}

``` { .lua .api-signature }
guiInterface:setTextAcceptedCallback( editBoxName, callback )
```

Sets a callback to be called when the text change is accepted

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `editBoxName` | string | The edit box name |
| `callback` | string | Function to be called when text is committed |

### setTextChangedCallback {#settextchangedcallback}

``` { .lua .api-signature }
guiInterface:setTextChangedCallback( editBoxName, callback )
```

Sets a callback to be called when the text is changed

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `editBoxName` | string | The edit box name |
| `callback` | string | Function to be called when text is edited |

### setVisible {#setvisible}

``` { .lua .api-signature }
guiInterface:setVisible( widgetName, visible )
```

Sets a widget to be visible or not

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `visible` | boolean | True if visible |

### setWidgetState {#setwidgetstate}

``` { .lua .api-signature }
guiInterface:setWidgetState( widgetName, state )
```

Sets the state of a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `state` | integer | The widget state [sm.gui.widgetStates](../Static-Functions/sm.gui.md#widgetstates) |

### setWorldPosition {#setworldposition}

``` { .lua .api-signature }
guiInterface:setWorldPosition( worldPosition, world? )
```

Sets the world position for a world gui

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `worldPosition` | [Vec3](Vec3.md) | The position to set. |
| `world` *(optional)* | [World](World.md) | The world, defaults to same as the script |

### stopEffect {#stopeffect}

``` { .lua .api-signature }
guiInterface:stopEffect( widgetName, effectName, immediate?, useHistory? )
```

Stops an effect playing at a widget

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `widgetName` | string | The name of the widget |
| `effectName` | string | The name of the effect |
| `immediate` *(optional)* | boolean | When true, the effect stops immediately (Defaults to false) |
| `useHistory` *(optional)* | boolean | If the effect should use call history (Defaults to false) |

### stopGridEffect {#stopgrideffect}

``` { .lua .api-signature }
guiInterface:stopGridEffect( gridName, index, effectName )
```

Stopts an effect playing inside a grid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The Gui interface |
| `gridName` | string | The name of the grid |
| `index` | integer | The index in the grid |
| `effectName` | string | The name of the effect |

### trackQuest {#trackquest}

``` { .lua .api-signature }
guiInterface:trackQuest( name, title, mainQuest, questTasks, icon? )
```

Adds a quest to the quest tracker

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The QuestGui interface |
| `name` | string | The name of quest |
| `title` | string | The quest title to be displayed in the tracker |
| `mainQuest` | boolean | If the quest is a main quest (Displayed on top in the tracker) |
| `questTasks` | table | The table of quest tasks to display in the log Task{ name = string, text = string, count = number, target = number, complete = boolean } |
| `icon` *(optional)* | string | The icon to display in the tracker (Optional) |

### untrackQuest {#untrackquest}

``` { .lua .api-signature }
guiInterface:untrackQuest( questName )
```

Removes a quest from the quest tracker

/

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `gui` | [GuiInterface](GuiInterface.md) | The QuestGui interface |
| `questName` | string | The name of quest |
