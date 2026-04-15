from loguru import logger
import os

def get_module_logger(module_name):
    """Get a configured logger for a specific module."""
    module_logger = logger.bind(module=module_name)
    return module_logger

def configure_module_logger(module_name):
    """Configure a logger for a specific module with its own file."""
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    module_logger = logger.bind(module=module_name)
    module_logger.add(
        os.path.join(logs_dir, f"{module_name}_{{time:YYYY-MM-DD}}.log"),
        rotation="00:00",
        retention="30 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG",
        filter=lambda record: record["extra"].get("module") == module_name
    )
    
    return module_logger
