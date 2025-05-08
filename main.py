import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.entry = tk.Entry(root, font=('Arial', 20), bd=10, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('C',4,2), ('+',4,3),
            ('=',5,0,4)
        ]

        for b in buttons:
            text, row, col = b[0], b[1], b[2]
            colspan = b[3] if len(b) == 4 else 1
            self.create_button(text, row, col, colspan)

    def create_button(self, val, row, col, colspan):
        btn = tk.Button(self.root, text=val, padx=20, pady=20,
                        font=('Arial', 14),
                        command=lambda: self.click(val))
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def click(self, key):
        if key == 'C':
            self.expression = ''
        elif key == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = 'Error'
        else:
            self.expression += key
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
