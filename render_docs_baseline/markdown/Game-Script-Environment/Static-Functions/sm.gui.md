# sm.gui

The <strong>gui</strong> library contains various utility functions for handling user interfaces.

This library can only be used on the client.

## Constants

### widgetStates {#widgetstates}

Widget states

| Value |
| --- |
| disabled, |
| normal, |
| highlighted, |
| pushed, |
| disabled_checked, |
| normal_checked, |
| highlighted_checked, |
| pushed_checked |

**Returns:**

| Type | Description |
| --- | --- |
| table | The widget states list. |

## Server + Client

### chatMessage {#chatmessage}

``` { .lua .api-signature }
sm.gui.chatMessage( message )
```

Prints text in the chat gui.

> **Note:**
> Will not be sent to other players.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `message` | string | The message. |

### createWidget {#createwidget}

``` { .lua .api-signature }
sm.gui.createWidget(  )
```

> **Deprecated:**
> Use [sm.gui.createGuiFromLayout](#createguifromlayout)
>

Removed! Does nothing.

### getItemIconFromUuid {#getitemiconfromuuid}

``` { .lua .api-signature }
sm.gui.getItemIconFromUuid( uuid )
```

Gets the item resource, group and name for an item icon from a uuid

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| {string, string, string, string, string}	The item resource, group, name, trackingType and shapeType. |  |

### setCenterIcon {#setcentericon}

``` { .lua .api-signature }
sm.gui.setCenterIcon(  )
```

> **Deprecated:**
> Use [sm.gui.setInteractionText](#setinteractiontext)
>

Removed! Does nothing.

### setCharacterDebugText {#setcharacterdebugtext}

``` { .lua .api-signature }
sm.gui.setCharacterDebugText( character, text, clear? )
```

Set a text for the character that will be displayed above its head. Only has effect in dev build.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `character` | [Character](../Userdata/Character.md) | The character. |
| `text` | string | The debug text. |
| `clear` *(optional)* | boolean | If true the previous text will be overwritten. (Defaults to true) |

### setGarageImportGuiStorage {#setgarageimportguistorage}

``` { .lua .api-signature }
sm.gui.setGarageImportGuiStorage( container )
```

Set the storage container for the garage creation import gui to use

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container import gui should use for materials. |

## Client-only

### bindDisplayMessageCallback {#binddisplaymessagecallback}

``` { .lua .api-signature }
sm.gui.bindDisplayMessageCallback( callback )
```

Sets a target callback for generic notification popups

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `callback` | string | Function to be called when a alert message is called |

### blockInGameMenu {#blockingamemenu}

``` { .lua .api-signature }
sm.gui.blockInGameMenu( block )
```

Sets the blocking state for the in game menu.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `block` | boolean | The new blocking state for the in game menu. |

### computeTextSize {#computetextsize}

``` { .lua .api-signature }
sm.gui.computeTextSize( text, font, align, maxWidth?, replaceTags? )
```

Calculates the 720 widget size required to display a text

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `text` | string | The text to compute. |
| `font` | string | The font to use. |
| `align` | string | The text alignment. |
| `maxWidth` *(optional)* | number | The maximum desired widget width before wrapping (optional) (Defaults to -1) |
| `replaceTags` *(optional)* | boolean | Should tags be replaced before calculating? (optional) (Defaults to true) |

**Returns:**

| Type | Description |
| --- | --- |
| {number, number} | The calculated width and height. |

### createAmmunitionContainerGui {#createammunitioncontainergui}

``` { .lua .api-signature }
sm.gui.createAmmunitionContainerGui( destroyOnClose? )
```

Create a ammunition container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createBagIconGui {#createbagicongui}

``` { .lua .api-signature }
sm.gui.createBagIconGui( destroyOnClose? )
```

> **Deprecated:**
> use createWorldIconGui
>

Create a bag icon GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createBatteryContainerGui {#createbatterycontainergui}

``` { .lua .api-signature }
sm.gui.createBatteryContainerGui( destroyOnClose? )
```

Create a battery container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createBeaconIconGui {#createbeaconicongui}

``` { .lua .api-signature }
sm.gui.createBeaconIconGui( destroyOnClose? )
```

> **Deprecated:**
> use createWorldIconGui
>

Create a beacon icon GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createChallengeHUDGui {#createchallengehudgui}

``` { .lua .api-signature }
sm.gui.createChallengeHUDGui( destroyOnClose? )
```

Create a challenge HUD GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createChallengeMessageGui {#createchallengemessagegui}

``` { .lua .api-signature }
sm.gui.createChallengeMessageGui( destroyOnClose? )
```

Create a challenge message HUD GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createCharacterCustomizationGui {#createcharactercustomizationgui}

``` { .lua .api-signature }
sm.gui.createCharacterCustomizationGui( destroyOnClose? )
```

Create a character customization GUI.

> **Note:**
> Character customization gui has two magic callbacks
> Mouse drag cl_onDragZoneUsed ( number, number )
> Mouse scroll cl_onDragZoneUsed ( number )

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createChemicalContainerGui {#createchemicalcontainergui}

``` { .lua .api-signature }
sm.gui.createChemicalContainerGui( destroyOnClose? )
```

Create a chemical container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createCompassHudGui {#createcompasshudgui}

``` { .lua .api-signature }
sm.gui.createCompassHudGui( destroyOnClose? )
```

Create a compass hud GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createContainerGui {#createcontainergui}

``` { .lua .api-signature }
sm.gui.createContainerGui( destroyOnClose? )
```

Create a container GUI, for showing two containers.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createCraftBotGui {#createcraftbotgui}

``` { .lua .api-signature }
sm.gui.createCraftBotGui( destroyOnClose? )
```

Create a craft bot GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createDressBotGui {#createdressbotgui}

``` { .lua .api-signature }
sm.gui.createDressBotGui( destroyOnClose? )
```

Create a dress bot GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createEngineGui {#createenginegui}

``` { .lua .api-signature }
sm.gui.createEngineGui( destroyOnClose? )
```

Create a engine GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createFertilizerContainerGui {#createfertilizercontainergui}

``` { .lua .api-signature }
sm.gui.createFertilizerContainerGui( destroyOnClose? )
```

Create a fertilizer container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createGasContainerGui {#creategascontainergui}

``` { .lua .api-signature }
sm.gui.createGasContainerGui( destroyOnClose? )
```

Create a gas container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createGlowstickContainerGui {#createglowstickcontainergui}

``` { .lua .api-signature }
sm.gui.createGlowstickContainerGui( destroyOnClose? )
```

Create a glowstick container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createGuiFromLayout {#createguifromlayout}

``` { .lua .api-signature }
sm.gui.createGuiFromLayout( layout, destroyOnClose?, settings? )
```

Create a GUI from a layout file.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `layout` | string | Path to the layout file |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |
| `settings` *(optional)* | table | Table with bool settings for: isHud, isInteractive, needsCursor |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createHideoutGui {#createhideoutgui}

``` { .lua .api-signature }
sm.gui.createHideoutGui( destroyOnClose? )
```

Create a hideout gui GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createLogbookGui {#createlogbookgui}

``` { .lua .api-signature }
sm.gui.createLogbookGui( destroyOnClose? )
```

Create a log book GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createMechanicStationGui {#createmechanicstationgui}

``` { .lua .api-signature }
sm.gui.createMechanicStationGui( destroyOnClose? )
```

Create a mechanic station dispenser GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createMininghubDispenserGui {#createmininghubdispensergui}

``` { .lua .api-signature }
sm.gui.createMininghubDispenserGui( destroyOnClose? )
```

Create a mining hub dispenser GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createNameTagGui {#createnametaggui}

``` { .lua .api-signature }
sm.gui.createNameTagGui( destroyOnClose? )
```

Create a name tag GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createOreCrusherContainerGui {#createorecrushercontainergui}

``` { .lua .api-signature }
sm.gui.createOreCrusherContainerGui( destroyOnClose=false )
```

Create a ore crusher container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose=false` | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createPortableCrafterGui {#createportablecraftergui}

``` { .lua .api-signature }
sm.gui.createPortableCrafterGui( destroyOnClose? )
```

Create a portable craftbot GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createProspectorContainerGui {#createprospectorcontainergui}

``` { .lua .api-signature }
sm.gui.createProspectorContainerGui( destroyOnClose? )
```

Create a prospector container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createQuestTrackerGui {#createquesttrackergui}

``` { .lua .api-signature }
sm.gui.createQuestTrackerGui( destroyOnClose? )
```

Create a quest tracker GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createRefineryContainerGui {#createrefinerycontainergui}

``` { .lua .api-signature }
sm.gui.createRefineryContainerGui( destroyOnClose=false )
```

Create a refinery container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose=false` | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSawbotGui {#createsawbotgui}

``` { .lua .api-signature }
sm.gui.createSawbotGui( destroyOnClose? )
```

Create a saw bot GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSeatGui {#createseatgui}

``` { .lua .api-signature }
sm.gui.createSeatGui( destroyOnClose? )
```

Create a seat GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSeatUpgradeGui {#createseatupgradegui}

``` { .lua .api-signature }
sm.gui.createSeatUpgradeGui( destroyOnClose? )
```

Create a seat upgrade GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSeedContainerGui {#createseedcontainergui}

``` { .lua .api-signature }
sm.gui.createSeedContainerGui( destroyOnClose? )
```

Create a seed container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSteeringBearingGui {#createsteeringbearinggui}

``` { .lua .api-signature }
sm.gui.createSteeringBearingGui( destroyOnClose? )
```

Create a steering bearing upgrade GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createSurvivalHudGui {#createsurvivalhudgui}

``` { .lua .api-signature }
sm.gui.createSurvivalHudGui( destroyOnClose? )
```

Create a survival hud GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createWaterContainerGui {#createwatercontainergui}

``` { .lua .api-signature }
sm.gui.createWaterContainerGui( destroyOnClose? )
```

Create a water container GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createWaypointIconGui {#createwaypointicongui}

``` { .lua .api-signature }
sm.gui.createWaypointIconGui( destroyOnClose? )
```

> **Deprecated:**
> use createWorldIconGui
>

Create a waypoint icon GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createWorkbenchGui {#createworkbenchgui}

``` { .lua .api-signature }
sm.gui.createWorkbenchGui( destroyOnClose? )
```

Create a workbench GUI.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### createWorldIconGui {#createworldicongui}

``` { .lua .api-signature }
sm.gui.createWorldIconGui( width, height, layout?, destroyOnClose? )
```

Create a world icon GUI from a layout file.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `width` | integer | The width. |
| `height` | integer | The height. |
| `layout` *(optional)* | string | Path to the layout file (Defaults to "$GAME_DATA/Gui/Layouts/Hud/Hud_WorldIcon.layout") |
| `destroyOnClose` *(optional)* | boolean | If true the gui is destroyed when closed, otherwise the gui can be reused. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| [GuiInterface](../Userdata/GuiInterface.md) | The gui interface to the created gui. |

### displayAlertText {#displayalerttext}

``` { .lua .api-signature }
sm.gui.displayAlertText( text, duration?, queued? )
```

Displays an alert message at the top of the screen for a set duration.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `text` | string | The message to be displayed |
| `duration` *(optional)* | number | The time in seconds during which the message is shown. Defaults to 4 seconds |
| `queued` *(optional)* | boolean | If true the message is queued, otherwise it is displayed instantly. Defaults to false |

### endFadeToBlack {#endfadetoblack}

``` { .lua .api-signature }
sm.gui.endFadeToBlack( duration, force? )
```

Fades the screen back from a fade to black.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `duration` | number | Animation duration |
| `force` *(optional)* | boolean | If true, start the fade out from full black even if there was no fade to black active. (Defaults to false) |

### exitToMenu {#exittomenu}

``` { .lua .api-signature }
sm.gui.exitToMenu(  )
```

Exits the current game and returns to the main menu

> **Note:**
> Can only be used in the Challenge Mode

### getCurrentLanguage {#getcurrentlanguage}

``` { .lua .api-signature }
sm.gui.getCurrentLanguage(  )
```

Returns the current users language setting.

**Returns:**

| Type | Description |
| --- | --- |
| string | The language setting ex. "English". |

### getKeyBinding {#getkeybinding}

``` { .lua .api-signature }
sm.gui.getKeyBinding( action, hyper? )
```

Returns the set binding for an action as a string

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `action` | string | The action |
| `hyper` *(optional)* | boolean | If the string should contain hyper text (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| string | The key binding |

### getScreenSize {#getscreensize}

``` { .lua .api-signature }
sm.gui.getScreenSize(  )
```

Returns the size of the screen.

**Returns:**

| Type | Description |
| --- | --- |
| integer,integer | The screen size as width and height. |

### hasActiveGui {#hasactivegui}

``` { .lua .api-signature }
sm.gui.hasActiveGui(  )
```

Returns whether the player has an active gui or not

**Returns:**

| Type | Description |
| --- | --- |
| boolean | guiActive	Whether the player has an active gui or not. |

### hideGui {#hidegui}

``` { .lua .api-signature }
sm.gui.hideGui( visible )
```

Set gui visibility.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `visible` | boolean | The gui visibility |

### hideHotbar {#hidehotbar}

``` { .lua .api-signature }
sm.gui.hideHotbar( visible )
```

Set hotbar visibility.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `visible` | boolean | The hotbar visibility |

### openGarageImportGui {#opengarageimportgui}

``` { .lua .api-signature }
sm.gui.openGarageImportGui(  )
```

Open the garage creation import GUI

### setGarageButtonCallback {#setgaragebuttoncallback}

``` { .lua .api-signature }
sm.gui.setGarageButtonCallback( callback )
```

Sets a button callback to be called when the button is pressed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `callback` | string | Function to be called when button is pressed |

### setGarageErrorCallback {#setgarageerrorcallback}

``` { .lua .api-signature }
sm.gui.setGarageErrorCallback( callback )
```

Sets a callback to be called when an error with the import is met.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `callback` | string | Function to be called when error is met |

### setInteractionText {#setinteractiontext}

``` { .lua .api-signature }
sm.gui.setInteractionText( text1, binding1?, text2?, binding2?, text3? )
```

Set the binding text displayed at the center.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `text1` | string | The leftmost segment. |
| `binding1` *(optional)* | string | The left white segment. |
| `text2` *(optional)* | string | The mid or end segment. |
| `binding2` *(optional)* | string | The right white segment. |
| `text3` *(optional)* | string | The rightmost segment. |

### setProgressFraction {#setprogressfraction}

``` { .lua .api-signature }
sm.gui.setProgressFraction( progress )
```

Set the progress fraction filling the circle icon displayed at the center.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `progress` | number | The fraction that determines how much of the circle is filled. |

### startFadeToBlack {#startfadetoblack}

``` { .lua .api-signature }
sm.gui.startFadeToBlack( duration, timeout )
```

Fades the screen to black and back after timeout.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `duration` | number | Animation duration |
| `timeout` | number | Seconds until the fade fades back |

### startFadeToBlackWaitForWorld {#startfadetoblackwaitforworld}

``` { .lua .api-signature }
sm.gui.startFadeToBlackWaitForWorld( duration, timeout )
```

Fades the screen to black, waits for the world to finish loading, then fades back.

First waits until timeout, then holds black until the world is ready or a max timeout is reached.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `duration` | number | Animation duration |
| `timeout` | number | Seconds until the fade starts waiting for the world |

### ticksToTimeString {#tickstotimestring}

``` { .lua .api-signature }
sm.gui.ticksToTimeString( ticks )
```

Converts ticks to a HH:MM:SS string representation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `ticks` | integer | Game ticks |

**Returns:**

| Type | Description |
| --- | --- |
| string | time		Human time formatted string |

### translateLocalizationTags {#translatelocalizationtags}

``` { .lua .api-signature }
sm.gui.translateLocalizationTags( text )
```

Translates all localization tags in a text using the current language.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `text` | string | The text containing localization tags |

**Returns:**

| Type | Description |
| --- | --- |
| string | The text with translated tags |
