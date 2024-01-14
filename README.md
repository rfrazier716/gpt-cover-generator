# Cover Letter Generator
Basic Python Script to generate resume-specific cover letters using Chat GPT

## Requirements

- An OpenAI Developer Account and API Key (Each cover letter request will cost ~$0.03)
- Python 3.10 or higher

## Installation

### Installing Dependencies
- Clone the respository 
- in the project directory, create a new python virtual environment `python3 -m virtualenv .venv`
- activate the virtual environment
    - on linux: `source ./.venv/bin/activate`
    - on windows: `.\.venv\Scripts\activate.ps1`
- install the dependencies `python -m pip install -r requirements.txt`

### Adding User Specific Details
- Create a file `resume.txt` at the project root and paste your resume. Apply any necessary formatting to make it text readable
- If you want to provide an example cover letter to follow, create a file `cover_letter.txt` in the project root and paste the cover letter into it.
- create a file `.env` in the project root and add your OpenAI API key. The contents of the file should look like below:
  
    ```
    OPENAI_API_KEY = sk_KEY_GOES_HERE
    ```

## Usage
- Create a new file with the job description in `/jobs/<job_id>.txt`
- update the script so that the `job_id` variable matches the file name
- run the script
- you'll now have a file `/jobs/<job_id>_cover.txt` with the generated cover letter

