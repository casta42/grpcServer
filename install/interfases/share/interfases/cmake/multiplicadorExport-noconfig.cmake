#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "interfases::multiplicador" for configuration ""
set_property(TARGET interfases::multiplicador APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(interfases::multiplicador PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libmultiplicador.so"
  IMPORTED_SONAME_NOCONFIG "libmultiplicador.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS interfases::multiplicador )
list(APPEND _IMPORT_CHECK_FILES_FOR_interfases::multiplicador "${_IMPORT_PREFIX}/lib/libmultiplicador.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
