import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    project_root = Path(__file__).parent.parent
    env_file_path = os.getenv('environment_file_path')
    env_type = os.getenv('environment_type')

    if env_type == 'production':
        env_file_path = env_file_path if env_file_path else 'env/.env.production'
    elif env_type == 'stage':
        env_file_path = env_file_path if env_file_path else 'env/.env.stage'
    elif env_type == 'development':
        env_file_path = env_file_path if env_file_path else 'env/.env.development'
    elif env_type == 'local':
        env_file_path = env_file_path if env_file_path else 'env/.env.local'
    elif env_type == 'test':
        env_file_path = env_file_path if env_file_path else 'env/.env.test'
    else:
        raise ValueError(f'Unknown env type: {env_type}')

    dotenv_path = os.path.join(project_root, env_file_path)

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(f'Env file not found: {dotenv_path}')
