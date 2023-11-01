```dataviewjs
//Min Number of link before showing up
const InterestLevel = 0 ; 

//"hash" the missing links to find similar one (uppercase, space) could use some lemmatization.
//const hashMissingLink = ( x ) => x.toUpperCase()
const hashMissingLink = ( x ) => x.toUpperCase().replace(/[\s/\\]+/,"")

const r = 
Object.entries(dv.app.metadataCache.unresolvedLinks) 
	.filter( ( [k,v] )=> Object.keys( v ).length ) 
	.flatMap( ( [k,v] ) => 
      Object.keys( v ).map(x => 
              ({ key: hashMissingLink( x ) 
               , originalLink : dv.fileLink( x )
               , source: `- ${ dv.fileLink( k ) }`
               , source_and_originalLink: `- ${dv.fileLink( k )} (${dv.fileLink( x )})`
               })
        ))  
  .sort( (a,b) => dv.compare( a.key, b.key ) )

dv.list(
   dv.array( r )
      .groupBy( t => t.key )
      .where( t => t.rows.length > InterestLevel  )
      .sort( t => t.rows.length , "desc")
      .map( t => t.rows[0].originalLink + " ("+t.rows.source.length+"): \n" + t.rows.source_and_originalLink.join("\n") + "" )
)
```
