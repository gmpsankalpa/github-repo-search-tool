import os
from dotenv import load_dotenv
import requests
import tkinter as tk
from tkinter import scrolledtext, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load environment variables from .env file
load_dotenv()

# Access the GitHub token from the environment
github_token = os.getenv("GITHUB_TOKEN")

def search_github_repositories(query, token):
    base_url = "https://api.github.com/search/repositories"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "sort": "stars", "order": "desc"}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()["items"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_repository_info(repository):
    info = (
        f"<b>Repository:</b> {repository['name']}<br/>"
        f"<b>Description:</b> {repository['description']}<br/>"
        f"<b>Stars:</b> {repository['stargazers_count']}<br/>"
        f"<b>URL:</b> <a href='{repository['html_url']}'>{repository['html_url']}</a><br/><br/>"
    )
    return info

def save_to_pdf(filename, title, content):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list to hold the flowables (elements) of the PDF
    pdf_content = []

    # Add title to the PDF
    pdf_content.append(Paragraph(title, styles['Title']))

    for line in content.split('\n'):
        if line.strip():
            para = Paragraph(line, styles['Normal'])
            pdf_content.append(para)
        else:
            pdf_content.append(Spacer(1, 12))  # Add some vertical space between entries

    doc.build(pdf_content)

def export_to_pdf():
    query = search_entry.get()
    repositories = search_github_repositories(query, github_token)

    if repositories:
        pdf_content = ""
        for repo in repositories:
            pdf_content += display_repository_info(repo)

        title = f"GitHub Repository Search Results for '{query}'"

        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if file_path:
            save_to_pdf(file_path, title, pdf_content)

def search_button_clicked():
    query = search_entry.get()
    repositories = search_github_repositories(query, github_token)

    if repositories:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)

        for index, repo in enumerate(repositories, start=1):
            result_text.insert(tk.END, f"\nResult #{index}\n")
            result_text.insert(tk.END, f"Repository: {repo['name']}\n")
            result_text.insert(tk.END, f"Description: {repo['description']}\n")
            result_text.insert(tk.END, f"Stars: {repo['stargazers_count']}\n")
            result_text.insert(tk.END, f"URL: {repo['html_url']}\n\n")

        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No repositories found.")
        result_text.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("GitHub Repository Search")

search_label = tk.Label(root, text="Search Query:")
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_button_clicked)
search_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=80, height=20, state=tk.DISABLED)
result_text.pack(pady=10)

export_button = tk.Button(root, text="Export to PDF", command=export_to_pdf)
export_button.pack(pady=10)

root.mainloop()
