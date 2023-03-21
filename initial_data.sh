#!/bin/bash
# Check virtual environment
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Passing..."
else
    source env/bin/activate
fi

# Load data 
python manage.py loaddata placements/fixtures/student.json
python manage.py loaddata placements/fixtures/company.json
python manage.py loaddata placements/fixtures/job_posting.json
python manage.py loaddata placements/fixtures/placement.json
