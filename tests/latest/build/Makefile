#
# @brief   latest
# @version 1.1.2
# @date    2023-12-29 23:16:20.256592
# @company None, free software to use 2023
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

CC=g++
RM=rm

include ccflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=latest

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@ `pkg-config gtkmm-3.0 --libs`

.cc.o:
	$(CC) $(CFLAGS) $< -o $@ `pkg-config gtkmm-3.0 --cflags`

clean:
	$(RM) -rf *.o $(EXECUTABLE)
