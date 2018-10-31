import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_user(host):
    u = host.user('redis')

    assert u.name == 'redis'
    assert 'redis' in u.groups


def test_redis_conf_file(host):
    f = host.file('/etc/redis/6379.conf')

    assert f.exists
    assert f.user == 'redis'

    s = list(filter(lambda x: len(x) > 0, f.content_string.split('\n')))

    assert 'bind 0.0.0.0' in s
    assert 'protected-mode yes' in s
    assert 'port 6379' in s
    assert 'tcp-backlog 511' in s
    assert 'timeout 0' in s
    assert 'tcp-keepalive 300' in s
    assert 'daemonize yes' in s
    assert 'supervised no' in s
    assert 'pidfile /var/run/redis/6379.pid' in s
    assert 'loglevel notice' in s
    assert 'logfile ""' in s
    assert 'databases 16' in s
    assert 'always-show-logo yes' in s
    assert 'save 900 1' in s
    assert 'save 300 10' in s
    assert 'save 60 10000' in s
    assert 'stop-writes-on-bgsave-error yes' in s
    assert 'rdbcompression yes' in s
    assert 'rdbchecksum yes' in s
    assert 'dbfilename dump.rdb' in s
    assert 'dir ./' in s
    assert 'maxclients 10000' in s
    assert 'appendonly no' in s
    assert 'appendfilename "appendonly.aof"' in s
    assert 'appendfsync everysec' in s
    assert 'no-appendfsync-on-rewrite no' in s
    assert 'auto-aof-rewrite-percentage 100' in s
    assert 'auto-aof-rewrite-min-size 64mb' in s
    assert 'aof-load-truncated yes' in s
    assert 'aof-use-rdb-preamble yes' in s
    assert 'lua-time-limit 5000' in s
    assert 'slowlog-log-slower-than 10000' in s
    assert 'slowlog-max-len 128' in s
    assert 'latency-monitor-threshold 0' in s
    assert 'notify-keyspace-events ""' in s
    assert 'hash-max-ziplist-entries 512' in s
    assert 'hash-max-ziplist-value 64' in s
    assert 'list-max-ziplist-size -2' in s
    assert 'list-compress-depth 0' in s
    assert 'set-max-intset-entries 512' in s
    assert 'zset-max-ziplist-entries 128' in s
    assert 'zset-max-ziplist-value 64' in s
    assert 'hll-sparse-max-bytes 3000' in s
    assert 'stream-node-max-bytes 4096' in s
    assert 'stream-node-max-entries 100' in s
    assert 'activerehashing yes' in s
    assert 'client-output-buffer-limit normal 0 0 0' in s
    assert 'client-output-buffer-limit replica 256mb 64mb 60' in s
    assert 'client-output-buffer-limit pubsub 32mb 8mb 60' in s
    assert 'client-query-buffer-limit 1gb' in s
    assert 'proto-max-bulk-len 512mb' in s
    assert 'hz 10' in s
    assert 'dynamic-hz yes' in s
    assert 'aof-rewrite-incremental-fsync yes' in s
    assert 'rdb-save-incremental-fsync yes' in s
    assert 'lfu-log-factor 10' in s
    assert 'lfu-decay-time 1' in s


def test_redis_init_file(host):
    f = host.file('/etc/init.d/redis-6379')

    assert f.exists


def test_redis_service(host):
    f = host.file('/var/run/redis/6379.pid')

    assert f.exists
