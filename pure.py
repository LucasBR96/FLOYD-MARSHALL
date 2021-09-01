import numpy
import sys
from itertools import product, permutations

def get_k_costs( V , E ):
    
    idx = list( V )
    n = len( V )
    M = numpy.ones( ( n + 1 , n , n ) )

    seq = product( range( n ) , repeat = 2 )
    for i , j in seq:
        tup = ( idx[ i ] , idx[ j ] )
        M[ 0 , i , j ] = E.get( tup , sys.maxsize )

    for k in range( n ):
        
        D = numpy.zeros( ( 2 , n , n ) )
        D[ 0 ] = M[ k ]

        a = M[ k , : , k ].reshape( n , 1 )
        b = M[ k , k , : ].reshape( 1 , n )
        D[ 1 ] = a + b

        M[ k + 1 ] = D.min( axis = 0 , keepdims = False )

    return idx , M
        
def warshall_costs( V , E ):

    idx , M = get_k_costs( V , E )
    n = len( idx )
    M = M[ n ]
    
    A = dict()
    seq = permutations( range( n ) , repeat = 2 )
    for i , j in seq:
        if M[ i , j ] == sys.maxsize:
            continue

        tup = ( idx[ i ] , idx[ j ] )
        A[ tup ] = M[ i , j ]
    return A

def get_k_paths( V , E ):

    idx , M = get_k_costs( V , E )
    n = len( idx )
    
    P = -1*numpy.ones( ( n + 1 , n , n ) )
    seq = product( range( n ) , repeat = 2 )
    for i , j in seq:
        tup = ( idx[ i ] , idx[ j ] )
        if tup in E:
            P[ 0 , i , j ] = i

    #--------------------------------------------------
    # Não vetorizada
    for k in range( n ):
        for i , j in seq:

            a = M[ k , i , j ]
            b = M[ k , i , k ] + M[ k , k , j ]

            P[ k + 1 , i , j ] = P[ k , i , j ]
            if a > b:
                P[ k + 1 , i , j ] = P[ k , k , j ]
    #--------------------------------------------------
    # falta vetorizar
    
    return idx , P

def warshall_paths( V , E )

    idx , P = get_k_paths( V , E )
    n = len( idx )   
    seq = product( range( n ) , repeat = 2 )

    P = P[ n ]
    s_seq = set( seq )
    A = dict()
    while s_seq:

        start , end = s_seq.pop()
        if P[ start , end ] == -1: continue

        path = [ ]
        while start != end:
            path.append( end )
            end = P[ start , end ]
        else:
            path.append( start )
            path.reverse()

        path = list( map ( lambda x: idx[ x ] , path ) )


