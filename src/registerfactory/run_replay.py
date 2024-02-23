from replay_factory import ReplayExecutorFactory
# need to import executor in order to register it
from apps.replay_local import LocalReplayExecutor
from apps.replay_remote import RemoteReplayExecutor

def run():

    # Creates a local executor
    local = ReplayExecutorFactory.create_replay_executor('local')
    local_out = local.run('ls -latr')
    print(local_out)

    remote = ReplayExecutorFactory.create_replay_executor('remote')
    remote_out = remote.run('ls -l')
    print(remote_out)
    remote.download("database")

    remote.transform("XYZ")


if __name__ == '__main__':
    run()