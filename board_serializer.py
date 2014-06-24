import shutil
import os

class BoardSerializer(object):
    """
    Writes out a chessboard to the filesystem using links
    """
    def __init__(self, directory):
        self.directory = directory
        self.reset()

    def reset(self):
        if os.path.isdir(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)
        self.curr_dir = self.directory

    def serialize_board(self, board):
        next_dir = os.path.join(self.curr_dir, '.next')
        os.makedirs(next_dir)
        for i, line in enumerate(board.split('\n\n')):
            line_prefix = str(10-i)
            line_content = line_prefix + line
            if i == 1:
                line_content = '   A B C D E F G H'
            elif i == 0:
                line_content = ' '
            elif i > 9:
                line_content = ' ' * (i - 8)
            line_path = os.path.join(self.curr_dir, line_content)
            os.symlink(next_dir, line_path)
        self.curr_dir = next_dir
