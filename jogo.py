import tkinter as tk

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_botoes()

    def criar_botoes(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.root, text=' ', width=10, height=3,
                                              font=("Arial", 24), command=lambda i=i, j=j: self.jogar(i, j))
                self.botoes[i][j].grid(row=i, column=j)

    def jogar(self, i, j):
        if self.tabuleiro[i][j] == ' ':
            self.tabuleiro[i][j] = self.jogador_atual
            self.botoes[i][j].config(text=self.jogador_atual)
            if self.verificar_vencedor():
                self.mostrar_vencedor()
            else:
                self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != ' ':
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != ' ':
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True
        return False

    def mostrar_vencedor(self):
        vencedor = self.jogador_atual
        resultado = tk.Label(self.root, text=f"Jogador {vencedor} venceu!", font=("Arial", 16))
        resultado.grid(row=3, column=0, columnspan=3)
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(state="disabled")  # Desabilitar os botões após o vencedor

# Iniciar o jogo
root = tk.Tk()
jogo = JogoDaVelha(root)
root.mainloop()
