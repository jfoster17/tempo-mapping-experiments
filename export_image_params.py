
def index_color_template(index, color):
    return [index, int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)]

def from_to_template(from_index, from_color, to_index, to_color):
    return {'type': 'algorithmic',
            'algorithm': 'esriCIELabAlgorithm',
            'fromColor': index_color_template(from_index, from_color),
            'toColor': index_color_template(to_index, to_color)}

def gen_colorRamp(cmap, N=256):
    colorRamp = []
    linspace = list(range(N) if N == 256 else (256 * i // (N - 1) for i in range(N)))
    for i in range(N-1):
        color_i = cmap(linspace[i])
        color_j = cmap(linspace[i+1])
        colorRamp.append(from_to_template(linspace[i], color_i,linspace[i+1], color_j))
    return colorRamp


def gen_colorMap(cmap):
   return [index_color_template(i, cmap(i)) for i in range(256)]



def gen_renderingRule(cmap, cmap_N = 256, vmin = int(1e14), vmax = int(1.5e16), image_mean=159933132046326.3, image_std = 1037511280757571.9):
    renderingRule = {
    'rasterFunction': 'Colormap',
    'rasterFunctionArguments': {
        # 'Colormap': list(gen_colorMap(cmap, N = cmap_N)),
        'Raster': {
        'rasterFunctionArguments': {
            'StretchType': 5,

            'Statistics': [[vmin, # min value
                            vmax, # 150*10^14 /cm^2
                            image_mean, # mean value
                            image_std # std
                            ]],
            'DRA': False,
            'UseGamma': False,
            'Gamma': [1],
            'ComputeGamma': False
            },
        'rasterFunction': 'Stretch',
        'outputPixelType': 'U8',
        'variableName': 'Raster'
        }
        },
    'variableName': 'Raster'
    }
    
    if cmap_N == 256:
        renderingRule['rasterFunctionArguments']['Colormap'] = gen_colorMap(cmap)
    else:
        renderingRule['rasterFunctionArguments']['colorRamp'] = {'type': 'multipart', 'colorRamps':gen_colorRamp(cmap, N = cmap_N)}
    
    return renderingRule


MOSAIC_RULE = {'ascending': True,
 'mosaicMethod': 'esriMosaicCenter',
 'multidimensionalDefinition': [{'variableName': 'NO2 Troposphere',
   'values': [],
   'isSlice': False}],
 'mosaicOperation': 'MT_FIRST'}


from colormap import svs_tempo_cmap


spatial_reference = {'wkt': """
                     PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",
                        GEOGCS["GCS_WGS_1984",
                            DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],
                            PRIMEM["Greenwich",0.0],
                            UNIT["Degree",0.0174532925199433]],
                     PROJECTION["Mercator_Auxiliary_Sphere"],
                     PARAMETER["False_Easting",0.0],
                     PARAMETER["False_Northing",0.0],
                     PARAMETER["Central_Meridian",-102.39086151122439],
                     PARAMETER["Standard_Parallel_1",0.0],
                     PARAMETER["Auxiliary_Sphere_Type",0.0],
                     UNIT["Meter",1.0]]
                     """}

imageSR = spatial_reference
bboxSR = spatial_reference