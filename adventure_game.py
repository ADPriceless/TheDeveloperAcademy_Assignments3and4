class HauntedHouse:
    def __init__(self) -> None:
        self.player_x, self.player_y = 0, 0
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
    haunted_house = HauntedHouse()
    haunted_house.play()


if __name__ == '__main__':
    main()
