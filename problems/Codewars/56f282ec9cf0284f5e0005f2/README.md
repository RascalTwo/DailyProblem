[_metadata_:generated]: - "true"

# Incorrect array_remove method

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                  |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`56f282ec9cf0284f5e0005f2`](https://www.codewars.com/kata/56f282ec9cf0284f5e0005f2) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

You come across a method for removing all odd numbers from an array
#removing all odd numbers from an array
```
def remove_odd_numbers_from_array(a)
  a.each do |x|
	  if x%2!=0
		  a.delete x
	  end
  end
  return a
end
```
<br>
This method does not work as expected. Can you correct it
