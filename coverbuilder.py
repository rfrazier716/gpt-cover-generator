from openai import OpenAI
from dotenv import load_dotenv
from jinja2 import Template
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import os

template_dir = Path(__file__).parent / "templates"
resume_path = Path(__file__).parent / "resume.txt"
cover_letter_path = Path(__file__).parent / "cover_letter.txt"
job_dir = Path(__file__).parent / "jobs"

# create an openAI Client
load_dotenv()


def generate_cover_letter(system_prompt, user_prompt) -> str:
    client = OpenAI()

    response = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[
        {
          "role": "system",
          "content": system_prompt},
        {
          "role": "user",
          "content": user_prompt},
      ],
      temperature=1,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    

    return response.choices[0].message.content

def create_system_prompt() -> str:
    kwargs = {}
    with open(template_dir / "system.jinja") as fii:
        template = Template(fii.read())

    with open(resume_path) as fii:
        kwargs["resume"] = fii.read()
    
    try:
        with open(cover_letter_path) as fii:
            kwargs["cover_letter"] = fii.read()
    except IOError:
        print("no cover letter provided")
    
    # populate the template with the resume
    return template.render(**kwargs)

def get_job_description(li_job_id: str) -> str:
    job_filename = li_job_id + ".txt"
    if os.path.isfile(job_dir / job_filename):
        with open(job_dir / job_filename) as fii:
            body = fii.read()
            return body
    else:
        raise IOError("File Does not Exist")

def create_user_prompt(job_description: str) -> str:
    with open(template_dir / "prompt.jinja") as fii:
        template = Template(fii.read())
    
    # populate the template with the resume
    return template.render(posting=job_description)

def main():
    job_id = "3799866958"
    cover_letter_filename = job_id + "_cover.txt"
    if os.path.isfile(job_dir / cover_letter_filename):
        print("Cover letter already generated for job ID, exiting")
        return
    
    # Load the System template
    system = create_system_prompt()

    # load the cover letter template
    description = get_job_description(job_id)
    user = create_user_prompt(description)

    # Query the Model
    cover_letter = generate_cover_letter(system, user)
    with open(job_dir / cover_letter_filename, "w+") as foo:
        foo.write(cover_letter)



if __name__ == '__main__':
    main()