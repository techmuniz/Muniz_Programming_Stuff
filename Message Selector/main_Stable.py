import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
import pyperclip
import json

def load_data():
    try:
        with open("save_data.json", "r") as f:
            data = json.load(f)
            # Certificar-se de que todas as chaves necessárias existam
            for key in ("texts", "button_texts", "counters"):
                if key not in data:
                    data[key] = []
            return data
    except FileNotFoundError:
        return {"texts": [], "button_texts": [], "counters": []}

ui_texts = {
    "copy": "Copy Text",
    "edit": "Edit Box Name",
    "clear": "Clear",
    "save_exit": "Save and Exit",
    "num_boxes": "How many text boxes do you want?",
    "rename_button": "Enter a new button name:",
    "copied": "Text copied!",
    "edit_count": "Edit Count",
    "new_count_value": "New count value:",
    "invalid_input": "Invalid Input",
    "enter_valid_number": "Please enter a valid number."
}

def edit_box_size(text_widgets):
    new_width = simpledialog.askinteger("Size", "Enter the new width:", minvalue=10, maxvalue=200)
    if new_width:  # Se o usuário inseriu um valor, ajuste a largura das caixas de texto
        for text_widget in text_widgets:
            text_widget.config(width=new_width)

def copy_text_to_clipboard(text_widget, counter, status_message):
    text_to_copy = text_widget.get("1.0", tk.END).strip()
    pyperclip.copy(text_to_copy)
    status_message.set(ui_texts["copied"])
    counter["value"] += 1
    counter["label"].config(text=str(counter["value"]))

def clear_text(text_widget, counter):
    text_widget.delete("1.0", tk.END)
    counter["value"] = 0
    counter["label"].config(text="0")

def edit_button_name(button):
    new_name = simpledialog.askstring(ui_texts["edit"], ui_texts["rename_button"])
    if new_name:
        button.config(text=new_name)

def edit_counter(counter):
    new_count_str = simpledialog.askstring(ui_texts["edit_count"], ui_texts["new_count_value"])
    try:
        new_count = int(new_count_str)
        if new_count >= 0:
            counter["value"] = new_count
            counter["label"].config(text=str(new_count))
    except (TypeError, ValueError):
        messagebox.showerror(ui_texts["invalid_input"], ui_texts["enter_valid_number"])

def create_text_boxes_and_buttons(container, num_boxes, saved_data):
    text_widgets = []
    copy_buttons = []  # Collect the 'copy' buttons for saving their texts afterwards
    counters = []  # New list to store counter dict items for each text box
    for i in range(num_boxes):
        frame = tk.Frame(container)
        frame.pack(pady=10, fill=tk.X)

        text_cmd_frame = tk.Frame(frame)
        text_cmd_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        text_field = scrolledtext.ScrolledText(text_cmd_frame, height=8, width=30)
        text_field.grid(row=0, column=0, sticky='ew')
        if i < len(saved_data["texts"]):
            text_field.insert(tk.END, saved_data["texts"][i])
        text_widgets.append(text_field)

        cmd_frame = tk.Frame(text_cmd_frame)
        cmd_frame.grid(row=0, column=1, padx=5, sticky='ns')

        initial_count = saved_data["counters"][i] if i < len(saved_data["counters"]) else 0
        counter = {"value": initial_count, "label": tk.Label(cmd_frame, text=str(initial_count))}
        counter["label"].pack(side=tk.TOP)
        counters.append(counter)  # Save counter to list
        counter["label"].bind("<Button-1>", lambda event, c=counter: edit_counter(c))

        status_message = tk.StringVar(value="")
        status_label = tk.Label(cmd_frame, textvariable=status_message)
        status_label.pack(fill='both', expand=True)

        button_text = ui_texts["copy"] if i >= len(saved_data["button_texts"]) else saved_data["button_texts"][i]
        copy_button = tk.Button(cmd_frame, text=button_text, command=lambda tw=text_field, c=counter, sm=status_message: copy_text_to_clipboard(tw, c, sm))
        copy_button.pack(fill=tk.X)
        copy_buttons.append(copy_button)  # Add this button to the list for later reference

        edit_button = tk.Button(cmd_frame, text=ui_texts["edit"], command=lambda btn=copy_button: edit_button_name(btn))
        edit_button.pack(fill=tk.X)

        clear_button = tk.Button(cmd_frame, text=ui_texts["clear"], command=lambda tw=text_field, c=counter: clear_text(tw, c))
        clear_button.pack(fill=tk.X)

    return text_widgets, copy_buttons, counters

def save_data(text_widgets, copy_buttons, counters):
    data = {
        "texts": [tw.get("1.0", tk.END).strip() for tw in text_widgets],
        "button_texts": [btn.cget("text") for btn in copy_buttons],
        "counters": [c["value"] for c in counters]
    }
    with open("save_data.json", "w") as f:
        json.dump(data, f)

def main():
    saved_data = load_data()
    num_text_boxes = simpledialog.askinteger("Input", ui_texts["num_boxes"], initialvalue=max(len(saved_data["texts"]), 1))

    if num_text_boxes:
        main_window = tk.Tk()
        main_window.title("Copy & Paster")

        main_frame = tk.Frame(main_window)
        main_frame.pack(fill=tk.BOTH, expand=1)

        set_box_size_button = tk.Button(main_frame, text="Set Box Size", command=lambda: edit_box_size(text_widgets))
        set_box_size_button.pack(pady=(0,10))

        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        main_window.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        text_widgets, copy_buttons, counters = create_text_boxes_and_buttons(content_frame, num_text_boxes, saved_data)

        save_and_exit_button = tk.Button(main_window, text=ui_texts["save_exit"], command=lambda: (save_data(text_widgets, copy_buttons, counters), main_window.destroy()))
        save_and_exit_button.pack(pady=(10,0))

        main_window.mainloop()

if __name__ == "__main__":
    main()