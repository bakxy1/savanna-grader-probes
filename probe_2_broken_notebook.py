# PROBE 2, deliberately broken notebook (syntax error below).
# Purpose: show what a CONTENT failure looks like, as opposed to a staging failure.
# Expected on a healthy run:
#   File submitted: pass (the file arrived fine)
#   test_gate_notebook_loads...: fail (notebook does not load)
#   everything else: fail
# If instead "File submitted" itself fails, that run hit the staging bug,
# independent of this file's broken content.
import marimo

app = marimo.App(

def this_is_not_valid_python(:
    return
