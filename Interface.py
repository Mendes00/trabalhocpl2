import subprocess
from tkinter import *
from tkinter import ttk

def calcular_soma():
    num1 = entrada_num1.get()
    num2 = entrada_num2.get()
    
    if not num1.isdigit() or not num2.isdigit():
        resultado_var.set("Erro: Digite números válidos!")
        return
    
    try:
        processo = subprocess.run(
            ["./soma.exe", num1, num2],
            capture_output=True,
            text=True,
            check=True
        )
        
        resultado_var.set(f"Resultado: {processo.stdout.strip()}")
        
    except FileNotFoundError:
        resultado_var.set("Erro: Arquivo soma.exe não encontrado")
    except subprocess.CalledProcessError as e:
        resultado_var.set(f"Erro: {e.stderr.strip()}")

root = Tk()
root.title("Calculadora Elegante")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

style = ttk.Style()
style.configure("TFrame", background="#f5f5f5")
style.configure("TLabel", background="#f5f5f5", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)

mainframe = ttk.Frame(root, padding="20")
mainframe.pack(expand=True, fill=BOTH)

ttk.Label(mainframe, text="Calculadora em C + Python", 
          font=("Helvetica", 16, "bold")).pack(pady=10)

frame_entrada = ttk.Frame(mainframe)
frame_entrada.pack(pady=10)

ttk.Label(frame_entrada, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entrada_num1 = ttk.Entry(frame_entrada, font=("Helvetica", 12), width=15)
entrada_num1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entrada_num2 = ttk.Entry(frame_entrada, font=("Helvetica", 12), width=15)
entrada_num2.grid(row=1, column=1, padx=5, pady=5)

btn_calcular = ttk.Button(
    mainframe, 
    text="Calcular Soma", 
    command=calcular_soma,
    style="TButton"
)
btn_calcular.pack(pady=20)

resultado_var = StringVar()
resultado_var.set("Resultado: ")
ttk.Label(
    mainframe, 
    textvariable=resultado_var,
    font=("Helvetica", 14, "bold"),
    foreground="#2c3e50"
).pack()

root.mainloop()
