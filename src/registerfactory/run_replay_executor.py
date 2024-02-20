import click
import json
import pprint

# from replay_local import LocalReplayExecutor
# from replay_remote import RemoteReplayExecutor
from replay_factory import ReplayExecutorFactory

'''
@click.group(<name>) creates a command that instantiates a group class
a group is intended to be a set of related commands
@click.argument(<argument name>) tells us that we will be passing an argument
and referring to that argument in the function by the name we pass it
@click.pass_context tells the group command that we're going to be using
the context, the context is not visible to the command unless we pass this

In our example we'll name our group "replay"
'''

def start(app):
    print(f"Starting replay for application: {app}")
    pass

@click.group("replay")
@click.pass_context
@click.argument("application")
def replay(ctx, application):
    """ An example CLI for replaying an application """
    # _stream = open(application)
    # _dict = json.load(_stream)
    # _stream.close()
    # ctx.obj = _dict
    _run = start(application)

@replay.command('check_context_object')
@click.pass_context
def check_context(ctx):
    pprint.pprint(type(ctx.obj))


@replay.command('run')
# @click.option('--rtype', default='local', help='type of replay to run')
@click.pass_context
def run(ctx):
    """ An example CLI for running replay """

    click.echo('Running replay...')

    ## run_type = ctx.obj['run_type']
    run_type = 'local'
    if run_type == 'local':
        print("Run type is local!!!")
        # replay_executor = LocalReplayExecutor()
        # stdout, _ = replay_executor.run('ls -latr')
        # print(stdout)
        # Create a local replay executor
        local = ReplayExecutorFactory.create_replay_executor('local')
        local_out = local.run('ls -latr')
        print(local_out)
    elif run_type == 'remote':
        # replay_executor = RemoteReplayExecutor()
        pass
    else:
        print(f"Replay Executor {run_type} is invalid!")


# EXAMPLE USAGE: python3 run_replay_executor.py ENGINE1 run
def main():
    replay(prog_name="replay")


if __name__ == '__main__':
    main()