# LuaComplete for Sublime Text 3 (BETA)
LuaComplete is an ST3 plugin that does auto-completing of Lua code. It uses the [lua-complete](https://github.com/FourierTransformer/lua-complete) engine for auto-completion and makes your Lua development a lot easier!

## Installation
1. Install [lua-complete](https://github.com/FourierTransformer/lua-complete#setup)

2. Install the plugin. I'm working on a few more things before getting it in Package Control. Currently, you can only install if manually:
    ```
    cd /Users/[user]/Library/Application Support/Sublime Text 3/Packages/
    git clone https://github.com/FourierTransformer/LuaComplete-Sublime LuaComplete
    ```

3. That's about it! LuaComplete will start up the server and send code automatically via the client. There are a few settings that can be tweaked, as referenced below.

## Settings
The default settings should work out of the box, but they can be modified via the Preferences menu or from the Command Palette (`Ctrl+Shift+P` and type LuaComplete). Make any changes in the User settings. Here are the default settings:
```
{
    // Path to the directory containing lua-complete executables
    // if installed everywhere, just "lua-complete" should be fine
    "path": "lua-complete",

    // Port to use for the lua-complete client and server
    "port": 24548,

    // additional include location
    // by default lua-complete will search lua's regular 
    // installed module paths (packages.path)
    // 
    // The LuaComplete plugin will send the currently
    // open folder in the sublime text view for analysis
    // 
    // Additional include locations can be specified in a
    // semi-colon delimited list below (be sure to comment out the line below)
    // "additional_includes": "/my/random/file/path;/another/path"
}
```

## Features and Shortcomings
 * It will only auto-complete things in tables - which includes most lua modules!
 * It can only determine function parameters for Lua functions (it currently doesn't know if a parameter is optional or not).
 * It should work with project-level files (by searching through the folder open in sublime text or folder the file resides in)
 * In the future, it should include function parameters for the built-in lua functions. However, it is not possible to determine function parameters for other C functions - without hard-coding them in.

## Comparison between Lua and C functions
The LuaComplete plugin will show the difference between when it can fill in function parameters (for Lua functions) and when it can't (for C functions). Take a look at the example below:

### Lua Function
The Lua function parameters get auto-completed and in the Sublime Text auto-complete hover - the function is described as `function ()`:

### C Function
The C functions parameters don't get auto-completed and the function is described as `function`:

