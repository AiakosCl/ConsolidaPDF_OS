import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os
import platform
import subprocess

def seleccionar_pdfs():
    root = tk.Tk()
    root.withdraw()
    archivos_pdf = filedialog.askopenfilenames(
        title="Selecciona los archivos PDF en el orden deseado",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    return list(archivos_pdf)

def abrir_carpeta(carpeta_destino):
    sistema = platform.system()
    try:
        if sistema == "Darwin":  # macOS
            subprocess.run(["open", carpeta_destino])
        elif sistema == "Windows":
            # Solo se ejecuta en Windows
            import os
            os.startfile(carpeta_destino)
        elif sistema == "Linux":
            subprocess.run(["xdg-open", carpeta_destino])
        else:
            messagebox.showinfo("Atención", f"No se pudo abrir la carpeta automáticamente en {sistema}.")
    except Exception as e:
        messagebox.showerror("Error al abrir carpeta", f"Ocurrió un error:\n\n{e}")

def consolidar_pdfs(archivos, nombre_salida):
    try:
        merger = PdfMerger()
        for archivo in archivos:
            merger.append(archivo)
        merger.write(nombre_salida)
        merger.close()

        messagebox.showinfo(
            "Fusión completada",
            f"El archivo consolidado fue guardado exitosamente en:\n\n{nombre_salida}"
        )

        carpeta_destino = os.path.dirname(nombre_salida)
        abrir_carpeta(carpeta_destino)

    except Exception as e:
        messagebox.showerror("Error durante la fusión", f"Ocurrió un error:\n\n{e}")

if __name__ == "__main__":
    archivos = seleccionar_pdfs()
    if archivos:
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Archivo PDF", "*.pdf")],
            title="Guardar PDF consolidado como"
        )
        if output_path:
            consolidar_pdfs(archivos, output_path)
    else:
        messagebox.showinfo("Sin selección", "No se seleccionaron archivos PDF.")

# Este script permite al usuario seleccionar múltiples archivos PDF,
# los fusiona en un solo archivo PDF y guarda el resultado en una ubicación especificada.
# Además, abre la carpeta contenedora del archivo generado en macOS.
# Asegúrate de tener instaladas las bibliotecas necesarias:
# pip install PyPDF2
# Este script está diseñado para funcionar en macOS, pero puede adaptarse para otros sistemas operativos.
# Nota: En sistemas Windows, puedes cambiar "open" por "explorer" en la línea de subprocess.run.
# En Linux, podrías usar "xdg-open" o "nautilus" dependiendo de tu entorno de escritorio.
# Asegúrate de que el entorno tenga acceso a la terminal para ejecutar el comando de apertura de carpeta.
# Este script es una herramienta útil para consolidar documentos PDF de manera sencilla y rápida.
# Asegúrate de que el entorno tenga acceso a la terminal para ejecutar el comando de apertura de carpeta.
# Este script es una herramienta útil para consolidar documentos PDF de manera sencilla y rápida.
# Puedes personalizar el título de la ventana y los mensajes según tus necesidades.
# Asegúrate de que el entorno tenga acceso a la terminal para ejecutar el comando de apertura de carpeta.
# Este script es una herramienta útil para consolidar documentos PDF de manera sencilla y rápida.
# Puedes personalizar el título de la ventana y los mensajes según tus necesidades.