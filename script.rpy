# script.rpy

define a = Character("Alex")
define p = Character("You")
define n = Character(None)

label start:
    scene black
    with dissolve

    n "Ren'Py sample — 'Reunion Moment' (branching, state, conditions)."
    n "Press F2 anytime to toggle the debug overlay."

    menu:
        "Start the Moment":
            jump moment_reunion
        "Quit":
            return