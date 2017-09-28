#!/usr/bin/env python
import gdb

class BreakpointIfOtherInStack(gdb.Breakpoint):
    def __init__(self, spec, name):
        super(BreakpointIfOtherInStack, self).__init__(spec)
        self.name = name

    def stop(self):
        frame = gdb.selected_frame().older()
        return frame.name() == self.name

class bs(gdb.Command):
    """Set break on BREAKPOINT1 if BREAKPOINT2 in stack
Usage: bs BREAKPOINT1 BREAKPOINT2"""
    
    def __init__(self):
        super (bs, self).__init__("bs", gdb.COMMAND_USER)
    
    def invoke(self, arg, from_tty):
        self.dont_repeat()
        break1=""
        break2=""
        try:
            break1, break2 = gdb.string_to_argv(arg)
        except ValueError as e:
            print("bs error: ", e)
            print(bs.__doc__)
        breakpoint = BreakpointIfOtherInStack(break1, break2)
bs()
