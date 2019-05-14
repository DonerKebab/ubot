import unittest

import ubot

class TestUBotMethods(unittest.TestCase):

    def test_change_direction(self):
        current_direction = 'N'
        turn = 'R'
        expect_new_direction = 'E'
        self.assertEqual(ubot.change_direction(turn, current_direction), expect_new_direction)

    def test_move(self):
        self.current_state = {'x': 0, 'y': 0, 'current_direction': 'N'}
        self.command = 'W12'
        self.exptect_new_state = {'x': 0, 'y': 12, 'current_direction': 'N'}

        self.assertEqual(ubot.move(self.command, self.current_state), self.exptect_new_state)

    def test_process_command(self):
        self.command = 'RW15RW1'
        self.exptect_new_state = {'x': 15, 'y': -1, 'current_direction': 'S'}

        self.assertEqual(ubot.process_command(self.command), self.exptect_new_state)


if __name__ == '__main__':
    unittest.main()
