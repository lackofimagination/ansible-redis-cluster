import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('candidate')


def test_cluster_nodes(host):
    cmd = host.run('redis-cli cluster nodes')

    assert cmd.rc == 0
    assert len(cmd.stdout.split('\n')) == 6
