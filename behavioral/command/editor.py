class Editor:
    self.text = []

    def check_selection(self, idx):
        if len(self.text) > idx:
            return True
        else:
            print("Bad Selection!")

    def get_selection(self, idx):
        if self.check_selection(idx):
            return self.text[idx]

    def delete_selection(self, idx):
        if self.check_selection(idx):
            self.text.pop(idx)

    def replace_selection(self, text, idx):
        if self.check_selection(idx):
            self.text[idx] = text

