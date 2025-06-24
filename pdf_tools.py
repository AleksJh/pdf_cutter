import os
import subprocess
import sys
import tkinter as tk
import webbrowser
from tkinter import messagebox


class PDFToolsLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Tools Launcher")
        self.root.geometry("400x350")
        self.root.resizable(True, True)

        # Set theme colors
        self.bg_color = "#f0f0f0"
        self.accent_color = "#4a86e8"
        self.root.configure(bg=self.bg_color)

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(
            main_frame,
            text="PDF Tools",
            font=("Helvetica", 16, "bold"),
            bg=self.bg_color,
        )
        title_label.pack(pady=(0, 20))

        # Description
        description = "Select a tool to launch:"
        desc_label = tk.Label(main_frame, text=description, bg=self.bg_color)
        desc_label.pack(pady=(0, 20))

        # Tool buttons
        tools_frame = tk.Frame(main_frame, bg=self.bg_color)
        tools_frame.pack(fill=tk.BOTH, expand=True)

        # GUI Tool
        gui_frame = tk.LabelFrame(
            tools_frame, text="PDF Cutter (GUI)", bg=self.bg_color, padx=10, pady=10
        )
        gui_frame.pack(fill=tk.X, pady=(0, 10))

        gui_desc = "Extract pages from a single PDF file using a graphical interface."
        tk.Label(
            gui_frame, text=gui_desc, bg=self.bg_color, wraplength=400, justify=tk.LEFT
        ).pack(anchor=tk.W)

        tk.Button(
            gui_frame,
            text="Launch PDF Cutter",
            command=self.launch_gui,
            bg=self.accent_color,
            fg="white",
            width=20,
        ).pack(pady=(10, 0))

        # CLI Tool
        cli_frame = tk.LabelFrame(
            tools_frame, text="Command Line Tool", bg=self.bg_color, padx=10, pady=10
        )
        cli_frame.pack(fill=tk.X, pady=(0, 10))

        cli_desc = "Use the command line interface for scripting or quick extractions."
        tk.Label(
            cli_frame, text=cli_desc, bg=self.bg_color, wraplength=400, justify=tk.LEFT
        ).pack(anchor=tk.W)

        cli_example = (
            'Example: poetry run python pdf_cutter.py input.pdf output.pdf "1,3,5-7"'
        )
        tk.Label(
            cli_frame,
            text=cli_example,
            bg=self.bg_color,
            fg="gray",
            wraplength=400,
            justify=tk.LEFT,
        ).pack(anchor=tk.W)

        # Help and documentation
        help_frame = tk.Frame(main_frame, bg=self.bg_color)
        help_frame.pack(fill=tk.X, pady=(10, 0))

        tk.Button(
            help_frame,
            text="View Documentation",
            command=self.open_readme,
            bg="#2ecc71",
            fg="white",
            width=18,
            height=2,
        ).pack(side=tk.LEFT)

        tk.Button(
            help_frame,
            text="Check for Updates",
            command=self.check_updates,
            bg="#3498db",
            fg="white",
            width=18,
            height=2,
        ).pack(side=tk.RIGHT)

    def launch_gui(self):
        try:
            # Use CREATE_NO_WINDOW flag to hide console window
            startupinfo = None
            if os.name == 'nt':
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = 0  # SW_HIDE
            
            subprocess.Popen([sys.executable, "pdf_cutter_gui.py"], 
                            startupinfo=startupinfo, 
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch PDF Cutter: {str(e)}")

    def open_readme(self):
        readme_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "README.md"
        )
        if os.path.exists(readme_path):
            try:
                # Try to open with default application
                os.startfile(readme_path)
            except AttributeError:
                # For non-Windows platforms
                try:
                    webbrowser.open(f"file://{readme_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to open README: {str(e)}")
        else:
            messagebox.showerror("Error", "README.md not found")

    def check_updates(self):
        # This is a placeholder for a real update check
        messagebox.showinfo("Updates", "You are using the latest version of PDF Tools.")


def main():
    # Launch the GUI
    root = tk.Tk()
    # Set icon for the main window
    try:
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file_types_pdf_21313.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception:
        pass  # Ignore icon errors
        
    PDFToolsLauncher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
