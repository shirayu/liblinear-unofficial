This is an official repository of LIBLINEAR by Yuta Hayashibe (shirayu).


I added following script. (Their license is GPL3).

- ``setup.py``
- ``VERSION``
- ``python/__init__.py``

You can **install** LIBLINEAR in the general way.: ``sudo python  setup.py install``

This enables us to

- add two LIBLINEAR commands: ``liblinear-predict`` and ``liblinear-train``
    - You can call these commands from anywhere. (Be aware to set ``$PATH``)
- call python libraries from python scripts to just added
    - ``import ll.liblinear``
    - ``import ll.liblinearutil``


You may copy files to the latest LIBLINEAR source folder to install the latest version.
When you do so, please change the number in the file ``VERSION``. 

Enjoy!
