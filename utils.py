def calculate_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def smooth_move(prev_x, prev_y, target_x, target_y, factor=0.2):
    # Exponential moving average
    smooth_x = (1 - factor) * prev_x + factor * target_x
    smooth_y = (1 - factor) * prev_y + factor * target_y
    return smooth_x, smooth_y
