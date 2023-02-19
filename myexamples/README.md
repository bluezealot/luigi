# Start luigi server command
``luigid``

# Access to luigi server
``http://localhost:8082/``

# Start run config testing task
``PYTHONPATH='.' luigi --module DispatchTask DispatchTask``
``PYTHONPATH='.' luigi --module DispatchTaskWrapper DispatchTaskWrapper``