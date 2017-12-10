import sublime, sublime_plugin
from subprocess import Popen, PIPE, call, STDOUT
import sys, time

state = {}

def is_server_running(quick=False):

    # this is probably enough to see if everything is running
    if quick:
        if "server" in state:
            return True
        else:
            return False

    if "server" in state:
        if state["server"].poll() == None:
            return True
        else:
            return False
    else:
        return False

def start_server():
    # print("starting server")
    if not is_server_running():
        # clean up any old instances that may be running...
        stop_server()
        state["server"] = Popen(state["server_command"], shell=True)

    # else:
        # print("LuaComplete: server already running")

def stop_server():    
    # try to cleanly bring it down.
    shutdown = Popen(state["client_command"] + " -x", shell=True)
    shutdown.wait(.5)

    # if the command fails, and it's still running. terminate it.
    if shutdown.returncode != 0:
        if is_server_running():
            state["server"].terminate()

def create_completion(completion):
    (name, completion_type) = completion.split(":")
    completion_type = completion_type.strip()
    completion_name = name
    # add the '(' for functions!
    if completion_type.startswith("function"):
        completion_name = name + "("

        # it's a Lua func and params have been found
        # if "|" in completion_type
        # doing this for the speed!
        if len(completion_type) >= 10:
            # split out the function params
            params = completion_type[11:].split()

            # set the completion type to just the start
            completion_type = completion_type[0:9] + "(Lua)"

            # figure this thing out
            completion_name = completion_name + ", ".join([ "${{{num}:{name}}}".format(num=num+1, name=val) for (num, val) in enumerate(params)])
            completion_name = completion_name + ")"
        
        # for c funcs, we can't do completion
        else:
            completion_name = completion_name + "$1)"


    return "{0}\t{1}".format(name, completion_type), completion_name


class LuaComplete(sublime_plugin.EventListener):    
    def on_query_completions(self, view, prefix, locations):
        global state

        position = locations[0]
        scopes = view.scope_name(position).split()
        if ('source.lua' not in scopes):
            return None

        # load the server if it's not running.
        if not is_server_running(quick=True):
            start_server()

        # we can only autocomplete certain things
        current_char = view.substr(position-1)
        if current_char not in [":", ".", "[", "("]:
            return None

        # build the main command
        command = "{client} -i -c {pos}".format(client=state["client_command"], pos=str(position))
        
        # append the filename if it exists
        file_name = view.file_name()
        if file_name is not None:
            command = command + " -f '{0}'".format(file_name)

        window_vars = view.window().extract_variables()
        if "folder" in window_vars:
            command = command + " -r '{0}'".format(window_vars["folder"])

        # get the file contents
        file_contents = view.substr(sublime.Region(0, view.size())).encode('utf8')
        
        # send it to the client
        print(command)
        client = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        # print(file_contents)
        # print(position)

        # send communicate on stdin to the client
        output = client.communicate(file_contents)[0].decode('utf-8')
        # print("returncode", client.returncode)

        if client.returncode == 0:
            view.set_status("a", "")
            output = output.splitlines()
            output_type = output[0]
            # print(output_type)
            # main output is on lines 1 and below
            output = output[1:]
            # print(output)
            if output_type == "table":
                return [ create_completion(x) for x in output ]

        else:
            view.set_status("a", "lua-complete failed to return")

    def __exit__(self, type, value, traceback):
        stop_server()

# start and stop are really only used for debug
# class StartServerCommand(sublime_plugin.ApplicationCommand):
#     def run(self):
#         start_server()

# class StopServerCommand(sublime_plugin.ApplicationCommand):
#     def run(self):
#         stop_server()

class ClearCacheCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        stop_server()
        start_server()

def plugin_loaded():
    global state
    state["settings"] = sublime.load_settings("LuaComplete.sublime-settings")

    # strip out the path/port
    path = state["settings"].get("path")
    port = state["settings"].get("port")

    # setup the command.
    state["server_command"] = "{path} server -p {port}".format(path=path, port=port)
    state["client_command"] = "{path} client -p {port}".format(path=path, port=port)
