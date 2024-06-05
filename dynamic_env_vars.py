import os
from typing import Any


def get_env(env_var: str) -> Any:
    """Retrieve the value of an environment variable.

    Args:
        env_var (str): The name of the environment variable.

    Returns:
        Any: The value of the environment variable or a default value.

    Raises:
        KeyError: If the environment variable is not found and there is no default.
    """

    default_values = {
        's3-object-storage': 'fplair-eventbridge-testing',
        'apiIdConfigPath': 'api-id-config/',
        'apiSearchQueueEventPath': 'api-search-queue/',
        'apiSearchQueueResponsePath': 'api-search-response/',
        's3-to-db-mapping-dir': 's3-to-db-mapping/',
        'upload_portal_s3_mapping': 'upload_portal_s3_mapping/',
        'ai_s3_mapping': 'ai_s3_mapping/'
    }

    env_specific_values = {
        'dev': {
            'db_family': 'im547-digitalatlas-dev',
            's3Core': '2xnv-dev-im547-digitalatlas-core'
        },
        'qa': {
            'db_family': 'im547-digitalatlas-qa',
            's3Core': '2xqv-qa-im547-digitalatlas-core'
        }
    }

    env = os.getenv('ENV', 'qa')  # Default to 'dev' if 'ENV' is not set
    print(f"ENV: {env}")

    # Check if the requested variable is environment-specific
    if env_var in ['db_family', 's3Core']:
        if env in env_specific_values and env_var in env_specific_values[env]:
            return env_specific_values[env][env_var]
        else:
            raise KeyError(f"Environment variable '{env_var}' not found for environment '{env}'.")

    # Fallback to default values
    try:
        return os.environ[env_var]
    except KeyError:
        if env_var in default_values:
            return default_values[env_var]
        raise KeyError(f"Environment variable '{env_var}' not found and no default value provided.")


# Example usage:
if __name__ == "__main__":
    print(get_env('s3Core'))  # Depending on the ENV value, it will return the appropriate s3Core
    print(get_env('db_family'))  # Depending on the ENV value, it will return the appropriate db_family
    print(get_env('s3-object-storage'))  # Will return the default value