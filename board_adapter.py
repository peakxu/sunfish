unicode_from_piece = {
    'K': '\u2654',
    'Q': '\u2655',
    'R': '\u2656',
    'B': '\u2657',
    'N': '\u2658',
    'P': '\u2659',
    'k': '\u265A',
    'q': '\u265B',
    'r': '\u265C',
    'b': '\u265D',
    'n': '\u265E',
    'p': '\u265F',
    '.': '.',
    ' ': ' ',
}

class BoardAdapter(object):
    @classmethod
    def unicode_board(cls, board):
        lines = board.split('\n')
        unicode_lines = [cls.unicode_line(line) for line in lines]
        return '\n\n'.join(unicode_lines)

    @classmethod
    def unicode_line(cls, line):
        expanded_str = ' '.join([unicode_from_piece[p] for p in line])
        return expanded_str.decode('unicode-escape')
