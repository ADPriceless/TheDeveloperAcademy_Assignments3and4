import random


def reshape2d(one_dim: list) -> list[list]:
    '''Basic reshape 1d `list` into 2d `list`. `one_dim` must have even number of elements. 
    Could be changed to cover more cases (e.g. a 3x3 grid)'''
    length = len(one_dim)
    assert length % 2 == 0
    two_dim = [one_dim[:length//2], one_dim[length//2:]]
    return two_dim


class HauntedHouse:
    def __init__(self, 
                 rooms: list[str],
                 room_descriptions: dict[str, str]
    ) -> None:
        self.house = reshape2d(rooms)
        self.room_descriptions = room_descriptions
        
        self.player_x, self.player_y = 0, 0
        self.dx, self.dy = 0, 0
        self.X_MIN, self.X_MAX = 0, len(self.house) - 1
        self.Y_MIN, self.Y_MAX = 0, len(self.house[0]) - 1
        self.valid_action = False
        
        self.ghost_x = random.randint(0, self.X_MAX)
        self.ghost_y = random.randint(0, self.Y_MAX)

        self.playing = True
        self.game_over = False


    def _show_intro(self) -> None:
        '''Print the intro'''
        print('Intro')

    def _initial_ask_to_play(self) -> None:
        self._ask_to_play('Dare you enter? ')

    def _ask_to_play(self, message: str) -> None:
        '''Ask the player if they want to play'''
        while True:
            answer = input(message).lower()
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
        print(f'You have entered the {room}! {description}')

    def _present_options(self) -> None:
        '''Print options that are available player'''
        print('Here are your options: keep playing, quit')

    def _player_action(self) -> None:
        '''Take the action that the player chooses'''
        while True:
            action = input('What to do? ').lower()
            match action.split(' '):
                case ['quit']: 
                    self.playing = False
                    self.game_over = True
                    self.valid_action = True
                    break
                case [*_, 'left']: 
                    self.dx = -1
                    break
                case [*_, 'right']: 
                    self.dx = 1
                    break
                case [*_, 'up']: 
                    self.dy = 1
                    break
                case [*_, 'down']: 
                    self.dy = -1
                    break
                case ['search', *_, 'room']:
                    self._search_room()
                    break
                case _: 
                    print('I don\'t understand that answer')
        self._move_player()

    def _search_room(self) -> None:
        '''Logic to search the room for a ghost'''
        if self.player_x == self.ghost_x \
            and self.player_y == self.ghost_y:
            print('You found the ghost!')
            self.valid_action = True
            self.game_over = True
        else:
            print('No ghost here!')

    def _move_player(self) -> None:
        if self.player_x + self.dx < self.X_MIN:
            print('Hmm... it looks like you cannot go over there')
        elif self.player_x + self.dx > self.X_MAX:
            print('Hmm... it looks like you cannot go over there')
        elif self.player_y + self.dy < self.Y_MIN:
            print('Hmm... it looks like you cannot go over there')
        elif self.player_y + self.dy > self.Y_MAX:
            print('Hmm... it looks like you cannot go over there')
        else:
            if self.dx != 0 or self.dy != 0:
                self.player_x += self.dx
                self.player_y += self.dy
                self.valid_action = True
        self.dx, self.dy = 0, 0

    def _play_again(self) -> None:
        self._ask_to_play('Play again? ')

    def play(self) -> None:
        while self.playing:
            self._show_intro()
            self._initial_ask_to_play()
            while not self.game_over:
                self._describe_room()
                while not self.valid_action:
                    self._present_options()
                    self._player_action()
                self.valid_action = False # reset valid_action for next turn
            self._play_again()
        print('Goodbye!')


def main():
    ROOMS = ('Kitchen', 'Living Room','Dining Room', 'Toilet')
    DESCRIPTIONS = ROOMS
    room_descriptions = {room: desc for (room, desc) in zip(ROOMS, DESCRIPTIONS)}

    haunted_house = HauntedHouse(ROOMS, room_descriptions)
    haunted_house.play()


if __name__ == '__main__':
    main()
