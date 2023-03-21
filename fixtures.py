from django.core.serializers import serialize
from placements.models import Student, Company, JobPosting, Placement

# Students
students = [
    Student(
        name="John Smith",
        email="john@example.com",
        roll_number="001",
        status="Available",
    ),
    Student(
        name="Jane Doe", email="jane@example.com", roll_number="002", status="Placed"
    ),
]

data = serialize("json", students)

with open("data_students.json", "w") as f:
    f.write(data)


# Companies
companies = [
    Company(name="Google", website="https://www.google.com", email="info@google.com"),
    Company(
        name="Facebook", website="https://www.facebook.com", email="info@facebook.com"
    ),
]

data = serialize("json", companies)

with open("data_companies.json", "w") as f:
    f.write(data)


# Job Postings
job_postings = [
    JobPosting(
        company=companies[0],
        title="Software Engineer",
        description="Looking for a software engineer to join our team.",
        qualifications="Bachelor's degree in computer science.",
    ),
    JobPosting(
        company=companies[1],
        title="Data Analyst",
        description="Looking for a data analyst to join our team.",
        qualifications="Master's degree in statistics.",
    ),
]

data = serialize("json", job_postings)

with open("data_job_postings.json", "w") as f:
    f.write(data)


# Placements
placements = [
    Placement(
        student=students[0],
        job_posting=job_postings[0],
        date="2022-01-01",
        is_accepted=False,
    ),
    Placement(
        student=students[1],
        job_posting=job_postings[1],
        date="2022-01-02",
        is_accepted=True,
    ),
]

data = serialize("json", placements)

with open("data_placements.json", "w") as f:
    f.write(data)
