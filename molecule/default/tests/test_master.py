"""Role testing files using testinfra."""
testinfra_hosts = ["master.osgiliath.test"]


def test_csi_provisioner_hostname_is_created(host):
    command = """kubectl get ns | grep -c 'hostpath-provisioner'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0


def test_csi_pod_is_created(host):
    command = """kubectl get po -n hostpath-provisioner | \
    grep -c 'hostpath-provisioner-csi'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0


def test_csi_operator_pod_is_created(host):
    command = """kubectl get po -n hostpath-provisioner | \
    grep -c 'hostpath-provisioner-operator'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0
