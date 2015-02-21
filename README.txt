This is a terse (but not efficient) definiton of the Geometric Algebra, in the smallest possible code
It makes no reference whatsoever to dot or wedge product, or the zoo of blades.

This is a multiplication system where the input types and values determine the input types.
It is an extension of complex numbers into arbitrary dimensions.
This implementation supports 30 dimensions (though in practice, it runs in O( 2^(2d) ) time(!)

A practical use is definitely for 3D space.
More work will need to be done to support unusual geometries like 5D conformal geometry, which is used for doing
simplified work in 3D space.

Note:

 - Indexing is done by bits.  Bit-count determines which blade a value is a member of.
 - e000 is the scalar basis.  e0, e00, e000, etc are all equivalent.  e01 == e001, etc.
 - The indexing for these vectors is in *binary*, not in decimal.
 - The blade numbers are in decimal.  ie:  a = (a_0 + a_1 + a_2 + a_3)
 - a_1 for 3D expands to:  a001 e001 + a010 e010 + a100 e100
 - The basis vectors e do NOT commute in general.
 - The same index for an e results in just 1.  ie:
   * a e001 e010 e100 e010 
   * -a e001 e010 e010 e100 (1 swap) 
   * -a e001 e100
   * -a e101 
 - Bit ordering is not a common explanation for GA, but using it is the key breakthrough here
 - For a vector space, all vectors are the e strings with 1 bit set, like:
   * e00001, e0010, e0100, e100
 - For a scalar, it's just the space with 0 bits set, of which there can be only one:
   * e0000
 - For a bivector, it is all combinations with 2 bits set:
   * e0011, e0101, e0110, e1001, e1010, e1100

The two key things are 
  * just to have multivectors be arrays of length 2^(1<<d) for whatever dimension is supported.
  * use bit addressing to find the elements
  * use a function that counts bitswaps (currently horribly inefficient) to find sign

For cases where the dimensions are not orthogonal, the function that determines i and multiplier will differ.
But the distribution of multiplication over addition, and commuting of scalars with basis vectors fixes everything except for that function returning (i, multiplier)
