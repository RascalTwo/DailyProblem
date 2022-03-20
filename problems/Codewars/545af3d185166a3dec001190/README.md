[_metadata_:generated]: - "true"

# Enumerable Magic #20 - Cascading Subsets

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`545af3d185166a3dec001190`](https://www.codewars.com/kata/545af3d185166a3dec001190) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

Create a method **each_cons** that accepts a list and a number **n**, and returns cascading subsets of the list of size **n**, like so:

    each_cons([1,2,3,4], 2)
      #=> [[1,2], [2,3], [3,4]]
    
    each_cons([1,2,3,4], 3)
      #=> [[1,2,3],[2,3,4]]
      
As you can see, the lists are cascading; ie, they overlap, but never out of order.
