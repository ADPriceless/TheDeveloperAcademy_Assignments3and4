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
        self.rooms_descriptions = room_descriptions
        self.playing = False

    def _show_intro(self) -> None:
        '''Print the intro'''

    def _ask_to_play(self) -> None:
        '''Ask the player if they want to play'''

    def _describe_room(self) -> None:
        '''Print room description'''

    def _present_options(self) -> None:
        '''Print options that are available player'''

    def _player_action(self) -> None:
        '''Take the action that the player chooses'''

    def play(self):
        self._show_intro()
        self._ask_to_play()
        if self.playing:
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
