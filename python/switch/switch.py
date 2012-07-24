
"""
I felt like destroying something beautiful.
"""

from contextlib import contextmanager


class CaseEscape( Exception ):
    pass


class CaseRange:
    def __init__( self, start, stop ):
        self._start = start
        self._stop  = stop
        
    def __iter__( self ):
        return iter( xrange( self._start ,
                             self._stop  ) )


class Case:
    def __init__( self, value ):
        self._value   = value
        self._success = False
        return
    
    def _succeed( self ):
        self._success = True
        return True
    
    def escape( self ):
        raise CaseEscape( self )
    
    def range( self, start, stop ):
        return CaseRange( start, stop )
    
    def __call__( self, *args ):
        if self._success:
            return True
        if not args:
            return self._succeed()
        for arg in args:
            if isinstance( arg, CaseRange ):
                for cra in arg:
                    if cra == self._value:
                        return self._succeed()
            else:
                if arg == self._value:
                    return self._succeed()
        return False


@contextmanager
def switch( value ):
    case = Case( value )
    try:
        yield case
    except CaseEscape, e:
        # only capture this switch's escapes
        if e[0] == case:
            pass
        else:
            raise
