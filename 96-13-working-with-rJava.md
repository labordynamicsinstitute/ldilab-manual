(working-with-rJava)=
# Working with rJava

Below you will find details of a rJava error and how it was resolved.

## rJava Error

```
Error: Error installing package 'rJava': 
=================================
* installing *source* package 'rJava' ...
** package 'rJava' successfully unpacked and MD5 sums checked
** using staged installation
Generate Windows-specific files (src/jvm-w32) ...
make: Entering directory '/c/.../Temp/RtmpUVjaDY/renv-package-new-13b84f6a7cd0/rJava/src/jvm-w32'
dlltool --as as  --input-def jvm64.def --kill-at --dllname jvm.dll --output-lib libjvm.dll.a
gcc  -O2 -c -o findjava.o findjava.c
gcc  -s -o findjava.exe findjava.o
make: Leaving directory '/c.../Temp/RtmpUVjaDY/renv-package-new-13b84f6a7cd0/rJava/src/jvm-w32'
Find Java...
ERROR*> JavaSoft\{JRE|JDK} can't open registry keys.
ERROR: cannot find Java Development Kit.
  Please set JAVA_HOME to specify its location manually
ERROR: configuration failed for package 'rJava'
* removing 'L:/Workspace/aearep-XXXX/123456/renv/library/windows/R-4.4/x86_64-w64-mingw32/.renv/1/rJava'
install of package 'rJava' failed [error code 1]
```

## Potential Resolutions

At the beginning of the R script, place the following:

```
Sys.setenv(JAVA_HOME='L:\\common\\azulJava\\jdk\\jre')
install.packages("rJava")
library(rJava)
```

If that doesn't work, try:

```
Sys.setenv(JAVA_HOME = "L:/common/azulJava/jdk")
install.packages("rJava")
library(rJava)
```


