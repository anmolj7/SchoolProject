import tkinter as tk
import tkinter.messagebox as tkMessageBox
from functools import partial
# For passing argument with onclick event in tkiner.


def check_list(List):
    # Checks if a list's all the elements are same
    return len(set(List)) == 1


class App:
    def __init__(self, N=3):
        self.Buttons = []
        self.N = N
        self.app = tk.Tk()
        self.app.title('TicTacToe-EmperorAj')
        self.app.geometry("600x300")

        tk.Label(self.app, text="Tic-tac-toe Game", font=('Helvetica', '15')).grid(row=0, column=0)
        tk.Label(self.app, text="Player 1: X", font=('Helvetica', '10')).grid(row=1)
        tk.Label(self.app, text="Player 2: O", font=('Helvetica', '10')).grid(row=2)

        self.turn = 1
        self.flag = 0

        self.create_widgets()
        self.app.mainloop()

    def on_click(self, button_idx):
        if self.Buttons[button_idx]['text'] == " ":
            self.Buttons[button_idx]['text'] = self.return_item()
            self.check_for_win()

    def create_widgets(self):
        for i in range(self.N**2):
            temp_btn = tk.Button(self.app, text=" ", bg="green", fg="Black", width=6, height=2, font=("Helvetica", "20"), command=partial(self.on_click, i))
            self.Buttons.append(temp_btn)
            self.Buttons[i].grid(row=1+i//self.N, column=1+i % self.N)

    def return_item(self):
        if self.turn % 2:
            ans = "X"
        else:
            ans = "O"
        self.turn += 1
        return ans

    def win_indices(self):
        for row in range(self.N):
            yield [row * self.N + col for col in range(self.N)]
        for col in range(self.N):
            yield [row * self.N + col for row in range(self.N)]
        yield [i * self.N + i for i in range(self.N)]
        yield [i * self.N + self.N - 1 - i for i in range(self.N)]

    def is_winner(self, decorator):
        for indices in self.win_indices():
            if check_list([self.Buttons[idx]['text'] for idx in indices]) and self.Buttons[indices[0]]['text'] == decorator:
                return True
        return False

    def check_for_win(self):
        self.flag += 1
        if self.is_winner("X"):
            self.win("X")
        elif self.is_winner("O"):
            self.win("O")
        elif self.flag == self.N**2:
            tkMessageBox.showinfo("Game Complete", "This is a tie.")
            self.ExitApplication()

    def win(self, player):
        ans = f"Game complete, player {player} won."
        tkMessageBox.showinfo("Game Complete", ans)
        self.ExitApplication()

    def ExitApplication(self):
        MsgBox = tk.messagebox.askquestion('New Game', 'Do you want to start a new game? ',
                                           icon='warning')
        if MsgBox == 'yes':
            self.app.destroy()
            main()
        else:
            self.app.destroy()


def main():
    App()


if __name__ == '__main__':
    main()
