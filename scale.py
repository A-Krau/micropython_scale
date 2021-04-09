def bit_map(val, init_bit = 16, scale_bit = 8):
    init_range = pow(2,init_bit)
    print(init_range)
    scale_range = pow(2,scale_bit)
    print(scale_range)
    
    val_scaler = float(val) / float(init_range)
    print(val_scaler)
    
    val_out = int(val_scaler * scale_range)
    return val_out

def scale_range(val, init_low, init_high,scale_low, scale_high):
    init_range = init_high-init_low
    scale_range = scale_high - scale_low

    scale = float(val) / float(init_range)

    val_out = scale * scale_range
    return val_out
