#
# @brief   new_simple_test
# @version 1.1.4
# @date    2024-07-03 23:43:06.717714
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

CC=g++
RM=rm

include ccflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=new_simple_test

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@ `pkg-config gtkmm-3.0 --libs`

.cc.o:
	$(CC) $(CFLAGS) $< -o $@ `pkg-config gtkmm-3.0 --cflags`

clean:
	$(RM) -rf *.o $(EXECUTABLE)
