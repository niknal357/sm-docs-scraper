# GameClass script template

[Back to GameClass](GameClass.md)

Copy this starter script and remove anything you do not need.

```lua
Game = class()

-- Constants
-- Docs: GameClass.html#defaultinventorysize
Game.defaultInventorySize = 40
-- Docs: GameClass.html#enableaggro
Game.enableAggro = true
-- Docs: GameClass.html#enableammoconsumption
Game.enableAmmoConsumption = false
-- Docs: GameClass.html#enablefuelconsumption
Game.enableFuelConsumption = false
-- Docs: GameClass.html#enablelimitedinventory
Game.enableLimitedInventory = false
-- Docs: GameClass.html#enablerecipes
Game.enableRecipes = true
-- Docs: GameClass.html#enablerestrictions
Game.enableRestrictions = false
-- Docs: GameClass.html#enableupgrade
Game.enableUpgrade = false

-- Server callbacks
-- Docs: GameClass.html#server_oncreate
function Game.server_onCreate( self )
end

-- Docs: GameClass.html#server_ondestroy
function Game.server_onDestroy( self )
end

-- Docs: GameClass.html#server_onrefresh
function Game.server_onRefresh( self )
end

-- Docs: GameClass.html#server_onfixedupdate
function Game.server_onFixedUpdate( self, timeStep )
end

-- Docs: GameClass.html#server_onreceiveupdate
function Game.server_onReceiveUpdate( self )
end

-- Docs: GameClass.html#server_onplayerjoined
function Game.server_onPlayerJoined( self, player, newPlayer )
end

-- Docs: GameClass.html#server_onplayerleft
function Game.server_onPlayerLeft( self, player )
end

-- Docs: GameClass.html#server_onreset
function Game.server_onReset( self )
end

-- Docs: GameClass.html#server_onrestart
function Game.server_onRestart( self )
end

-- Docs: GameClass.html#server_onsavelevel
function Game.server_onSaveLevel( self )
end

-- Docs: GameClass.html#server_ontestlevel
function Game.server_onTestLevel( self )
end

-- Docs: GameClass.html#server_onstoptest
function Game.server_onStopTest( self )
end

-- Docs: GameClass.html#server_onunload
function Game.server_onUnload( self )
end

-- Client callbacks
-- Docs: GameClass.html#client_oncreate
function Game.client_onCreate( self )
end

-- Docs: GameClass.html#client_ondestroy
function Game.client_onDestroy( self )
end

-- Docs: GameClass.html#client_onrefresh
function Game.client_onRefresh( self )
end

-- Docs: GameClass.html#client_onfixedupdate
function Game.client_onFixedUpdate( self, timeStep )
end

-- Docs: GameClass.html#client_onupdate
function Game.client_onUpdate( self, deltaTime )
end

-- Docs: GameClass.html#client_onclientdataupdate
function Game.client_onClientDataUpdate( self, data, channel )
end

-- Docs: GameClass.html#client_onlocalplayerchangedworld
function Game.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: GameClass.html#client_onloadingscreenlifted
function Game.client_onLoadingScreenLifted( self )
end

-- Docs: GameClass.html#client_onlanguagechange
function Game.client_onLanguageChange( self, language )
end

-- Docs: GameClass.html#client_onunstuck
function Game.client_onUnstuck( self )
end
```
