# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/carbon/Documents/interfases_hw1/src/interfases

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/carbon/Documents/interfases_hw1/build/interfases

# Include any dependencies generated for this target.
include CMakeFiles/multiplicador.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/multiplicador.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/multiplicador.dir/flags.make

CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o: CMakeFiles/multiplicador.dir/flags.make
CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o: /home/carbon/Documents/interfases_hw1/src/interfases/src/multiplicador.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/carbon/Documents/interfases_hw1/build/interfases/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o -c /home/carbon/Documents/interfases_hw1/src/interfases/src/multiplicador.cpp

CMakeFiles/multiplicador.dir/src/multiplicador.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/multiplicador.dir/src/multiplicador.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/carbon/Documents/interfases_hw1/src/interfases/src/multiplicador.cpp > CMakeFiles/multiplicador.dir/src/multiplicador.cpp.i

CMakeFiles/multiplicador.dir/src/multiplicador.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/multiplicador.dir/src/multiplicador.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/carbon/Documents/interfases_hw1/src/interfases/src/multiplicador.cpp -o CMakeFiles/multiplicador.dir/src/multiplicador.cpp.s

# Object files for target multiplicador
multiplicador_OBJECTS = \
"CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o"

# External object files for target multiplicador
multiplicador_EXTERNAL_OBJECTS =

libmultiplicador.so: CMakeFiles/multiplicador.dir/src/multiplicador.cpp.o
libmultiplicador.so: CMakeFiles/multiplicador.dir/build.make
libmultiplicador.so: CMakeFiles/multiplicador.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/carbon/Documents/interfases_hw1/build/interfases/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libmultiplicador.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/multiplicador.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/multiplicador.dir/build: libmultiplicador.so

.PHONY : CMakeFiles/multiplicador.dir/build

CMakeFiles/multiplicador.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/multiplicador.dir/cmake_clean.cmake
.PHONY : CMakeFiles/multiplicador.dir/clean

CMakeFiles/multiplicador.dir/depend:
	cd /home/carbon/Documents/interfases_hw1/build/interfases && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/carbon/Documents/interfases_hw1/src/interfases /home/carbon/Documents/interfases_hw1/src/interfases /home/carbon/Documents/interfases_hw1/build/interfases /home/carbon/Documents/interfases_hw1/build/interfases /home/carbon/Documents/interfases_hw1/build/interfases/CMakeFiles/multiplicador.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/multiplicador.dir/depend

