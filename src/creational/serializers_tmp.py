'''
A General Purpose Object Factory
The implementation of SerializerFactory is a huge improvement 
from the original example. It provides great flexibility to 
support new formats and avoids modifying existing code.

Still, the current implementation is specifically targeted 
to the serialization problem above, and it is not reusable 
in other contexts.

Factory Method can be used to solve a wide range of problems. 
An Object Factory gives additional flexibility to the design 
when requirements change. Ideally, you’ll want an implementation 
of Object Factory that can be reused in any situation without 
replicating the implementation.

There are some challenges to providing a general purpose 
implementation of Object Factory, and in the following sections 
you will look at those challenges and implement a solution that 
can be reused in any situation.
'''

