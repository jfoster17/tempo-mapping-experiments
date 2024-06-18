
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm

r = [0.231373,0.227451,0.223529,0.215686,0.211765,0.211765,0.207843,0.207843,0.211765,0.211765,0.219608,0.227451,0.235294,0.247059,0.258824,0.270588,0.286275,0.298039,0.317647,0.329412,0.345098,0.364706,0.376471,0.396078,0.411765,0.427451,0.450980,0.466667,0.486275,0.501961,0.521569,0.541176,0.556863,0.580392,0.596078,0.615686,0.635294,0.650980,0.674510,0.690196,0.705882,0.725490,0.741176,0.760784,0.772549,0.788235,0.803922,0.819608,0.835294,0.847059,0.858824,0.874510,0.886275,0.898039,0.905882,0.917647,0.925490,0.933333,0.945098,0.949020,0.956863,0.964706,0.968627,0.972549,0.976471,0.980392,0.984314,0.988235,0.992157,0.992157,0.996078,0.996078,0.996078,1.00000,1.00000,1.00000,1.00000,1.00000,1.00000,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.996078,0.992157,0.992157,0.992157,0.988235,0.988235,0.984314,0.980392,0.976471,0.972549,0.964706,0.960784,0.952941,0.949020,0.941176,0.937255,0.929412,0.925490,0.917647,0.909804,0.905882,0.898039,0.890196,0.882353,0.874510,0.870588,0.858824,0.850980,0.847059,0.835294,0.827451,0.819608,0.811765,0.803922,0.792157,0.784314,0.772549,0.764706,0.756863,0.745098,0.737255,0.725490,0.713726,0.705882,0.694118,0.686275,0.674510,0.662745,0.654902,0.639216,0.631373,0.619608,0.607843,0.600000,0.584314,0.576471,0.564706,0.552941,0.541176,0.529412,0.521569,0.509804,0.501961,0.490196,0.478431,0.470588,0.462745,0.450980,0.443137,0.435294,0.427451,0.415686,0.407843,0.400000,0.388235,0.380392,0.372549,0.364706,0.356863,0.345098,0.337255,0.329412,0.321569,0.313726,0.301961,0.294118,0.286275,0.278431,0.266667,0.258824,0.250980,0.239216,0.231373,0.223529,0.215686,0.207843,0.196078,0.188235,0.180392,0.172549,0.164706,0.156863,0.149020,0.145098,0.137255,0.133333,0.125490,0.121569,0.117647,0.113725,0.109804,0.105882,0.101961,0.101961,0.0980392,0.0941176,0.0941176,0.0901961,0.0901961,0.0862745,0.0823529,0.0823529,0.0784314,0.0745098,0.0745098,0.0705882,0.0666667,0.0666667,0.0627451,0.0627451,0.0588235,0.0549020,0.0549020,0.0509804,0.0509804,0.0470588,0.0431373,0.0431373,0.0392157,0.0392157,0.0352941,0.0313726,0.0313726,0.0313726,0.0274510,0.0274510]
g = [ 0.462745,0.470588,0.474510,0.486275,0.494118,0.501961,0.517647,0.529412,0.541176,0.552941,0.564706,0.580392,0.592157,0.607843,0.623529,0.635294,0.650980,0.662745,0.674510,0.686275,0.698039,0.709804,0.721569,0.733333,0.741176,0.752941,0.760784,0.768627,0.780392,0.788235,0.792157,0.800000,0.807843,0.815686,0.823529,0.827451,0.835294,0.839216,0.847059,0.854902,0.858824,0.866667,0.870588,0.878431,0.882353,0.886275,0.894118,0.901961,0.905882,0.913725,0.917647,0.925490,0.929412,0.937255,0.941176,0.945098,0.952941,0.956863,0.960784,0.964706,0.968627,0.972549,0.976471,0.976471,0.980392,0.980392,0.980392,0.980392,0.976471,0.976471,0.972549,0.968627,0.964706,0.960784,0.952941,0.949020,0.941176,0.937255,0.929412,0.921569,0.913725,0.905882,0.898039,0.890196,0.878431,0.870588,0.862745,0.850980,0.843137,0.831373,0.823529,0.811765,0.803922,0.792157,0.780392,0.772549,0.756863,0.749020,0.733333,0.721569,0.709804,0.698039,0.686275,0.670588,0.654902,0.643137,0.627451,0.615686,0.600000,0.584314,0.572549,0.556863,0.545098,0.529412,0.517647,0.505882,0.494118,0.482353,0.466667,0.458824,0.447059,0.435294,0.427451,0.415686,0.407843,0.396078,0.388235,0.376471,0.368627,0.356863,0.349020,0.337255,0.329412,0.321569,0.309804,0.301961,0.294118,0.290196,0.282353,0.274510,0.270588,0.262745,0.258824,0.254902,0.250980,0.247059,0.239216,0.235294,0.231373,0.227451,0.223529,0.219608,0.215686,0.211765,0.207843,0.203922,0.200000,0.196078,0.192157,0.188235,0.184314,0.180392,0.176471,0.172549,0.168627,0.164706,0.160784,0.156863,0.152941,0.149020,0.145098,0.141176,0.141176,0.137255,0.133333,0.129412,0.125490,0.121569,0.117647,0.113725,0.109804,0.105882,0.105882,0.101961,0.0980392,0.0941176,0.0901961,0.0862745,0.0823529,0.0823529,0.0784314,0.0745098,0.0745098,0.0705882,0.0705882,0.0705882,0.0666667,0.0666667,0.0666667,0.0666667,0.0666667,0.0666667,0.0666667,0.0666667,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0627451,0.0588235,0.0588235,0.0588235,0.0588235,0.0549020,0.0549020,0.0549020,0.0509804,0.0509804,0.0509804,0.0509804,0.0470588,0.0470588,0.0470588,0.0431373,0.0431373,0.0431373,0.0392157,0.0392157,0.0392157,0.0352941,0.0352941,0.0352941,0.0352941,0.0313726,0.0313726,0.0313726,0.0274510,0.0274510,0.0274510,0.0235294,0.0235294,0.0235294,0.0235294,0.0196078,0.0196078,0.0196078,0.0156863,0.0156863,0.0156863]
b = [ 0.776471,0.776471,0.776471,0.776471,0.776471,0.776471,0.776471,0.772549,0.772549,0.768627,0.764706,0.760784,0.756863,0.749020,0.745098,0.737255,0.733333,0.725490,0.717647,0.713726,0.709804,0.701961,0.698039,0.690196,0.686275,0.686275,0.682353,0.678431,0.678431,0.674510,0.674510,0.674510,0.674510,0.674510,0.674510,0.670588,0.670588,0.666667,0.662745,0.662745,0.658824,0.654902,0.650980,0.643137,0.639216,0.635294,0.631373,0.631373,0.627451,0.627451,0.627451,0.627451,0.627451,0.631373,0.639216,0.643137,0.650980,0.658824,0.670588,0.678431,0.686275,0.698039,0.705882,0.717647,0.725490,0.729412,0.737255,0.741176,0.745098,0.745098,0.741176,0.737255,0.733333,0.725490,0.717647,0.709804,0.694118,0.686275,0.670588,0.654902,0.643137,0.623529,0.611765,0.592157,0.576471,0.564706,0.549020,0.533333,0.517647,0.505882,0.498039,0.482353,0.474510,0.462745,0.450980,0.443137,0.431373,0.423529,0.411765,0.403922,0.392157,0.384314,0.376471,0.364706,0.356863,0.349020,0.337255,0.333333,0.325490,0.321569,0.317647,0.313726,0.313726,0.313726,0.313726,0.317647,0.321569,0.325490,0.329412,0.337255,0.341176,0.349020,0.352941,0.360784,0.364706,0.368627,0.376471,0.380392,0.384314,0.388235,0.392157,0.396078,0.400000,0.400000,0.403922,0.407843,0.411765,0.415686,0.419608,0.423529,0.423529,0.431373,0.431373,0.435294,0.439216,0.443137,0.447059,0.450980,0.454902,0.458824,0.462745,0.466667,0.470588,0.474510,0.474510,0.478431,0.482353,0.482353,0.486275,0.486275,0.490196,0.490196,0.490196,0.494118,0.494118,0.494118,0.498039,0.498039,0.498039,0.501961,0.501961,0.501961,0.501961,0.501961,0.501961,0.501961,0.501961,0.498039,0.498039,0.498039,0.498039,0.494118,0.494118,0.494118,0.490196,0.490196,0.490196,0.486275,0.486275,0.482353,0.478431,0.474510,0.470588,0.466667,0.462745,0.454902,0.450980,0.443137,0.435294,0.427451,0.419608,0.411765,0.403922,0.396078,0.384314,0.376471,0.368627,0.360784,0.352941,0.341176,0.333333,0.325490,0.317647,0.309804,0.301961,0.294118,0.286275,0.282353,0.274510,0.266667,0.262745,0.254902,0.247059,0.243137,0.235294,0.227451,0.223529,0.215686,0.211765,0.203922,0.196078,0.192157,0.184314,0.180392,0.172549,0.164706,0.156863,0.152941,0.145098,0.141176,0.133333,0.125490,0.121569,0.113725,0.109804,0.101961,0.0941176,0.0901961,0.0862745,0.0784314,0.0745098,0.0666667,0.0627451,0.0588235,0.0549020,0.0509804]

svs_tempo_cmap = LinearSegmentedColormap.from_list('svs_tempo', list(zip(r, g, b)))

# register this new colormap with matplotlib

cm.register_cmap(name='svs_tempo', cmap=svs_tempo_cmap)