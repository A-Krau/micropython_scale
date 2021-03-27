# micropython_scale
So far all it does it scale numbers

## bit_map(val, init_bit, scale_bit)

val: value that is to be scaled
init_bit: initial bit value that val is based on, or max of range that is to be scaled
scale_bit: scaled bit value that output is to be based on, or max of range that is output

Scales values of a range to another.

Defaults to scaling 16 bit numbers to 8 bit.

```python
def bit_map(val, init_bit = 16, scale_bit = 8):
    init_range = pow(2,init_bit)
    print(init_range)
    scale_range = pow(2,scale_bit)
    print(scale_range)
    
    val_scaler = float(val) / float(init_range)
    print(val_scaler)
    
    val_out = int(val_scaler * scale_range)
    return val_out
```
