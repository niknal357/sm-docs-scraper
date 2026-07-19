# ToolClass script template

[Back to ToolClass](ToolClass.md)

Copy this starter script and remove anything you do not need.

```lua
Tool = class()

-- Constants
-- Docs: ToolClass.html#equipwhileseated
Tool.equipWhileSeated = false

-- Server callbacks
-- Docs: ToolClass.html#server_oncreate
function Tool.server_onCreate( self )
end

-- Docs: ToolClass.html#server_ondestroy
function Tool.server_onDestroy( self )
end

-- Docs: ToolClass.html#server_onrefresh
function Tool.server_onRefresh( self )
end

-- Docs: ToolClass.html#server_onfixedupdate
function Tool.server_onFixedUpdate( self, timeStep )
end

-- Docs: ToolClass.html#server_onreceiveupdate
function Tool.server_onReceiveUpdate( self )
end

-- Client callbacks
-- Docs: ToolClass.html#client_oncreate
function Tool.client_onCreate( self )
end

-- Docs: ToolClass.html#client_ondestroy
function Tool.client_onDestroy( self )
end

-- Docs: ToolClass.html#client_onrefresh
function Tool.client_onRefresh( self )
end

-- Docs: ToolClass.html#client_onfixedupdate
function Tool.client_onFixedUpdate( self, timeStep )
end

-- Docs: ToolClass.html#client_onupdate
function Tool.client_onUpdate( self, deltaTime )
end

-- Docs: ToolClass.html#client_onclientdataupdate
function Tool.client_onClientDataUpdate( self, data, channel )
end

-- Docs: ToolClass.html#client_onlocalplayerchangedworld
function Tool.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: ToolClass.html#client_onequip
function Tool.client_onEquip( self, animate )
end

-- Docs: ToolClass.html#client_onunequip
function Tool.client_onUnequip( self, animate )
end

-- Docs: ToolClass.html#client_onequippedupdate
function Tool.client_onEquippedUpdate( self, primaryState, secondaryState )
    return false, false
end

-- Docs: ToolClass.html#client_ontoggle
function Tool.client_onToggle( self )
    return false
end

-- Docs: ToolClass.html#client_onreload
function Tool.client_onReload( self )
    return false
end

-- Docs: ToolClass.html#client_canequip
function Tool.client_canEquip( self )
    return true
end
```
