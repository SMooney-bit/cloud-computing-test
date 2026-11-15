# Simple job-description similarity demonstration

jobs = {
    "HR Analyst": "analyze workforce data and prepare reports",
    "Data Analyst": "analyze operational data and prepare reports"
}

words1 = set(jobs["HR Analyst"].split())
words2 = set(jobs["Data Analyst"].split())

shared = words1 & words2

print("Job Description Similarity Demonstration")
print("Shared terms:", sorted(shared))
print("Number of shared terms:", len(shared))
