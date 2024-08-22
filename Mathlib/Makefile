CC = gcc
CFLAGS = -Wall -fPIC

all: libmymath.a test_program

libmymath.a: mymath.o
mymath.ar rcs libmymath.a mymath.o

mymath.o: mymath.c mymath.h
mymath.$(CC) $(CFLAGS) -c mymath.c

test_program: main.o libmymath.a
mymath.$(CC) -o test_program main.o -L. -lmymath

main.o: main.c mymath.h
mymath.$(CC) $(CFLAGS) -c main.c

clean:
mymath.rm -f *.o *.a test_program
