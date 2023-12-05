import tkinter as tk
import requests

class Job:
    def __init__(self, title, company, location, description, apply_url):
        self.title = title
        self.company = company
        self.location = location
        self.description = description
        self.apply_url = apply_url

class JobApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Listings")

        self.jobs = []  # List to store selected jobs

        self.text_box = tk.Text(root, height=20, width=80)
        self.text_box.grid(row=0, column=0, columnspan=2, pady=10)

        self.fetch_jobs_button = tk.Button(root, text="Fetch Jobs", command=self.fetch_jobs)
        self.fetch_jobs_button.grid(row=1, column=0, sticky="w", padx=10)

    def fetch_jobs(self):
        # Clear existing text
        self.text_box.delete(1.0, tk.END)

        # Adzuna API request
        api_url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
        payload = {
            "app_id": "448d6495",  # Replace with your Adzuna app ID
            "app_key": "214351c80e158b093f8aa6473bf75dc7",  # Replace with your Adzuna app key
            "results_per_page": 5,  # Adjust as needed
        }

        response = requests.get(api_url, params=payload)

        if response.status_code == 200:
            jobs = response.json().get("results", [])

            for i, job in enumerate(jobs):
                job_entry = f"{i + 1}. Title: {job['title']}, Company: {job['company']['display_name']}, " \
                            f"Location: {job['location']['display_name']}, Description: {job['description']}\n"
                self.text_box.insert(tk.END, job_entry)

                # Add an "Apply" button for each job using grid
                apply_button = tk.Button(self.root, text="Apply", command=lambda j=job: self.apply_for_job(j))
                apply_button.grid(row=i+2, column=1, sticky="e", padx=10)

            self.text_box.insert(tk.END, "\nClick 'Apply' next to a job to select it.")
        else:
            self.text_box.insert(tk.END, f"Failed to fetch job listings. Status code: {response.status_code}")

    def apply_for_job(self, job):
        # Add the selected job to the list
        selected_job = Job(
            title=job['title'],
            company=job['company']['display_name'],
            location=job['location']['display_name'],
            description=job['description'],
            apply_url=job['redirect_url']
        )
        self.jobs.append(selected_job)

        # Display the selected jobs in a separate window
        SelectedJobsPage(self.root, self.jobs)

class SelectedJobsPage:
    def __init__(self, root, jobs):
        self.root = root
        self.jobs = jobs

        self.selected_jobs_page = tk.Toplevel(root)
        self.selected_jobs_page.title("Selected Jobs")

        self.text_box = tk.Text(self.selected_jobs_page, height=20, width=80)
        self.text_box.pack(pady=10)

        self.display_jobs()

    def display_jobs(self):
        # Display selected jobs in the text box
        for i, job in enumerate(self.jobs):
            job_entry = f"{i + 1}. Title: {job.title}, Company: {job.company}, Location: {job.location}, Description: {job.description}\n"
            self.text_box.insert(tk.END, job_entry)

if __name__ == "__main__":
    root = tk.Tk()
    job_app = JobApp(root)
    root.mainloop()
        
        
        
        


