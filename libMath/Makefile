CC = gcc
CFLAGS = -Wall -fPIC

all: libmymath.a

libmymath.a: mymath.o
    ar rcs libmymath.a mymath.o

mymath.o: mymath.c
    $(CC) $(CFLAGS) -c mymath.c

clean:
    rm -f *.o *.a
