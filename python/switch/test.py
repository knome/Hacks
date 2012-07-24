
# example usage of the evil python switch statement

from switch import switch

print "FIRST TEST :: Skip entries, fallthrough and escape"
with switch( 27 ) as case:
    
    if case( 1, 5, 20, 40 ):
        print "ALPHA CASE SKIPPED"
        
    if case( case.range( 1, 20 ) ):
        print "BETA CASE SKIPPED"
        
    if case( 2 ):
        print "CHARLIE CASE SKIPPED"
        
    if case( 0, 15, 27, 30 ):
        print "DELTA CASE TAKEN"
        case.fallthrough()
        
    if case( case.range( 40, 60 ) ):
        print "EPSILON FALLTHROUGH"
        case.fallthrough()
        
    if case( 0 ):
        print "FOXTROT FALLTHROUGH"
        case.fallthrough()
        
    if case( 45 ):
        print "GULF FALLTHROUGH AND ESCAPE"
        case.escape()
        
    if case():
        print "DEFAULT CASE SKIPPED"
print


print "SECOND TEST :: Escape from outer case"
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


print "THIRD TEST :: Fallthrough by default"
with switch( 7, fallthrough = True ) as case:
    
    if case( 7 ):
        print "ALPHA CASE WITH DEFAULT FALLTHROUGH"
        
    if case( 10 ):
        print "BETA CASE WITH DEFAULT FALLTHROUGH"
        
    if case( 14 ):
        print "CHARLIE CASE ESCAPING"
        case.escape()
        
    if case( 23 ):
        print "UNREACHABLE"
print


print "FOURTH TEST :: Escape by default"
with switch( 7 ) as case:
    
    if case( 7 ):
        print "ALPHA CASE WITH MANUAL FALLTHROUGH"
        case.fallthrough()
        
    if case( 10 ):
        print "BETA CASE WITH DEFAULT ESCAPE"
        
    if case( 14 ):
        print "UNREACHED CHARLIE CASE ESCAPING"
        case.escape()
        
    if case( 23 ):
        print "UNREACHABLE"
print
