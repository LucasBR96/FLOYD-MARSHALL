import numpy
import sys

def update_cost( M , k ):
    
    result = []
    n = len( M ) # square matrix

    for i in range( n ):
        seq = []
        for j in range( n ):

            m1 = M[ i ][ j ]
            m2 = M[ i ][ k ] + M[ k ][ j ]
            
            m = m1 if m1 < m2 else m2
            seq.append( m )

        result.append( seq )
    return result

def init_matrix( V , E ):
    
    idx = list( v )
    n = len( idx )
    M = [ ]

    for i in range( n ):
        u = idx[ i ]
        seq = []
        for j in range( n ):
            v = idx[ j ]
            tup = ( u , v )
            M[ i ][ j ] = E.get( tup , sys.maxsize )
    return M , idx

def fw_min_paths( V , E ):
    
    M , idx = init_matrix( V , E )
    n = len( V )

    P = [ get_subpaths( M ) ]


def fw_min_costs( V , E ):

    M , idx = init_matrix( V , E )
    n = len( V )
    for k in range( n ):
        M = update_cost( M , k )
    
    Min_val = dict()
    for i in range( n ):
        u = idx[ i ]
        for j in range( n ):
            v = idx[ j ]
            
            tup = ( u , v )
            Min_val[ tup ] = M[ u ][ v ]

def vector_update_cost( M , k ):
    
    n = M.shape[ 0 ]

    #--------------------------------------------------
    # M[ i , k ] , 0 <= i < n
    arr1 = M[ : , k ].reshape( n , 1 )

    #--------------------------------------------------
    # M[ k , j ] , 0 <= j < n
    arr2 = M[ k ].reshape( 1 , n )

    #--------------------------------------------------
    # Mat[ 0 , i , j ] = M[ i , j ]
    # Mat[ 1 , i , j ] = M[ i , k ] + M[ k , j ]
    Mat = numpy.zeros( ( 2 , n , n ) )
    Mat[ 0 ] = M
    Mat[ 1 ] = arr1 + arr2
    return Mat.min( axis = 0 , keepdims = False )
    
