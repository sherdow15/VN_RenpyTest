
# bg
image bg cafe = "images/bg_cafe.jpg"
image bg cafe_night = "images/bg_cafe_night.jpg"
image bg park = "images/bg_park.jpg"
image bg park2 = "images/bg_park_2.jpg"
image bg parkN = "bg_park_night.jpg"


# Alex 
image alex neutral    = "images/alex/neutral.png"
image alex smile      = "images/alex/smile.png"
image alex angry      = "images/alex/angry.png"
image alex surprised  = "images/alex/surprised.png"

# Transforms 
transform pos_left:
    xalign 0.20
    yalign 1.0

transform pos_right:
    xalign 0.80
    yalign 1.0

transform pos_center:
    xalign 0.50
    yalign 0.

# Transforms in
transform enter_from_left:
    xalign -0.5
    linear 0.45 xalign 0.20

transform enter_from_right:
    xalign 1.5
    linear 0.45 xalign 0.80

# Transitions
define short_dissolve = Dissolve(0.25)
define medium_fade = Fade(0.5, 0.2, 0.5)

