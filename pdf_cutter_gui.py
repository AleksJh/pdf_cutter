import os
import threading
import tkinter as tk
import webbrowser
from tkinter import filedialog, messagebox, ttk

from PyPDF2 import PdfReader, PdfWriter


class PDFCutterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Cutter")
        self.root.geometry("600x450")
        self.root.resizable(True, True)

        # Set theme colors
        self.bg_color = "#f0f0f0"
        self.accent_color = "#4a86e8"
        self.root.configure(bg=self.bg_color)

        # Create variables
        self.input_pdf = tk.StringVar()
        self.output_pdf = tk.StringVar()
        self.pages_to_extract = tk.StringVar()
        self.status_text = tk.StringVar(value="Ready")
        self.total_pages = 0
        self.preview_pages = []

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input file selection
        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(input_frame, text="Input PDF:", bg=self.bg_color, anchor="w").pack(
            side=tk.LEFT
        )
        tk.Entry(input_frame, textvariable=self.input_pdf, width=50).pack(
            side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True
        )
        tk.Button(
            input_frame,
            text="Browse",
            command=self.browse_input,
            bg=self.accent_color,
            fg="white",
        ).pack(side=tk.LEFT)

        # Output file selection
        output_frame = tk.Frame(main_frame, bg=self.bg_color)
        output_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(output_frame, text="Output PDF:", bg=self.bg_color, anchor="w").pack(
            side=tk.LEFT
        )
        tk.Entry(output_frame, textvariable=self.output_pdf, width=50).pack(
            side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True
        )
        tk.Button(
            output_frame,
            text="Browse",
            command=self.browse_output,
            bg=self.accent_color,
            fg="white",
        ).pack(side=tk.LEFT)

        # Pages selection
        pages_frame = tk.Frame(main_frame, bg=self.bg_color)
        pages_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            pages_frame, text="Pages to extract:", bg=self.bg_color, anchor="w"
        ).pack(side=tk.LEFT)
        tk.Entry(pages_frame, textvariable=self.pages_to_extract, width=50).pack(
            side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True
        )

        # Help text
        help_text = "Format: 1,3,5-7 (individual pages and ranges)"
        tk.Label(
            main_frame, text=help_text, bg=self.bg_color, fg="gray", anchor="w"
        ).pack(fill=tk.X)

        # Spacer frame
        spacer_frame = tk.Frame(main_frame, bg=self.bg_color, height=20)
        spacer_frame.pack(fill=tk.X, pady=(10, 10))

        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(10, 0))

        tk.Button(
            buttons_frame,
            text="Extract Pages",
            command=self.extract_pages,
            bg=self.accent_color,
            fg="white",
        ).pack(side=tk.LEFT)

        # Status bar
        status_bar = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.progress_bar = ttk.Progressbar(status_bar, mode="indeterminate")
        self.progress_bar.pack(side=tk.RIGHT, padx=(0, 10), fill=tk.X, expand=True)

        tk.Label(status_bar, textvariable=self.status_text, anchor=tk.W, padx=10).pack(
            side=tk.LEFT, fill=tk.X
        )

    def browse_input(self):
        filename = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.input_pdf.set(filename)
            # Auto-generate output filename
            input_path = os.path.dirname(filename)
            input_name = os.path.basename(filename)
            base_name, _ = os.path.splitext(input_name)
            output_name = f"{base_name}_extracted.pdf"
            output_path = os.path.join(input_path, output_name)
            self.output_pdf.set(output_path)

            # Get total pages and set default page range
            try:
                reader = PdfReader(filename)
                self.total_pages = len(reader.pages)
                if self.total_pages > 0:
                    self.pages_to_extract.set(f"1-{self.total_pages}")
                self.status_text.set(f"PDF loaded: {self.total_pages} pages")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load PDF: {str(e)}")
                self.status_text.set("Error loading PDF")

    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if filename:
            self.output_pdf.set(filename)

    def parse_page_ranges(self, page_string):
        pages = []
        ranges = page_string.split(",")

        for r in ranges:
            r = r.strip()
            if "-" in r:
                try:
                    start, end = map(int, r.split("-"))
                    pages.extend(range(start, end + 1))
                except ValueError:
                    continue
            else:
                try:
                    pages.append(int(r))
                except ValueError:
                    continue

        return sorted(set(pages))  # Remove duplicates and sort

    def extract_pages(self):
        input_file = self.input_pdf.get()
        output_file = self.output_pdf.get()
        pages_str = self.pages_to_extract.get()

        if not input_file or not output_file or not pages_str:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not os.path.exists(input_file):
            messagebox.showerror("Error", f"Input file not found: {input_file}")
            return

        # Parse page ranges
        page_list = self.parse_page_ranges(pages_str)

        if not page_list:
            messagebox.showerror("Error", "No valid pages specified.")
            return

        self.status_text.set("Extracting pages...")
        self.progress_bar.start()

        # Run in a separate thread to keep UI responsive
        threading.Thread(
            target=self._extract_pages_thread,
            args=(input_file, output_file, page_list),
            daemon=True,
        ).start()

    def _extract_pages_thread(self, input_file, output_file, page_list):
        try:
            reader = PdfReader(input_file)
            writer = PdfWriter()

            total_pages = len(reader.pages)
            valid_pages = []

            for page_num in page_list:
                # Convert from 1-based (user input) to 0-based (PyPDF2 indexing)
                idx = page_num - 1
                if 0 <= idx < total_pages:
                    valid_pages.append(idx)

            if not valid_pages:
                self.root.after(
                    0,
                    lambda: messagebox.showerror("Error", "No valid pages to extract."),
                )
                self.root.after(
                    0, lambda: self.status_text.set("Error: No valid pages")
                )
                self.root.after(0, self.progress_bar.stop)
                return

            # Add selected pages to the writer
            for page_idx in valid_pages:
                writer.add_page(reader.pages[page_idx])

            # Create output directory if it doesn't exist
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Write the output file
            with open(output_file, "wb") as output_file_obj:
                writer.write(output_file_obj)

            success_message = f"Successfully extracted {len(valid_pages)} pages."
            self.root.after(0, lambda: messagebox.showinfo("Success", success_message))
            self.root.after(0, lambda: self.status_text.set(success_message))

            # Ask if user wants to open the file
            self.root.after(0, lambda: self.ask_open_file(output_file))

        except Exception as error:
            error_message = f"Failed to extract pages: {str(error)}"
            self.root.after(
                0,
                lambda: messagebox.showerror("Error", error_message)
            )
            self.root.after(0, lambda: self.status_text.set("Error extracting pages"))

        finally:
            self.root.after(0, self.progress_bar.stop)

    def ask_open_file(self, file_path):
        if messagebox.askyesno("Open File", "Do you want to open the extracted PDF?"):
            try:
                webbrowser.open(file_path)
            except Exception as error:
                messagebox.showerror("Error", f"Failed to open file: {str(error)}")


def main():
    root = tk.Tk()
    PDFCutterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
