
# example usage of the evil python switch statement

from switch import switch

print "FIRST TEST"
with switch( 27 ) as case:
    
    if case( 1, 5, 20, 40 ):
        print "ALPHA CASE SKIPPED"
        
    if case( case.range( 1, 20 ) ):
        print "BETA CASE SKIPPED"
        
    if case( 2 ):
        print "CHARLIE CASE SKIPPED"
        
    if case( 0, 15, 27, 30 ):
        print "DELTA CASE TAKEN"
        
    if case( case.range( 40, 60 ) ):
        print "EPSILON FALLTHROUGH"
        
    if case( 0 ):
        print "FOXTROT FALLTHROUGH"
        
    if case( 45 ):
        print "GULF FALLTHROUGH AND ESCAPE"
        case.escape()
        
    if case():
        print "DEFAULT CASE SKIPPED"
print

print "SECOND TEST"
with switch( "hello" ) as hello_case:
    
    if hello_case( "hello" ):
        
        with switch( "world" ) as world_case:
            
            if world_case( "something" ):
                print "CASE SOMETHING SKIPPED"
                
            if world_case( "world" ):
                print "WORLD CASE TAKEN AND ESCAPE FROM HELLO"
                hello_case.escape()
                
            if world_case():
                print "DEFAULT CASE SKIPPED"
                
    if hello_case():
        print "DEFAULT CASE SKIPPED"
print
