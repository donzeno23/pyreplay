import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

logger = logging.getLogger(__name__)

from collections.abc import Callable
from registerfactory.replay_base import ReplayExecutorBase

class ReplayExecutorFactory:
    """ The factory class for creating executors """

    # Keep an internal registry that maps name of the 
    # replay executor to the class itself
    registry = {}
    """ Internal registory for available executors """
    

    # We register new executors using Python decorators: which is a feature
    # that allows us to modify the behavior of a function or a class
    # NOTE: we decorate the class iteself, such that, during class declaration
    # it is automatically registered into the ReplayExecutorFactory's internal
    # registry
    @classmethod
    def register(cls, name: str) -> Callable:
        """ Class method to register Replay Executor class to the internal registry.

        Args: 
            name (str): The name of the replay executor

        Returns:
            The Executor class itself.
        """
        print(f"classmethod:register was called, using name: {name}")

        def inner_wrapper(wrapped_class: ReplayExecutorBase) -> Callable:
            if name in cls.registry:
                logger.warning(f"Replay Executor {name} already exists.  Will replace it'")
                print(f"WARNING: Replay Executor {name} already exists.  Will replace it'")
            print(f"DEBUG: Replay Executor {name} being added to registry.")
            cls.registry[name] = wrapped_class
            return wrapped_class
        
        return inner_wrapper


    @classmethod
    def create_replay_executor(cls, name: str, **kwargs) -> 'ReplayExecutorBase':
        """ Factory command to create the executor.

        This method gets the appropriate Replay Executor class from the registry
        and creates an instance of it, while passing in the paramters
        given in ``kwargs``.

        Args:
            name (str): The name of the executor to create.

        Returns:
            An instance of the executor that is created. 
        """

        if name not in cls.registry:
            logger.warning(f'Replay Executor {name} does not exist in the registry')
            print(f"WARNING: Replay Executor {name} does not exist in the registry")
            return None

        exec_class = cls.registry[name]
        replay_executor = exec_class(**kwargs)
        return replay_executor