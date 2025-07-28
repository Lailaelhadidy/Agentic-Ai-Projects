#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from job_posting_creator.crew import JobPostingCreator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory
os.makedirs('output', exist_ok=True)

def run():

    inputs = {
        'job_title': 'Senior Python Developer',
        'industry': 'Technology',
        'location': 'San Francisco, CA'
    }

    result= JobPostingCreator().crew().kickoff(inputs=inputs)

    print("\n\n=== JOB POSTING CREATED ===\n\n")
    print(result.raw)
    print("\n\nJob posting has been saved to output/job_posting.md")

if __name__ == "__main__":
    run()


