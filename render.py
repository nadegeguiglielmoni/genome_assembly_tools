"""Renders the readme from its jinja2 template and csv of assemblers"""
import csv
from dataclasses import dataclass
from typing import List, Optional, Type

from jinja2 import Environment, FileSystemLoader


@dataclass
class Software:
    """Used to allow automatic update-date retrieval in subclasses"""

    name: str
    link: str
    publication: Optional[str]
    last_update: Optional[str]

    def __post_init__(self):
        if not self.last_update:
            self.set_last_commit_date()

    def set_last_commit_date(self):
        # Dispatch based on URL pattern
        # e.g. gh api for github.com
        # git for other git providers
        # http response header for others ? (unreliable)
        ...


@dataclass
class Assembler(Software):
    technology: str


@dataclass
class PostProcessor(Software):
    task: str
    reads: str


def load_softwares(path: str, soft_type: Type[Software]) -> List[Software]:
    """Load a bunch of softwares from CSV file"""
    softs = []
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # csv fields expand to dataclass attrs
            print(row)
            softs.append(soft_type(**row))
    return softs


env = Environment(loader=FileSystemLoader("."), autoescape=True,)

# Load list of assemblers and render template
assemblers = load_softwares("data/assemblers.csv", Assembler)
template = env.get_template("templates/assemblers.tmpl")
print(template.render(assemblers=assemblers))

