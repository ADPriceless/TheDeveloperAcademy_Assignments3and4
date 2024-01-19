"""This file contains the rooms that are found in a haunted house and their descriptions.
The room name and its description must have the same index in their respective lists.
"""


INTRO = "\nYou find yourself standing at the creaking gates of Ravenhurst Manor, a dilapidated haunted house with a history steeped in mystery and ghostly lore. Armed with only a flickering lantern and your unwavering courage, you are at the start of a quest to uncover the secrets within its shadowy corridors and, most importantly, to find the elusive ghost that lurks within its walls."

ROOMS = ('Kitchen', 'Parlour','Dining Room', 'Basement') #, 'Library', 'Attic')

DESCRIPTIONS = ( # Thanks, OpenAI ;)
    "An oppressive stillness hangs in the air, broken only by the flickering of ethereal flames beneath long-extinguished burners, casting an eerie glow on forgotten cookware coated in a layer of ghostly dust.",
    "Time seems frozen, and faded Victorian-era furniture draped in dusty, moth-eaten fabrics sits in ghostly silence.",
    "A spectral banquet table is set with decaying elegance, adorned with tarnished silverware and ethereal candlesticks that flicker with ghostly flames.",
    "Ghostly shadows dance among cobweb-shrouded relics of a bygone era, casting an unsettling pall over the air thick with the residue of supernatural energy.",
    # "Moonlight filters through dusty, tattered curtains, revealing shelves lined with ancient, spectral tomes that seem to whisper forbidden knowledge to those who dare to enter.",
    # "The creaking floorboards seem to echo with the footsteps of ethereal inhabitants, trapped in a timeless dance between the realms of the living and the departed.",
)

GHOST_FOUND = "You found the ghost: a Victorian girl, holding her own severed head! She jumps at you but you fire your proton pack and catch her in the ghost trap!\nPhew... that was close."
GHOST_NOT_FOUND = "There is nothing here but silence..."
