import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os


class TextToJsonConverter:
    def __init__(self, template_file):
        with open(template_file, "r", encoding="utf-8") as f:
            self.template = json.load(f)

    def convert(self, input_file, output_file):
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Group every two lines into one and add a copy of the first line
        # to each group, so that every three lines can be converted into
        # a JSON object.
        new_lines = []
        for i in range(0, len(lines), 3):
            if i + 2 >= len(lines) or not lines[i].strip() or not lines[i + 1].strip():
                continue
            new_lines.append([lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()])
            new_lines[-1].insert(0, lines[i].strip())

        output_data = []
        for group in new_lines:
            data = self.template.copy()
            data["cmd"] = group[0]
            data["act"] = group[1]
            data["prompt"] = group[2]
            output_data.append(data)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)


class App:
    def __init__(self, master):
        self.master = master
        self.file_path = ""
        self.output_file_path = ""
        self.converter = TextToJsonConverter("template.json")

        self.create_widgets()

    def create_widgets(self):
        # label
        self.label = tk.Label(self.master, text="Text to JSON Converter", font=("Arial", 16))
        self.label.pack(pady=20)

        # select file button
        self.select_file_button = tk.Button(self.master, text="Select Input File", command=self.select_file)
        self.select_file_button.pack(pady=10)

        # select output file button
        self.select_output_button = tk.Button(self.master, text="Select Output File", command=self.select_output)
        self.select_output_button.pack(pady=10)

        # convert button
        self.convert_button = tk.Button(self.master, text="Convert to JSON", command=self.convert)
        self.convert_button.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()

    def select_output(self):
        self.output_file_path = filedialog.asksaveasfilename(defaultextension=".json")

    def convert(self):
        if not self.file_path:
            messagebox.showwarning("Error", "Please select an input file")
            return

        if not self.output_file_path:
            messagebox.showwarning("Error", "Please select an output file")
            return

        try:
            self.converter.convert(self.file_path, self.output_file_path)
            messagebox.showinfo("Success", "Conversion successful!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()