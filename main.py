"""
    Inicio do a minha atualização da calculadora em python.
    Vou transformar essa simples conta de soma em uma calculadora melhorada com uma interface usando Tkinter.
 
 TODO: Limitar o número de digitos no display;
"""
# Importando as bibliotecas necessárias
from sys import maxsize
from tkinter import * # Usando * significa que todas as bibliotecas estão sendo importadas
from tkinter import ttk


""" Aqui é a interface gráfica da calculadora """
# Definindo algumas cores para o programa
cor1 = '#3b3b3b' # Black - Cor do fundo da tela
cor2 = '#feffff' # White - Cor do texto
cor3 = '#38576b' # Dark Blue - Display
cor4 = '#eceff1' # Light Grey - Botões numéricos
cor5 = '#ffab40' # Orange - Botões de operação


# Configurações gerais da janela
janela = Tk() # Criando a janela principal
janela.title("Calculadora") # Titulo da janela principal que ficara no topo da tela
janela.geometry("235x310") # Tamanho da janela principal, width x height
janela.resizable(False, False) # Bloquear o tamanho da tela
janela.config(bg=cor1) # Configurando a cor de fundo da janela esse comando é necessário para mudar a cor de fundo da janela e o config é para mudar a cor de fundo do texto

# Criando os frames de display
frame_display = Frame(janela, width=235, height=50, bg=cor3) # Criando o frame de display da calculadora, após isso defino o tamanho da largura e altura
frame_display.grid(row=0, column=0) # Posicionando o frame de display na primeira linha e primeira coluna



""" Aqui inicia a parte lógica da calculadora """

# Variável todos_valores é global para que o valor seja acessível em todas as funções
todos_valores = ''
valor_text = StringVar() # Criando uma variável para o texto

# Criando a função que será executada quando o botão for clicado
def entrada_valores(event):
    global todos_valores # Variável global para que o valor seja acessível em todas as funções
    todos_valores = todos_valores + str(event) # Aqui é o que acontece quando o botão for clicado
    
    # Passando o resultado para o label de display
    valor_text.set(todos_valores) # Função para deletar um caracter do display


# Função de cálculo
def calcular():
    global todos_valores # Variável global para que o valor seja acessível em todas as funções
    resultado = eval(todos_valores) # Aqui é o cálculo
    valor_text.set(str(resultado)) # Passando o resultado para o label de display


# Função para limpar o display
def clear():
    global todos_valores # Variável global para que o valor seja acessível em todas as funções
    todos_valores = '' #
    valor_text.set('') # Limpando o display

""" Aqui termina a parte lógica da calculadora """

# Criando o Label de display
app_label = Label(frame_display, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor=E, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2) # Criando o label de display, após isso defino o tamanho da largura e altura, o padding, o relief, o anchor, o justify, o font, a cor de fundo e a cor do texto
app_label.place(x=0, y=0) # Posicionando o label de display

# Criando os frames do corpo da calculadora
frame_body = Frame(janela, width=235, height=268) # Criando o frame de botões da calculadora, após isso defino o tamanho da largura e altura
frame_body.grid(row=1, column=0) # Posicionando o frame de botões na segunda linha e primeira coluna


# Criando os frames de botões
# Primeira linha dos botões
# Foi definido a qual frame o botão será posicionado, o texto do botão, largura e altura, cor de fundo, font do texto, cor do texto, e o comando que será executado quando o botão for clicado
b_1 = Button(frame_body, command= clear, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=0) # Posicionamento do botão em relação ao frame x e y
b_2 = Button(frame_body, command= lambda: entrada_valores('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=119, y=0) 
b_3 = Button(frame_body, command= lambda: entrada_valores('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=178, y=0) 

# Segunda linha dos botões
b_4 = Button(frame_body, command= lambda: entrada_valores('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command= lambda: entrada_valores('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command= lambda: entrada_valores('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=119, y=52)
b_7 = Button(frame_body, command= lambda: entrada_valores('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=178, y=52)

# Terceira linha dos botões
b_8 = Button(frame_body, command= lambda: entrada_valores('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command= lambda: entrada_valores('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command= lambda: entrada_valores('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=119, y=104)
b_11 = Button(frame_body, command= lambda: entrada_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=178, y=104)

# Quarta linha dos botões
b_12 = Button(frame_body, command= lambda: entrada_valores('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command= lambda: entrada_valores('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command= lambda: entrada_valores('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=119, y=156)
b_15 = Button(frame_body, command= lambda: entrada_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=178, y=156)

# Quinta linha dos botões
b_16 = Button(frame_body, command= lambda: entrada_valores('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command= lambda: entrada_valores('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=119, y=208)
b_18 = Button(frame_body, command= calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=178, y=208)

""" Aqui termina a interface gráfica da calculadora """

janela.mainloop() # Fica em loop até que o usuário feche a janela
