# Deprecated: LuaComplete for Sublime Text 3
LuaComplete is no longer being worked on. There are numerous other lua code completion tools out there (with actual language-server support!)

Alternatives to take a look at:

    https://github.com/sumneko/lua-language-server
    https://github.com/EmmyLua/EmmyLua-LanguageServer


# Original README below
LuaComplete is an ST3 plugin that does auto-completing of Lua code. It uses the [lua-complete](https://github.com/FourierTransformer/lua-complete) engine for auto-completion and makes your Lua development a lot easier!
![Image of LuaComplete in Action](http://fouriertransformer.github.io/LuaComplete-Sublime/images/ftcsv-small.png)

## Installation
1. Install [lua-complete](https://github.com/FourierTransformer/lua-complete#setup)

2. Install the plugin. Currently, you can only install it manually:
    ```
    cd /Users/[user]/Library/Application Support/Sublime Text 3/Packages/
    git clone https://github.com/FourierTransformer/LuaComplete-Sublime LuaComplete
    ```

    I'm working on a few more things before getting it in Package Control.

3. That's about it! LuaComplete will start up the server and send code automatically via the client. There are a few settings that can be tweaked, as referenced below.

## Settings
The default settings should work out of the box, but they can be modified via the Preferences menu or from the Command Palette (`Ctrl+Shift+P` and type LuaComplete). Make any changes in the User settings. You will likely need to restart Sublime Text after changing settings. Here are the default settings:
```
{
    // Path to the directory containing lua-complete executables
    // if installed everywhere, just "lua-complete" should be fine
    "path": "lua-complete",

    // Port to use for the lua-complete client and server
    "port": 24548,

    // enable/disable toggle. it is enabled by default 
    // set it to false to turn off LuaComplete
    // and restart Sublime Text for it to take effect
    // "enabled": true,
    // NOTE: it can also be enabled/disabled via the command palette 
    // but will only stick until the next Sublime Text reboot

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

![Image of LuaComplete completing lua function parameters](http://fouriertransformer.github.io/LuaComplete-Sublime/images/dkjson.gif)

### C Function
The C functions parameters don't get auto-completed and the function is described as `function`:
![Image of LuaComplete completing lua function parameters](http://fouriertransformer.github.io/LuaComplete-Sublime/images/cjson.gif)

## Troubleshooting
If you see the error message "The lua-complete client failed to return" in the bottom right, try running the "LuaComplete: Clear Auto-complete Cache (Restart Server)" from the command palette. This will restart the server, and hopefully the client will be able to reconnect.

## Questions and Contributing
Feel free to open a Github issue with any questions/issues/features that you have! Also, check out [CONTRIBUTING.md](CONTRIBUTING.md) if you want to help!

## Licenses
LuaComplete is released under the [MIT License](LICENSE.md)
