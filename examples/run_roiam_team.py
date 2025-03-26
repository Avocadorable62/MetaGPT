from metagpt.team import Team
from metagpt.roles.product_manager import ProductManager
from metagpt.roles.architect import Architect
from metagpt.roles.engineer import Engineer
from metagpt.roles.qa_engineer import QaEngineer
from metagpt.roles.teacher import Teacher
from metagpt.roles.researcher import Researcher
from metagpt.roles.sales import Sales
from metagpt.roles.customer_service import CustomerService
from metagpt.roles.di.role_zero import RoleZero
from metagpt.roles.di.data_analyst import DataAnalyst

from pathlib import Path

# Define path to spec file
base = Path("workspace/projects/RoIAM_V2")
spec_file = base / "SPEC-001-RoIAM_V2.adoc"

# Read the .adoc spec
project_spec = spec_file.read_text() if spec_file.exists() else "Spec file not found."

# Compose the requirement message
project_summary = f"""
You are a multi-agent team working on a product called RoIAM_V2 — Realms of I AM.
This product is a symbolic, rotating, storytelling engine for Instagram.

Here is the official specification written by the founder:

### SPEC ###
{project_spec}
"""

# Initialize team
team = Team()

# Instantiate & hire all relevant agents
pm, _ = ProductManager(name="Emma")
arch, _ = Architect(name="Bob")
eng, _ = Engineer(name="Alex")
team.hire(QaEngineer(name="Edward"))
teach, _ = Teacher(name="Nova")
research, _ = Researcher(name="Zoe")
sales, _ = Sales(name="Drew")
cs, _ = CustomerService(name="Maya")
r0, _ = RoleZero(name="Zero")
analyst, _ = DataAnalyst(name="David")

team.hire(pm)
team.hire(arch)
team.hire(eng)
team.hire(qa)
team.hire(teach)
team.hire(research)
team.hire(sales)
team.hire(cs)
team.hire(r0)
team.hire(analyst)

# Start the project!
team.start_project(project_summary)
