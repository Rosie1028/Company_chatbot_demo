from langchain_core.tools import tool
import backend.db_access.db_helper as db_helper
from backend.db_access.user_info_helper import get_user_info
from ..helpers import create_csv_file

username = " "
data = get_user_info(username)


@tool
def create_my_research_group_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información del grupo de investigación del usuario en un archivo CSV."""
    return create_csv_file(
        db_helper.get_my_research_group_info(data["research_group_id"])
    )


@tool
def create_my_research_group_projects_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los proyectos del grupo de investigación del usuario en un archivo CSV."""
    return create_csv_file(
        db_helper.get_my_research_group_projects(data["research_group_id"])
    )


@tool
def create_my_projects_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los proyectos en los que ha participado el usuario en un archivo CSV."""
    return create_csv_file(db_helper.get_my_projects(data["my_employee_id"]))


@tool
def create_my_program_projects_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los proyectos del programa del usuario en un archivo CSV."""
    return create_csv_file(
        db_helper.get_my_program_projects(data["research_program_id"])
    )


@tool
def create_projects_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los proyectos en un archivo CSV."""
    return create_csv_file(db_helper.get_projects_info(username))


@tool
def create_persons_projects_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los proyectos de las personas en un archivo CSV."""
    return create_csv_file(db_helper.get_persons_projects_info(username))


@tool
def create_my_publications_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las publicaciones del usuario en un archivo CSV."""
    return create_csv_file(db_helper.get_my_publications(data["my_employee_id"]))


@tool
def create_my_research_group_publications_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las publicaciones del grupo de investigación del usuario en un archivo CSV."""
    return create_csv_file(
        db_helper.get_my_research_group_publications(data["research_group_id"])
    )


@tool
def create_my_program_publications_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las publicaciones del programa del usuario en un archivo CSV."""
    return create_csv_file(
        db_helper.get_my_program_publications(data["research_program_id"])
    )


@tool
def create_publications_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las publicaciones en un archivo CSV."""
    return create_csv_file(db_helper.get_publications_info(username))


@tool
def create_persons_publications_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las publicaciones de las personas en un archivo CSV."""
    return create_csv_file(db_helper.get_persons_publications_info(username))


@tool
def create_persons_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las personas en un archivo CSV."""
    return create_csv_file(db_helper.get_persons_info(username))


@tool
def create_contract_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de los contratos en un archivo CSV."""
    return create_csv_file(db_helper.get_contract_info(username))


@tool
def create_convocatorias_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las convocatorias en un archivo CSV."""
    return create_csv_file(db_helper.get_convocatorias_info(username))


@tool
def create_actions_info_csv(username=None):
    """Esta herramienta se utiliza para obtener la información de las acciones en un archivo CSV."""
    return create_csv_file(db_helper.get_actions_info(data["roles"]))
