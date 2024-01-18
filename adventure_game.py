def reshape2d(one_dim: list) -> list[list]:
    '''reshape 1d `list` into 2d `list`. `one_dim` must have even number of elements'''
    length = len(one_dim)
    assert length % 2 == 0
    two_dim = [one_dim[:length//2], one_dim[length//2:]]
    return two_dim


class HauntedHouse:
    def __init__(self, 
                 rooms: list[str],
                 room_descriptions: dict[str, str]
    ) -> None:
        self.player_x, self.player_y = 0, 0
        self.house = reshape2d(rooms)
        self.room_descriptions = room_descriptions
        self.playing = False

    def _show_intro(self) -> None:
        '''Print the intro'''
        print('Intro')

    def _ask_to_play(self) -> None:
        '''Ask the player if they want to play'''
        while True:
            answer = input('Do you want to play? ').lower()
            if answer in ('y', 'yes'):
                self.playing = True
                break
            elif answer in ('n', 'no'):
                self.playing = False
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
            if action in ('q', 'quit'):
                self.playing = False
                break
            elif action == 'keep playing':
                print('Ok')
                break
            else:
                print('I don\'t understand that answer')

    def play(self):
        self._show_intro()
        self._ask_to_play()
        while self.playing:
            self._describe_room()
            self._present_options()
            self._player_action()


def main():
    ROOMS = ('Kitchen', 'Living Room','Dining Room', 'Toilet')
    DESCRIPTIONS = ROOMS
    room_descriptions = {room: desc for (room, desc) in zip(ROOMS, DESCRIPTIONS)}

    haunted_house = HauntedHouse(ROOMS, room_descriptions)
    haunted_house.play()


if __name__ == '__main__':
    main()
