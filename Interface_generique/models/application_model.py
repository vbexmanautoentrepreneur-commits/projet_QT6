from dataclasses import dataclass

@dataclass
class ApplicationModel:

    user_name: str = ""
    version: str = "1.0.0"
    project_name: str = ""