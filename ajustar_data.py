def ajustar_data_lancar(data):
    data_formatada = data.split('-')
    data_formatada = data_formatada[-1] + data_formatada[1] + data_formatada[0]
    return data_formatada