from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, app, editor):
        self._app = app
        self._editor = editor
        self._backup = ''


    def save_backup(self):
        self._backup = self._editor.text

    def undo(self):
        self._editor.text = self._backup

    @abstractmethod
    def execute(self):
        pass


class CopyCommand(Command):
    def __init__(self, app, editor):
        super(CopyCommand, self).__init__(app, editor)

    def execute(self):
        self._app.clipboard = self._editor.get_selection()
        return False


class CutCommand(Command):
    def __init__(self, app, editor):
        super(CutCommand, self).__init__(app, editor)

    def execute(self):
        self.save_backup()
        self._app.clipboard = self._editor.get_selection()
        self._editor.delete_selection()
        return True


class PasteCommand(Command):
    def __init__(self, app, editor):
        super(PasteCommand, self).__init__(app, editor)

    def execute(self):
        self.save_backup()
        self._editor.replace_selection(self._app.clipboard)
        return True


class UndoCommand(Command):
    def __init__(self, app, editor):
        super(UndoCommand, self).__init__(app, editor)

    def execute(self):
        self._app.undo()
        return False


class CommandHistory:
    def __init__(self):
        self.__command_hist = []

    def push(self, c):
        self.__command_hist.append(c)

    def pop(self):
        if len(self.__command_hist) > 0:
            return self.__command_hist.pop(-1)



