This is an official repository of LIBLINEAR by Yuta Hayashibe (shirayu).


I added following scripts. (Their licenses are the modified BSD license).

- ``setup.py``
- ``VERSION``
- ``MANIFEST.in``
- ``python/__init__.py``

You can **install** LIBLINEAR in the general way.: ``sudo python  setup.py install``

This enables us to

- add two LIBLINEAR commands: ``liblinear-predict`` and ``liblinear-train``
    - You can call these commands from anywhere. (Be aware to set ``$PATH``)
- call python libraries from python scripts to just added
    - ``import ll.liblinear``
    - ``import ll.liblinearutil``


You may copy files to [the latest LIBLINEAR](http://www.csie.ntu.edu.tw/~cjlin/liblinear/) source folder to install the latest version.
When you do so, please change the number in the file ``VERSION``. 

Enjoy!
