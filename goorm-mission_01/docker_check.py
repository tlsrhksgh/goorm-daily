import docker

def get_containers():
        client = docker.from_env()
        return client.containers.list(all=True)

def get_container_info(container):
    stats = {
        'id': container.id,
        'name': container.name,
        'status': container.status,
        'uptime': container.attrs['State']['StartedAt']
    }

    return stats

def check_error_container() -> dict:
    for container in get_containers():
        container_info = get_container_info(container)
        if container_info['status'] != 'running':
            return container_info

    return None