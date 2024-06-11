#
# @brief   full_simple
# @version 1.1.3
# @date    2024-06-11 19:14:09.582669
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

CC=g++
RM=rm

include ccflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=full_simple

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@ `pkg-config gtkmm-3.0 --libs`

.cc.o:
	$(CC) $(CFLAGS) $< -o $@ `pkg-config gtkmm-3.0 --cflags`

clean:
	$(RM) -rf *.o $(EXECUTABLE)
