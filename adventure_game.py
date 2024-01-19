import random

from game_text import INTRO, ROOMS, DESCRIPTIONS, GHOST_FOUND


def reshape2d(one_dim: list) -> list[list]:
    '''Basic reshape 1d `list` into 2d `list`. `one_dim` must have even number of elements. 
    Could be changed to cover more cases (e.g. a 3x3 grid)'''
    length = len(one_dim)
    assert length % 2 == 0
    two_dim = [one_dim[:length//2], one_dim[length//2:]]
    return two_dim


class HauntedHouse:
    def __init__(self, 
                 intro: str,
                 rooms: list[str],
                 room_descriptions: dict[str, str],
                 ghost_found
    ) -> None:
        # variables for the map
        self.house = reshape2d(rooms)
        self.intro = intro
        self.room_descriptions = room_descriptions
        self.ghost_found = ghost_found
        
        # variables for the player
        self.player_x, self.player_y = 0, 0
        self.dx, self.dy = 0, 0
        self.X_MIN, self.X_MAX = 0, len(self.house) - 1
        self.Y_MIN, self.Y_MAX = 0, len(self.house[0]) - 1
        # `valid_action` flag is only set if the user action causes some change of game state
        # currently this is only to catch the ghost or move to a new room
        self.valid_action = False
        
        # variables for the ghost
        self.ghost_x = random.randint(0, self.X_MAX)
        self.ghost_y = random.randint(0, self.Y_MAX)

        # game state variables
        self.playing = True
        self.game_over = False

    def _show_intro(self) -> None:
        '''Print the intro'''
        print(self.intro)

    def _initial_ask_to_play(self) -> None:
        self._ask_to_play('Dare you enter? ')

    def _ask_to_play(self, message: str) -> None:
        '''Ask the player if they want to play with custom message'''
        while True:
            answer = input('\n' + message).lower()
            if answer in ('y', 'yes'):
                self.playing = True
                self.game_over = False
                break
            elif answer in ('n', 'no'):
                self.playing = False
                self.game_over = True
                break
            else:
                print('I don\'t understand that answer')

    def _describe_room(self) -> None:
        '''Print room description'''
        room = self.house[self.player_x][self.player_y]
        description = self.room_descriptions[room]
        print(f'\nYou have entered the {room}! {description}')

    def _present_options(self) -> None:
        '''Print options that are available player. This function could be expanded to
        remove options that the user has attempted'''
        print('\nHere are your options: go left, right, up, down or search room')

    def _player_action(self) -> None:
        '''Take the action that the player chooses'''
        while True:
            action = input('What to do? ').lower()
            match action.split(' '): # match on the words entered by user
                case ['quit']: 
                    self.playing = False
                    self.game_over = True
                    self.valid_action = True
                    break
                case [*_, 'left']: # *_ means player may type 'go left' and still match here
                    self.dx = -1
                    break
                case [*_, 'right']: # could add more logic in future to further parse user input
                    self.dx = 1
                    break
                case [*_, 'up']: 
                    self.dy = 1
                    break
                case [*_, 'down']: 
                    self.dy = -1
                    break
                case ['search', *_, 'room']:
                    # User may type 'search *the* room' or 'search *this* room' and still match.
                    # The user may also type 'search *banana* room' so more logic could be added
                    # in the future to further parse input.
                    self._search_room()
                    break
                case _:
                    print('I don\'t understand that answer')
        self._move_player()

    def _search_room(self) -> None:
        '''Logic to search the room for a ghost. This function may be expanded
        given more time to search for items to defeat the ghost, for example.'''
        if self.player_x == self.ghost_x \
            and self.player_y == self.ghost_y:
            print('\n' + self.ghost_found)
            self.valid_action = True
            self.game_over = True
        else:
            print('No ghost here!')

    def _move_player(self) -> None:
        '''Logic to move player through the rooms. Ensures player does not go
        out of bounds'''
        cant_go_there = '\nHmm... it looks like you cannot go over there'
        if self.player_x + self.dx < self.X_MIN:
            print(cant_go_there)
        elif self.player_x + self.dx > self.X_MAX:
            print(cant_go_there)
        elif self.player_y + self.dy < self.Y_MIN:
            print(cant_go_there)
        elif self.player_y + self.dy > self.Y_MAX:
            print(cant_go_there)
        else:
            if self.dx != 0 or self.dy != 0:
                self.player_x += self.dx
                self.player_y += self.dy
                self.valid_action = True
        self.dx, self.dy = 0, 0

    def _ask_to_play_again(self) -> None:
        self._ask_to_play('Play again? ')

    def play(self) -> None:
        while self.playing:
            self._show_intro()
            self._initial_ask_to_play()
            while not self.game_over: # main game loop
                self._describe_room()
                while not self.valid_action:
                    self._present_options()
                    self._player_action()
                self.valid_action = False # reset valid_action for next turn
            self._ask_to_play_again()
        print('\nGoodbye... and beware!')


def main():
    room_descriptions = {room: desc for (room, desc) in zip(ROOMS, DESCRIPTIONS)}
    haunted_house = HauntedHouse(INTRO, ROOMS, room_descriptions, GHOST_FOUND)
    haunted_house.play()


if __name__ == '__main__':
    main()
