"""Role testing files using testinfra."""
testinfra_hosts = ["master.osgiliath.test"]


def test_nfs_provisioner_helm_chart_created(host):
    command = """helm list --all-namespaces | \
    grep -c 'nfs-subdir'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0


def test_nfs_provisioner_pod_is_running(host):
    command = """kubectl get po -n nfs-subdir-provisioner | \
    grep nfs-subdir | \
    grep -c 'Running'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0
