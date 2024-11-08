import tkinter as tk
from tkinter import messagebox

# Variável de controle pro encerramento
saida = ''

# Funções de operação 
def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    if operacao in ('+', 'adicao'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Função pra processar e exibir o resultado
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = entry_operacao.get().strip().lower()
        resultado = calculadora(num1, num2, operacao)
        label_resultado.config(text=f"Resultado da operação: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Função pra sair
def sair():
    global saida
    saida = 'n'
    root.destroy()

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Calculadora")

tk.Label(root, text="Primeiro número:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Segundo número:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

tk.Label(root, text="Operação (+, -, *, / ou nome):").pack()
entry_operacao = tk.Entry(root)
entry_operacao.pack()

button_calcular = tk.Button(root, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(root, text="Resultado da operação:")
label_resultado.pack()

button_sair = tk.Button(root, text="Sair", command=sair)
button_sair.pack()

root.mainloop()
