# Red-ArchLinux
Comprobamos la conexión a la red usando los subprocesos
en python, simulando que ponemos en la terminal un ping a los
servidores de google y esperamos 3 segundos.

Si no hay conexión tardará menos de 3 segundos y no habrá ningún
error, pero si hay conexión , el ping se hará automaticamente hasta
los 3 segundos, que al cortarlo de manera brusca se lanzará un error
por eso mismo lo capturamos
