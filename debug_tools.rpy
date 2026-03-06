# ...existing code...
# debug_tools.rpy

default dbg_overlay_open = False
# Variable que muestra el label actual en el overlay
default current_label = ""

init python:
    if "keybinds" not in config.overlay_screens:
        config.overlay_screens.append("keybinds")

    # Helper para que labels puedan actualizar el valor mostrado
    def set_current_label(name):
        # Actualiza el label mostrado en el overlay
        store.current_label = name
        # Asegura que la opción "Main Menu" quede deshabilitada al cambiar de label
        # (evita que un valor True persistente lleve al menú principal inesperadamente)
        store.allow_main_menu = False
# ...existing code...

screen keybinds():
    key "K_F2" action ToggleScreen("debug_overlay")

screen debug_overlay():
    zorder 200
    modal False

    frame:
        xalign 0.02
        yalign 0.02
        padding (16, 12)

        vbox:
            spacing 6

            text "DEBUG OVERLAY (F2)" size 18

            # Muestra el label actual
            text "Current label: [current_label]" size 14

            text "tone: [tone]   trust: [trust]"
            text "mem_pos: [mem_pos]   mem_pain: [mem_pain]"
            text "bold: [bold]   apology_made: [apology_made]"
            text "hurt_topic: [hurt_topic]"

            null height 6
            text "Quick Set" size 14

            hbox:
                spacing 8
                textbutton "tone -3" action [SetVariable("tone", -3)]
                textbutton "tone 0" action [SetVariable("tone", 0)]
                textbutton "tone +3" action [SetVariable("tone", 3)]

            hbox:
                spacing 8
                textbutton "trust -2" action [SetVariable("trust", -2)]
                textbutton "trust 0" action [SetVariable("trust", 0)]
                textbutton "trust +2" action [SetVariable("trust", 2)]

            hbox:
                spacing 8
                textbutton "toggle bold" action ToggleVariable("bold")
                textbutton "toggle apology" action ToggleVariable("apology_made")

            hbox:
                spacing 8
                # existing increment buttons
                textbutton "mem_pos +1" action SetVariable("mem_pos", mem_pos + 1)
                textbutton "mem_pain +1" action SetVariable("mem_pain", mem_pain + 1)

            # NEW: decrement buttons for mem_pos and mem_pain
            hbox:
                spacing 8
                textbutton "mem_pos -1" action SetVariable("mem_pos", max(0, mem_pos - 1))
                textbutton "mem_pain -1" action SetVariable("mem_pain", max(0, mem_pain - 1))

            null height 6
            text "Jump" size 14
            textbutton "Jump to Moment (start)" action Jump("moment_reunion")

            null height 8
            # NEW: reset hurt_topic
            hbox:
                spacing 8
                textbutton "reset hurt_topic" action SetVariable("hurt_topic", "")

            textbutton "Close" action Hide("debug_overlay")
# ...existing code...