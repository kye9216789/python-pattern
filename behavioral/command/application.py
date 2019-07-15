from .editor import Editor
from .command import (Command, CopyCommand, CutCommand,
                      PasteCommand, UndoCommand)
class Application:
    self.clipboard = ''
    self.editors = []
    self.activate_editor = Editor()

    self.history = []

    self.buttons = []
    self.keys = []

    def create_ui(self):
        self.buttons.append(copy)
        self.buttons.append(cut)
        self.buttons.append(paste)
        self.buttons.append(undo)

        self.keys.append(copy)
        self.keys.append(cut)
        self.keys.append(paste)
        self.keys.append(undo)

    def copy(self):
        copycommand = CopyCommand(self, self.activate_editor)
        self.execute_command(copycommand)

    def cut(self):
        cutcommand = CutCommand(self, self.activate_editor)
        self.execute_command(cutcommand)

    def paste(self):
        pastecommand = PasteCommand(self, self.activate_editor)
        self.execute_command(pastecommand)

    def undo(self):
        undocommand = UndoCommand(self, self.activate_editor)
        self.execute_command(undocommand)

    def execute_command(self, command):
        if command_function.execute():
            self.history.appned(command)

    def undo(self):
        command = self.history.pop()
        if command is not None:
            command.undo()


