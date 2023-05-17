import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import subprocess

class CppIDE:
    def __init__(self, master):
        self.master = master
        self.master.title("Paper-Code V3 for C++: Editor and Compiler")
        self.master.geometry("800x600")
        
        self.create_widgets()
    
    def create_widgets(self):
        self.text_editor = scrolledtext.ScrolledText(self.master, width=100, height=30)
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        
        self.run_button = tk.Button(self.master, text="Run", command=self.run)
        self.run_button.pack(side=tk.BOTTOM)
    
    def run(self):
        code = self.text_editor.get("1.0", tk.END)
        file_name = "temp.cpp"
        
        # Write the code to a temporary file
        with open(file_name, "w") as f:
            f.write(code)
        
        # Compile the code
        try:
            subprocess.run(f"g++ {file_name} -o output", check=True, shell=True)
        except subprocess.CalledProcessError as e:
            self.text_editor.insert(tk.END, f"\n\nError:\n{e}\n")
            return
        
        # Run the compiled program
        try:
            output = subprocess.run("./output", capture_output=True, shell=True)
        except subprocess.CalledProcessError as e:
            self.text_editor.insert(tk.END, f"\n\nError:\n{e}\n")
            return
        
        # Print the output
        self.text_editor.insert(tk.END, f"\n\nOutput:\n{output.stdout.decode()}")
        
        # Remove the temporary files
        subprocess.run(f"rm {file_name} output", shell=True)

root = tk.Tk()
CppIDE(root)
root.mainloop()
