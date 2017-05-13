1. Cache.py 
	This is a main configuration file where you will declare which “Algorithm” to use at all cache levels to evaluate the performance.
	
	tags = Param.BaseTags(LRU(),​ "Tag store (replacement policy)")
	
	In order to run with different algorithm change the LRU() tag with =
		a. Fifo() – for Fifo.
		b. RandomRepl() – for random replacement
		c. LRU () – for least recently used
	Path – cd gem5/build/X86/mem/cache/Cache.py

2. base.cc
	This is a file which contains reference to all header files of Algorithms used.
	In base.cc file add below line –
	
		#include "mem/cache/tags/<algorithm_file_name>.hh"
		#include "mem/cache/tags/lru.hh"
		#include "mem/cache/tags/fifo.hh"
		#include "mem/cache/tags/random_repl.hh"
	Path: cd gem5/build/X86/mem/cache/base.cc

3. cache_level.py
	This file contains the main parameters like associativity, size etc. Here you can change associativity with assoc=8, change the cache size with size=”256kB” etc. 
	This file is referenced by three-level-cache.py in order to check how many caches and what kind of parameters are used for the given program.

4. three-level-cache.py
	This file contains the python code to run the gem5 with 3 level caches simulation.
	Path - cd gem5/configs/learning-gem5/part1/three-level-cache.py

5. two-level.py
	This file contains the python code to run the gem5 with 2 level caches. Path is same as three level.