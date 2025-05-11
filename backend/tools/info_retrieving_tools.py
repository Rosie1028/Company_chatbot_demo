from langchain_core.tools import tool
import backend.db_access.db_helper as db_helper
from backend.db_access.user_info_helper import get_user_info

username = " "
data = get_user_info(username)


@tool
def get_my_research_group_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de un grupo de investigacion, no se utiliza cuando el usuario quiere crear un csv"""
    return db_helper.get_my_research_group_info(data["research_group_id"])


# *Projects
@tool
def get_my_research_group_projects_info_tool(username=None):
    """Esta herramienta obtiene la informacion de los proyectos del grupo de investigacion del usuario"""
    return db_helper.get_my_research_group_projects(data["research_group_id"])


@tool
def get_my_projects_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de los proyectos en que un usuario ha participado como investigador"""
    return db_helper.get_my_projects(data["my_employee_id"])


@tool
def get_my_program_projects_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de los proyectos que se han llevado a cabo en un programa de investigacion"""
    return db_helper.get_my_program_projects(data["research_program_id"])


@tool
def get_projects_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de los proyectos en la base de datos"""
    return db_helper.get_projects_info(username)


@tool
def get_persons_projects_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las personas que han participado en proyectos"""
    return db_helper.get_persons_projects_info(username)


# *Publications
@tool
def get_my_publications_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las publicaciones en que un usuario ha participado como autor"""
    return db_helper.get_my_publications(data["my_employee_id"])


@tool
def get_my_research_group_publications_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las publicaciones en que un grupo de investigacion ha participado"""
    return db_helper.get_my_research_group_publications(data["research_group_id"])


@tool
def get_my_program_publications_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las publicaciones en que un programa de investigacion ha participado"""
    return db_helper.get_my_program_publications(data["research_program_id"])


@tool
def get_publications_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las publicaciones en la base de datos"""
    return db_helper.get_publications_info(username)


@tool
def get_persons_publications_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la infromacion de las personas que han participado en publicaciones"""
    return db_helper.get_persons_publications_info(username)


# * Get Persons Info
@tool
def get_persons_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la infromacion de las personas en la base de datos"""
    return db_helper.get_persons_info(username)


# * Get Contract Info
@tool
def get_contract_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de los contratos de la empresa"""
    return db_helper.get_contract_info(username)


# * Get Convocatorias Info
@tool
def get_convocatorias_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de las convocatorias"""
    return db_helper.get_convocatorias_info(username)


# * Actions
@tool
def get_actions_info_tool(username=None):
    """Esta herramienta se utiliza para obtener la informacion de como el usuario puede realizar acciones , usar cuando pregunta como hacer un procedimiento"""
    return db_helper.get_actions_info(data["roles"])
