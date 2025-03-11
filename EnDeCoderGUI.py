import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from EnDeCoder import EnDeCoder
import tkinter.scrolledtext as scrolledtext

class EnDeCoderApp:
    def __init__(self, root):
        self.setup_window(root)
        self.setup_styles()
        self.endecoder = EnDeCoder()
        self.create_layout()
        self.bind_shortcuts()

    def setup_window(self, root):
        self.root = root
        self.root.title("EnDeCoder Pro")
        self.root.geometry("800x600")

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.configure(bg='#2e3f4f')

        # Define consistent styles
        styles = {
            'TButton': {'padding': 5, 'font': ('Helvetica', 10), 'background': '#4a90e2', 'foreground': '#ffffff'},
            'Small.TButton': {'padding': 5, 'font': ('Helvetica', 8), 'background': '#4a90e2', 'foreground': '#ffffff'},
            'TLabel': {'font': ('Helvetica', 11), 'background': '#2e3f4f', 'foreground': '#ffffff'},
            'Header.TLabel': {'font': ('Helvetica', 14, 'bold'), 'background': '#2e3f4f', 'foreground': '#ffffff'},
            'TFrame': {'background': '#2e3f4f'},
            'TLabelframe': {'background': '#2e3f4f', 'foreground': '#ffffff'},
            'TLabelframe.Label': {'background': '#2e3f4f', 'foreground': '#ffffff'}
        }
        for style_name, settings in styles.items():
            self.style.configure(style_name, **settings)

    def create_layout(self):
        # Create main container with padding
        self.main_frame = ttk.Frame(self.root, padding="20", style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configure grid
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)

        # Create components
        self.create_header()
        self.create_input_section()
        self.create_file_panel()
        self.create_action_buttons()
        self.create_output_section()
        self.create_status_bar()

    def create_header(self):
        header_frame = ttk.Frame(self.main_frame, style='TFrame')
        header_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        header = ttk.Label(header_frame, text="EnDeCoder Professional", style='Header.TLabel')
        header.pack()

        subheader = ttk.Label(header_frame, text="Secure Text Encoding and Decoding", style='TLabel')
        subheader.pack()

    def create_input_section(self):
        input_frame = ttk.LabelFrame(self.main_frame, text="Input", padding="10", style='TLabelframe')
        input_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        # Input text with scrolled text widget
        ttk.Label(input_frame, text="Input Text:", style='TLabel').pack(anchor='w')
        self.input_text = scrolledtext.ScrolledText(input_frame, height=5, bg='#ffffff', fg='#000000', font=('Helvetica', 10))
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.input_text.bind("<Key>", self.deselect_file_on_input)

        # Key entry
        key_frame = ttk.Frame(input_frame, style='TFrame')
        key_frame.pack(fill=tk.X, pady=5)
        ttk.Label(key_frame, text="Key:", style='TLabel').pack(side=tk.LEFT)
        self.key_text = ttk.Entry(key_frame, font=('Helvetica', 10))
        self.key_text.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(key_frame, text="Generate Key", command=self.generate_key, style='TButton').pack(side=tk.RIGHT)

    def create_file_panel(self):
        file_panel = ttk.LabelFrame(self.main_frame, text="File Options", padding="10", style='TLabelframe')
        file_panel.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        self.file_path = tk.StringVar()
        ttk.Entry(file_panel, textvariable=self.file_path, font=('Helvetica', 10), state='readonly').pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.file_button = ttk.Button(file_panel, text="Select File", command=self.select_file, style='TButton')
        self.file_button.pack(side=tk.LEFT, padx=5)

    def create_action_buttons(self):
        button_frame = ttk.Frame(self.main_frame, style='TFrame')
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Encode", command=self.encode_text, style='TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Decode", command=self.decode_text, style='TButton').pack(side=tk.LEFT, padx=5)

    def create_output_section(self):
        output_frame = ttk.LabelFrame(self.main_frame, text="Output", padding="10", style='TLabelframe')
        output_frame.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        self.output_text = scrolledtext.ScrolledText(output_frame, height=5, bg='#ffffff', fg='#000000', font=('Helvetica', 10))
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.output_text.bind("<Key>", self.check_output)

    def create_status_bar(self):
        self.status = tk.StringVar(value="Welcome to EnDeCoder")
        self.status_bar = ttk.Label(self.root, textvariable=self.status, relief=tk.SUNKEN, anchor=tk.W, background='#4a90e2', foreground='#ffffff', font=('Helvetica', 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.save_button = ttk.Button(self.status_bar, text="Save", command=self.save_output, style='Small.TButton')
        self.save_button.pack(side=tk.RIGHT)
        self.save_button.pack_forget()

    def generate_key(self):
        key = self.endecoder.generate_key()
        self.key_text.delete(0, tk.END)
        self.key_text.insert(0, key)

    def encode_text(self):
        data = self.input_text.get(1.0, tk.END).strip()
        key = self.key_text.get().strip()
        if not data or not key:
            messagebox.showwarning("Input Error", "Please provide both text and key.")
            return
        encoded_data = self.endecoder.encode(data, key)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, encoded_data)
        self.status.set("Text encoded successfully.")
        self.check_output()

    def decode_text(self):
        data = self.input_text.get(1.0, tk.END).strip()
        key = self.key_text.get().strip()
        if not data or not key:
            messagebox.showwarning("Input Error", "Please provide both text and key.")
            return
        decoded_data = self.endecoder.decode(data, key)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, decoded_data)
        self.status.set("Text decoded successfully.")
        self.check_output()

    def save_output(self):
        data = self.output_text.get(1.0, tk.END).strip()
        if data:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if save_path:
                with open(save_path, 'w') as file:
                    file.write(data)
                self.status.set(f"File saved to {save_path}")

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
            with open(file_path, 'r') as file:
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, file.read())
            self.file_button.config(text="Deselect File", command=self.deselect_file)

    def deselect_file(self):
        self.file_path.set("")
        self.input_text.delete(1.0, tk.END)
        self.file_button.config(text="Select File", command=self.select_file)

    def deselect_file_on_input(self, event):
        if self.file_path.get():
            self.deselect_file()

    def check_output(self, event=None):
        if self.output_text.get(1.0, tk.END).strip():
            self.save_button.pack(side=tk.RIGHT)
        else:
            self.save_button.pack_forget()

    def bind_shortcuts(self):
        self.input_text.bind("<Control-a>", self.select_all)
        self.output_text.bind("<Control-a>", self.select_all)

    def select_all(self, event):
        event.widget.tag_add(tk.SEL, "1.0", tk.END)
        event.widget.mark_set(tk.INSERT, "1.0")
        event.widget.see(tk.INSERT)
        return 'break'

def main():
    root = tk.Tk()
    app = EnDeCoderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
