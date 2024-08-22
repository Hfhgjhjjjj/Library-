CC = gcc
CFLAGS = -Wall -g
LIBRARY = libdata_processing.a
SRC = data_processing.c
OBJ = $(SRC:.c=.o)

all: $(LIBRARY)

$(LIBRARY): $(OBJ)
    ar rcs $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $<

clean:
    rm -f $(OBJ) $(LIBRARY)
