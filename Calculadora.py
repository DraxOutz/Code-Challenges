import tkinter as tk

def adicionar_numero(num):
    entrada.insert(tk.END, num)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        limpar()
        entrada.insert(0, str(resultado))
    except Exception:
        limpar()
        entrada.insert(0, "Erro")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entrada (display)
entrada = tk.Entry(janela, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=4, height=2, command=calcular)
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, width=4, height=2, command=limpar)
    else:
        botao = tk.Button(janela, text=texto, width=4, height=2, command=lambda t=texto: adicionar_numero(t))
    botao.grid(row=linha, column=coluna)

janela.mainloop()
