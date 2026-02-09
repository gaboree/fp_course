def get_median_font_size(font_sizes):
    local_list = sorted(font_sizes)
    if font_sizes == []:
        return None
    median = 0
    nr_fonts = len(font_sizes)
    if  nr_fonts%2 == 0:
        median = local_list[nr_fonts//2 - 1]
    else:
        median = local_list[nr_fonts//2]
    return median
