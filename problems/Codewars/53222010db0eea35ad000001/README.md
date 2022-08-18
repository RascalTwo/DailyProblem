[_metadata_:generated]: - "true"

# Slope of a Line

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                    |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`53222010db0eea35ad000001`](https://www.codewars.com/kata/53222010db0eea35ad000001) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js) |

<!-- INFO TABLE END -->

## Task

Your challenge is to write a function named `getSlope`/`get_slope`/`GetSlope` that calculates the slope of the line through two points.

## Input

```if:javascript,python
Each point that the function takes in is an array 2 elements long. The first number is the x coordinate and the second number is the y coordinate.
If the line through the two points is vertical or if the same point is given twice, the function should return `null`/`None`.
```


```if:c
In C, the function `get_slope` is passed two `point` structures, each consisting of two `double` coordinates: `x` and `y`.

double get_slope(point a, point b, bool *is_slope);

If the line through the two points is vertical or if the same point is given twice, set the pointer `*is_slope` to `false`.
```


```if:csharp
`GetSlope` will take in two Point objects. If the line through the two points is vertical, or the two points are the same, return `null`.

The Point object:

~~~
public class Point : System.Object
{
  public double X;
  public double Y;
  
  public Point(double x, double y)
  {
    this.X = x;
    this.Y = y;
  }
  
  public override string ToString()
  {
    return $"({this.X}, {this.Y})";
  }
  
  public override bool Equals(object point)
  {
    // Typechecking
    if (point == null || point.GetType() != this.GetType())
    {
      return false;
    }
    
    return this.ToString() == point.ToString();
  }
}
~~~



```
