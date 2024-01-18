# Agenda   
## 1. Game spec (high-level)
- How does the game present itself to the user?
    - There is an intro
    - User types in name
    - Set of instructions of how to play
- How does the player interact with the game?
    - ?
- What features does the game have?
    - Player
        - movement: forward, left, right, backwards
    - Rooms
        - different rooms of a haunted house
        - game gives the description of the room when you enter
    - World/ map (the place in which the rooms exist)?
        - a grid of rooms
            - Initially all rooms are connected
                - Add logic later to determine which rooms connect to which
            - Room prompts player to choose a direction (if they choose one that they can't go, then the game tells them)
    - Is there an objective?
        - If so, what?
            - Find the ghost
    - Are there obstacles?
        - If so, what?
    - Is there a story?
        - If so, what?
            - In a haunted house
    - Modules
        - numpy?
            - No, just use vanilla Python

## 2. Code structure (high-level)
- How does the game implement the features discussed above?
    - Player
        - keeps track of its own position (stores co-ordinates in `variables` e.g. player_x and player_y)
    - Rooms
        - Name of the room stored as a `String` in a 2D `list` (like a grid)
        - `dictionary` to store the description of each room using the name of the room as the key
            - the name of the room is retrieved from the `list` using the co-ordinates of the player
        - A function to show options to player (up, down, left, right)
    - World
        - A function to stop the player from going out of bounds (out of the `list` index)

## 3. Division of labour
- Who is doing what?
    - Abdi: ?
    - Adam: ?
    - Alex: ?
    - Doug: ?
    - Louisa: ?
- How to organise contributions to the git repo?
    -   e.g if someone is dependent on  another's work to do theirs
    - git branch
