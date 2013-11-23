#!/usr/bin/env python 

import sys

def hapax_legomenon(filename):
    try: 
        f = open(filename)
	content = f.read().lower()
        #print content
        #print 
	lst_content = content.split()	
	set_content = list(set(lst_content))
	hapax_leg = []
	for el in set_content:
 	    num = lst_content.count(el)
	    if num == 1:
	        hapax_leg.append(el)
	    else:
	        pass
        #print hapax_leg
	del lst_content[:]
	del set_content[:]
	del lst_content
	del set_content
	return hapax_leg
    except:
        return -1



if __name__ == "__main__":
 
    if len(sys.argv) < 2 or  len(sys.argv) > 2:
        print 
	print " python hapax_legomenon filename"
	print " file name according to you"
	print 
	sys.exit(-1)

    else:
        hapax_leg = hapax_legomenon(sys.argv[1])
	if hapax_leg == -1:
	    print 
	    print "  file name is not valid"
	    print " python hapax_legemenon filename"
	    print " file name according to you"
	    print 

	    sys.exit(-1)
        
	else:
            print 
	    print " hapax Legomemon are: "
	    print 
	    print ", ".join(hapax_leg)
	    del hapax_leg[:]
	    del hapax_leg
	    sys.exit(0)        

