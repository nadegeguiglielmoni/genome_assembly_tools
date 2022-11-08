"""Dynamically renders the readme from its jinja2 template and csv of assemblers"""
import csv
from dataclasses import dataclass
from typing import Iterable, List, Optional, Type, TypeVar

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
class Processor(Software):
    task: str
    reads: str


S = TypeVar("S", Software, Assembler, Processor)


def load_softwares(path: str, soft_type: Type[S]) -> List[S]:
    """Load a bunch of softwares from CSV file"""
    softs = []
    with open(path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # csv fields expand to dataclass attrs
            softs.append(soft_type(**row))
    return softs


def fmt_processors(procs: Iterable[Processor]):
    """Format processors so that:
    + They are sorted by task, reads
    + Reads field is in italic
    + Only the first of each read type per task has a value
    """
    read_type = ""
    task = ""
    first = True
    fmt_procs = sorted(procs, key=lambda x: (x.task, x.reads))

    for pr in fmt_procs:
        # First processor in category ?
        if (pr.task != task) or (pr.reads != read_type):
            first = True

        read_type = pr.reads
        task = pr.task

        if not first:
            pr.reads = ""
        first = False

    # Add italics
    for pr in fmt_procs:
        if pr.reads:
            pr.reads = f"__{pr.reads}__"

    return fmt_procs


env = Environment(loader=FileSystemLoader("."), autoescape=False,)

# Load list of softwares and render templates consecutively.
# Just dump everything to stdout to compose the readme 🥴

### HEADER ###

with open("templates/header.md") as header:
    print(header.read())

### ASSEMBLERS ###

assemblers = load_softwares("data/assemblers.csv", Assembler)
template = env.get_template("templates/assemblers.j2")
print(template.render(assemblers=assemblers))

### PRE/POST PROCESSORS ###

print("## Assembly pre and post-processing")
procs = load_softwares("data/processors.csv", Processor)
template = env.get_template("templates/processors.j2")
# Gotta sort processors and edit them a bit for fancy md formatting
fmt_procs = fmt_processors(procs)
print(template.render(processors=fmt_procs))
