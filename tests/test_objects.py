"""
Test functions used to create k8s objects
"""
from kubespawner.objects import make_pod_spec, make_pvc_spec


def test_make_simplest_pod():
    """
    Test specification of the simplest possible pod specification
    """
    assert make_pod_spec(
        name='test',
        image_spec='jupyter/singleuser:latest',
        env={},
        volumes=[],
        volume_mounts=[],
        cpu_limit=None,
        cpu_guarantee=None,
        mem_limit=None,
        mem_guarantee=None,
        run_as_uid=None,
        fs_gid=None,
        image_pull_policy='IfNotPresent',
        node_selector=None,
    ) == {
        "metadata": {
            "name": "test"
        },
        "spec": {
            "securityContext": {},
            "containers": [
                {
                    "env": [],
                    "name": "notebook",
                    "image": "jupyter/singleuser:latest",
                    "imagePullPolicy": "IfNotPresent",
                    "ports": [{
                        "containerPort": 8888
                    }],
                    "volumeMounts": [],
                    "resources": {
                        "limits": {
                            "cpu": None,
                            "memory": None
                        },
                        "requests": {
                            "cpu": None,
                            "memory": None
                        }
                    }
                }
            ],
            "volumes": []
        },
        "kind": "Pod",
        "apiVersion": "v1"
    }

def test_set_pod_uid_fs_gid():
    """
    Test specification of the simplest possible pod specification
    """
    assert make_pod_spec(
        name='test',
        image_spec='jupyter/singleuser:latest',
        env={},
        volumes=[],
        volume_mounts=[],
        cpu_limit=None,
        cpu_guarantee=None,
        mem_limit=None,
        mem_guarantee=None,
        run_as_uid=1000,
        fs_gid=1000,
        image_pull_policy='IfNotPresent',
        node_selector=None,
    ) == {
        "metadata": {
            "name": "test"
        },
        "spec": {
            "securityContext": {
                "runAsUser": 1000,
                "fsGroup": 1000
            },
            "containers": [
                {
                    "env": [],
                    "name": "notebook",
                    "image": "jupyter/singleuser:latest",
                    "imagePullPolicy": "IfNotPresent",
                    "ports": [{
                        "containerPort": 8888
                    }],
                    "volumeMounts": [],
                    "resources": {
                        "limits": {
                            "cpu": None,
                            "memory": None
                        },
                        "requests": {
                            "cpu": None,
                            "memory": None
                        }
                    }
                }
            ],
            "volumes": []
        },
        "kind": "Pod",
        "apiVersion": "v1"
    }


def test_make_pod_resources_all():
    """
    Test specifying all possible resource limits & guarantees
    """
    assert make_pod_spec(
        name='test',
        image_spec='jupyter/singleuser:latest',
        env={},
        volumes=[],
        volume_mounts=[],
        cpu_limit=2,
        cpu_guarantee=1,
        mem_limit='1Gi',
        mem_guarantee='512Mi',
        image_pull_policy='IfNotPresent',
        run_as_uid=None,
        fs_gid=None,
        node_selector=None,
    ) == {
        "metadata": {
            "name": "test"
        },
        "spec": {
            "securityContext": {},
            "containers": [
                {
                    "env": [],
                    "name": "notebook",
                    "image": "jupyter/singleuser:latest",
                    "imagePullPolicy": "IfNotPresent",
                    "ports": [{
                        "containerPort": 8888
                    }],
                    "volumeMounts": [],
                    "resources": {
                        "limits": {
                            "cpu": 2,
                            "memory": '1Gi'
                        },
                        "requests": {
                            "cpu": 1,
                            "memory": '512Mi'
                        }
                    }
                }
            ],
            "volumes": []
        },
        "kind": "Pod",
        "apiVersion": "v1"
    }


def test_make_pod_with_env():
    """
    Test specification of a pod with custom environment variables
    """
    assert make_pod_spec(
        name='test',
        image_spec='jupyter/singleuser:latest',
        env={
            'TEST_KEY': 'TEST_VALUE'
        },
        volumes=[],
        volume_mounts=[],
        cpu_limit=None,
        cpu_guarantee=None,
        mem_limit=None,
        mem_guarantee=None,
        image_pull_policy='IfNotPresent',
        run_as_uid=None,
        fs_gid=None,
        node_selector=None,
    ) == {
        "metadata": {
            "name": "test"
        },
        "spec": {
            "securityContext": {},
            "containers": [
                {
                    "env": [{'name': 'TEST_KEY', 'value': 'TEST_VALUE'}],
                    "name": "notebook",
                    "image": "jupyter/singleuser:latest",
                    "imagePullPolicy": "IfNotPresent",
                    "ports": [{
                        "containerPort": 8888
                    }],
                    "volumeMounts": [],
                    "resources": {
                        "limits": {
                            "cpu": None,
                            "memory": None
                        },
                        "requests": {
                            "cpu": None,
                            "memory": None
                        }
                    }
                }
            ],
            "volumes": []
        },
        "kind": "Pod",
        "apiVersion": "v1"
    }

def test_make_pod_with_node_selector():
    """
    Test specification of a pod with a node selector
    """
    assert make_pod_spec(
        name='test',
        image_spec='jupyter/singleuser:latest',
        env={},
        volumes=[],
        volume_mounts=[],
        cpu_limit=None,
        cpu_guarantee=None,
        mem_limit=None,
        mem_guarantee=None,
        run_as_uid=None,
        fs_gid=None,
        image_pull_policy='IfNotPresent',
        node_selector={'disktype': 'ssd'},
    ) == {
        "metadata": {
            "name": "test"
        },
        "spec": {
            "securityContext": {},
            "containers": [
                {
                    "env": [],
                    "name": "notebook",
                    "image": "jupyter/singleuser:latest",
                    "imagePullPolicy": "IfNotPresent",
                    "ports": [{
                        "containerPort": 8888
                    }],
                    "volumeMounts": [],
                    "resources": {
                        "limits": {
                            "cpu": None,
                            "memory": None
                        },
                        "requests": {
                            "cpu": None,
                            "memory": None
                        }
                    }
                }
            ],
            "nodeSelector": {
                "disktype": "ssd"
            },
            "volumes": []
        },
        "kind": "Pod",
        "apiVersion": "v1"
    }

def test_make_pvc_simple():
    """
    Test specification of the simplest possible pvc specification
    """
    assert make_pvc_spec(
        name='test',
        storage_class='',
        access_modes=[],
        storage=None
    ) == {
        'kind': 'PersistentVolumeClaim',
        'apiVersion': 'v1',
        'metadata': {
            'name': 'test',
            'annotations': {
                'volume.beta.kubernetes.io/storage-class': ''
            }
        },
        'spec': {
            'accessModes': [],
            'resources': {
                'requests': {
                    'storage': None
                }
            }
        }
    }


def test_make_resources_all():
    """
    Test specifying all possible resource limits & guarantees
    """
    assert make_pvc_spec(
        name='test',
        storage_class='gce-standard-storage',
        access_modes=['ReadWriteOnce'],
        storage='10Gi'
    ) == {
        'kind': 'PersistentVolumeClaim',
        'apiVersion': 'v1',
        'metadata': {
            'name': 'test',
            'annotations': {
                'volume.beta.kubernetes.io/storage-class': 'gce-standard-storage'
            }
        },
        'spec': {
            'accessModes': ['ReadWriteOnce'],
            'resources': {
                'requests': {
                    'storage': '10Gi'
                }
            }
        }
    }

